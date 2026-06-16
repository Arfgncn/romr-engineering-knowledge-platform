"""
PLC Process Interface

Builds process-command packages for PLC-controlled physical subsystems.
"""

from dataclasses import dataclass


@dataclass
class PLCProcessCommand:
    paint_flow_enable: bool
    gun_heat_enable: bool
    induction_enable: bool
    atomizing_air_enable: bool
    suction_fan_enable: bool
    rotary_bell_rpm_setpoint: int
    purge_enable: bool = False
    glass_bead_enable: bool = False


@dataclass
class PLCReadiness:
    safety_ok: bool
    paint_temperature_ok: bool
    paint_pressure_ok: bool
    gun_ready: bool
    air_ready: bool
    suction_ready: bool
    robot_pose_valid: bool


class PLCProcessInterface:
    def allow_application(self, readiness: PLCReadiness) -> bool:
        return all([
            readiness.safety_ok,
            readiness.paint_temperature_ok,
            readiness.paint_pressure_ok,
            readiness.gun_ready,
            readiness.air_ready,
            readiness.suction_ready,
            readiness.robot_pose_valid,
        ])

    def build_application_command(self, line_required: bool, readiness: PLCReadiness, rpm: int = 250) -> PLCProcessCommand:
        allowed = line_required and self.allow_application(readiness)
        return PLCProcessCommand(
            paint_flow_enable=allowed,
            gun_heat_enable=True,
            induction_enable=True,
            atomizing_air_enable=allowed,
            suction_fan_enable=allowed,
            rotary_bell_rpm_setpoint=rpm,
            glass_bead_enable=allowed,
        )

    def build_purge_command(self) -> PLCProcessCommand:
        return PLCProcessCommand(
            paint_flow_enable=False,
            gun_heat_enable=True,
            induction_enable=True,
            atomizing_air_enable=True,
            suction_fan_enable=True,
            rotary_bell_rpm_setpoint=100,
            purge_enable=True,
            glass_bead_enable=False,
        )
