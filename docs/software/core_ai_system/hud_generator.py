"""
HUD Generator

Creates ghost-line and driver guidance messages.
"""

from dataclasses import dataclass


@dataclass
class HUDFrame:
    point_id: str
    ghost_line_active: bool
    guidance_text: str
    warning_level: str


class HUDGenerator:
    def create_frame(self, point_id: str, message: str, deviation_cm: float = 0.0) -> HUDFrame:
        level = "good" if abs(deviation_cm) <= 3 else "warning"
        return HUDFrame(point_id, True, message, level)
