# What the Mind Space effort found

The V1 effort mapped in [#1](https://github.com/cjrsmith/thnk/issues/1) was **paused on
17 September 2026** to re-scope the project. The spatial Mind Space — the 3D universe of
Thoughts on bearings around a Self — is being left behind, and whatever replaces it is a fresh
effort rather than a resumption of that map.

This file exists because the map records a **route to a destination that is being redrawn**, and
most of what was learned is worth more than the route. What follows is what survives the
re-scope: facts about the data, one model correction, and one finding that generalises past any
particular layout. Detail lives on the tickets linked from each section.

## The finding that outlives the layout

**The angular channel and the colour channel must encode the same grouping, or they fight.**

Colour was already Topic's — settled long before, and reaffirmed by
[#2](https://github.com/cjrsmith/thnk/issues/2) ("Topic-as-appearance survives") and by
[ADR-0001](adr/0001-computed-channels-and-declared-channels.md), which makes colour a *computed*
channel of Topic. Giving the **bearing** to Trains therefore set two channels against each other:
each Train arm was a mix of Topic colours, and the space read as noise. Giving the bearing to
Topics made the two channels reinforce — one colour per arm, and the space resolved into legible
regions.

That was the user's read at block fidelity, and it is the closest thing
[#15](https://github.com/cjrsmith/thnk/issues/15) reached to an answer. It is a statement about
**channel agreement**, not about 3D, so it should survive into whatever the re-scope produces: any
representation that groups by position and colours by something else will have the same problem.

## Facts about the actual data

Measured from the real seed — 500 Thoughts drawn from 270 real commits and 230 `~/Notes`
fragments over 450 days. These are facts about how this user actually thinks, so they constrain
any future design.

| | |
| --- | --- |
| Trains that stay inside a single Topic | **114 of 125** |
| Train-mate pairs sharing a Topic | **83%** (2414 of 2900) |
| Thoughts whose Train holds no one else | **42** (8.4%) |
| Largest Topic | **193 of 500 Thoughts** |
| Topic count | 22, and plateauing |
| Train count | 125 in 15 months, growing without bound |

**A Train of Thought is almost always a run within one Topic.** This is the fact that most
reshapes the design, and it was not suspected before it was measured. Grouping by Train and
grouping by Topic produce nearly the same neighbourhoods 83% of the time, so the two compete over
a 17% margin — and 42 Thoughts have no contemporaries at all, so any mechanism built on
co-locating contemporaries does nothing for one Thought in twelve.

The skew matters too: one Topic holds 38% of everything. Any structure that treats a group as a
unit has to survive a group of 193 as well as the median group of 3.

## The model correction

**Radius is per-Thought Attention. It is never creation order.**

The [#6](https://github.com/cjrsmith/thnk/issues/6) prototype gave each group a single Attention
score and then stepped its members outward by creation index — so distance-from-the-Self secretly
meant *time*, which the glossary explicitly forbids (*Age has no effect on Position*). The error
was invisible because a time-ordered line looks plausible; it surfaced only when the arms were
rebuilt as volumes and something had to decide where along the arm each block sat.

Rebuilding it correctly gave the group a shape that means something: a group is **held at its
inner tip** by its most attended member, and its *length* is the **spread of Attention inside it**
rather than its member count. A group worked through this morning is a tight clump near the Self;
one where a single member kept being revisited while the rest were forgotten is a long tail.

**Watch for this class of bug.** A prototype that renders a plausible picture can encode a rule
nobody chose. It was caught by changing the shape, not by reading the code.

## The cost of "a group moves as one"

The glossary had Attention including *"that of the Arm it sits on, since an Arm moves as one and
is held by its most attended Thought"*. Made into a dial and swept, that rule turns out to be
load-bearing and dangerous at scale:

- At full cohesion with **Trains** owning the bearing, arms stay distributed; radii span 12.5–89.8.
- At full cohesion with **Topics** owning the bearing, every one of the 22 arms is held by the best
  of its members — and one of them gets 193 chances — so all 22 collapse toward the Self. Radii
  span 12.5–64.5 and **the Deep empties completely.**

So group cohesion is safe for small groups and destroys the space for large ones. Restated without
reference to any layout: **coupling a group's position to its best member does not scale with group
size.** It also multiplies the cost of a mis-grouping by the group's size — a wrong assignment drags
3 Thoughts under Trains and 193 under Topics, which is
[#13](https://github.com/cjrsmith/thnk/issues/13)'s concern at sixty times the magnitude.

## What was never tested

Stated plainly so a future reader does not assume more was settled than was.

- **The serendipity question was not run.** [#15](https://github.com/cjrsmith/thnk/issues/15) asked
  whether co-location actually delivers accidents — whether you notice contemporaries you were not
  looking for, or reach for the lens anyway. The prototype was instrumented to count exactly that
  (a counted lens, an "I wasn't looking for this" mark, both kinds of accident classified) but no
  session was logged. **The answer recorded is about legibility, not serendipity.**
- **2D versus 3D was never chosen.** The geometry is known — 3D's advantage over 2D at the core is
  exactly `√N/π`, so it only pays above about 10 bearings — but the choice was left downstream of
  #15 and #15 did not settle it.
- **Attention parameters** (τ, impulse magnitudes, settling period, per-kind weights) were never
  given values. Attention in every prototype was *swept*, never seeded — Neglect cannot be derived
  from commit history — so no prototype reaction is evidence about real Attention behaviour.

## Where things are

- **Map**: [#1](https://github.com/cjrsmith/thnk/issues/1) — Destination, Notes, and every decision
  with a link to the ticket holding its detail.
- **Glossary**: [CONTEXT.md](../CONTEXT.md) — describes the Mind Space model as it stood when the
  effort paused. Expect the re-scope to invalidate parts of it; it was not edited to anticipate that.
- **Prototypes**, both throwaway, on branches out of `main`:
  - `prototype/bearing` — `prototypes/bearing/arms.html`. Three arrangements, groups as curving
    volumes, cohesion/swirl/thickness dials, the counted lens and accident marks. Double-click it.
  - `prototype/still-frame` — `prototypes/still-frame/flythrough.html`. The #6 version. Contains the
    creation-order bug described above; kept as the record of the geometry analysis.
- **Research**: [docs/research.md](research.md) — context, not direction. Several of its
  recommendations rest on premises the map retracted.
