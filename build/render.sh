#!/bin/bash
# Render a pptx to PDF + JPGs for visual QA. Usage: render.sh deck.pptx outdir [dpi]
set -e
SK=/root/.claude/skills/synced/086d875c-95b4-4191-b83f-05ead39e51be_5177831a-348a-4957-96f1-0f2a9d7b5ed2/pptx
DECK=$1; OUT=$2; DPI=${3:-80}
mkdir -p "$OUT"; cp "$DECK" "$OUT/"; cd "$OUT"
B=$(basename "$DECK" .pptx)
rm -f "$B.pdf" slide-*.jpg
timeout 240 python3 $SK/scripts/office/soffice.py --headless --convert-to pdf "$B.pptx" >/dev/null 2>&1
pdftoppm -jpeg -r $DPI "$B.pdf" slide 2>/dev/null
pdfinfo "$B.pdf" 2>/dev/null | grep Pages
