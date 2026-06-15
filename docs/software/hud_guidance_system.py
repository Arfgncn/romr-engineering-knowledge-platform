"""
HUD Guidance System

Generates driver guidance messages from RMDE path and application state.
"""

from dataclasses import dataclass


@dataclass
class HUDMessage:
    text: str
    level: str = "info"
    ghost_line_active: bool = True


class HUDGuidanceSystem:
    def alignment_message(self, deviation_cm: float) -> HUDMessage:
        if abs(deviation_cm) <= 3:
            return HUDMessage("Alignment is correct. Maintain current path.", "good")
        if deviation_cm > 3:
            return HUDMessage("Make a slight left correction.", "warning")
        return HUDMessage("Make a slight right correction.", "warning")
