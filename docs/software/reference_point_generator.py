"""50 cm reference point generator."""
from dataclasses import dataclass

@dataclass
class ReferencePoint:
    p_id: str
    distance_m: float
    road_width_m: float
    center_line_allowed: bool
    edge_line_required: bool
    line_type: str
    robot_target_y_m: float
    vehicle_speed_kmh: float
    paint_flow_kg_min: float
    glass_bead_flow_g_m2: float
    driver_command: str

class ReferencePointGenerator:
    def generate(self, road_length_m: float, road_width_m: float, center_line_allowed: bool, line_type: str) -> list[ReferencePoint]:
        points = []
        n = int(road_length_m / 0.5) + 1
        for i in range(n):
            distance = round(i * 0.5, 2)
            target_y = 0.0 if center_line_allowed else round(road_width_m / 2 - 0.20, 2)
            points.append(ReferencePoint(
                p_id=f"P{i}", distance_m=distance, road_width_m=road_width_m,
                center_line_allowed=center_line_allowed, edge_line_required=True,
                line_type=line_type, robot_target_y_m=target_y, vehicle_speed_kmh=5.0,
                paint_flow_kg_min=0.0, glass_bead_flow_g_m2=0.0,
                driver_command="Maintain path" if center_line_allowed else "Apply edge reference line",
            ))
        return points
