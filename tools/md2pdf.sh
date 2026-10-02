#!/bin/bash
# usage: tools/md2pdf.sh input.md output.pdf   -> A4, black-and-white print PDF
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
python3 -c "import markdown" 2>/dev/null || pip install -q markdown
CHROME=$(ls /opt/pw-browsers/chromium-*/chrome-linux/chrome 2>/dev/null | head -1)
[ -z "$CHROME" ] && CHROME=$(command -v chromium || command -v chromium-browser || command -v google-chrome)
HTML="$(mktemp --suffix=.html)"
python3 "$DIR/md2html.py" "$1" "$HTML" "$DIR/style.css"
"$CHROME" --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer --print-to-pdf="$2" "file://$HTML" 2>/dev/null
rm -f "$HTML"
echo "$2: $(pdfinfo "$2" 2>/dev/null | awk '/Pages/{print $2}') pages"
