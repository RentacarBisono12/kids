# ES-01 · ¿Quién dice muu? Los animales de la granja

- Serie: Pipo y Lula · Idioma: español · Edad objetivo: 2–5 años
- Formato: 1920×1080, 30 fps, H.264 + AAC, ~2:45
- Guion: `guion.md` · Líneas: `lineas.tsv` · Escenas: `duraciones.tsv`, `animacion.tsv`

## Para subir a YouTube

**Título** (máx. 100 caracteres)
> ¿Quién dice MUU? 🐮 Animales de la granja y sus sonidos | Pipo y Lula

**Descripción**
> ¡Hola, amigos! Pipo y Lula visitan la granja y descubren a la vaca, el cerdito, la oveja,
> el gallo, el pato y el caballo. ¿Sabes cómo dice cada uno? ¡Dilo con ellos!
>
> En este video los niños aprenden:
> 🐮 Vaca – ¡muu!  🐷 Cerdito – ¡oinc, oinc!  🐑 Oveja – ¡beee!
> 🐓 Gallo – ¡quiquiriquí!  🦆 Pato – ¡cuac, cuac!  🐴 Caballo – ¡iiih!
>
> Video educativo para niños de 2 a 5 años. Ritmo tranquilo, sin luces intermitentes.
> Animación y voces creadas con herramientas de inteligencia artificial y revisadas por nuestro equipo.

**Etiquetas**
animales de la granja, sonidos de animales, animales para niños, video educativo para niños,
la vaca dice muu, aprender animales, pipo y lula, dibujos animados en español, preescolar,
canciones infantiles, granja para niños

**Configuración obligatoria**
- Público: **"Sí, es contenido creado para niños"** (COPPA). Es verdad: la audiencia principal son niños.
- Contenido alterado o sintético: **marcar "Sí"**. Las imágenes, la animación y las voces son generadas con IA.
- Categoría: Educación · Idioma del video: Español · Licencia: Estándar de YouTube.
- Ubicación en playlist sugerida: "Pipo y Lula – Aprende con nosotros".

## Entradas (verificadas)
| Tipo | Fuente | Verificación |
|---|---|---|
| 32 fotogramas | gpt_image_2_5 (Higgsfield), ref. hoja de personajes `513e0e77…` | Aprobados por el usuario en la galería |
| 32 animaciones | seedance_2_0_mini 720p, sin audio | ffprobe 1280×720 24 fps; saltoLuz < 2 (sin flashes); 0 cortes; movimiento > 0,8 |
| 38 voces | ElevenLabs (text2speech_v2) vía Higgsfield, voces Pixie (Pipo), Ines (Lula), Benji (animales) | Transcripción Whisper en español |
| Rótulos | `ov.html` (Fredoka), 11 paneles | PNG con alpha, fuente verificada |

## Audio y licencias
| Pista | Fuente | Licencia | Prueba |
|---|---|---|---|
| Voces | Generadas en Higgsfield (plan Plus de la cuenta) | Uso comercial según términos de Higgsfield | Jobs en `jobs.tsv` |
| Música | **Ninguna** | — | — |
| Efectos | **Ninguno** (los sonidos de animales los dicen las voces) | — | — |

## Checklist
- [x] ffprobe de cada entrada
- [x] Fotogramas revisados por persona
- [x] Rótulos: alpha = yes, Fredoka verificada
- [x] Planos de 5–8 s, sin flashes (medido)
- [x] Sin música de licencia dudosa
- [ ] Salida final: ffprobe + Whisper + revisión humana completa antes de publicar
