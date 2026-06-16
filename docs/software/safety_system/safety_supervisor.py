"""
Safety Supervisor

Target: Beckhoff Safety PLC
Role: Safety permission logic.
"""

from dataclasses import dataclass


@dataclass
class SafetyState:
    e_stop_ok: bool
    fire_ok: bool
    robot_zone_ok: bool
    overtemperature_ok: bool
    pressure_ok: bool


class SafetySupervisor:
    def permit_application(self, state: SafetyState) -> bool:
        return all([
            state.e_stop_ok,
            state.fire_ok,
            state.robot_zone_ok,
            state.overtemperature_ok,
            state.pressure_ok,
        ])
