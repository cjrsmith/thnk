# Does the bearing belong to Trains or Topics? — throwaway

**Open `arms.html`.** Double-click it; nothing to install.

Built for [#15](https://github.com/cjrsmith/thnk/issues/15). It replaces the
[#6](https://github.com/cjrsmith/thnk/issues/6) flythrough for this question only —
`prototypes/still-frame/` stays as the record of the geometry analysis.

## Read this before you fly it

The ticket assumed Train-arms and Topic-arms show you different neighbours. **In this seed
they mostly don't.**

| | |
| --- | --- |
| Trains that stay inside one Topic | **114 of 125** |
| Train-mate pairs sharing a Topic | **83%** (2414 of 2900) |
| Thoughts whose Train holds no one else | **42** — co-location delivers them nothing |
| Largest Topic | **193 of 500 Thoughts** |

A Train is almost always a run *within* one Topic. So arrangement 1's unsought contemporary is,
83% of the time, also an unsought topic-mate — someone you'd have bumped into under arrangement 3
anyway. **The angular channel is only buying the 17%.** Fly free-range and you will mostly compare
each arrangement against itself and find no difference: the same confident-wrong-answer shape #6
warned about, pointing the other way this time. Hence the **Send me somewhere that discriminates**
button, which drops you in one of the **11** Trains that actually cross a Topic boundary.

## What changed from the #6 flythrough

Three things, and all three change what an **Arm** is.

### 1. Radius is per-Thought Attention, not creation order

The old `layout()` gave a whole arm one attention score and stepped its members outward by
creation index — so radius-within-an-arm secretly meant **time**, which the glossary forbids
(*Age has no effect on Position*). Now each Thought sits at its own radius and an Arm is **held at
its inner tip** by its most attended member, with less-attended members trailing outward.

Arm *length* therefore stops being member count and becomes **the spread of Attention inside the
arm**. A Train you worked through this morning is a tight bright clump near the Self. A Train where
you kept returning to one Thought and forgot the rest is a long tail with its holder at the front.
The holder wears a small green chevron.

### 2. Cohesion is a dial, not a rule

*"An Arm moves as one, held by its most attended Thought"* is the open half of this ticket, so it
is a slider rather than an assumption.

- **Cohesion = 0** — every Thought floats at its own radius. No context restoration at all.
- **Cohesion = 1** — every member is pulled to its holder's radius. A rigid clump that moves as one.

This one control replaces what would have been a separate arrangement-3 sub-toggle, and it sweeps
in *either* arrangement, so the two are compared on identical machinery.

### 3. An Arm is a volume, not a line

Members drift laterally around a **curving** spine instead of queueing one behind the next — the
spiral-galaxy reading rather than a row of beads. Two constraints on that:

- The swirl is a function of **radius alone**, so the arc is a fixed landmark. A Thought slides
  along a track that never itself moves. A curve whose *shape* drifted would be precisely the
  system-driven rearrangement [#2](https://github.com/cjrsmith/thnk/issues/2) named as the enemy
  of spatial memory. **Worth watching for directly**: as Attention changes, a Thought on a curved
  arm sweeps sideways as well as outward. Is the arm still the thing you remember?
- Lateral scatter is **self-similar** — proportional to the arm's own extent, with a floor growing
  as the cube root of its size. Density per member is therefore constant, so a 3-block Train arm
  and a 193-block Topic arm are the same kind of object at different sizes. Neither arrangement is
  judged at a fidelity the other isn't given. **That fairness is the point** — #6's lesson was that
  an instrument too coarse for one arm produces a confident wrong result, not a null one.

## The instrument

The two counters that decide the ticket, shown bottom-left per arrangement:

- **Hold `L`** — summon the Train of whatever is under the cursor. The Train list is **never
  passively displayed** in any arrangement (the #6 flythrough showed it always, in both arms,
  which made this unmeasurable). Every summon is counted. **Heavy summoning under arrangement 1
  means the channel is being paid for and not used.**
- **Press `N`** on a **hovered** block — "I wasn't looking for this". Hovered, not opened, because
  reading a neighbour *without* clicking it is exactly what co-location is supposed to buy. Each
  mark is classified **contemporary** / **topical** / **neither**, relative to whatever you last
  opened or were sent to.
- Opens that weren't in your search results are logged automatically. That half is the honest
  signal; the keypress catches noticing-without-opening.

Both kinds of accident are counted, deliberately. Arrangement 3 has its own serendipity — the
unsought *topic*-mate — and scoring only contemporaries would hand arrangement 1 the result by
construction.

`Copy the log` puts the tallies and the full event list on the clipboard (and the console) to
paste onto the issue.

## Configurations

`#arr=lens&cohere=1&dim=2&profile=close` in the URL reopens an exact view. `arr` is
`train` | `topic` | `lens`.

One is worth opening first, `#arr=lens&cohere=1`: at full cohesion arrangement 3 pins all 22
Topic arms near the Self — each held by the best of its members, and one of them has 193 chances —
so the whole space collapses into a knot and **the Deep empties completely**. That is
[#13](https://github.com/cjrsmith/thnk/issues/13)'s wrong-weld cost multiplied by sixty: a bad weld
drags 3 Thoughts under arrangement 1 and 193 under a cohering arrangement 3.

## What it can't tell you

- **Attention is swept per Thought, not seeded.** Neglect isn't derivable from commit history.
  Any reaction that depends on it should say which sweep it was under.
- Arm shape is tuned by eye. If an arrangement wins, the slider values that made it win are part
  of the answer — record them.
- It says nothing about **motion**; the motion law lives in
  [#12](https://github.com/cjrsmith/thnk/issues/12). Radius here is a static score, not a drift law.
- It does not settle **2D vs 3D**. The toggle is kept so the consequence stays visible, but the
  map has dimensionality downstream of this ticket.

## The part worth keeping

`layout()` is pure — no DOM, no globals. Everything below the shell marker is throwaway.
