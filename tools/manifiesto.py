#!/usr/bin/env python3
"""Genera el manifiesto JSON de un episodio para tools/armar_episodio.py.

Uso: python3 tools/manifiesto.py <dir_episodio> [escenas_coma] > manifiesto.json
Lee en <dir_episodio>: duraciones.tsv, videos.lst, audio_v2.lst (+ audio_dur.tsv),
lineas.tsv, paneles.tsv. Cada línea de voz arranca 0.4 s después del inicio de
la escena o 0.3 s después de la anterior; si la línea anterior es una pregunta
de participación (marcada con pausa=2 en lineas.tsv) se dejan 2 s de silencio.
"""
import csv, json, os, sys

CDN = "https://d8j0ntlcm91z4.cloudfront.net/user_3Gv0xgr4xyMhZDx7tZiyu8WgdvX/"

def lst(path):
    return dict(l.split() for l in open(path) if l.strip())

def main():
    d = sys.argv[1]
    solo = set(int(x) for x in sys.argv[2].split(",")) if len(sys.argv) > 2 else None
    durs = {int(r["escena"]): int(r["seg"]) for r in csv.DictReader(open(f"{d}/duraciones.tsv"), delimiter="\t")}
    vids = lst(f"{d}/videos.lst")
    auds = lst(f"{d}/audio_v2.lst")
    adur = {k: float(v) for k, v in lst(f"{d}/audio_dur.tsv").items()}
    paneles = {int(k): int(v) for k, v in lst(f"{d}/paneles.tsv").items()}
    lineas = {}
    for r in csv.DictReader(open(f"{d}/lineas.tsv"), delimiter="\t"):
        lineas.setdefault(int(r["escena"]), []).append(r)
    esc = []
    for n in sorted(durs):
        if solo and n not in solo:
            continue
        t, ls = 0.4, []
        for r in lineas.get(n, []):
            i = r["indice"]
            ls.append({"url": CDN + auds[i] + ".mp3", "t": round(t, 2)})
            t += adur[i] + (2.0 if r.get("pausa") == "2" else 0.3)
        if t - 0.3 > durs[n]:
            print(f"AVISO escena {n}: voces {t:.1f}s > {durs[n]}s", file=sys.stderr)
        esc.append({"n": n, "dur": durs[n], "video": CDN + vids[str(n)] + ".mp4",
                    "panel": paneles.get(n), "lineas": ls})
    json.dump({"fps": 30, "T": 0.3, "overlays_png": "ov.png", "escenas": esc}, sys.stdout, indent=1)

if __name__ == "__main__":
    main()
