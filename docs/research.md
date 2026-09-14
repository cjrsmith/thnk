# Thought / Memory App — Product and Architecture Research

> A calm spatial memory for everything you think about: capture thoughts, connect them, rediscover them, and eventually hand them to agents to act on.

**Status:** Repository seed document; consolidated brainstorming, not an approved implementation specification.  
**Prepared:** 14 September 2026.  
**Primary source:** “Brainstorm thought memory app,” conversation ID `6aa41d36-a104-83eb-ab7b-2d95c3f4d374`, plus its attached `task_management.md`, reproduced in Appendix A.  
**Intended use:** Product context, architecture exploration, and continuity for future development and agent sessions. No application name, repository structure, stack, sync provider, or launch scope has been formally selected.

## Contents

- [Product concept](#1-product-concept-and-motivation) and [decision register](#2-direction-and-decision-register)
- [Thought model](#3-domain-model-thought-as-the-primitive) and [lenses/search](#4-lenses-views-and-search)
- [Spatial UI, globe, and keyboard interaction](#5-visual-and-interaction-design)
- [Colour and themes](#6-colour-semantics-and-themes)
- [AI and agents](#7-ai-and-agent-integration)
- [Omarchy/Quickshell](#8-omarchy-and-quickshell-integration) and [mobile capture](#9-cross-platform-mobile-and-capture-everywhere)
- [Architecture and local-first sync](#10-architecture-and-persistence)
- [Technology tradeoffs](#11-technology-tradeoffs) and [Obsidian comparison](#12-obsidian-comparison-and-differentiation)
- [MVP/phases](#13-mvp-and-phased-development), [principles](#14-principles-to-preserve), [open questions](#15-open-questions), and [next steps](#16-recommended-next-steps)
- [Original source attachment](#appendix-a--original-task_managementmd) and [verified references](#appendix-b--primary-source-verification-and-references)

## Reading guide and evidence status

This document consolidates all six turns available from the referenced conversation, including the original attachment. Later user clarifications take precedence over earlier assistant interpretations. The conversation records a request for mock art and later feedback about that art, but the retrieved record contains no actual generated image to inspect. The visual requirements below come from that feedback and the written discussion; they are not a reconstruction of unseen pixels.

Three kinds of statements are distinguished:

- **User direction:** Explicit goals, preferences, or corrections expressed by the user.
- **Session proposal:** An idea or recommendation developed in the conversation, still subject to validation.
- **Consolidation recommendation:** A clarification or practical next step added here to make the research actionable. These are not retrospectively attributed to the user.

Technical facts supported by current primary-source checks appear in Appendix B. The original assistant's opaque citation tokens are not reusable references and have not been copied as evidence. Earlier claims about product superiority, ease of sync, or a stack being “best” are treated as hypotheses rather than established findings.

## 1. Product concept and motivation

### 1.1 The problem

The user currently captures thoughts in many phone/Notepad notes. Individual notes often contain unrelated ideas, informal backlogs, films to watch, gifts, and planning fragments. Information becomes hard to find because its original container does not match the context in which it is needed later.

AI conversations create a second form of loss. A discussion may explore X, Y, Z and A, B, C, then implementation proceeds with X, Y, Z. The deferred ideas and the reasoning connecting them remain buried in conversation history. The user wants to see what is still outstanding, with the original context intact.

The desired tool sits between simple notes, a to-do list, and heavyweight project management. It is primarily a personal thought-management tool and external long-term memory. It should also be capable of becoming shared memory for the user and agents.

### 1.2 Product thesis

**Everything captured starts as a Thought.** It can later behave like an idea, task, question, decision, reference, film recommendation, gift idea, reminder, requirement, or agent job. Capture must not depend on deciding which of these it is.

The core loop is:

```text
capture → place / organise → relate → rediscover → act → retain the result
```

The user's memorable formulation is that each thought should feel like a physical block. The app should make the shape of their thinking visible, with details available when needed.

### 1.3 Relationship to Better Backlog

The user described this as related to an earlier “Better Backlog” idea, particularly its visual treatment of work as physical objects whose age and relationships can be perceived. This app broadens that premise from backlog items to anything the user thinks about.

The earlier assistant claimed to remember additional Better Backlog details, including size/value and WASD-style navigation. Those recollections are not independently sourced here. The confirmed carry-over is the user's emphasis on visual blocks, age, flexibility, and keyboard interaction.

### 1.4 What success looks like

- Capturing a thought is easier than opening another miscellaneous note.
- The user can retrieve all film thoughts, project ideas, or related decisions regardless of where they were originally captured.
- A thought can belong in several useful contexts without copying it.
- Deferred ideas remain visible after immediate work is complete.
- Opening the app feels calm and inviting; the user is not confronted by a dashboard of fields and panels.
- Later, selecting a thought can start useful agent work with relevant context already assembled, and the results return to the same memory.

These are proposed validation criteria, not results demonstrated by an existing prototype.

## 2. Direction and decision register

| Topic | Current position | Status |
| --- | --- | --- |
| Primary purpose | Personal, visual thought memory; flexible enough for notes and tasks | User direction |
| Capture | Write first; decide where it belongs later, if ever | User direction |
| Default appearance | Extremely simple; no permanent left sidebar, right inspector, or metadata dashboard | User direction; supersedes the cluttered mock-up |
| Cards | Title only when collapsed; expand to reveal details | User direction |
| Colour | Colour contributes information; elegant and restrained, not monochrome-only | User correction |
| Spatial experience | Tactile movement, glowing cards, depth, graded focus/blur, cards moving around one another | User direction |
| Globe/cluster | Explore rotating the thought space like a globe or ball | Strong user interest; exact interaction unvalidated |
| Input | Fully usable by keyboard; mouse should be optional | User direction |
| Platforms | Start from Arch Linux/Omarchy, but support capture on a phone and eventually access elsewhere | User direction |
| Agents | Launch agents or groups through Herdr from thoughts; agents can contribute back | User direction for eventual capability |
| Data architecture | Shared memory core independent of any UI; local-first copies; views separate from thoughts | Session proposal, strongly aligned with requirements |
| Stack | Tauri 2 + Rust + Svelte/TypeScript became the latest recommendation after mobile entered scope | Session recommendation, not user approval |
| Main alternative | Qt Quick/QML with a suitable native core; Flutter also deserves evaluation | Session consideration |
| AI timing | Validate capture and spatial interaction first; mobile expansion before sophisticated AI | Latest session recommendation |
| 3D implementation | True 3D versus a 2D/2.5D depth illusion remains undecided | Open question |

### How the recommendations evolved

1. **Initial Linux-focused concept:** Odin + raylib + SQLite was favoured for a custom, game-like spatial world. Tauri was the pragmatic alternative.
2. **Omarchy/theme clarification:** The recommendation shifted toward an Odin core with a Quickshell/QML presentation layer, local IPC, and SQLite. This avoided implementing an entire text/UI toolkit in a renderer.
3. **Phone/everywhere requirement:** The recommendation shifted again toward a cross-platform application using Tauri/Rust/Svelte, with Quickshell as an optional Omarchy adapter. Qt/QML and Flutter remained plausible alternatives.
4. **Minimalism and globe feedback:** Permanent panels were explicitly rejected. The smallest useful product became title-first floating cards with focus, expansion, keyboard navigation, search, and local persistence. The rotating cluster became an important prototype question.

The earlier sample directory containing an `inspector` and the earlier black-and-white framing are superseded. Do not treat all historical recommendations as simultaneous requirements.

## 3. Domain model: Thought as the primitive

### 3.1 Capture and gradual enrichment

A new Thought needs only content and automatically assigned identity/timestamps. A useful starting model is:

```text
Thought
  id
  title
  body                  optional
  created_at
  last_touched_at
```

The earliest sketch used a single `text` field. The later title-only card requirement suggests distinguishing a short display title from optional detail. Whether a title is the first line, manually entered, or generated is unresolved. Generating one must not block capture or depend on AI being available.

A Thought may accumulate optional status, context, importance, semantic colour role, source, attachments, and relationships. Do not require these fields in a capture form.

Example:

```text
Title: Humans react when the harvester approaches
Body: Explore fear behaviour and how it affects harvesting.
Context: We Harvest Humans
Status: later
Source: design discussion
Relations: PART_OF → Harvester; RELATED_TO → Human behaviour
```

### 3.2 Relationships and grouping

Session examples included `PART_OF`, `RELATED_TO`, `DERIVED_FROM`, and `BLOCKS`. These are candidate relationship types, not a frozen ontology.

Frames/groups can visually gather thoughts without turning into rigid folders. A thought may participate in several groups or contexts. A frame's visual containment and a semantic `PART_OF` relationship should be distinguishable.

The source attachment asks whether there should be no separate “subtask” type: a larger piece of work could instead be broken into smaller Thoughts connected to the whole. Preserve that as an open modeling choice. It does not mean dependency, ownership, or execution state can be ignored.

**Consolidation recommendation:** Keep the initial relation vocabulary small and extensible. Differentiate explicit saved links from AI suggestions and from temporary proximity in a layout. Nearby cards should not silently acquire a permanent semantic relationship.

### 3.3 Tasks as a behaviour of Thoughts

A thought such as “Implement human crop growth” can acquire a status and be completed. A Backlog Lens can filter for project-related thoughts with unfinished status, while another view arranges the same thoughts around design concepts.

The original sketches suggested `active`, `later`/`someday`, `complete`, and blocked states. The exact lifecycle is unresolved. Neutral ideas, films, and references should not all look overdue merely because they lack completion.

Reminders were included in the broader vision, but notification scheduling was not designed. Do not infer a reminder engine as part of the first release.

### 3.4 Sources, history, and attachments

Preserve where a Thought came from: a conversation, pasted note, voice capture, URL, photo, agent output, or manual entry. A source can yield multiple Thoughts without losing its original text or context.

For conversations, preserve both implemented and deferred ideas, their rationale, and their relationships. “Not in V1” should mean retained for later, not discarded.

Events were proposed to record who changed what, support history/undo, and later assist sync. Examples include user creation, an AI-suggested link being accepted or rejected, and an agent returning findings. The exact event schema and whether events are the storage authority are still architectural choices.

## 4. Lenses, views, and search

### 4.1 Separate identity from placement

**A Thought's position belongs to a view, not to the Thought itself.** The same film Thought might appear in Films, Sci-fi Inspiration, and Things I Keep Forgetting, with a different arrangement in each.

```text
Thought: Watch 2001: A Space Odyssey
  ├── placement in Films
  ├── placement in Sci-fi Inspiration
  └── placement in Things I Keep Forgetting
```

“Lens” is the session's term for a surface onto the underlying memory. Candidate lenses include Films, We Harvest Humans, Game Ideas, AI Agents, Wedding, Pinepeak, Things to Do Soon, and Thoughts Untouched for Six Months. These are examples from the discussion, not mandatory built-in categories.

### 4.2 View modes

- Manually arranged spatial canvas.
- Filtered or query-generated collection.
- Temporary search/focus arrangement.
- AI-suggested cluster.
- List or backlog arrangement of the same objects.
- Relationship/neighbourhood exploration.
- Potential rotating globe/constellation view.

The app's long-term memory is not a collection of separate disconnected whiteboards. Lenses expose the same underlying objects. Whether every temporary view can be saved is open.

### 4.3 Search as transformation of the space

The session proposed pressing `/`, typing a query, and watching relevant Thoughts gather while irrelevant ones dim or recede. Related clusters might form around results. `Esc` restores the previous view.

This is a proposed interaction, not a requirement that every search physically move the whole world. Preserve orientation and manual layout. A temporary search arrangement must not overwrite saved placements.

Start with ordinary text/full-text search. Natural language queries such as “films I wanted to watch,” semantic expansion, and automatic grouping are later capabilities. Do not imply that basic full-text search alone can understand all those queries.

## 5. Visual and interaction design

### 5.1 Visual north star

The user wants a simple, elegant, beautiful thought space with almost no persistent chrome. Colour, form, position, movement, and focus should help recognise information at a glance. The user explicitly finds sidebars and detail panels overwhelming.

Collapsed cards show their titles. Bodies, metadata, provenance, and controls appear only when needed. Early sketches showing age, type, and agent details on every card illustrate possible information, not the final default density.

Visual ingredients discussed:

- Floating rounded cards or blocks.
- Soft coloured glow, subtle illuminated borders, and restrained bloom.
- Glassy/frosted surfaces where readability supports them.
- Smooth motion, easing, and a sense of mass or resistance.
- Depth, soft shadows, gradual dimming and blur.
- Subtle relationship lines or proximity cues, avoiding a dense web of edges.
- Optional icons or small generated images for recognition, without making them a capture requirement.

The initial empty black canvas is a useful starting image, but not a mandate for a monochrome or dark-only app.

### 5.2 Four presentation states

| State | Experience |
| --- | --- |
| World / idle | Title-only coloured cards; little permanent UI; relationships suggested through space |
| Focus | Selected Thought moves forward, sharpens and expands; related Thoughts remain available; background recedes |
| Command | A small temporary input for adding, searching, switching lenses, or eventually launching agents |
| Edit | Minimal inline or focused editor with the detail necessary for the current Thought |

These are conceptual states, not necessarily four independent screens. `Esc` should provide a predictable route back through them.

### 5.3 Tactility, aging, and physical behaviour

The user wants cards to move out of each other's way and the space to feel physically responsive. Session proposals included related Thoughts gently attracting, dragging one near another suggesting a link, and an active agent causing a subtle pulse.

Age might affect border strength, texture, opacity, typography, or a “dusty” appearance. Revisiting a thought could make it appear to wake up. These are exploratory encodings: old does not necessarily mean unimportant, and aging must not make valuable memories unreadable.

**Consolidation recommendation:** Separate logical importance, time since creation, and time since interaction. Avoid encoding all three with the same dimming effect. Movement should respond to an action and settle; continuous drifting may undermine calm and spatial memory.

### 5.4 Globe / 3D-like rotating cluster

The user's later proposal is more specific than an infinite 2D whiteboard:

- Arrange Thoughts in a ball, cluster, constellation, or sphere-like space.
- Rotate the whole cluster to bring Thoughts into the foreground.
- Keep foreground Thoughts sharp and more prominent.
- Gradually blur/dim Thoughts toward the background.
- Let related Thoughts accompany the focused object.
- Have cards avoid overlap and move around one another naturally.
- Combine depth-dependent focus with glow and bloom.

The value to test is whether this makes exploring and remembering thoughts easier and more pleasant. Claims in the conversation that it “changes cognition” were design enthusiasm, not empirical evidence.

Two implementation directions remain open:

| Approach | Benefits to explore | Costs/questions |
| --- | --- | --- |
| 2D/2.5D projection | Depth illusion using scale, position, opacity, blur, and ordering; can preserve conventional text editing | Occlusion, collision avoidance, and coherent rotation still need design |
| True 3D scene | Direct camera rotation and spatial arrangement; potentially richer depth behaviour | Readability, picking, focus navigation, text rendering, orientation, and performance need validation |

**Consolidation recommendation:** Prototype both a restrained planar layout and a rotating cluster using the same small dataset. Keep text facing the user unless testing establishes a benefit from another behaviour. Test loss of orientation, accidental movement, overlap, keyboard navigation, and reduced-motion operation before committing the architecture to 3D.

### 5.5 Keyboard-first behaviour

The requirement is full keyboard operation. Exact bindings below were suggestions, not final assignments:

| Suggested input | Candidate action |
| --- | --- |
| `Super+M` | Summon quick capture or memory overlay; final distinction to be decided |
| `Super+Shift+M` | Open the full memory space |
| `h/j/k/l` or directional keys | Move focus between Thoughts |
| `Shift` + movement | Move a selected card |
| `Enter` | Focus/open; submit in capture context |
| `i` | Enter editing |
| `Esc` | Leave editing/focus/search/overlay predictably |
| `/` | Search |
| `x` | Complete a task-like Thought |
| `r` or `@` | Eventually choose Research, Implement, Plan, Discuss, or Custom Agent |

Command examples were `add thought`, `search genetics`, `show films`, and `launch agent`. Mouse drag, pan, zoom, and later touch gestures should complement keyboard use.

**Consolidation recommendation:** Distinguish text entry from navigation commands, check existing system shortcut conflicts, and define deterministic focus movement in a rotated cluster. Include a discoverable temporary help surface, visible focus, and a non-spatial navigation option. Reduced motion and non-colour cues support the calm interface rather than requiring permanent extra panels.

## 6. Colour semantics and themes

### 6.1 Two separate layers

1. **Application/theme palette:** Background, foreground, surface, accent, urgency, and related presentation tokens that harmonise with the user's desktop.
2. **Meaning carried by Thoughts:** Context/project identity, type, state, provenance, activity, or recency.

The user wants actual colour because it contributes to understanding. A dark theme can be colourful; a light theme should also be possible. The discussion mentioned Tokyo Night, Rose Pine, Flexoki Light, and Catppuccin as examples of different palette interpretations.

### 6.2 Candidate mappings, not settled rules

| Palette role in the session | Example meaning |
| --- | --- |
| Blue | Project/context |
| Yellow | Idea/question |
| Green | Completed/resolved |
| Red | Blocked/urgent |
| Purple | AI-generated or agent-related |
| Cyan | Reference/information |

A different proposal used colour families for projects: We Harvest Humans in purple, Agent Kernel in blue, Pinepeak in green, Wedding in pink. These two schemes compete if each card has only one primary colour; they cannot both be treated as settled.

The conversation suggested storing a role such as `yellow` rather than a fixed hex value. **Consolidation recommendation:** Prefer an actual semantic token such as `idea` or a stable context identity, mapped through the theme to a palette role. This keeps meaning intact even when a theme needs a different hue.

Open choices include user overrides, how to represent multiple contexts, and whether state/provenance should use a small marker instead of the whole card. Test light/dark contrast and colour-vision differences; glow must not be the only focus indicator.

## 7. AI and agent integration

### 7.1 AI curation

The desired curator can split a messy note into atomic Thoughts, group films or other related content, suggest links, find relevant memories, and preserve ideas from discussions. It should help organise without forcing a filing step at capture time.

The session also proposed an Inbox as a temporary “new/unreviewed” state rather than a folder the user must constantly empty. Clear suggestions can be reviewed; uncertain items may stay visible for manual placement. The memory should become more useful with organisation but remain useful without it.

Start with deterministic search and manual links. Later consider semantic search, embeddings, clustering, enrichment, and language-based retrieval. AI availability must not determine whether a Thought can be saved or opened.

### 7.2 Thoughts as starting points for work

The user wants to select a Thought and launch an agent or group of agents in Herdr. Candidate actions include research, planning, implementation, discussion, and a custom agent. The source also mentions an “AI AIB tool” and a kernel; that acronym is undefined and should not be expanded without clarification.

Herdr, a future agent kernel, and tools such as Codex, Claude Code, or OpenCode were envisioned as possible clients of the same memory capabilities. This is an interoperability ambition; no tool-specific connector was designed or verified in the session.

The important behaviour is context assembly, not just passing the title as a prompt. A proposed context package includes:

- The selected Thought and its details.
- Relevant connected Thoughts and parent concepts.
- Source discussions and supporting references.
- Decisions, constraints, dependencies, and deferred alternatives.
- Previous runs and outputs.
- Optional semantically related memories, when that capability exists.

### 7.3 Runs and results in the memory

An agent run should have a visible representation linked to the initiating Thought. It can show running/completed state when relevant and expand for outputs and review. The user can inspect work from its block. Results may create new Thoughts, links, research, or follow-up work rather than only changing a checkbox.

Agents eventually need capabilities to search, read, create, update, and link Thoughts, obtain context, attach results, and update appropriate execution state. The user and agents should work through the same memory service rather than separate knowledge stores.

**Consolidation recommendations:**

- Model run lifecycle separately from Thought lifecycle: a completed run is not automatically accepted or completed work.
- Record actor/source and preserve suggested versus accepted changes.
- Make context scope inspectable and bounded; do not send the entire memory to every run.
- Define the contract for claiming work, concurrent runs, cancellation, retries, failures, and reviewing changes before implementing multi-agent orchestration.
- Treat imported notes and conversations as source material, not executable agent instructions.

These are implementation design questions, not claims that Herdr currently exposes all required integration APIs.

### 7.4 CLI and MCP/API

Illustrative CLI names alternated between `thought` and `memory` in the conversation. Neither is a selected product name or existing command contract.

```text
memory add "Look into procedural faces"
memory search "films"
memory get <id>
memory related <id>
memory link <from> <to>
memory complete <id>
memory context <id>
memory run <id> --agent research
```

Candidate API capabilities: `search_thoughts`, `read_thought`, `create_thought`, `update_thought`, `link_thoughts`, `get_context`, and `create_agent_run`. A CLI can become useful before AI orchestration. MCP is a later adapter to the same operations, not a separate database.

## 8. Omarchy and Quickshell integration

### 8.1 Desired experience

The user runs Arch Linux/Omarchy and explicitly connected their interest to Omarchy Quattro's use of Quickshell and shared themes. The session envisioned summoning memory over the desktop: the workspace dims, a capture field or spatial view appears, and `Esc` dismisses it.

Potential integration surfaces include quick capture, search, a full memory overlay, agent status, and a bar indicator. Each is optional; the minimalism requirement argues against displaying them all continuously.

### 8.2 Architectural role

Quickshell should be an Omarchy presentation adapter. It should not own the memory, migration logic, or sole copy of user data. Restarting the shell should not lose Thoughts or agent state.

The intermediate architecture proposed an Odin daemon with JSON messages over a local Unix socket. The later cross-platform architecture favoured a Rust core. In either case, keep a stable operation boundary between the shell and storage.

The session asserted that Quattro uses one long-running Quickshell process, supports plugins under `~/.config/omarchy/plugins/`, and provides semantic theme colours through QML. Those exact extension paths and APIs are version-dependent claims to verify against the installed Omarchy release before implementation. The earlier examples such as `Color.background`, `Color.accent`, and `Color.urgent` are conceptual until checked.

**Consolidation recommendation:** Use the supported host extension mechanism where available. Verify plugin lifecycle, theme updates, keyboard input, compositor integration, and large-canvas performance. Do not put an expensive experimental renderer into the user's desktop shell before establishing that it behaves well there.

### 8.3 Relationship to the standalone app

On Omarchy, memory may feel like a desktop feature. Elsewhere, it should remain a normal application. A Qt/QML route could share some visual components with Quickshell; a Tauri route would share domain operations and data contracts while using a separate QML adapter. That second route has a real additional UI maintenance cost.

## 9. Cross-platform, mobile, and capture everywhere

### 9.1 One memory, device-appropriate interfaces

The phone requirement changes the project's boundary. It is one personal memory system with several interfaces, not exclusively an Omarchy application.

Desktop emphasises exploration, spatial manipulation, editing, relationships, and agent work. Mobile emphasises capturing before a thought is forgotten, then browsing, searching, and opening details. A small screen does not need a compressed copy of the desktop canvas.

The proposed phone opening screen is essentially “What's on your mind?” with type and microphone entry plus recent Thoughts. A couple of seconds to capture was an aspirational interaction target, not a measured result. No project/type/tag/priority selection should be required.

### 9.2 Voice

Capture audio promptly and retain audio, transcript when available, timestamp, and device/source metadata. A later process can extract a concise Thought and suggest relationships. The original recording and wording should remain accessible if a generated summary is wrong.

Open questions: local versus remote transcription, recording retention, offline transcription, language support, and how one recording produces several Thoughts. Saving the recording locally should not wait for transcription.

### 9.3 OS share sheet and attachments

Eventually accept shared URLs, text, images/photos, film references, and articles, optionally with a short annotation. Each capture becomes a Thought with source/attachment information rather than requiring separate bookmark and reference systems.

Native share targets/extensions, lifecycle behaviour, permissions, and packaging need platform-specific validation. A framework supporting Android/iOS does not automatically implement all those features.

For the Tauri candidate, iOS development also requires access to macOS and Xcode; the existing Linux machine alone is not the complete iOS build setup. Android requires its SDK/NDK toolchain. [Tauri prerequisites](https://v2.tauri.app/start/prerequisites/)

### 9.4 Other surfaces

Browser access, a watch “remember this” interaction, widgets, and deeper automation were longer-term possibilities. They are not MVP commitments. Android versus iPhone priority has not been stated and materially affects the first mobile proof of concept.

## 10. Architecture and persistence

### 10.1 Proposed separation

```text
Desktop spatial UI        Omarchy/Quickshell        CLI / MCP / agent adapter
        \                        |                          /
         +------------- local memory operations ---------+
                                  |
                        shared domain/storage core
                                  |
                         local SQLite + attachments
                                  |
                       sync adapter / pending changes
                                  |
                        optional sync service
                                  |
                     phone local core + local storage
                                  |
                   capture / voice / share / search UI
```

This is a logical diagram. The core may be a library inside the app, a local service, or a combination. A desktop daemon should not be assumed to map directly onto mobile lifecycle rules.

The core owns Thought identity, relationships, queries, persistence, and domain operations. Views own placements and presentation state. Adapters expose capabilities to shells, devices, and agents.

### 10.2 Starting storage concepts

| Record | Responsibility |
| --- | --- |
| `thoughts` | Content and intrinsic metadata |
| `edges` | Saved relationships, including provenance where needed |
| `views` / `lenses` | View definitions and filters |
| `placements` | Per-view position, ordering, and later optional depth/pinning |
| `sources` | Original notes/conversations/captures and origin references |
| `attachments` | Metadata and references to audio/images/files |
| `runs` | Agent invocation, state, outputs, and links to originating Thoughts |
| `events` | History/actor information and potentially sync operations |

The original sketch listed the first four plus runs/events. Sources and attachments make explicit concepts introduced later in the conversation. This is a responsibility map, not a final schema; several records can be introduced only when their feature is built.

SQLite plus full-text search is the recommended starting point. A graph-shaped domain does not require a dedicated graph database. Store placements separately even if V1 only exposes one lens. Keep migrations and export in view from the beginning.

### 10.3 Local-first sync

Each device should accept and persist captures without internet. Synchronisation happens afterward. A server can help exchange records or events, but is not required for basic local use.

The session suggested a small HTTPS/WebSocket API, a server database or event stream, and mutation events containing identity, device, version, and time. It advised against starting with CRDTs. These are a candidate direction, not a complete protocol.

**Consolidation recommendation:** Even one user can edit on two disconnected devices. Atomic records simplify some cases but do not remove conflicts. Decide at least:

- Stable IDs created offline and idempotent delivery of retried mutations.
- How an interrupted sync resumes and how pending captures survive app termination.
- Update/update and update/delete conflicts, including link and attachment changes.
- Tombstones/deletion propagation and recovery from accidental deletion.
- Per-device cursors/versions rather than relying only on wall-clock timestamps.
- Whether layout synchronises, stays device-local, or has device-specific variants.
- Schema migration compatibility across devices on different app versions.
- Authentication, device enrollment, encryption expectations, and backup/export.

A first sync implementation can preserve conflicting text versions for review rather than silently losing one. A decision about CRDTs can be deferred; a decision to retain data during conflicts cannot.

The earlier server “canonical event stream” drawing should not be interpreted as cloud ownership of memory or proof that event sourcing is required. Distinguish an audit log, a delivery queue, and an authoritative event-sourced database.

### 10.4 AI placement

The session favoured server/agent-side AI initially, with devices receiving suggested classifications and links. That is a later service choice, not a requirement to upload every Thought automatically. Local models and on-device embeddings remain possibilities. Capture, local search, and manual organisation must remain usable without AI.

## 11. Technology tradeoffs

The important decision is which stack best supports a calm, polished spatial interface and reliable capture across the required devices. The initial enthusiasm for a language should not outweigh text input, mobile integration, or ownership of the core.

| Stack / approach | Why it was considered | Main tradeoff or validation need | Current role |
| --- | --- | --- | --- |
| **Odin + raylib + SQLite** | Data-oriented, custom rendering; direct control over a world of cards, edges, selection, camera, and animation; aligned with interest in Odin | Building polished editing, selection, IME, clipboard, accessibility, HiDPI, focus, and app behaviour requires substantial additional work; mobile integration needs evidence | Strong visual experiment; earlier Linux-only favourite |
| **Odin core + Quickshell/QML** | Keep memory/CLI in a systems core and use QML for rich animated shell UI | IPC and packaging; separate UI/core toolchains; shell integration is Linux-specific; mobile still needs an application path | Intermediate Omarchy-first proposal |
| **Odin core + standalone Qt/QML** | Preserve Odin interest with a mature visual toolkit and standalone window | Integration boundary and mobile packaging must be proved; do not assume reuse is automatic | Viable alternative to an all-custom UI |
| **Tauri 2 + Rust + Svelte/TypeScript** | Latest recommendation; web text/layout tools, Rust core and CLI ecosystem, desktop/mobile application architecture | System-webview differences, Linux rendering performance, mobile lifecycle/plugins and share extension work; QML adapter is a separate UI | Leading candidate, pending focused prototypes |
| **Qt Quick/QML + C++ + SQLite** | Animated scene graph, touch-oriented UI, strong native toolkit path; conceptual fit with Quickshell | C++ complexity, packaging, deployment, and distribution/license model need evaluation | Serious co-finalist |
| **Rust + Qt/QML** | Rust core ecosystem plus QML visual layer | Binding/tooling selection adds a bridge to maintain | Alternative core/UI combination |
| **Rust + egui** | Mentioned as a Rust UI option | Text-heavy, mobile, accessibility, and polished spatial interaction suitability was not explored | Mentioned, not evaluated deeply |
| **Flutter** | Custom visuals/animation and broad platform reach from one UI codebase | Dart/toolchain preference, native integrations, Linux desktop behaviour, and Quickshell duplication | Credible option; should not be dismissed without a small trial |
| **GTK4/libadwaita + Rust** | Conventional Linux application development | Fit with this custom spatial language and desired cross-platform reach needs work | Lower priority for the specific concept |
| **Godot** | Quick experiment with nodes, camera, text, lines, and tweens | Product editing, native integration, and service/CLI architecture are separate problems | Useful disposable interaction prototype |
| **React Native** | Mobile-oriented option mentioned in later comparison | Linux desktop and complex spatial surface were not investigated | Requires more research if shortlisted |
| **Electron** | Web-based desktop shell with bundled rendering engine | Runtime/resource tradeoff and separate mobile strategy | Earlier dismissal was a preference, not a technical impossibility |
| **Browser/PWA** | Anywhere access and a potential fast prototype | Offline storage durability, native capture hooks, and platform behaviour require validation | Possible companion; not selected |

### 11.1 Why Odin appealed, and why the recommendation changed

The scene contains arrays of Thoughts, relationships, positions, selections, viewports, and runs transformed into visuals each frame. That data-oriented, game-like problem makes Odin/raylib attractive. The harder product problem is everything around the rectangles: text handling, accessibility, native lifecycle, packaging, and mobile capture.

The conversation successively moved UI work into QML, then reconsidered the full product around cross-platform delivery. Odin is not prohibited; it simply stopped being a requirement. Introducing multiple core languages without a demonstrated benefit would add friction.

Odin documents Android/iOS compilation subtargets, so mobile should not be described as impossible. The unresolved issue is the complete application workflow and integration effort, not merely compiler reach. [Odin overview](https://odin-lang.org/docs/overview/)

### 11.2 Current recommendation

Use **Tauri 2 + Rust + Svelte/TypeScript + SQLite/FTS as the leading prototype candidate**, with **Qt Quick/QML as the strongest alternative from the session** and Flutter available if mobile experience or custom rendering proves decisive.

Start the visual experiment with ordinary UI elements/HTML/SVG/CSS where practical. Move the scene to Canvas/WebGL or a specialised renderer only when effects or measured scale justify it. A renderer change must retain editing, keyboard focus, and accessibility. The sphere idea is a reason to test rendering early, not proof that a particular graphics engine is necessary.

Do not copy the original star rankings into an architecture decision. Compare actual capture/editing, blur/glow/rotation, frame pacing, resource use, native mobile hooks, and packaging on the user's hardware. Platform support is an entry criterion, not evidence of a finished app experience.

## 12. Obsidian comparison and differentiation

### 12.1 Meaningful overlap

The user's question—could Obsidian already solve this?—deserves a practical answer. Obsidian offers local notes, links/backlinks, tags, search, Canvas, Graph, mobile apps, and extension possibilities. Atomic notes and flexible canvases can address parts of the present problem immediately. Canvas also has an open JSON format relevant to interoperability.

The primary-source check adds an important correction to the session's simplified comparison: Canvas supports text-only cards as well as note files, and Graph already offers filters, colour groups, configurable forces, local neighbourhood views, and keyboard navigation. These capabilities should be part of the baseline rather than claimed as absent. [Obsidian Canvas](https://help.obsidian.md/plugins/canvas), [Obsidian Graph](https://help.obsidian.md/plugins/graph)

The session's shorthand was “a note system with visual features” versus “a visual thought-space that stores notes.” That is a product framing, not proof that Obsidian cannot support atomic Thoughts or agent workflows through configuration and plugins.

### 12.2 Proposed differences to validate

| Dimension | This app's intended emphasis | Fair comparison question |
| --- | --- | --- |
| Capture | No required filing/type decision; one tiny Thought at a time | Does this remove meaningful friction beyond a simple Obsidian capture workflow? |
| Spatial work | Focus, arrange, edit, connect, and act within the space itself | Does it improve daily use beyond Canvas and Graph? |
| Visual calm | Title-only cards, hidden detail, no permanent sidebars | Can the simpler interaction stay discoverable and efficient? |
| Physicality | Rotation, collision avoidance, depth, blur and glow | Does the effect support recall or become distracting? |
| Lenses | The same objects in saved, generated, and temporary arrangements | Is this easier than existing notes/canvas conventions? |
| Agent execution | Context assembly, launch, review, and retained results built into Thoughts | Does native integration save enough work over external tools/plugins? |
| Device ecosystem | One memory with dedicated capture, desktop, shell, and machine interfaces | Is the total experience better enough to justify maintaining it? |

These are proposed differentiators as a combination, not claims that each feature is unique. A globe alone does not justify building an entire memory system.

### 12.3 Build versus use

The session suggested trying Obsidian for one or two weeks with one vault, little folder structure, roughly one note per thought, and modest Canvas/Graph use. Record what helps, what causes friction, and whether the desired spatial experience remains absent.

Alternatively, build the smallest spatial prototype immediately. The practical comparison is the same: test it against the current Notes workflow and a deliberately simple existing tool. Do not make building a better general-purpose Obsidian the project scope.

### 12.4 Other products mentioned

The conversation named Heptabase (cards/whiteboards and linked knowledge), AFFiNE (documents/databases/whiteboard), Capacities (object-oriented knowledge), and Lino AI Canvas (AI-assisted connected canvas) as references. It also used Miro and Notion as examples of broader workspaces the user does not want to recreate.

Prior assertions about Heptabase CLI/Linux support, Capacities MCP capabilities, and Lino's current platform availability are research leads unless independently verified. Their current feature sets and plans were not exhaustively audited for this consolidation. No single competitor was established as an exact substitute, and novelty was not proven.

## 13. MVP and phased development

### 13.1 First question

**Is capturing and manipulating thoughts as calm spatial objects actually more useful to this user than keeping miscellaneous notes?**

The first release should answer this before investing in a full AI, sync, or agent platform. The globe concept is important enough for an early small experiment, but it need not block a useful basic canvas.

### 13.2 Proposed sequence

| Phase | Scope | Evidence needed to continue |
| --- | --- | --- |
| **0 — Interaction and stack proof** | Small realistic set of title-only cards; expand/edit; compare planar and rotating layouts; glow/blur; keyboard use; save/reopen; brief target-phone integration spike | Chosen stack can deliver the required feel and basic input without obvious platform blockers |
| **1 — Local Linux MVP** | Create/edit/delete/recover Thoughts, pan/zoom/move, focus/expand, restrained colour, manual connections, text search, keyboard controls, SQLite persistence | User prefers it for a real set of thoughts and can retrieve them reliably |
| **1b — Useful organisation and access** | Simple groups and lenses, placements per view, CLI capture/search/get, export; basic task status when needed | Same Thought works across contexts without duplicates; capture is convenient outside the main window |
| **2 — Sync foundation** | Offline IDs, durable pending changes, retries, conflict preservation, attachment strategy | Two devices can create/edit offline and reconnect without silent loss |
| **3 — Mobile companion** | Fast text capture, recent/browse/search/detail; then voice and share-sheet integration | User stops putting random thoughts into the old Notes app because this is easier |
| **4 — Omarchy adapter** | Supported Quickshell integration, summon/dismiss, theme mapping, optional status | Integration improves daily access while remaining calm and robust |
| **5 — AI curation** | Split mixed notes, suggest links/groups, preserve source text, semantic retrieval where useful | Suggestions improve retrieval and are easy to inspect/correct |
| **6 — Herdr and agents** | Context packages, launch, run objects, outputs, review, agent read/write API; then groups of agents | Work can start and return without manual context copying, with understandable state |

This sequence reconciles the original canvas→lenses→CLI→AI→agents proposal with the later preference for mobile expansion before AI. Quickshell can move earlier if it cheaply improves capture, and a small mobile feasibility check belongs early even though full mobile delivery follows sync. These phases are recommendations, not dated commitments.

### 13.3 Keep out of the first product slice

Do not initially require a complete ontology, rich document editor, vector database/RAG infrastructure, autonomous global reorganisation, multi-agent orchestration, a watch app, extensive dashboards, or a full synchronised 3D universe. Keep these ideas as retained future Thoughts with context rather than deleting them from consideration.

### 13.4 Representative acceptance scenarios

1. Capture a film thought without choosing a folder; restart the app and find it again.
2. Open a title-only card, edit its details, and return to the uncluttered world using only the keyboard.
3. Place one Thought in two lenses, change its content once, and see the change in both.
4. Search and clear the search without losing the previous manual arrangement.
5. Break a mixed note into separate Thoughts while retaining their common source.
6. Mark X/Y/Z complete while A/B/C remain discoverable as deferred ideas with their rationale.
7. In the sync phase, capture on an offline phone and desktop, reconnect, and retain both sets of work; preserve conflicting edits.
8. In the agent phase, launch from a Thought, inspect the context used, and review linked results without equating run completion with accepted work.

Scenarios 1–4 validate the early product; later scenarios become relevant as their phases are introduced.

## 14. Principles to preserve

1. **Capture first.** Organisation and enrichment are optional follow-up work.
2. **A Thought can grow.** Its initial simplicity should not prevent rich context later.
3. **One identity, many lenses.** Presentation never forces duplicated memory.
4. **Calm by default.** Titles first; detail and controls appear with intent.
5. **Colour and motion have a job.** They should aid recognition, focus, or feedback.
6. **Spatial memory matters.** Automatic movement should preserve orientation and be reversible.
7. **Keyboard operation is complete.** It is not an extra shortcut layer over mouse-only controls.
8. **Local capture is dependable.** Network or AI failure must not prevent remembering something.
9. **The core outlives the interface.** Shells, apps, CLIs, and agents are adapters onto shared memory.
10. **Context survives decisions.** Deferred possibilities and original sources remain retrievable.
11. **Agents contribute visibly.** Their actions and outputs have provenance and reviewable state.
12. **Organisation adds value without becoming a duty.** An uncurated inbox still contains useful memory.
13. **Build for the user's actual needs.** Validate daily usefulness before broadening into a general platform.

## 15. Open questions

### Product and behaviour

- What is the first phone platform: Android, iPhone, or both?
- Is the dominant daily activity capture, retrieval, exploration, or planning?
- How should titles be derived without introducing another editing step?
- Which status fields are useful without turning all thoughts into tasks?
- Should groups be semantic relationships, purely visual frames, or both?
- What exactly does the source's “AI AIB” refer to?

### Spatial design

- Is a globe the default home, a lens, or a temporary navigation mode?
- Are Thoughts on a sphere's surface, distributed through a volume, or only projected to appear deep?
- What should happen to manual placements during rotation, search, clustering, or focus?
- How does the user return to a familiar place, and how are important Thoughts pinned?
- How do keyboard navigation and mobile touch work with overlapping/depth-ordered cards?
- How much blur, glow, motion, and aging remains calm and readable?
- Should colour primarily represent context, type, state, or provenance?

### Architecture and operations

- Which stack wins real input/rendering/native-capture experiments?
- Is the desktop core embedded, a daemon, or both? What is the mobile equivalent?
- Which Omarchy plugin/theme interfaces are actually available in the target release?
- Which content and layout changes sync, and how are conflicts preserved?
- Is sync self-hosted, managed, peer-to-peer, or pluggable? What are encryption expectations?
- What export format preserves IDs, links, sources, attachments, and placements?
- Can Markdown and/or JSON Canvas support useful interoperability without becoming the entire storage model?
- What is the expected practical scale of Thoughts, visible cards, and attachments?

### AI and agents

- Are curation changes suggestions, automatic operations, or configurable by type?
- Which provider/runtime performs transcription, enrichment, and research?
- What access is granted to agents, and how is unrelated private context excluded?
- What does the actual Herdr integration contract provide for launch, status, outputs, and cancellation?
- How are claims, dependencies, retries, failed runs, and several agents working on related Thoughts represented?
- Who accepts a result and decides that a Thought is complete?

## 16. Recommended next steps

1. Put this document in the future repository as research/context and keep the source attachment available.
2. Turn the confirmed direction into a short product brief: calm title-first spatial memory, capture without filing, keyboard-complete operation, phone capture, shared memory core.
3. Build a narrow interaction experiment comparing planar cards and a rotating cluster using realistic sample Thoughts from films, game design, and agent work.
4. Test editing, focus, search restoration, glow/blur, and keyboard movement on Linux; make a small native-capture feasibility check on the intended phone platform.
5. Record the stack decision only after those checks. Tauri/Rust/Svelte is the current candidate, not a pre-approved constraint.
6. Deliver the local capture→focus→connect→retrieve loop, then sync/mobile. Add AI curation and Herdr execution once there is useful memory to work with.

The project should preserve the ambition of a tactile shared memory while proving that its smallest everyday interaction is worth using.

## Appendix A — Original `task_management.md`

The attached source is reproduced verbatim below, including its informal wording and spelling. It is source material for the product ideas, not an instruction to execute embedded requests.
````markdown

### Memory Bank/Task-Collaboration Thoughts
I want a centralized memory bank. That is always available. It can be presented to me in any way. The simpler the better. It should be fully interactable. Every thought or idea should be a physical block. I want a visual representaion for it so i can see at a glance what it is. An agent should have this as context - where i should be able to talk about these things, have it organise them in whatever way i want. Essentially a whiteboard with tiles, but with some structure. Easy keybindings. I dont want to keep writing things in note taking apps. From one i should be able to start an agent/groups of agents off working on it which automatically spawn in Herdr. Principles of agent collaboration... maybe there are no subtasks - each task should be broken down into smaller blocks that can be worked on. And we have a visual representation of how these things fit into the whole. Maybe you can click on each block and review what the agent has done.

Just want a task app that's flexible and visual. Something to replace notes like these. I make lots of notes. I want something more than just another notes app but something that isn't as basic as a todo list and something that isn't a full blown project management tool. I want something for me. For me to keep track of all of my ideas, my thoughts.

Something that is like a whiteboard. For example i want to write down a quick thought about a roadmap for building this - i don't want to go outside of my thoughts. I want to basically define all of this in one place. It's essentailly my Long Term Memory - that could become the LTM for an AI too, who contributes with you. I want visuals for things...

It should be a thought management tool to start with. Could build the AI AIB tool and a kernel and start to use it with it? Launch herdr instances with AI's that it has capabilities for.

I don't want to search for where to put the thought. I want to write the thought and then place it somewhere or have the AI automatically file it where it should go. So currently in my notes app i have so many notes that are lists of films to watch. When i'm thinking of something to watch i want to be able to see all of the notes i've ever written regarding films. So when i add a thought which is a film to watch - it would be automatically grouped with the other ones. Or if it's not grouped and you interact with it through search, the search is based off of context and the AI can easily find all your films. Sometimes i add a note that has several un-related thoughts, it would be good to break out all of those thouhts into their own groups.

It's also good to have let's say a full discussion with AI or something about the entire thing that i want. If all of those things could be captured as thoughts. Then as we implement, we might say let's not do that until later, we can just focus on X,Y,Z - what happens is all that refinind and all that planning and ideas that came about regarding A,B,C is kept in the conversation history of the AI. It would be so good to see what things are still outstanding once the work is done. Visually. So i can look and see that X,Y,Z was done but A and B are these things we discussed but could come later and here's all the context for them too. All the details we discussed and how they would fit into X,Y,Z. 

Instead of copy and pasting notes, trigger an agent and they have all the context there.
````

## Appendix B — Primary-source verification and references

Checked 2026-09-14. This is a bounded fact check supporting the conversation consolidation, not a stack selection or exhaustive market survey. Sources below are live documentation and branch references; specific versions, plugin coverage, release status, and performance require verification at implementation time. Recommendation/inference is labelled explicitly.

### 1. Tauri 2: credible desktop/mobile route, with platform-specific work

Tauri supports desktop and mobile targets and accepts frontends that compile to HTML, JavaScript and CSS. Rust can implement application logic, with Swift/Kotlin integrations where needed. This supports considering Svelte as a frontend; it does not establish that Svelte or Tauri is the best choice for this UI. [Tauri introduction](https://v2.tauri.app/start/)

Tauri uses platform webviews: WebView2 on Windows, Android System WebView, and WebKit on Apple platforms/Linux (WebKitGTK on Linux). Runtime capabilities vary by device/OS/distribution. **Inference:** prototype blur, bloom, large card counts, input and spatial animation on the actual Linux target and phone before committing. Do not assume Chrome desktop results represent Linux Tauri. [Webview versions](https://v2.tauri.app/reference/webview-versions/)

Tauri mobile plugins can invoke Kotlin/Java and Swift code. **Inference:** receiving shares, background capture, recording and OS extensions should be explicit native-integration spikes; mobile support alone does not prove a ready-made plugin exists for the complete workflow. [Mobile plugin development](https://v2.tauri.app/develop/plugins/develop-mobile/)

iOS development requires macOS and Xcode; Android needs its own SDK/NDK toolchain. [Prerequisites](https://v2.tauri.app/start/prerequisites/)

### 2. Qt/QML: relevant to animation and portable applications, distinct from Quickshell

Qt Quick provides QML visual components, animation, input, models/views and a C++ extension API. Its rendering/effects facilities are relevant to the proposed tactile cards. **Inference:** Qt Quick is a credible alternative for the full app, especially if shared QML expertise with a desktop integration matters; it still needs usability/performance trials. [Qt Quick](https://doc.qt.io/qt-6/qtquick-index.html)

Qt supports desktop operating systems as well as Android and iOS. Support depends on the selected release and individual modules. Do not describe Qt as inherently Linux-only or incapable of a mobile client. [Supported platforms](https://doc.qt.io/qt-6/supported-platforms.html)

### 3. Flutter: broad platform support, native features still need integration

Flutter supports iOS, Android, web and Windows/macOS/Linux deployment. Platform integrations may use existing plugins or custom native code, and new targets require appropriate tooling. Its own documentation recommends adaptive/responsive design. **Inference:** Flutter merits a serious mobile-oriented comparison, but a common codebase does not remove the need for a different phone interaction design, platform feature work, or testing the spatial rendering approach. [Platform integration](https://docs.flutter.dev/platform-integration), [Supported platforms](https://docs.flutter.dev/reference/supported-platforms)

### 4. Odin/raylib: powerful rendering exploration; application plumbing is a tradeoff

Odin's overview explicitly exposes iOS and Android subtargets, so “Odin cannot target phones” would be too strong. Its installation documentation distinguishes compiler host platforms from broader compilation targets. Neither document establishes a complete mobile application toolkit or effortless deployment path. [Odin overview](https://odin-lang.org/docs/overview/), [Getting started](https://odin-lang.org/docs/install/)

raylib advertises 3D, shader/postprocessing, input/audio and Android support, and describes itself as suitable for graphical applications and prototyping. Its README also states important defaults/limitations: a single window/context and text drawing without RTL, ligatures or emoji support. **Inference:** it is attractive for testing the rotating cluster's physical feel, but a polished note editor adds substantial text-input, accessibility, navigation, platform integration and packaging work. The main README's platform list is not proof of a supported iOS application path; validate any intended iOS backend separately rather than asserting either impossibility or parity. [raylib README](https://github.com/raysan5/raylib)

### 5. SQLite FTS5: viable local keyword search building block

FTS5 provides full-text search through SQLite virtual tables, supports term/phrase/prefix queries and includes ranking/highlight/snippet facilities. **Inference:** a local database with FTS5 is a reasonable initial keyword-search approach; semantic retrieval is an optional additional index. FTS5 is not a synchronization protocol or an AI memory model. [SQLite FTS5 documentation](https://sqlite.org/fts5.html)

### 6. Obsidian: considerable real overlap; avoid weak differentiation claims

Obsidian Canvas offers a 2D infinite space for notes, text cards, media, web pages, connections and groups, with dragging, resizing, colors and panning/zooming. It stores `.canvas` files in the open JSON Canvas format. Text-only cards are distinct from note files and do not appear in backlinks until converted to files. [Canvas documentation](https://help.obsidian.md/plugins/canvas)

Graph view visualizes note links, supports global and local graphs, filters, color groups, configurable forces and keyboard navigation. Therefore physical force layout, graph navigation, colors and focus on a local neighborhood are not by themselves differentiators. [Graph view documentation](https://help.obsidian.md/plugins/graph)

Obsidian has iOS and Android apps, command palette/hotkeys/plugin features on mobile, and explicitly advertises mobile graph view. Phone access or keyboard control alone are not distinctive. [Obsidian mobile](https://obsidian.md/mobile)

JSON Canvas is designed for readable, interoperable infinite-canvas data and can be implemented as import/export/storage by other applications. **Inference:** consider it for optional 2D canvas interchange, but it is not automatically a complete encoding of thought semantics, task state, agent history, or 3D layout. [JSON Canvas](https://jsoncanvas.org/)

**Product inference:** differentiation should be tested as a coherent experience: thought as the shared primitive; capture/revisit/act without filing overhead; title-only calm focus; an optional rotatable depth interface; integrated human/agent work with visible provenance; and device-appropriate capture. These are proposed product outcomes, not proven absence claims about every Obsidian community plugin. A hands-on Obsidian baseline is more informative than a feature checklist.

### 7. Quickshell and Omarchy: real integration surfaces; pin the target version

Quickshell is a QML/Qt Quick toolkit for desktop components including bars, widgets and lockscreens, with Wayland/window-manager integration. **Inference:** use it as an Omarchy capture/search/agent-status surface over a shared core; it is not itself a cross-platform mobile app framework. [Quickshell](https://quickshell.org/)

The official Omarchy repository's `quattro` branch documents a single long-running Quickshell host, third-party plugins, panel/overlay/menu/service kinds, and IPC for summon/hide/toggle/call. It documents plugin discovery and per-user configuration. This verifies a branch-level integration design, not the release installed on the user's machine. Before implementation, inspect/pin the actual installed Omarchy revision and its contract. [Omarchy Quattro shell README](https://github.com/omacom/omarchy/blob/quattro/shell/README.md)

**Not established by this bounded check:** a stable generic theme-token API usable by the new application, live theme propagation guarantees, or a guarantee that the user's installation has the documented plugin contract. Preserve theme adoption as a design goal and a version-specific integration task. No exact Quattro release date/version claim is needed in the consolidation.
