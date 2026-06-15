"""
Pre-Survey Module

Collects and normalizes road survey data from cameras, LiDAR, RTK-GNSS and IMU.
"""

from dataclasses import dataclass


@dataclass
class SurveyInput:
    road_width_m: float
    lane_count: int
    road_length_m: float
    road_type: str
    surface_condition: str = "unknown"
    existing_line_detected: bool = False


class PreSurveyModule:
    def collect_manual_prototype_data(
        self,
        road_width_m: float,
        lane_count: int,
        road_length_m: float,
        road_type: str,
        surface_condition: str = "unknown",
    ) -> SurveyInput:
        return SurveyInput(
            road_width_m=road_width_m,
            lane_count=lane_count,
            road_length_m=road_length_m,
            road_type=road_type,
            surface_condition=surface_condition,
        )
