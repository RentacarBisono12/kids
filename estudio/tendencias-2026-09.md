# Estudio: qué se ve más en YouTube infantil (septiembre 2026)

Fuentes públicas (no tenemos acceso a YouTube Analytics ni a datos privados).
Las cifras son las que publica cada fuente; ver lista al final.

## 1. Qué domina en vistas

| Señal | Dato | Qué nos dice |
|---|---|---|
| Videos más vistos de YouTube | Baby Shark 17,3 mil M · Wheels on the Bus (CoComelon) 9,3 mil M · Bath Song 7,6 mil M · Johny Johny 7,2 mil M · Phonics Song 7,1 mil M | El contenido infantil preescolar es el más visto de la plataforma. Los temas ganadores son **rutinas** (baño), **vehículos**, **animales** y **aprender letras**. |
| Canal más visto en español | El Reino Infantil: 8,8 mil M de vistas ene–may 2026, 71 M de suscriptores. La Granja de Zenón cumple 15 años | En español ganan los **animales de granja** y personajes recurrentes (La Vaca Lola, El Gallo y la Pata). |
| Preescolar en EE. UU. (0–5 años) | Bluey 24 % de las cuentas; Ms Rachel, Super Simple Songs y CoComelon 22 % cada uno. Ms Rachel: 434 M de vistas en 30 días | Crecen dos cosas: **personajes que conversan** (Bluey) y el **aprendizaje guiado que le habla al niño** (Ms Rachel: pausas, preguntas, repetición). |
| Otros canales grandes | Pinkfong, ChuChu TV, D Billions, Pocoyó (31 M en español), Happy Learning, Smile and Learn | Aprender **colores, números y animales** con animación 2D/3D sencilla es una fórmula probada. |

## 2. El riesgo principal: la política contra el contenido "producido en masa"

- En julio de 2025 YouTube cambió el nombre de su política a **"contenido no auténtico"**. En julio de 2026 aclaró que **no se monetiza** el contenido genérico o hecho con plantillas, ni el contenido insatisfactorio.
- En enero de 2026 **cerró 16 canales** de contenido masivo hecho con IA (4,7 mil M de vistas y 35 M de suscriptores).
- Más de 200 organizaciones pidieron a Google prohibir el "AI slop" dirigido a niños.
- **Usar IA no desmonetiza por sí solo.** Lo que se castiga es lo repetitivo, sin trama y sin valor.

**Conclusión:** el canal debe tener **personajes propios y recurrentes**, **una historia y un objetivo educativo en cada episodio**, guiones escritos y revisados por una persona, y variedad entre episodios. No debe publicar compilaciones infinitas ni loops hipnóticos.

## 3. Estrategia recomendada

**Formato:** mini-episodios de 2,5 a 4 min con **dos personajes que conversan y le hablan al niño**. Toman lo que funciona de Bluey (diálogo) y de Ms Rachel (pregunta, pausa, respuesta).
- Cortes lentos (4–6 s), una idea por escena y repetición de la palabra clave 3 veces.
- Pausas de participación: "¿Tú lo sabes?" + 2 s de silencio + la respuesta.

**Personajes (los mismos en los dos idiomas; el nombre no se traduce):**
- **Pipo**: pollito amarillo, curioso, pregunta todo. Voz aguda y alegre.
- **Lula**: conejita lila, paciente, explica. Voz cálida y clara.

**Temas, ordenados por demanda comprobada:**

| Prioridad | Tema | Evidencia | Idioma del piloto |
|---|---|---|---|
| 1 | Animales de la granja y sus sonidos | Zenón / Reino Infantil, n.º 1 en español | ES |
| 2 | Rutinas: baño, dientes, dormir | Bath Song, 7,6 mil M | ES |
| 3 | Colores | Ms Rachel, D Billions, Pinkfong | EN |
| 4 | Contar del 1 al 10 con vehículos (autobús) | Wheels on the Bus, 9,3 mil M | EN |
| siguientes | Letras/fonética, formas, emociones, opuestos, clima | Phonics Song 7,1 mil M; Bluey (emociones) | alternar |

**Ritmo de publicación:** 1 episodio largo por idioma a la semana, y 2–3 Shorts 9:16 por episodio tomados de sus mejores escenas.

**Por qué no hacemos canciones (todavía):** los éxitos son canciones, pero:
- Las canciones famosas **tienen dueño**. Baby Shark y La Vaca Lola están protegidas.
- Higgsfield **no ofrece un modelo de música** para uso general, y la voz sintética no canta bien.
- Por tu regla, **no usamos música sin licencia comprobable**.

Opción segura para música de fondo: **Biblioteca de audio de YouTube** (YouTube Studio → Biblioteca de audio). Es gratis para videos de YouTube. Guarda una captura de la ficha de cada pista como prueba. Los pilotos funcionan sin música: voces + silencio.

## 4. Producción y costos (precios de Higgsfield consultados hoy)

| Pieza | Modelo | Créditos |
|---|---|---|
| Fotograma clave / fondo | gpt_image_2_5 | 0,25 por imagen |
| Voz de un personaje (1 línea) | seed_audio (TTS) | 0,2 por línea |
| Animación 6 s, 720p, con referencia de audio (movimiento de boca) | seedance_2_0_mini | 6 |
| Animación 5 s sin audio | kling3_0 std | 7,5 |
| Animación 6 s, 1080p | seedance_2_0 std | 54 |

Pipeline por episodio:
1. Hoja de personaje: Pipo y Lula, una vez para toda la serie.
2. Fotograma clave por escena (imagen con referencia de la hoja).
3. Voces TTS por línea. Se generan **por separado para ES y EN**, así la voz de cada personaje es la misma en todos los episodios.
4. Animación image-to-video (seedance mini con la voz como referencia de audio para mover la boca).
5. Rótulos HTML, montaje, xfade y mezcla de voces en el sandbox, según `CLAUDE.md`.

**Estimado por episodio de ~3 min (≈32 escenas, ≈40 líneas):** 32×6 + 32×0,25 + 40×0,2 ≈ **210 créditos**. Si una escena falla, se regenera: presupuesta ~300.
**Saldo actual: 0 créditos (plan gratis).** No se puede generar nada hasta recargar.

## 5. Cumplimiento (no negociable)

- Marca **"Hecho para niños: Sí"** en todos. No hay comentarios ni anuncios personalizados: esto reduce los ingresos, y es lo correcto.
- Divulgación de IA: la casilla de contenido "alterado o sintético" es obligatoria cuando el contenido parece real. En dibujos animados no suele aplicar, pero **recomiendo marcarla igualmente**: es honesto y protege el canal ante revisiones de contenido no auténtico.
- Sin flashes, sin sustos, sin personajes de marcas ajenas, sin imitar La Granja de Zenón ni CoComelon.

## Fuentes
- Statista, canales "made for kids" más suscritos: https://www.statista.com/statistics/1240228/leading-youtube-channels-made-for-kids-worldwide-by-subscribers/
- Wikipedia, videos más vistos: https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos
- RouteNote, top 10 más vistos 2026: https://routenote.com/blog/most-viewed-youtube-videos/
- PRODU, El Reino Infantil 8,8 mil M en 2026: https://www.produ.com/television/noticias/el-reino-infantil-supera-los-88-millones-de-views-en-2026/
- Bloomberg Línea, Reino Infantil 5.600 M: https://www.bloomberglinea.com/estilo-de-vida/argentina-reino-infantil-lidera-youtube-en-espanol-con-5600-millones-de-vistas-en-lo-que-va-de-2026/
- Infobae, La Granja de Zenón 15 años: https://www.infobae.com/teleshow/2026/09/17/la-granja-de-zenon-cumple-15-anos-y-repasa-su-salto-de-youtube-al-mundo/
- Señal News, Bluey lidera el preescolar en EE. UU.: https://senalnews.com/en/content/usa-bluey-dominates-streaming-preschool-consumption
- vidIQ, estadísticas de Ms Rachel: https://vidiq.com/youtube-stats/channel/@msrachel/
- Tubefilter, política de contenido no auténtico (jul 2026): https://www.tubefilter.com/2026/07/13/youtube-inauthentic-content-monetization-policy-update/
- TechCrunch, YouTube aclara políticas sobre AI slop: https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/
- Bloomberg, piden prohibir videos IA para niños: https://www.bloomberg.com/news/articles/2026-04-01/google-faces-demands-to-prohibit-ai-videos-for-kids-on-youtube
- Fortune, carta de 200 organizaciones: https://fortune.com/2026/04/01/ai-slop-200-organizations-letter-youtube-google/
