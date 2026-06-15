"""
Robot Command Layer

Converts RMDE decisions into industrial robot and X/Y rail target commands.
"""

from dataclasses import dataclass


@dataclass
class RobotCommand:
    reference_point_id: str
    target_x_m: float
    target_y_m: float
    target_z_m: float
    wrist_angle_deg: float
    gun_enable: bool
    safe_standby: bool = False


class RobotCommandLayer:
    def build_commands(self, decisions, nozzle_height_m: float = 0.25) -> list[RobotCommand]:
        commands = []
        for i, d in enumerate(decisions):
            commands.append(
                RobotCommand(
                    reference_point_id=d.reference_point_id,
                    target_x_m=i * 0.5,
                    target_y_m=d.robot_target_y_m,
                    target_z_m=nozzle_height_m,
                    wrist_angle_deg=0.0,
                    gun_enable=d.line_required,
                )
            )
        return commands
