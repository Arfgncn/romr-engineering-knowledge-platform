"""Robot command layer."""
from dataclasses import dataclass

@dataclass
class RobotCommand:
    reference_id: str
    x_start_m: float
    x_end_m: float
    y_target_m: float
    z_height_mm: float
    tool_angle_deg: float
    line_width_cm: float
    paint_temperature_c: float

class RobotCommandLayer:
    def from_reference_point(self, p_id: str, distance_m: float, robot_target_y_m: float, line_width_cm: float) -> RobotCommand:
        return RobotCommand(
            reference_id=p_id,
            x_start_m=distance_m,
            x_end_m=distance_m + 0.5,
            y_target_m=robot_target_y_m,
            z_height_mm=25.0,
            tool_angle_deg=0.0,
            line_width_cm=line_width_cm,
            paint_temperature_c=210.0,
        )
