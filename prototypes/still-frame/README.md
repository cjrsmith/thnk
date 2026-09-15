# Still frame of the Mind Space — throwaway prototype

Answers one question from [#6](https://github.com/cjrsmith/thnk/issues/6): **does a still
frame of the Mind Space read?**

**Throwaway. Not a stack decision.** Plain HTML and hand-rolled canvas projection, no
framework, no build step, no CDN. Open `index.html` by double-clicking it.

## Why there is no motion in it

The motion law changed five times on 15 Sep 2026. Everything here is a static property of
one rendered picture, so nothing in it depends on what radius *means*. The motion question
lives in [#12](https://github.com/cjrsmith/thnk/issues/12) and needs a two-visit instrument
this prototype deliberately does not attempt.

## What to do with it

The bottom bar (or `←` / `→`) cycles the **three arrangements** on the table:

1. **Trains own the bearing** — contemporaries are co-located. 125 bearings, longest arm 17.
2. **Topics own the bearing, Trains deleted** — 22 bearings, longest arm 193.
3. **Topics own the bearing, Trains as a lens** — Trains are recorded but never drawn;
   hovering summons a Thought's contemporaries on demand.

Dimensionality is a *separate* control, because it is a consequence of the angle choice
rather than a peer of it: Topic plateaus in the tens of bearings and 2D suffices forever,
while Train grows without bound and needs 3D within a few years.

The third arrangement is the one to watch. It costs no permanent channel and works under
either encoding — but a lens is worse than co-location for *noticing*: you find the
contemporaries you went looking for, not the ones you stumble across.

Drag to rotate, scroll to zoom, hover for content. **Timed retrieval** is bottom-left: hit
*Start trial*, find the named Thought, click it. It logs median time per condition. Task
time is the measure because [#2](https://github.com/cjrsmith/thnk/issues/2) found subjective
reaction to be anti-signal — users preferred the condition that measurably slowed them.

Right-hand controls sweep `R/r_min`, the Train clustering gap, the attention profile, label
density, wear/dust, and whether Arms are drawn as implied by their Thoughts or as connectors
running from the Self.

## Two crowding numbers, because they disagree

The HUD reports both, and the gap between them is the point:

- **Typical** — mean spacing among bearings that actually reach the core. An Arm with no
  attended Thought never comes near the centre, so only the active working set counts.
- **Minimum** — the closest *pair*, which is what actually collides.

Golden-angle bearings are spread so evenly that a random subset of size `m` keeps the **full**
set's minimum gap once `m > ~√N`. At the even profile with `angle = Train`, 15 of 125 bearings
reach the core: typical spacing is a comfortable 5.24 units, minimum is **0.39** — a 13×
divergence, and the minimum is what you see as overlap.

## Data provenance — read before trusting any number

| Source | Content | Timing |
| --- | --- | --- |
| 270 commits across 5 repos | real | **real** |
| 230 fragments from `~/Notes` | real | **synthesised** — one mtime per file, spread backwards over a plausible window |

500 Thoughts, 22 Topics, 125 Trains, 450 days. Trains are clustered globally by time gap, so
they can span Topics — which is what makes the Train-vs-Topic comparison meaningful.

**Neglect is not derivable from either source.** Radial distribution is therefore *swept*,
not seeded: the attention profile control moves between a mostly-neglected space and a
mostly-held-close one. Any conclusion sensitive to that profile must say so.

Only 11 of 125 Trains span more than one Topic. Partly real (you work on one repo per
sitting), partly an artifact of the seed. If real thinking clusters the same way, Train and
Topic are near-redundant — which is itself relevant to #6's headline question, but this data
cannot settle it.

## The part worth keeping

`layout()` in `index.html` is pure — no DOM, no globals. If the still frame reads, that
function lifts out; the page around it does not.
