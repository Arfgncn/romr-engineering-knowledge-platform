"""Road Marking Decision Engine V1."""
from dataclasses import dataclass

@dataclass
class RoadInput:
    road_width_m: float
    road_type: str
    lane_count: int
    existing_line: bool
    line_condition: str
    road_surface: str
    country_scenario: str

@dataclass
class DecisionOutput:
    center_line_allowed: bool
    edge_line_required: bool
    line_type: str
    reason: str

class RMDEDecisionEngine:
    def decide(self, road: RoadInput, min_centerline_width_m: float = 5.5) -> DecisionOutput:
        if road.road_type in ("two_way", "narrow_two_way") and road.road_width_m < min_centerline_width_m:
            return DecisionOutput(False, True, "right_edge_line", "Road width below centerline threshold")
        if road.existing_line and road.line_condition == "good":
            return DecisionOutput(True, True, "existing_line_reference", "Existing line accepted as reference")
        if road.line_condition == "broken":
            return DecisionOutput(True, True, "estimated_reference_line", "Broken marking reconstructed from adjacent segments")
        if not road.existing_line and road.road_surface == "new_asphalt":
            return DecisionOutput(True, True, "new_digital_road_model_line", "New asphalt geometry generated digitally")
        return DecisionOutput(True, True, "standard_lane_marking", "Default standards-based marking")
