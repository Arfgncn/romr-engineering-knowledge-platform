"""Road classification module."""
from dataclasses import dataclass

@dataclass
class RoadClass:
    road_type: str
    application_zone: str
    confidence: float

class RoadClassifier:
    def classify(self, road_width_m: float, lane_count: int, road_type_hint: str) -> RoadClass:
        if road_type_hint:
            return RoadClass(road_type=road_type_hint, application_zone="standard_segment", confidence=0.75)
        if lane_count >= 4:
            return RoadClass("divided_highway", "standard_segment", 0.70)
        if road_width_m < 5.5:
            return RoadClass("narrow_two_way", "standard_segment", 0.65)
        return RoadClass("two_way", "standard_segment", 0.60)
