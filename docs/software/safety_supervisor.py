"""
Safety Supervisor

Checks whether robot, gun, induction, pressure and emergency states allow operation.
"""

from dataclasses import dataclass


@dataclass
class SafetyState:
    e_stop_ok: bool
    robot_safe: bool
    gun_temperature_ok: bool
    pressure_ok: bool
    fire_alarm_ok: bool


class SafetySupervisor:
    def allow_operation(self, state: SafetyState) -> bool:
        return all([
            state.e_stop_ok,
            state.robot_safe,
            state.gun_temperature_ok,
            state.pressure_ok,
            state.fire_alarm_ok,
        ])
