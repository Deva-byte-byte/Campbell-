#!/usr/bin/env bash
# Installs the rendering toolchain for chapter-note PDFs.
set -euo pipefail
pip install -q weasyprint pypdfium2
if [ -z "$(fc-list | grep -i carlito)" ]; then
  apt-get install -y -q fonts-crosextra-carlito >/dev/null 2>&1 \
    || { apt-get update -q >/dev/null && apt-get install -y -q fonts-crosextra-carlito >/dev/null; }
fi
python3 -c "import weasyprint, pypdfium2; print('WeasyPrint', weasyprint.__version__)"
[ -n "$(fc-list | grep -i carlito)" ] && echo "Carlito installed"
