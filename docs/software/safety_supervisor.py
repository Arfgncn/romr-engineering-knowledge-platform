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
    service_covers_closed: bool = True
    generator_ok: bool = True
    suction_ok: bool = True


class SafetySupervisor:
    def allow_operation(self, state: SafetyState) -> bool:
        return all([
            state.e_stop_ok,
            state.robot_safe,
            state.gun_temperature_ok,
            state.pressure_ok,
            state.fire_alarm_ok,
            state.service_covers_closed,
            state.generator_ok,
            state.suction_ok,
        ])

    def alarm_list(self, state: SafetyState) -> list[str]:
        alarms = []
        if not state.e_stop_ok:
            alarms.append("E_STOP_ACTIVE")
        if not state.robot_safe:
            alarms.append("ROBOT_SAFETY_ZONE")
        if not state.gun_temperature_ok:
            alarms.append("GUN_OVERTEMPERATURE")
        if not state.pressure_ok:
            alarms.append("PAINT_PRESSURE_ALARM")
        if not state.fire_alarm_ok:
            alarms.append("FIRE_ALARM")
        if not state.service_covers_closed:
            alarms.append("SERVICE_COVER_OPEN")
        if not state.generator_ok:
            alarms.append("GENERATOR_ALARM")
        if not state.suction_ok:
            alarms.append("SUCTION_FAILURE")
        return alarms
