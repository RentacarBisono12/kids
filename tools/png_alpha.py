#!/usr/bin/env python3
"""Imprime 'yes' si el PNG tiene canal alpha (equivalente a `sips -g hasAlpha`)."""
import struct, sys

with open(sys.argv[1], "rb") as f:
    head = f.read(33)
if head[:8] != b"\x89PNG\r\n\x1a\n":
    raise SystemExit("no es PNG")
w, h, depth, ctype = struct.unpack(">IIBB", head[16:26])
print(f"{w}x{h}", "hasAlpha:", "yes" if ctype in (4, 6) else "no")
sys.exit(0 if ctype in (4, 6) else 1)
