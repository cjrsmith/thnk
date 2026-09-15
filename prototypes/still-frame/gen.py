#!/usr/bin/env python3
"""Build seed data for the thnk still-frame prototype.

Provenance, stated plainly because the prototype's conclusions depend on it:
  - COMMITS: real timestamps, real content, real bursts and silences. Trustworthy.
  - NOTES:   real content, SYNTHESISED timestamps. A markdown file has one mtime,
             so fragments are spread backwards over a plausible window. The bursts
             they form are invented; their content and rough era are real.
Neglect (time since last interaction) is NOT derivable from either source, so the
prototype sweeps it rather than seeding it. See profiles in the HTML.
"""
import json, os, random, re, subprocess, sys, glob

random.seed(20260915)
OUT = os.path.dirname(os.path.abspath(__file__))
DAY = 86400

thoughts = []

# ---- commits: the backbone -------------------------------------------------
with open(os.path.join(OUT, "commits.tsv")) as f:
    for line in f:
        parts = line.rstrip("\n").split("\t")
        if len(parts) != 3:
            continue
        ts, repo, subject = parts
        thoughts.append({
            "t": int(ts),
            "topic": repo,
            "content": subject.strip(),
            "src": "commit",
        })

# ---- note fragments: real content, synthesised timing ----------------------
NOTES = os.path.expanduser("~/Notes")
PER_FILE_CAP = 22
for path in sorted(glob.glob(os.path.join(NOTES, "*.md"))):
    stem = os.path.basename(path)[:-3]
    mtime = int(os.path.getmtime(path))
    frags = []
    with open(path, errors="replace") as f:
        for raw in f:
            s = raw.strip()
            m = re.match(r"^(#{1,3}\s+|[-*]\s+)(.*)$", s)
            if not m:
                continue
            body = m.group(2).strip()
            body = re.sub(r"[*_`\[\]]", "", body)
            body = re.sub(r"\s+", " ", body)
            if 12 <= len(body) <= 110:
                frags.append(body)
    if not frags:
        continue
    if len(frags) > PER_FILE_CAP:
        frags = random.sample(frags, PER_FILE_CAP)
    # spread backwards from mtime over a window, in a few clustered sittings
    window = random.choice([21, 45, 90]) * DAY
    n_sit = max(1, len(frags) // 5)
    sittings = sorted(mtime - random.randint(0, window) for _ in range(n_sit))
    for body in frags:
        base = random.choice(sittings)
        thoughts.append({
            "t": base + random.randint(0, 3 * 3600),
            "topic": stem,
            "content": body,
            "src": "note",
        })

thoughts.sort(key=lambda x: x["t"])

# ---- Trains of Thought: global time clustering -----------------------------
# A Train is context, not subject: "everything I was thinking about on Tuesday
# afternoon". So cluster across topics by time gap alone. This is what makes the
# angle=Train vs angle=Topic comparison meaningful -- Trains genuinely span Topics.
GAP = 4 * 3600
train_id = 0
for i, th in enumerate(thoughts):
    if i > 0 and th["t"] - thoughts[i - 1]["t"] > GAP:
        train_id += 1
    th["train"] = train_id

# assign stable ids
for i, th in enumerate(thoughts):
    th["id"] = i

topics = sorted({t["topic"] for t in thoughts})
ntrains = train_id + 1
span_days = (thoughts[-1]["t"] - thoughts[0]["t"]) / DAY

# train stats -- lifetime matters for arm length
from collections import defaultdict
tr = defaultdict(list)
for th in thoughts:
    tr[th["train"]].append(th)
sizes = sorted(len(v) for v in tr.values())
multi_topic = sum(1 for v in tr.values() if len({x["topic"] for x in v}) > 1)

meta = {
    "generated": "2026-09-15",
    "n_thoughts": len(thoughts),
    "n_topics": len(topics),
    "n_trains": ntrains,
    "topics": topics,
    "span_days": round(span_days, 1),
    "t_min": thoughts[0]["t"],
    "t_max": thoughts[-1]["t"],
    "commits": sum(1 for t in thoughts if t["src"] == "commit"),
    "notes": sum(1 for t in thoughts if t["src"] == "note"),
    "train_size_median": sizes[len(sizes)//2],
    "train_size_max": sizes[-1],
    "trains_spanning_topics": multi_topic,
}

with open(os.path.join(OUT, "seed.json"), "w") as f:
    json.dump({"meta": meta, "thoughts": thoughts}, f, separators=(",", ":"))

print(json.dumps(meta, indent=2))
