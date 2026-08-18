# Police Agent ג€” Distributed Cops-and-Robbers over P2P

**Group:** Hassarma-Agents (`uoh-mh01`)
**Role:** `police`
**Companion repository (thief agent): https://github.com/mohamadhassarma/uoh-mh01-thief**

> Both repositories of this group must be cross-linked. This is the police repo;
> the link above points at the thief repo, and that repo links back here.

---

## 1. Formal model ג€” Dec-POMDP

> **TODO (required):** scientific description of the formalism used to model the race ג€”
> state space, observations, and the uncertainty structure. See Ch. 1 of the rulebook.

## 2. FastMCP orchestration dilemmas

> **TODO (required):** discussion of the development trade-offs around inter-agent
> communication: turn management, network-failure handling, the roles of the
> Orchestrator and the Gatekeeper. See Ch. 2 and Ch. 8.

## 3. Strategies implemented

> **TODO (required):** the decision-making mechanism chosen, belief map, pheromone
> trails, and how the move is selected. See Ch. 4 and Ch. 6.

## 4. Reinforcement-learning curves / experiments

> **TODO (required):** figures, tables, curves. Attach GUI belief-map screenshot and
> a Replay screenshot showing `Verified OK`.

## 5. Results and reflection

> **TODO (required):** league results, what worked, what did not.

---

## Repository contents (mandatory checklist)

- [x] `README.md` ג€” this academic report
- [x] `config/` ג€” `game.json` (signed shared contract) + `police/game.toml` (private)
- [x] `prd/` ג€” one PRD per development stage
- [x] `PLAN.md` ג€” development plan
- [x] `TODO.md` ג€” task list
- [ ] Annotated git tag `v1.0-submission` pushed
- [ ] GUI belief-map screenshot attached
- [ ] Replay screenshot with `Verified OK` attached
- [ ] No secrets committed (`credentials.json`, `token.json` are gitignored)

## Running

```powershell
uv sync
uv run python -m uoh_mh01 peer --role police
```

Replay a saved match (stage 6):

```powershell
uv run python -m uoh_mh01 replay --log logs/police_match.json
```

## Process separation

The police and thief agents **must** run as two fully separate processes under
separate configuration directories. This repository contains the `police` side only.
No shared memory, no shared variables, no shared live module between the two roles.

## References

- The rulebook (`docs/police_thief_p2p.pdf` in the reference repo below) is the sole
  binding specification.
- [`rmisegal/Game-P2P-Cop-Chase`](https://github.com/rmisegal/Game-P2P-Cop-Chase) —
  the course's official reference implementation. Read for understanding and
  cross-checked against; no code from it is vendored into this repository.
- [`Imreec/copthief-league-protocol`](https://github.com/Imreec/copthief-league-protocol) —
  a student-authored interop/conformance kit pinning byte-level wire constructions
  (canonical JSON, commit-reveal, agreement signatures, `game_id`/`game_uid`) the
  rulebook leaves as prose. Not a specification; consulted for PRD-03/PRD-07 and
  credited here per its own terms. No code from it is vendored into this repository —
  its published test vectors are ported into this project's own test suite as
  fixtures instead (stage 3).