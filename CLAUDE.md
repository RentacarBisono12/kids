# Canal infantil de YouTube — pipeline de producción

Este pipeline está probado. No lo reemplaces por otro.

## Dónde corre cada cosa
- **Video (ffmpeg, ffprobe, ImageMagick, Pillow):** SIEMPRE en el sandbox de
  Higgsfield (`sandbox_exec`). No asumas ffmpeg/node/Pillow en la máquina local.
- El sandbox se destruye ~10 s después de cada llamada: encadena todo en UN
  comando con `&&`, o usa `background:true` (15 min).
- **Rótulos/gráficos:** HTML/CSS rasterizado con Chrome headless LOCAL
  (`tools/render_overlays.sh`). Nunca `drawtext` para layouts de más de una línea.

## Mover archivos
`media_upload` → PUT a la URL prefirmada → `media_confirm`.
Queda en `https://d2ol7oe51mr4n9.cloudfront.net/user_<ID>/<media_id>.<ext>`.
- Si `SignedHeaders` incluye `if-none-match`, manda `-H 'If-None-Match: *'` (si no, 403).
- CloudFront cachea por URL: si corriges un archivo, pide un `media_upload` NUEVO.
  Nunca reutilices una URL anterior.

## Rótulos (Chrome headless)
- `--default-background-color=00000000` → PNG con alpha. Verifica:
  `sips -g hasAlpha overlays.png` (Mac) o `python3 tools/png_alpha.py overlays.png` → "yes".
- `--virtual-time-budget=20000` es obligatorio (si no, las fuentes no cargan a tiempo).
- Fuentes LOCALES: `tools/fetch_fonts.sh "Fredoka:wght@600;700"` las baja a
  `templates/fonts/`. En la sesión en la nube, Chrome no confía en el proxy y un
  `<link>` a Google Fonts cae a Arial SIN error. Mira siempre el PNG antes de subirlo.
- Apila TODOS los rótulos en una sola imagen 1920 × 1080·N (`templates/ov.html`),
  súbela una vez y recorta en ffmpeg con `crop=1920:1080:0:<i*1080>`.

## Patrones de ffmpeg (1920x1080, 30 fps; 9:16 solo para Shorts)
Ken Burns:
    ffmpeg -i img.jpg -vf "scale=2304:1296:force_original_aspect_ratio=increase,\
    crop=2304:1296,zoompan=z='min(zoom+0.00085,1.16)':x='iw/2-(iw/zoom/2)':\
    y='ih/2-(ih/zoom/2)':d=<N>:s=1920x1080:fps=30,format=yuv420p" \
    -frames:v <N> -r 30 seg.mp4

Material que no llena el cuadro (fondo borroso + nítido encima, nunca recortar):
    [0:v]fps=30,split=2[a][b];
    [a]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,
       gblur=sigma=40,eq=brightness=-0.13[bg];
    [b]scale=-2:1080[fg];
    [bg][fg]overlay=(W-w)/2:(H-h)/2

Rótulo con entrada suave:
    [1:v]crop=1920:1080:0:<Y>,format=rgba,fade=t=in:st=0.18:d=0.5:alpha=1[o];
    [0:v][o]overlay=0:0:format=auto,format=yuv420p

Transiciones: offsets ACUMULATIVOS — genera la cadena con
`python3 tools/xfade.py --t 0.3 <d0> <d1> ...` (no los calcules a mano).
    off_1 = d_0 - T ; off_i = off_(i-1) + d_i - T ; total = Σd - (n-1)·T

Salida:
    -c:v libx264 -profile:v high -preset medium -crf 20 -pix_fmt yuv420p -r 30
    -c:a aac -b:a 128k -movflags +faststart
Si no hay audio: `-f lavfi -i anullsrc=r=44100:cl=stereo -shortest` igualmente.

## Disciplina obligatoria
1. `ffprobe` a CADA entrada antes de planear:
       ffprobe -v error -select_streams v:0 \
         -show_entries stream=width,height,r_frame_rate,duration \
         -show_entries stream_side_data=rotation -of default=noprint_wrappers=1 x.mp4
   La rotación de celular vive en `stream_side_data`, no en width/height.
2. No confíes en nombres de archivo: extrae frames, arma hoja de contacto, súbela y MÍRALA.
3. No digas "listo" sin haber ejecutado el comando y visto la salida.

## Reglas del contenido infantil
- Sin flashes ni estroboscopio (convulsiones + política de YouTube).
- Cortes lentos: 3–6 s por plano.
- Tipografía redondeada, contraste muy alto, pocas palabras por pantalla.
- Música solo con licencia demostrable. Registra la prueba en el `brief.md` del episodio.
- "Hecho para niños" declarado con la verdad. Declararlo mal puede costar el canal.

## Lecciones de producción (ES-01, oct 2026)
- **Voces:** usar `text2speech_v2` con `variant: "elevenlabs"`. `seed_audio` lee el español con
  acento inglés (Whisper lo detecta como ~57 % español). Verifica cada línea con faster-whisper.
- **Animación:** `seedance_2_0_mini`, 720p, `generate_audio:false`, `start_image` = job del
  fotograma (1 crédito/s). Si responde con un preset ("IN THE DARK"), reintenta con
  `declined_preset_id`. Límite: ~6 videos en paralelo; 429 = espera, no reintentes en bucle.
- **Sandbox:** la llamada MCP corta a ~60 s aunque pidas más → todo lo largo con
  `background:true`. Un `sleep 880` en background mantiene vivos los archivos entre llamadas.
- **Rótulos en la nube:** si la sesión corre en un contenedor que no puede subir a
  `upload.higgsfield.ai`, rasteriza el mismo HTML en el sandbox con Playwright
  (`tools/render_overlays_sandbox.js`, verifica "fuentes cargadas: Fredoka").
- **Revisión sin ver:** la salida de texto del sandbox se corta ~20 KB, así que no sirve para
  traer imágenes. Revisión numérica: ffprobe, salto de luminancia (signalstats YAVG <3 = sin
  flashes), `scdet` (0 cortes), píxel del rótulo, y Whisper sobre el audio final. El ojo
  humano revisa fotogramas en la galería de Higgsfield antes de animar.
- **Montaje:** `tools/manifiesto.py` + `tools/armar_episodio.py` (xfade/acrossfade, loudnorm -16 LUFS).
  Un solo grafo xfade con 32 entradas 1080p muere (memoria/lease): unir en grupos de 8
  (intermedio .mkv crf14 + PCM) y luego los grupos. Corre en `background:true`.
- **Entrega:** subir el MP4 final y la miniatura (1280×720 JPG) con `media_upload` en la MISMA
  sesión del sandbox antes de que expire; el enlace de CloudFront es lo que se entrega.

## Estructura
- `episodios/<slug>/brief.md` — guion, plano a plano, licencias (copia `episodios/_plantilla`).
- `templates/ov.html` — plantilla de rótulos apilados.
- `tools/` — utilidades locales (sin ffmpeg): rasterizado, verificación de alpha, offsets xfade.
