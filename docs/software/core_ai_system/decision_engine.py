"""
Road Marking Decision Engine

Target: NVIDIA Jetson AGX Orin Industrial
Role: Determines what will be marked, where it will be marked, and with which parameters.
"""

from dataclasses import dataclass


@dataclass
class MarkingDecision:
    point_id: str
    line_type: str
    line_width_cm: float
    line_thickness_mm: float
    target_speed_kmh: float
    robot_target_y_m: float
    paint_temperature_c: float
    hud_message: str


class DecisionEngine:
    def decide(self, point_id: str, road_width_m: float, road_type: str, country: str = "turkiye") -> MarkingDecision:
        if road_type == "two_way_narrow" or road_width_m < 5.8:
            return MarkingDecision(point_id, "right_edge_line", 14.0, 1.5, 5.0, road_width_m / 2 - 0.20, 215.0, "CENTER LINE DISABLED — EDGE LINE MODE ACTIVE")
        return MarkingDecision(point_id, "lane_marking", 14.0, 1.5, 5.0, 0.0, 215.0, "STANDARD LINE APPLICATION")
