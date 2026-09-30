#!/usr/bin/env python3
"""Genera la cadena xfade con offsets acumulativos.

Uso: python3 tools/xfade.py [--t 0.3] [--transition fade] d0 d1 d2 ...
  off_1 = d_0 - T ; off_i = off_(i-1) + d_i - T ; total = sum(d) - (n-1)*T
"""
import argparse

p = argparse.ArgumentParser()
p.add_argument("--t", type=float, default=0.3, help="duración de la transición (s)")
p.add_argument("--transition", default="fade")
p.add_argument("durations", type=float, nargs="+")
a = p.parse_args()

d, T, n = a.durations, a.t, len(a.durations)
if n < 2:
    raise SystemExit("hacen falta al menos 2 segmentos")
if any(x <= T for x in d):
    raise SystemExit(f"cada segmento debe durar más que T={T}")
for i, x in enumerate(d):
    if not 3 <= x <= 6:
        print(f"# AVISO: plano {i} dura {x}s (regla infantil: 3–6 s)")

parts, off, prev = [], 0.0, "0:v"
for i in range(1, n):
    off += d[i - 1] - T
    out = "v" if i == n - 1 else f"x{i}"
    parts.append(f"[{prev}][{i}:v]xfade=transition={a.transition}:duration={T}:offset={off:.3f}[{out}]")
    prev = out

print(";".join(parts))
print(f"# duración final = {sum(d) - (n - 1) * T:.3f} s  (map: [v])")
