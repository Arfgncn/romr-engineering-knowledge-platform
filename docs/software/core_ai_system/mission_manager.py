"""
Mission Manager

Handles mission start, stop, task state, and high-level execution cycle.
"""

from dataclasses import dataclass


@dataclass
class MissionState:
    mission_id: str
    active: bool = False
    current_reference_point: str | None = None


class MissionManager:
    def __init__(self, mission_id: str):
        self.state = MissionState(mission_id=mission_id)

    def initialize(self) -> None:
        self.state.active = True

    def run_demo_cycle(self) -> None:
        self.state.current_reference_point = "P0"
        print(f"[MISSION] {self.state.mission_id} active at {self.state.current_reference_point}")

    def stop(self) -> None:
        self.state.active = False
