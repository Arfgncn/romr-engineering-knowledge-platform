"""
Speed Synchronization Module

Target: Beckhoff IPC
Role: Synchronizes vehicle speed, robot motion, paint flow and heat targets.
"""

from dataclasses import dataclass


@dataclass
class SpeedTarget:
    target_speed_kmh: float
    hud_speed_message: str


class SpeedSynchronizationModule:
    def process(self, requested_speed_kmh: float, measured_speed_kmh: float) -> SpeedTarget:
        delta = measured_speed_kmh - requested_speed_kmh
        if abs(delta) <= 0.3:
            return SpeedTarget(requested_speed_kmh, "MAINTAIN SPEED")
        if delta > 0.3:
            return SpeedTarget(requested_speed_kmh, "REDUCE SPEED")
        return SpeedTarget(requested_speed_kmh, "INCREASE SPEED SLIGHTLY")
