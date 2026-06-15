"""
RMDE Decision Engine

Generates road marking decisions using road model, reference points, and standards.
"""

from dataclasses import dataclass


@dataclass
class MarkingDecision:
    reference_point_id: str
    line_required: bool
    line_type: str
    line_width_cm: float
    line_color: str
    vehicle_speed_kmh: float
    robot_target_y_m: float


class RMDEDecisionEngine:
    def decide_basic_edge_line(self, reference_points, line_width_cm: float = 14.0, color: str = "white") -> list[MarkingDecision]:
        decisions = []
        for p in reference_points:
            decisions.append(
                MarkingDecision(
                    reference_point_id=p.point_id,
                    line_required=True,
                    line_type="right_edge_line",
                    line_width_cm=line_width_cm,
                    line_color=color,
                    vehicle_speed_kmh=p.vehicle_speed_kmh,
                    robot_target_y_m=(p.road_width_m / 2.0) - 0.20,
                )
            )
        return decisions
