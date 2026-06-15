"""
Induction Heat Controller

Prototype controller for multi-zone induction heating setpoints.
"""

from dataclasses import dataclass


@dataclass
class HeatZoneCommand:
    zone_id: str
    target_temp_c: float
    enable: bool


class InductionHeatController:
    def build_ramp_profile(self, outlet_target_c: float = 220.0) -> list[HeatZoneCommand]:
        return [
            HeatZoneCommand("zone_1_preheat", 120.0, True),
            HeatZoneCommand("zone_2_softening", 160.0, True),
            HeatZoneCommand("zone_3_melting", 190.0, True),
            HeatZoneCommand("zone_4_stabilization", outlet_target_c, True),
            HeatZoneCommand("zone_5_gun_inlet", outlet_target_c, True),
        ]
