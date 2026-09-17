# thnk — handoff for the re-scope

**Written** 17 September 2026 · **Repo** `/home/csmith/Projects/thnk` (GitHub `cjrsmith/thnk`, **public**)
**Previous session** charted and drove a wayfinder map through ~36 hours of design. Everything is
pushed; `main` is at `14d5fc1`.

---

## 1. What the next session is for

The user has **re-scoped the project**, in their words:

> "I've been thinking about actually just sticking to the main thing which is going to be adding
> things, adding thoughts into the tray that I can move around. I think that should be the main
> thing and we should forget about the whole 3D galaxy space thing and how we represent the data.
> So I'm really going to simplify this."

So: **capture → Tray → arrange in a Frame.** The 3D spatial Mind Space is abandoned.

This is a scope reduction, not a restart. A large amount of settled design survives it, and the
first job is to work out precisely what does. Do not re-derive it — §3 and §4 below are the map.

**Do not begin by rewriting tickets.** The existing map was built around a destination that no
longer exists. Establish the new destination with the user first (§6).

---

## 2. Where everything lives

Read these rather than reconstructing them:

| What | Where |
| --- | --- |
| **The domain glossary — the authority on vocabulary** | `CONTEXT.md` |
| Computed vs declared visual channels | `docs/adr/0001-computed-channels-and-declared-channels.md` |
| **What the abandoned effort found, written for exactly this moment** | `docs/mind-space-findings.md` |
| Original brainstorm; treat as context, not direction | `docs/research.md` |
| The wayfinder map (destination, notes, decisions, fog, out-of-scope) | https://github.com/cjrsmith/thnk/issues/1 |

Resolutions live as the **last comment** on each closed issue. Ticket comment chains record up to
five superseded models — read `CONTEXT.md` and the resolution, not the chain.

Throwaway prototype branches, all local-only: `prototype/still-frame`, `prototype/bearing`,
`research/*`. Two stale agent worktrees exist under `.claude/worktrees/` and can be pruned.

---

## 3. What survives the re-scope

These were decided, are independent of the 3D space, and should be carried forward.

- **The Thought is the primitive**, with Label (many, searchable), Topic (one, what it is about),
  Value (declared, an ordered rung), Origin (how it entered; a restore preserves it).
- **Capture** — [#4](https://github.com/cjrsmith/thnk/issues/4). A resident process, 100ms p99 to
  caret, never loses a keystroke, summoned via a `special:thnk` Hyprland workspace. Capture **asks
  for nothing**; a `/` constructs, `@` references grammar lets you declare instead. `Ctrl+Enter`
  means "another one, in the same breath".
- **The Tray** — [#11](https://github.com/cjrsmith/thnk/issues/11). Transient, additive across
  several searches, one at a time, never persisted. **Now the centre of the product.**
- **Frames** — also #11. Infinite plane, half-block snapping, drag/box-select/tidy-into-column,
  made only by framing a Tray. Nothing ever moves except what you drag.
- **Two exits, not three.** Pop absorbed Delete, and records *done* or *dropped*.
- **Age as wear, Neglect as dust** — and ADR-0001's rule: *the system weathers the block; you shape
  and cast it.* Computed channels act on the surface; declared ones are form and substance.
- **Arranging is not attending.** Moving a Placement is never an Interaction, so grooming a backlog
  leaves the dust intact. Gathering into a Tray does not count either.
- **Acts are stored; conditions are computed.** This predicted every storage answer in
  [#5](https://github.com/cjrsmith/thnk/issues/5) and is worth keeping as a standing rule.
- **The schema** — #5's resolution comment. Mostly survives; see §4 for the parts that do not.
- **Omarchy theming** — [#3](https://github.com/cjrsmith/thnk/issues/3). Ship a
  `themed/thnk.<ext>.tpl`; read the rendered file from `~/.local/state/omarchy/current/theme/`;
  watch the *parent* directory because the theme dir is replaced wholesale. Fully unaffected.
- **One portable finding from [#15](https://github.com/cjrsmith/thnk/issues/15)**: *position and
  colour must group by the same thing, or they fight.* It is a claim about channel agreement, not
  about 3D, and it applies to any arrangement surface including a Frame.

---

## 4. What dies with the Mind Space — and the holes it leaves

**Concepts with no home once the space goes:** the Self, the Deep, Drift, Arm, and Attention *as
distance*. Also golden-angle bearings, `r_min`, 2D-vs-3D, the core-capacity maths, and Topic-pull.

**Tickets that are now moot or need rewriting from scratch:**
[#12](https://github.com/cjrsmith/thnk/issues/12) (motion damages memory — no motion),
[#14](https://github.com/cjrsmith/thnk/issues/14) (six channels — but see below),
[#8](https://github.com/cjrsmith/thnk/issues/8) (stack — its hard 3D requirements evaporate),
[#9](https://github.com/cjrsmith/thnk/issues/9) (search — its subject was searching *the space*),
[#13](https://github.com/cjrsmith/thnk/issues/13) (triage), [#10](https://github.com/cjrsmith/thnk/issues/10) (the V1 spec).

**Four questions the re-scope opens. These are the substance of the next conversation.**

1. **What do you see when you open the app?** The Mind Space was the home screen. With it gone
   there is a hole: the Frames list, a search box, the last Frame, or something new.
2. **Do Trains of Thought still earn their place?** Their entire job was owning the angular
   channel. But #15 measured that **114 of 125 Trains sit inside a single Topic**, and 83% of
   Train-mate pairs share a Topic — so Trains and Topics were already near-redundant, and the
   capture-time win (`Ctrl+Enter` files for free) may be deliverable by Topic alone.
3. **Does Attention survive without distance to express it?** Glow remains available, and dust
   still means something. But Attention's whole purpose was positional. If it goes, the interaction
   log, the decay constant τ, and the per-kind weight table all go with it — a large simplification,
   and #5's schema changes.
4. **What replaces the Mind Space as the thing that makes this not-just-another-notes-app?** The
   original thesis was that seeing thoughts in space beats a list. Frames are a well-trodden
   surface (Obsidian Canvas, Miro). Worth being explicit about the answer rather than discovering
   later that the differentiator left with the galaxy.

**#14 is worth keeping in some form.** A Frame has no positional encoding of time, so wear, dust,
glow and colour are the *only* way a Thought's metadata is visible there. The channels matter more
after the re-scope, not less — only the 3D-with-shaders framing dies.

---

## 5. Things that will bite you

- **Ticket bodies lie.** Several were written five model changes before they were read. The
  previous session's clearest lesson: *re-read the map before building, not after.*
- **An instrument too coarse for one arm of a comparison does not produce a null result — it
  produces a confident wrong one.** Both of #6's errors were instances.
- **#15's prototypes silently encoded creation order as radius, not Attention**, in every build
  since #6. Treat prototype findings as provisional until the layout is checked against the
  glossary.
- **Multiple Claude sessions work this repo concurrently**, editing the same issues and sometimes
  `CONTEXT.md`. Use `ListAgents` / `SendMessage`. Claim a ticket by assigning it *before* working.
  One session left a stale claim when it ended.
- **The repo is public.** The user knows; it is worth remembering before writing anything candid.
- The user pushes back well and changes direction decisively. Give recommendations, not surveys,
  and say plainly when they have overturned something they previously decided.

---

## 6. Suggested first moves

1. Call the Skill tool for **`wayfinder`** — the effort is a wayfinder map and the re-scope is a
   re-charting, not a fresh start.
2. Call it for **`grilling`** and **`domain-modeling`** together, and settle the **new destination**
   before touching any ticket. The four questions in §4 are the frontier.
3. Then: rewrite the map's Destination, move the Mind Space and its concepts to **Out of scope**
   (they are ruled beyond the destination, not fog), close or rewrite the moot tickets, and update
   `CONTEXT.md` — it currently opens by describing a space that no longer exists.

**Suggested skills:** `wayfinder`, `grilling`, `domain-modeling`, and `prototype` when a question
needs a rough artifact to react to. `research` only for facts outside the repo. `omarchy` if the
theming or keybind work comes up.
