#!/usr/bin/env python3
"""Monta un episodio en el SANDBOX de Higgsfield (ffmpeg) a partir de un manifiesto JSON.

Manifiesto (generado por tools/manifiesto.py):
{
  "fps": 30, "T": 0.3, "overlays_png": "ov.png",
  "escenas": [
    {"n": 1, "dur": 5, "video": "<url mp4>", "panel": null | 0..N,
     "lineas": [{"url": "<url audio>", "t": 0.4}, ...]}
  ]
}
Uso (en el sandbox):  python3 armar_episodio.py manifiesto.json salida.mp4
Pasos: descarga -> segmento por escena (1920x1080@30, voces con adelay, rótulo con
fade de entrada) -> xfade/acrossfade por grupos de 8 -> unión de grupos + loudnorm -> H.264/AAC.
"""
import json, os, subprocess, sys

def sh(cmd):
    print("+", " ".join(cmd)[:200], flush=True)
    subprocess.run(cmd, check=True)

def bajar(url, dst):
    if not os.path.exists(dst):
        sh(["curl", "-fsS", "-m", "120", "-o", dst, url])
    return dst

def segmento(e, ov, fps, tmp):
    n, d = e["n"], e["dur"]
    v = bajar(e["video"], f"{tmp}/v{n}.mp4")
    ins = ["-i", v]
    fc = [f"[0:v]scale=1920:1080:flags=lanczos,fps={fps},trim=0:{d},setpts=PTS-STARTPTS,format=yuv420p[v0]"]
    vlast = "v0"
    idx = 1
    if e.get("panel") is not None:
        ins += ["-loop", "1", "-t", str(d), "-i", ov]
        y = 1080 * e["panel"]
        fc.append(f"[{idx}:v]crop=1920:1080:0:{y},format=rgba,fade=t=in:st=0.18:d=0.5:alpha=1[o]")
        fc.append(f"[{vlast}][o]overlay=0:0:format=auto,format=yuv420p[v1]")
        vlast = "v1"
        idx += 1
    alabels = []
    for k, l in enumerate(e.get("lineas", [])):
        a = bajar(l["url"], f"{tmp}/a{n}_{k}" + os.path.splitext(l["url"])[1])
        ins += ["-i", a]
        ms = int(l["t"] * 1000)
        fc.append(f"[{idx}:a]aresample=44100,aformat=channel_layouts=stereo,adelay={ms}|{ms}[a{k}]")
        alabels.append(f"[a{k}]")
        idx += 1
    ins += ["-f", "lavfi", "-t", str(d), "-i", "anullsrc=r=44100:cl=stereo"]
    alabels.append(f"[{idx}:a]")
    fc.append("".join(alabels) + f"amix=inputs={len(alabels)}:normalize=0:duration=longest,atrim=0:{d},asetpts=PTS-STARTPTS[aout]")
    out = f"{tmp}/seg{n:02d}.mp4"
    sh(["ffmpeg", "-y", "-v", "error", *ins, "-filter_complex", ";".join(fc),
        "-map", f"[{vlast}]", "-map", "[aout]", "-t", str(d),
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-r", str(fps),
        "-c:a", "aac", "-b:a", "192k", out])
    return out

FINAL = ["-c:v", "libx264", "-profile:v", "high", "-preset", "medium", "-crf", "20",
         "-pix_fmt", "yuv420p", "-r", "30",
         "-c:a", "aac", "-b:a", "128k", "-ar", "44100", "-movflags", "+faststart"]
INTERMEDIO = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "14", "-pix_fmt", "yuv420p",
              "-r", "30", "-c:a", "pcm_s16le"]

def unir(files, durs, T, out, final=False):
    """xfade/acrossfade con offsets acumulativos; loudnorm solo en la pasada final."""
    if len(files) == 1 and not final:
        return files[0]
    ins, fc = [], []
    for f in files:
        ins += ["-i", f]
    vprev, aprev, off = "0:v", "0:a", 0.0
    for i in range(1, len(files)):
        off += durs[i - 1] - T
        vo, ao = ("vout", "amid") if i == len(files) - 1 else (f"x{i}", f"y{i}")
        fc.append(f"[{vprev}][{i}:v]xfade=transition=fade:duration={T}:offset={off:.3f}[{vo}]")
        fc.append(f"[{aprev}][{i}:a]acrossfade=d={T}[{ao}]")
        vprev, aprev = vo, ao
    if len(files) == 1:
        fc.append("[0:v]null[vout]")
    fc.append(f"[{aprev}]" + ("loudnorm=I=-16:TP=-1.5:LRA=11" if final else "anull") + "[aout]")
    sh(["ffmpeg", "-y", "-v", "error", "-threads", "2", *ins, "-filter_complex", ";".join(fc),
        "-map", "[vout]", "-map", "[aout]", *(FINAL if final else INTERMEDIO), out])
    return out

def main():
    man = json.load(open(sys.argv[1]))
    salida = sys.argv[2]
    tmp = "work"; os.makedirs(tmp, exist_ok=True)
    fps, T = man.get("fps", 30), man.get("T", 0.3)
    segs = [segmento(e, man["overlays_png"], fps, tmp) for e in man["escenas"]]
    durs = [e["dur"] for e in man["escenas"]]
    # Un solo grafo con 32 entradas 1080p muere por memoria en el sandbox:
    # se une en grupos de 8 (intermedio sin pérdidas audibles) y luego los grupos.
    G, GD = [], []
    for g in range(0, len(segs), 8):
        ds = durs[g:g + 8]
        G.append(unir(segs[g:g + 8], ds, T, f"{tmp}/grupo{g // 8}.mkv"))
        GD.append(sum(ds) - (len(ds) - 1) * T)
    total = sum(durs) - (len(durs) - 1) * T
    print(f"duracion esperada {total:.2f}s", flush=True)
    unir(G, GD, T, salida, final=True)

if __name__ == "__main__":
    main()
