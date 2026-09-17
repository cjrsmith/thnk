# thnk

A canvas for the things you think. Anything you think about is captured in a keystroke, from
wherever you are, and lands on a strip at the edge of one infinite canvas. You drag what matters
onto the canvas and put it where it makes sense to you, and things you put near each other are
read as belonging together.

Note what this does **not** claim. The app arranges nothing and never will: the only thing that
moves is what you drag. What it does instead is *show you what it knows* — a block carries its
own age, its neglect, its worth, and the burst of thinking it arrived in, written on its surface.
That is what makes a canvas you arranged by hand still legible six months later. If you never drag
a Thought off the strip, it stays on the strip, and that is a normal outcome rather than a
backlog.

## Language

### The primitive

**Thought**:
The single primitive. Anything captured — an idea, a film to watch, a question, a task, a
fragment of a conversation. It has content and a creation time from the moment it exists;
everything else is optional and can be added later.
_Avoid_: Note, card, item, task, entry

**Block**:
How a Thought is drawn: a solid object with a shape, a colour, a material and a weathered
surface, carrying the Thought's text. A Thought renders as the same Block wherever it appears.
Block is about appearance, Thought is about substance — use the word that matches what you mean.
_Avoid_: Card, node, tile, icon

**Label**:
A tag describing what a Thought is about, or what is in it. A Thought carries zero or more. A
Label may be a word, an emoji, or both, and its emoji is stuck on the Block like a sticker.
Labels are the material for search, and they are the **only global statement of aboutness the
model has**.
_Avoid_: Tag, keyword, category, topic

**Train of Thought**:
A run of Thoughts captured in one breath — everything that came out of your head in one sitting.
A Thought belongs to at most one Train, or to none. The Train is **declared at capture**, either
by continuing the one in progress or by naming an earlier one, and is never inferred afterwards.
The Thoughts on one Train need not be about the same thing; what they share is the moment they
arrived. Rendered as the Block's **shape and colour together**.
_Avoid_: Session, thread, stream, burst, topic

**Value**:
What a Thought is worth, declared by hand and never inferred. An ordered ladder of a few fixed
rungs, rendered as the material the Block is made of — glass by default, then bronze, silver,
gold, diamond. Unset is the normal state, and Value is global: a Thought is worth what it is
worth wherever it appears.
_Avoid_: Priority, importance, weight, score, rank

**Origin**:
How a Thought came to exist — typed at capture, imported from elsewhere, returned by an agent.
Recorded once and never rewritten: restoring a backup preserves each Thought's original Origin
rather than stamping the whole batch as an import.
_Avoid_: Source, provenance, created-by, import

### The canvas

**Canvas**:
The one infinite plane the app is made of. It is the only surface, and it is the app's home.
Position on it is stored, and set **only by hand** — nothing is ever placed, moved or tidied by
the system.
_Avoid_: Board, whiteboard, workspace, space, mind space

**Landing Strip**:
The column at the edge of the Canvas where a captured Thought arrives, newest at the top. It is
where a Thought lives until you place it, and reading down it reads backwards through time.
Staying there indefinitely is an ordinary fate, not a failure to process.
_Avoid_: Inbox, tray, queue, feed, dock

**Placement**:
A Thought's stored **position and size** on the Canvas. Both are set by hand. Size says *how big
this is to me* and is declared, not derived from anything.
_Avoid_: Position, coordinates, location

**Group**:
Blocks close enough together on the Canvas to be read as one thing. Membership is **computed from
position and never stored**: drag a Block near others and it joins, drag it away and it leaves.
A Group is drawn as an outline around whatever it currently holds, and it can be named. A Group is
how you say what Thoughts have to do with each other; Labels are how you find them in order to
say it.
_Avoid_: Cluster, box, container, folder, topic

**Window**:
A plain panel that opens over the Canvas showing a collection of Blocks as a grid: everything on
one Thought's Train, or everything sharing one Label. It is the only view other than the Canvas,
and it is transient — you open it, look, and dismiss it. It replaces drawing lines between
Blocks.
_Avoid_: Frame, panel, modal, view, lens

### Time and wear

**Interaction**:
A deliberate act directed at one Thought — something you did to it, not something that happened
to it. Opening it, editing it, changing its Labels, and assigning it to a Train all count.
**Looking at a Thought is not an Interaction**, nor is being rendered, appearing in search
results, or appearing in a Window. **Arranging is not attending**: dragging a Placement around the
Canvas is work directed at the Canvas, not at the Thought, and never counts however much of it you
do. Creating a Thought is itself an Interaction, so nothing is ever born neglected.
_Avoid_: Touch, access, view, use

**Age**:
How long ago a Thought was created. It only ever grows, and no act reverses it. Rendered as
wear — the Block cracks, chips and diminishes.
_Avoid_: Staleness, decay, lifespan

**Neglect**:
How long since a Thought was last interacted with. Rendered as dust, which falls away the moment
you touch it, revealing the Age beneath. Age is how old a thing is; Neglect is how long you have
left it alone.
_Avoid_: Staleness, inactivity, dormancy

**Popped**:
Acted upon, and so gone — the film watched, the idea built, the thought brought into reality. The
positive exit, and the point of capturing anything. The act is kept — when it was popped, and
whether it was *done* or *dropped* — but a popped Thought no longer appears in ordinary search and
must be asked for. There is no separate deletion.
_Avoid_: Done, completed, closed, archived, deleted

## Vocabulary not in play

These words have settled meanings in this project's history and are recorded so they are not
quietly reused for something else. None of them is V1 vocabulary.

**Retired** — cut from the model, not merely deferred:

- **Topic** — "the single thing a Thought is about", one per Thought. Absorbed by **Label** for
  finding things and by **Group** for saying what they have to do with each other.
- **Attention** — accumulated Interaction weight, decaying over time, rendered as glow. It existed
  to compute a Thought's distance from the Self; with no Self there is nothing for it to feed.
  The interaction log that would have fed it is still written.
- **The Self**, **the Deep**, **Drift**, **Arm**, and **Position** as a *computed* quantity — all
  properties of the Mind Space, which no longer exists.
- **Tray** — a transient gathering pulled out of the Mind Space by searching. Its two jobs are now
  done by the **Landing Strip** (holding what has just arrived) and the **Window** (holding what a
  question returned).

**Held back** — intact, deferred past V1, and expected back:

- **Mind Space** — a computed spatial representation of every Thought. A visualisation layer over
  the same data, to be re-derived from scratch rather than resumed.
- **Frame** — a named, saved arrangement, of which there would be many. The Canvas is the single
  unnamed one.
- **Cluster** — a Group with *stored* membership, which can be reparented, reflowed and queried.
- **Archive**, **Revival**, and automatic expiry — what happens to a Thought both old and long
  neglected.
- **Triage** — assigning an untrained Thought to a Train *after* capture. Capture already files
  the common case; this is the leftovers, and AI-assisted later.
- **Dusting** — clearing the dust from many Thoughts at once.
