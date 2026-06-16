"""
HUD Guidance System

Target: NVIDIA Jetson AGX Orin Industrial
Role: Driver visual guidance and ghost-line output.
"""

from dataclasses import dataclass


@dataclass
class HUDMessage:
    text: str
    level: str


class HUDGuidanceSystem:
    def alignment_message(self, deviation_cm: float) -> HUDMessage:
        if abs(deviation_cm) <= 3:
            return HUDMessage("PATH ALIGNMENT: GOOD", "good")
        if deviation_cm > 3:
            return HUDMessage("MAKE A SLIGHT LEFT CORRECTION", "warning")
        return HUDMessage("MAKE A SLIGHT RIGHT CORRECTION", "warning")
