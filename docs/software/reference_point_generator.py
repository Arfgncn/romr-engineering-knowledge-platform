"""
Reference Point Generator

Generates 50 cm reference points for digital road-model-based marking.
"""

from dataclasses import dataclass


@dataclass
class ReferencePoint:
    point_id: str
    distance_m: float
    road_width_m: float
    lane_count: int
    line_type: str | None = None
    robot_target_y_m: float | None = None
    vehicle_speed_kmh: float = 5.0
    paint_flow_rate_kg_h: float | None = None


class ReferencePointGenerator:
    def generate(self, road_length_m: float, road_width_m: float, lane_count: int, interval_m: float = 0.5) -> list[ReferencePoint]:
        points = []
        count = int(road_length_m / interval_m) + 1
        for i in range(count):
            points.append(
                ReferencePoint(
                    point_id=f"P{i}",
                    distance_m=round(i * interval_m, 3),
                    road_width_m=road_width_m,
                    lane_count=lane_count,
                )
            )
        return points
