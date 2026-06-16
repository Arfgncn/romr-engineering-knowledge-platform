"""
Induction Heat Controller

Target: Beckhoff IPC
Role: Multi-zone induction temperature target management.
"""

from dataclasses import dataclass


@dataclass
class HeatSetpoint:
    zone: str
    temp_c: float
    enable: bool


class InductionHeatController:
    def build_setpoints(self, target_temp_c: float = 215.0) -> list[HeatSetpoint]:
        return [
            HeatSetpoint("preheat", 120.0, True),
            HeatSetpoint("softening", 160.0, True),
            HeatSetpoint("melting", 190.0, True),
            HeatSetpoint("stabilization", target_temp_c, True),
            HeatSetpoint("gun_inlet", target_temp_c, True),
        ]
