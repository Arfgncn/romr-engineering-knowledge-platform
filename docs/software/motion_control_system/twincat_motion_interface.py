"""
TwinCAT Motion Interface

Target: Beckhoff TwinCAT IPC
Role: Deterministic real-time motion execution interface.
"""

from dataclasses import dataclass


@dataclass
class MotionTarget:
    x_m: float
    y_m: float
    speed_kmh: float


class TwinCATMotionInterface:
    def validate_target(self, target: MotionTarget) -> bool:
        return target.speed_kmh <= 7.0

    def execute_target(self, target: MotionTarget) -> str:
        if not self.validate_target(target):
            return "TARGET_REJECTED"
        return "TARGET_ACCEPTED"
