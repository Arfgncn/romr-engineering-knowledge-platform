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


class PLCProcessInterface:
    def build_application_command(self, line_required: bool, rpm: int = 250) -> PLCProcessCommand:
        return PLCProcessCommand(
            paint_flow_enable=line_required,
            gun_heat_enable=True,
            induction_enable=True,
            atomizing_air_enable=line_required,
            suction_fan_enable=line_required,
            rotary_bell_rpm_setpoint=rpm,
        )
