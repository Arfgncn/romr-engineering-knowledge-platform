"""Induction heat control target generator."""
from dataclasses import dataclass

@dataclass
class HeatZoneTarget:
    zone_id: str
    target_temperature_c: float
    max_temperature_c: float
    power_limit_percent: float

class InductionHeatController:
    def staged_targets(self, final_temp_c: float = 210.0) -> list[HeatZoneTarget]:
        return [
            HeatZoneTarget("Z1_PREHEAT", 120.0, 150.0, 45.0),
            HeatZoneTarget("Z2_MELT", 170.0, 190.0, 65.0),
            HeatZoneTarget("Z3_STABILIZE", 195.0, 215.0, 75.0),
            HeatZoneTarget("Z4_FINAL", final_temp_c, 225.0, 85.0),
            HeatZoneTarget("GUN_BODY", final_temp_c, 225.0, 55.0),
        ]
