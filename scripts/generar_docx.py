"""Convierte un CV o carta en Markdown sencillo a Word (.docx).

Uso:  py scripts/generar_docx.py ofertas/<carpeta>/cv.md
Crea cv.docx junto al .md. Admite: # títulos, ## secciones, ### subsecciones,
listas con "- ", **negrita**, *cursiva* y párrafos normales.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt, RGBColor

AZUL = RGBColor(0x1F, 0x4E, 0x79)
FORMATO = re.compile(r"(\*\*.+?\*\*|\*.+?\*)")


def añadir_texto(parrafo, texto: str) -> None:
    for trozo in FORMATO.split(texto):
        if not trozo:
            continue
        if trozo.startswith("**") and trozo.endswith("**"):
            parrafo.add_run(trozo[2:-2]).bold = True
        elif trozo.startswith("*") and trozo.endswith("*"):
            parrafo.add_run(trozo[1:-1]).italic = True
        else:
            parrafo.add_run(trozo)


def convertir(origen: Path) -> Path:
    doc = Document()
    for s in doc.sections:
        s.top_margin = s.bottom_margin = Cm(1.8)
        s.left_margin = s.right_margin = Cm(2)
    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(10.5)
    normal.paragraph_format.space_after = Pt(3)

    for linea in origen.read_text(encoding="utf-8").splitlines():
        l = linea.rstrip()
        if not l.strip() or l.strip().startswith(("<!--", ">")):
            continue
        if l.startswith("# "):
            p = doc.add_paragraph()
            r = p.add_run(l[2:].strip())
            r.bold, r.font.size, r.font.color.rgb = True, Pt(18), AZUL
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        elif l.startswith("## "):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(10)
            r = p.add_run(l[3:].strip().upper())
            r.bold, r.font.size, r.font.color.rgb = True, Pt(11.5), AZUL
        elif l.startswith("### "):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(6)
            añadir_texto(p, f"**{l[4:].strip()}**")
        elif l.lstrip().startswith(("- ", "* ")):
            p = doc.add_paragraph(style="List Bullet")
            añadir_texto(p, l.lstrip()[2:])
        else:
            añadir_texto(doc.add_paragraph(), l.strip())

    destino = origen.with_suffix(".docx")
    doc.save(destino)
    return destino


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    print(f"Creado: {convertir(Path(sys.argv[1]))}")
