# Mind Space prototypes — throwaway

**Open `flythrough.html`.** Double-click it; nothing to install.

`index.html` is the earlier still-frame version. It is kept only as a record of the geometry
analysis on [#6](https://github.com/cjrsmith/thnk/issues/6); **it asked the wrong question**
and should not be used to judge the design.

## What changed, and why

The still frame timed you finding a Thought by looking for it. That tests a job the Mind Space
does not have — it was settled earlier that the Mind Space is *primarily representational* and
**search does retrieval**. It also rendered Thoughts as dots with labels floating over them,
orbited a fixed ball, and relitigated Train-vs-Topic, which [#4](https://github.com/cjrsmith/thnk/issues/4)
had already closed by settling that a Train forms at capture.

`flythrough.html` fixes those:

| Still frame | Flythrough |
| --- | --- |
| Orbit a ball, zoom in and out | **Fly through it** — `WASD`, `R`/`F`, drag to look, `shift` to boost |
| Dots with labels overlaid | **Blocks with the Thought written on them** |
| Click one at a time | **Click opens a card anchored to the block**, its Train highlighted, `↑`/`↓` steps through |
| Timed retrieval task | **Search** — the actual way you would find something |
| Everything crowded together | **Spread** control; you move among them |

## What it is for

Not "can you find things". That is search's job. The question is:

> **Does flying through this read, and does it feel like somewhere you would keep your thinking?**

Worth watching for:
- Do blocks stay readable at the distance you naturally fly at, or must you get nose-to-nose?
- When you open one, does seeing its Train light up tell you anything you wanted to know?
- Do wear and dust read as *different things* at a glance, or just as noise?
- Do 22 Topic colours stay distinguishable once blocks overlap?
- Is the Deep a place you would go, or a mess you would avoid?

## Data

500 Thoughts, 22 Topics, 125 Trains, 450 days — **270 real commits** (real timestamps) plus
**230 `~/Notes` fragments** (real content, **synthesised** timing, since a file has one mtime).

**Attention is swept, not seeded.** Neglect cannot be derived from commit history, so the
Far/Even/Near control moves between a mostly-neglected space and a mostly-attended one. Any
reaction that depends on that setting should say which one it was.

## The part worth keeping

`layout()` is pure — no DOM, no globals. It says nothing about motion, deliberately: the motion
law changed five times on 15 Sep 2026 and lives in [#12](https://github.com/cjrsmith/thnk/issues/12).
