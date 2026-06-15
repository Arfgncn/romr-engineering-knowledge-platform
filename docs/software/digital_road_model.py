"""
Digital Road Model Module

Purpose:
Converts survey and classification data into a structured road geometry model
used by the 50 cm reference point generator and RMDE decision engine.
"""

from dataclasses import dataclass


@dataclass
class RoadEdge:
    left_m: float
    right_m: float


@dataclass
class DigitalRoadSegment:
    segment_id: str
    length_m: float
    road_width_m: float
    lane_count: int
    road_type: str
    edges: RoadEdge
    surface_condition: str
    slope_percent: float = 0.0


class DigitalRoadModelBuilder:
    def build_basic_segment(
        self,
        segment_id: str,
        length_m: float,
        road_width_m: float,
        lane_count: int,
        road_type: str,
        surface_condition: str = "unknown",
    ) -> DigitalRoadSegment:
        half = road_width_m / 2.0
        return DigitalRoadSegment(
            segment_id=segment_id,
            length_m=length_m,
            road_width_m=road_width_m,
            lane_count=lane_count,
            road_type=road_type,
            edges=RoadEdge(left_m=-half, right_m=half),
            surface_condition=surface_condition,
        )
