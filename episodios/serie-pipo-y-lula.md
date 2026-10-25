# Serie: Pipo y Lula / Pipo & Lula

Público: 2–5 años. Mismos personajes en español y en inglés; los nombres no se traducen.

## Personajes (prompt base para la hoja de personaje)
- **Pipo**: pollito bebé amarillo, redondo, ojos grandes negros con brillo, pico naranja
  corto, dos plumitas en la cabeza, botitas rojas. Curioso, pregunta todo, se ríe fácil.
- **Lula**: conejita lila claro, orejas largas con interior rosa, ojos marrones,
  bufanda turquesa. Tranquila, amable, explica despacio.
- Estilo: animación 3D suave tipo preescolar, formas redondas, colores saturados pero
  no fluorescentes, luz de día cálida, sin sombras duras, fondo sencillo.

Prompt de la hoja (gpt_image_2_5, 16:9):
> Character model sheet for a preschool 3D animated series. Two characters side by side,
> front, 3/4 and side views, neutral pose and happy expression. Character 1 "Pipo": a
> small round baby chick, soft yellow, big glossy black eyes, short orange beak, two tiny
> head feathers, little red boots. Character 2 "Lula": a light lilac bunny, long ears with
> pink inside, warm brown eyes, turquoise scarf. Soft rounded shapes, gentle warm daylight,
> plain light background, no text.

## Voces (se eligen UNA vez y quedan fijas; escucha el preview de Higgsfield antes de decidir)
| Personaje | ES — candidata | EN — candidata | Ajuste seed_audio |
|---|---|---|---|
| Pipo | Pixie / Marisol | Pixie / Kayla | pitch_rate alto, speech_rate −10 % |
| Lula | Ines / Elena | Luna / Daisy | speech_rate −15 %, tono cálido |

### Prueba de voces (25-oct-2026, seed_audio, transcrito con Whisper)
| Prueba | Resultado | Decisión |
|---|---|---|
| Pipo ES — Pixie (pitch +3, rate −10) | Se entiende; "muu" lo deletreó como "M-U-U" | Usar. Escribir "¡muuuu!" |
| Lula ES — Ines (rate −15) | Correcto | Usar |
| Lula ES — Marisol | Whisper lo detecta como inglés; "quién es" → "Kenneth" | Descartar |
| Pipo EN — Pixie | Correcto ("Pipo" → "Pupil"; nombre inventado, aceptable) | Usar |
| Lula EN — Luna | Correcto, 0,98 de confianza en inglés | Usar |
Falta que una persona las escuche: Whisper solo confirma que se entienden, no si suenan bien para niños.

Hoja de personajes aprobada: job `513e0e77-0e6a-4645-a961-21e86c27c00f` (variante B).
Úsala como referencia de imagen en cada fotograma clave.

## Reglas de guion
- Escenas de 4–6 s, una idea por escena.
- La palabra clave se dice 3 veces: la presenta un personaje, la repite el otro y la repite el niño.
- Pausa de participación: pregunta a cámara → 2 s de silencio → respuesta.
- Cero sustos, cero peleas, cero flashes. Si hay un "problema", se resuelve con calma.
- Apertura fija de 5 s ("¡Hola, soy Pipo!" / "¡Y yo soy Lula!") y cierre fijo de 6 s ("¡Adiós, amigos!"). Crean ritual, pero el cuerpo del episodio es siempre nuevo.
