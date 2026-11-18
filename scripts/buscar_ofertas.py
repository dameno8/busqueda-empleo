"""Busca ofertas nuevas en los portales configurados en config/busqueda.toml.

Uso:  py scripts/buscar_ofertas.py          (Windows)
      python3 scripts/buscar_ofertas.py     (Linux / Mac / Codex web)

Guarda las ofertas nuevas (no vistas antes) en ofertas/busquedas/AAAA-MM-DD.csv
y apunta sus enlaces en ofertas/vistas.csv para no repetirlas.
"""

from __future__ import annotations

import csv
import datetime as dt
import sys
import time
import tomllib
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CONFIG = RAIZ / "config" / "busqueda.toml"
CARPETA_BUSQUEDAS = RAIZ / "ofertas" / "busquedas"
VISTAS = RAIZ / "ofertas" / "vistas.csv"

COLUMNAS = ["titulo", "empresa", "ubicacion", "fecha_publicacion", "portal",
            "termino", "url", "salario", "remoto", "descripcion"]


def cargar_config() -> dict:
    with open(CONFIG, "rb") as f:
        return tomllib.load(f)


def cargar_vistas() -> set[str]:
    if not VISTAS.exists():
        return set()
    with open(VISTAS, encoding="utf-8", newline="") as f:
        vistas = set()
        for fila in csv.DictReader(f):
            vistas.add(fila["url"])
            if fila.get("clave"):
                vistas.add(fila["clave"])
        return vistas


def clave(r: dict) -> str:
    """Identifica la misma oferta aunque venga de otro portal."""
    return f"{r['titulo'].lower().strip()}|{r['empresa'].lower().strip()}"


def apuntar_vistas(nuevas: list[dict]) -> None:
    nuevo = not VISTAS.exists()
    VISTAS.parent.mkdir(parents=True, exist_ok=True)
    hoy = dt.date.today().isoformat()
    with open(VISTAS, "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(["fecha", "url", "clave"])
        for r in nuevas:
            w.writerow([hoy, r["url"], clave(r)])


def salario(fila) -> str:
    mn, mx = fila.get("min_amount"), fila.get("max_amount")
    partes = [str(int(v)) for v in (mn, mx) if v == v and v is not None]  # v == v descarta NaN
    if not partes:
        return ""
    return f"{'-'.join(partes)} {fila.get('currency') or ''} {fila.get('interval') or ''}".strip()


def texto(v) -> str:
    return "" if v is None or v != v else str(v)  # v != v -> NaN


def buscar(cfg: dict, scrape_jobs) -> list[dict]:
    radio_millas = max(1, round(cfg.get("radio_km", 50) / 1.609))
    horas = int(cfg.get("dias_antiguedad", 7)) * 24
    excluir = [p.lower() for p in cfg.get("excluir_en_titulo", [])]
    resultados: list[dict] = []

    for portal in cfg.get("portales", ["indeed"]):
        for termino in cfg["terminos"]:
            print(f"· {portal}: «{termino}» ...", end=" ", flush=True)
            try:
                df = scrape_jobs(
                    site_name=[portal],
                    search_term=termino,
                    google_search_term=f"{termino} empleo {cfg['ubicacion']}",
                    location=cfg["ubicacion"],
                    distance=radio_millas,
                    is_remote=bool(cfg.get("solo_remoto", False)),
                    results_wanted=int(cfg.get("resultados_por_busqueda", 25)),
                    hours_old=horas,
                    country_indeed="spain",
                    linkedin_fetch_description=True,
                    description_format="markdown",
                    verbose=0,
                )
            except Exception as e:  # un portal caído no debe parar el resto
                print(f"error ({type(e).__name__})")
                continue
            print(f"{len(df)} ofertas")
            for _, fila in df.iterrows():
                titulo = texto(fila.get("title"))
                if any(p in titulo.lower() for p in excluir):
                    continue
                resultados.append({
                    "titulo": titulo,
                    "empresa": texto(fila.get("company")),
                    "ubicacion": texto(fila.get("location")),
                    "fecha_publicacion": texto(fila.get("date_posted")),
                    "portal": portal,
                    "termino": termino,
                    "url": texto(fila.get("job_url")),
                    "salario": salario(fila),
                    "remoto": texto(fila.get("is_remote")),
                    "descripcion": texto(fila.get("description"))[:6000],
                })
            time.sleep(3)  # pausa para no saturar los portales
    return resultados


def filtrar_nuevas(resultados: list[dict], vistas: set[str]) -> list[dict]:
    nuevas, ya = [], set(vistas)
    for r in resultados:
        if not r["url"] or r["url"] in ya or clave(r) in ya:
            continue
        nuevas.append(r)
        ya.update({r["url"], clave(r)})
    return nuevas


def guardar(nuevas: list[dict]) -> Path:
    CARPETA_BUSQUEDAS.mkdir(parents=True, exist_ok=True)
    destino = CARPETA_BUSQUEDAS / f"{dt.date.today().isoformat()}.csv"
    existe = destino.exists()
    with open(destino, "a", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNAS)
        if not existe:
            w.writeheader()
        w.writerows(nuevas)
    return destino


def main() -> int:
    try:
        from jobspy import scrape_jobs
    except ImportError:
        print("Falta instalar las dependencias: py -m pip install -r requirements.txt")
        return 1

    cfg = cargar_config()
    resultados = buscar(cfg, scrape_jobs)
    nuevas = filtrar_nuevas(resultados, cargar_vistas())

    if not nuevas:
        print(f"\nSin ofertas nuevas ({len(resultados)} encontradas, todas vistas o filtradas).")
        return 0

    destino = guardar(nuevas)
    apuntar_vistas(nuevas)
    print(f"\n{len(nuevas)} ofertas nuevas guardadas en {destino.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
