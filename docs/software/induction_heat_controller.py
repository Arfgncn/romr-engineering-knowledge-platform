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
    max_temp_c: float


class InductionHeatController:
    def build_ramp_profile(self, outlet_target_c: float = 220.0) -> list[HeatZoneCommand]:
        return [
            HeatZoneCommand("zone_1_preheat", 120.0, True, 150.0),
            HeatZoneCommand("zone_2_softening", 160.0, True, 185.0),
            HeatZoneCommand("zone_3_melting", 190.0, True, 215.0),
            HeatZoneCommand("zone_4_stabilization", outlet_target_c, True, 240.0),
            HeatZoneCommand("zone_5_gun_inlet", outlet_target_c, True, 240.0),
        ]

    def compensate_for_flow(self, base_target_c: float, flow_rate_kg_h: float, nominal_flow_kg_h: float) -> float:
        if nominal_flow_kg_h <= 0:
            return base_target_c
        ratio = flow_rate_kg_h / nominal_flow_kg_h
        if ratio > 1.2:
            return min(base_target_c + 10.0, 240.0)
        if ratio < 0.6:
            return max(base_target_c - 10.0, 180.0)
        return base_target_c

    def safe_to_heat(self, measured_temp_c: float, max_temp_c: float, flow_rate_kg_h: float) -> bool:
        if measured_temp_c >= max_temp_c:
            return False
        if flow_rate_kg_h <= 0:
            return False
        return True
