"""Small pure helpers for turn_receiver.py, split out purely to keep that
file under the project's ~150-line budget.
"""

from __future__ import annotations

from ..domain.state import MatchState, Side
from .protocol import MoveRequest


def sender_position(state: MatchState, sender: Side):
    return state.cop_pos if sender is Side.POLICE else state.thief_pos


def counter_mismatch(request: MoveRequest, expected: MatchState) -> str | None:
    """B2: every message carries the sender's own post-action counters; the
    receiver rejects any message whose counters don't match what its OWN
    local state expects — the one place a lost/duplicated/reordered message
    is caught rather than silently applied. See PRD-02 'Stage 2
    corrections'."""
    if request.police_actions_taken != expected.police_actions_taken or request.thief_actions_taken != expected.thief_actions_taken:
        return (
            f"counter mismatch: sender claims police={request.police_actions_taken} "
            f"thief={request.thief_actions_taken}, my local state expects "
            f"police={expected.police_actions_taken} thief={expected.thief_actions_taken}"
        )
    return None
