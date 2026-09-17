# Computed channels and declared channels use separate visual registers

A Thought's block carries several channels of information, and they come from two different
places: some the system computed from facts, and some the user declared by hand.
We decided these may never share a visual register. **The system weathers the block; the user
shapes and casts it** — computed channels act only on the *surface*, declared channels are
*form* and *substance*. If the two looked alike, you could never tell what the app is telling
you from what you told it yourself, which is the one thing a representational interface cannot
afford to get wrong.

## Amended, 17 September 2026

The decision below stands unchanged. The **roster** it was written against does not, because the
re-scope that retired the Mind Space also retired two of its channels and moved a third. As of the
re-scope:

- **Computed, and only ever on the surface**: wear (Age), dust (Neglect), **shape and colour
  together** (Train of Thought).
- **Declared, as form and substance**: size (Placement), material (Value), and the **emoji sticker**
  a Label puts on the block.

Glow is gone with Attention. Colour was Topic's and is now the Train's, sharing that encoding with
shape — which is legitimate *within* one register, and is not the register collision this ADR
forbids. Whether shape and colour can in fact carry a Train count that grows without bound is an
open question on the map, not a settled one.

The final sentence of **Consequences** referred to the Mind Space, which no longer exists. Declared
size now lives on the Placement because a Placement is the only hand-set thing on the canvas, and
the reason is unchanged: a declared channel belongs wherever the hand-set facts already live.

## Considered Options

The alternative was simply rationing channels — capping the block at four or five and refusing
new ones. That was the position before size and Value were proposed, and it fails the moment a
genuinely useful channel arrives: you end up trading away something already earned. The
register split scales instead of rationing, and it happened to resolve the concrete collision
that prompted it. Dust, wear and material were all competing for the same surface; once
weathering sits *on top of* material rather than replacing it, gold stays legibly gold whether
pristine or filthy, and a cracked gold block reads as "a valuable thing you have neglected" —
which is exactly the sentence it should say.

## Consequences

Every future channel must declare which register it belongs to before it can be designed, and
a declared channel can never be expressed as surface treatment however convenient that is.
This is why Value is rendered as material and is **not** theme-swappable: the theme dresses the
background, the mist around Trains of Thought, and the chrome, but never the Thoughts. It is
also why declared size lives on the Placement rather than the Thought — the Mind Space has no
hand-set properties at all, and a manually sized block there would be the first.
