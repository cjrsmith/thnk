# thnk

A calm spatial memory. Everything you think about is captured as a Thought and takes its
place in a single space shaped by what you attend to — what matters now stays close, what you
let go drifts outward — so the shape of your thinking is something you can see rather than
something you file.

Note what this does **not** claim. Time is visible *on* a Thought, as wear, but not in where it
sits: the space has two channels, and Attention and grouping have taken both. You can see that
a Thought is old. You cannot see which Thoughts are its contemporaries. That was the founding
promise of this project and it has been eroded by successive model changes rather than
deliberately dropped — see [#6](https://github.com/cjrsmith/thnk/issues/6).

## Language

### The primitive

**Thought**:
The single primitive. Anything captured — an idea, a film to watch, a question, a task, a
fragment of a conversation. It has content and a creation time from the moment it exists;
everything else is optional and can be added later.
_Avoid_: Note, card, item, block, task, entry

**Label**:
A tag describing what is _in_ a Thought. A Thought carries zero or more. Labels are the
material for search and filtering; they are not expressed as position.
_Avoid_: Tag, keyword, category

**Topic**:
The single thing a Thought is _about_. At most one per Thought.
_Avoid_: Project, context, group, primary label

**Value**:
What a Thought is worth, declared by hand and never inferred. An ordered ladder of a few
fixed rungs, rendered as the material the block is made of — glass by default, then bronze,
silver, gold, diamond. Unset is the normal state. Value is global: a Thought is worth what it
is worth wherever it appears.
_Avoid_: Priority, importance, weight, score, rank

**Train of Thought**:
A collection of Thoughts spanning a period of time, belonging together by _context_ rather
than by subject — everything you were thinking about on one Tuesday afternoon. The Thoughts
in one Train may be about entirely different things. A Thought belongs to at most one Train,
or to none until it is triaged.
_Avoid_: Session, thread, stream, burst, arm

**Triage**:
Assigning a floating Thought to a Train of Thought, or starting a new one for it. Done by
hand at first, AI-assisted later.
_Avoid_: Filing, sorting, processing, inbox

### The mind space

**Mind Space**:
The one raw space containing every Thought. It is the app's home and its primary
interface — not a view of the data but the representation of it.
_Avoid_: Galaxy, world, canvas, graph, universe

**The Self**:
The invisible centre of the Mind Space. It is you. New Thoughts appear around it and
everything you attend to is drawn back toward it, so nearness to the Self means *currently
relevant* — never *recently created*.
_Avoid_: Core (reserved for the architectural core), nucleus, origin, home

**The Deep**:
The far outer reaches of the Mind Space, where forgotten Thoughts end up. Nothing is
destroyed there and nothing is hidden; it is simply distant.
_Avoid_: Black hole, edge, periphery, archive (which is a different thing)

**Drift**:
The continuous outward movement of a Thought that is not being attended to. Drift is fast
near the Self and slows the further out a Thought gets, so a Thought recedes sharply once
neglected and then lingers in the Deep rather than vanishing.
_Avoid_: Decay, aging, sinking, expiry

**Attention**:
The accumulated weight of every Interaction with a Thought, each one fading over time. It is
what holds a Thought near the Self, and it is the only thing that does. Rendered as glow: the
most attended Thoughts burn brightest and the Deep is cold. In the Mind Space glow is
redundant with nearness and reinforces it; in a Frame, which has no Self and no distance, glow
is the only sign of Attention there is.
_Avoid_: Score, relevance, heat, priority

**Position**:
Where a Thought sits in the Mind Space. Always *computed*, never stored, never manually set.
Angle comes from the Thought's Train of Thought; distance from the Self is set by Attention.
Because Attention accumulates, Position depends on a Thought's whole history, not on any one
moment in it.
_Avoid_: Coordinates, location, placement (which means something else)

**Arm**:
The visible shape a Train of Thought makes in the Mind Space — its Thoughts in sequence at
the Train's own bearing. An Arm moves as one: the whole Train is held by its most attended
Thought, so returning to any one Thought brings its whole context back.
_Avoid_: Spiral, branch, spoke, cluster

### Time and attention

**Interaction**:
A deliberate act directed at one Thought — something you did to it, not something that
happened to it. Opening it, editing it, changing its Labels, assigning it to a Train of
Thought, and reviving it all count. **Looking at a Thought is not an Interaction**, nor is
being rendered, appearing in search results, gathering it into a Tray, or adding it to a
Frame. **Arranging is not attending**: dragging a Thought's Placement around a Frame is work
directed at the Frame, not at the Thought, and never counts however much of it you do.
Creating a Thought is itself an Interaction, so nothing is ever born neglected. Interactions
differ in weight, and some are worth nothing — see Dusting.
_Avoid_: Touch, access, view, use

**Age**:
How long ago a Thought was created. It only ever grows, and no act reverses it. Rendered as
wear — the block cracks, chips and diminishes. Age has no effect on Position.
_Avoid_: Staleness, decay, lifespan

**Neglect**:
How long since a Thought was last interacted with. Rendered as dust, which falls away the
moment you touch it, revealing the Age beneath. Distinct from Attention: Neglect is *recency*,
Attention is *accumulated weight*. A Thought touched once yesterday has no dust but little
Attention; one touched fifty times last year is dusty and has drifted far out.
_Avoid_: Staleness, inactivity, dormancy, distance

**Dusting**:
Clearing the dust from every Thought in a Frame at once — blowing off the cobwebs. Dusting is
an Interaction, so Neglect genuinely resets, but it carries **no Attention weight**, so nothing
moves in the Mind Space. It is the one act that changes how a Thought looks without changing
where it sits.
_Avoid_: Refreshing, touching, bumping, cleaning

**Popped**:
Acted upon, and so out of the Mind Space — the film watched, the idea built, the thought
brought into reality. The positive exit, and the point of capturing anything. Popping is
global and immediate: a popped Thought leaves the Mind Space and every Frame at once. The act
is kept — when it was popped, and whether it was *done* or *dropped* — but a popped Thought no
longer appears in ordinary search and must be asked for. There is no separate deletion.
_Avoid_: Done, completed, closed, archived, deleted

**Archive**:
Where a Thought goes if it is ever allowed to expire — old *and* long-neglected, under a
limit the user sets in years, always by notification and never silently. Offers keep, revive,
or delete. A Thought held in a Frame is exempt.
_Avoid_: Trash, bin, cold storage, inbox

**Revival**:
Returning a Thought from the Archive to the Mind Space. Revival is an Interaction, so it
restores Attention — but Age is untouched. Revival grants standing, not youth.
_Avoid_: Restore, undelete, refresh, renew

### Arrangements

**Tray**:
A transient gathering of Thoughts pulled out of the Mind Space by searching or by hand. A Tray
has no arrangement, no name and no permanence: it holds what you have just grabbed so you can
see it. One exists at a time, it does not survive quitting, and it is thrown away by ignoring
it. Most Trays never become anything more — looking was the point.
_Avoid_: Basket, selection, staging, handful, drawer (which is how it opens, not what it is)

**Framing**:
Turning a Tray into a Frame. The only way a Frame is made.
_Avoid_: Saving, promoting, converting

**Frame**:
A named, saved arrangement of Thoughts on an open plane — a frame of mind. Where the Mind
Space is computed, a Frame is planar and arranged by hand. The same Thought may appear in many
Frames without being copied, and a Thought renders identically wherever it appears; a Frame
simply has no position to read.
_Avoid_: View, layer, workspace, board, lens

**Placement**:
A Thought's stored position **and size** within one Frame. Both are set by hand and mean
nothing outside that Frame — a Thought sized large in a backlog to say *this is a big piece of
work* is unchanged everywhere else. Placements exist only in Frames; the Mind Space has none.
_Avoid_: Position (which is computed), coordinates
