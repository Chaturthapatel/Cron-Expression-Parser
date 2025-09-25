#!/usr/bin/env python3
import sys

RANGES = {
    "minute": (0, 59),
    "hour": (0, 23),
    "day": (1, 31),
    "month": (1, 12),
    "weekday": (0, 6),
}

def expand(expr, field):
    start, end = RANGES[field]
    if expr == "*":
        return list(range(start, end + 1))
    
    vals = set()
    for part in expr.split(","):
        if part.startswith("*/"):
            step = int(part[2:])
            vals.update(range(start, end + 1, step))
        elif "-" in part:
            s, e = map(int, part.split("-"))
            vals.update(range(s, e + 1))
        else:
            vals.add(int(part))
    return sorted(vals)

def parse(expr):
    m, h, d, mo, w, cmd = expr.split(maxsplit=5)
    data = {f: expand(v, f) for f, v in zip(["minute","hour","day","month","weekday"], [m,h,d,mo,w])}
    data["command"] = cmd
    return data

def show(data):
    for k in ["minute","hour","day","month","weekday"]:
        print(f"{k:<8}{' '.join(map(str, data[k]))}")
    print(f"command {data['command']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: cron_parser.py "<cron expression>"')
        sys.exit(1)
    show(parse(sys.argv[1]))
