"""
KUKA Robot Bridge

Target: KUKA Controller + Beckhoff
Role: Robot command bridge and safety interlock coordination.
"""

from dataclasses import dataclass


@dataclass
class KukaPose:
    x_m: float
    y_m: float
    z_m: float
    pitch_deg: float


class KukaRobotBridge:
    def send_pose(self, pose: KukaPose, safety_ok: bool) -> str:
        if not safety_ok:
            return "ROBOT_COMMAND_BLOCKED_BY_SAFETY"
        return f"KUKA_POSE_ACCEPTED: {pose}"
