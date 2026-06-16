"""
Robot Path Planner

Converts RMDE marking decisions into robot target poses.
"""

from dataclasses import dataclass


@dataclass
class RobotTarget:
    point_id: str
    x_m: float
    y_m: float
    z_m: float
    pitch_deg: float
    gun_enable: bool


class RobotPathPlanner:
    def build_target(self, point_id: str, distance_m: float, target_y_m: float, gun_height_m: float = 0.25) -> RobotTarget:
        return RobotTarget(point_id, distance_m, target_y_m, gun_height_m, 0.0, True)
