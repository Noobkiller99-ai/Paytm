#!/bin/bash
# Rebuild every deliverable from inputs/. Run from the repo root: bash build/build_all.sh
set -e
cd "$(dirname "$0")"
SK=/root/.claude/skills/synced/086d875c-95b4-4191-b83f-05ead39e51be_5177831a-348a-4957-96f1-0f2a9d7b5ed2
python3 build_annexure.py ../inputs/Paytm_Track_B_VOCs.xlsx ../Paytitude_R2_Annexure.xlsx
python3 $SK/xlsx/scripts/recalc.py ../Paytitude_R2_Annexure.xlsx 60      # LibreOffice recalculation (any headless recalc works)
python3 check_numbers.py ../Paytitude_R2_Annexure.xlsx | tail -1           # workbook vs model.py
python3 build_deck.py ../Paytitude_R2.pptx ../storyboard.md
python3 $SK/pptx/scripts/office/validate.py ../Paytitude_R2.pptx
python3 audit.py ../Paytitude_R2.pptx > /dev/null && echo "audit ok"
python3 number_audit.py ../Paytitude_R2.pptx > /dev/null
OUT=$(mktemp -d); bash render.sh ../Paytitude_R2.pptx "$OUT" && cp "$OUT/Paytitude_R2.pdf" ../Paytitude_R2.pdf
echo "done: Paytitude_R2.pptx, Paytitude_R2.pdf, Paytitude_R2_Annexure.xlsx, storyboard.md"
