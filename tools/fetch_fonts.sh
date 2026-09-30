#!/usr/bin/env bash
# Descarga fuentes de Google Fonts a templates/fonts/ y genera fonts.css local.
# Así el rasterizado no depende de la red de Chrome (en la nube, Chrome no confía
# en el proxy y cae a Arial sin avisar).
# Uso: tools/fetch_fonts.sh "Fredoka:wght@600;700"
set -euo pipefail
dir="$(cd "$(dirname "$0")/.." && pwd)/templates/fonts"; mkdir -p "$dir"
# UA moderno → Google devuelve woff2
css=$(curl -fsS -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36" \
  "https://fonts.googleapis.com/css2?family=${1// /+}&display=block")
out="$css"
for url in $(grep -o 'https://fonts.gstatic.com/[^)]*' <<<"$css" | sort -u); do
  f="$(basename "$url")"; curl -fsS -o "$dir/$f" "$url"; out="${out//$url/$f}"
done
printf '%s\n' "$out" > "$dir/fonts.css"
ls "$dir"
