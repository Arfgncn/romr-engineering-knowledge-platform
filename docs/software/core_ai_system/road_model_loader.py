"""
Digital Road Model Loader

Loads pre-survey road data and 50 cm reference points.
"""

from dataclasses import dataclass


@dataclass
class RoadReferencePoint:
    point_id: str
    distance_m: float
    road_width_m: float
    road_type: str
    lane_count: int


class RoadModelLoader:
    def generate_demo_model(self, road_length_m: float = 100.0, interval_m: float = 0.5) -> list[RoadReferencePoint]:
        return [
            RoadReferencePoint(f"P{i}", round(i * interval_m, 3), 7.0, "urban_road", 2)
            for i in range(int(road_length_m / interval_m) + 1)
        ]
