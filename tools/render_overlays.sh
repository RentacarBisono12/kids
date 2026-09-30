#!/usr/bin/env bash
# Rasteriza templates/ov.html (o el HTML indicado) a PNG con alpha.
# Uso: tools/render_overlays.sh <ov.html> <n_paneles> [salida.png]
set -euo pipefail
html="$1"; n="$2"; out="${3:-overlays.png}"

if [[ -n "${CHROME:-}" ]]; then :
elif [[ -x "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" ]]; then
  CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
elif [[ -x /opt/pw-browsers/chromium ]]; then CHROME=/opt/pw-browsers/chromium
else echo "No encuentro Chrome; define CHROME=/ruta" >&2; exit 1; fi

extra=()
[[ "$(uname)" == Linux && $EUID -eq 0 ]] && extra+=(--no-sandbox)
# Contenedor en la nube: Chrome no lee HTTPS_PROXY solo; sin esto Google Fonts no carga.
[[ -n "${HTTPS_PROXY:-}" ]] && extra+=(--proxy-server="$HTTPS_PROXY")

"$CHROME" --headless=new --disable-gpu --hide-scrollbars "${extra[@]}" \
  --default-background-color=00000000 \
  --virtual-time-budget=20000 \
  --window-size=1920,$((1080 * n)) \
  --screenshot="$out" "file://$(cd "$(dirname "$html")" && pwd)/$(basename "$html")" 2>/dev/null

if [[ "$(uname)" == Darwin ]]; then sips -g hasAlpha "$out"
else python3 "$(dirname "$0")/png_alpha.py" "$out"; fi
