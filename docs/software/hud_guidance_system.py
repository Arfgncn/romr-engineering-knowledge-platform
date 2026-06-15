"""HUD ghost-line and driver guidance module."""
from dataclasses import dataclass

@dataclass
class HUDMessage:
    ghost_line_visible: bool
    path_status: str
    next_action: str
    voice_message: str
    quality_status: str
    safety_status: str

class HUDGuidanceSystem:
    def render_state(self, deviation_cm: float, safety_ok: bool, quality_ok: bool) -> HUDMessage:
        if not safety_ok:
            return HUDMessage(False, "LOCKED", "STOP", "Safety stop active", "UNKNOWN", "FAULT")
        if abs(deviation_cm) > 5:
            return HUDMessage(True, "OUT_OF_TOLERANCE", "CORRECT_ALIGNMENT", "Correct alignment", "CHECK", "OK")
        return HUDMessage(True, "GOOD", "KEEP_STRAIGHT", "Alignment is correct", "GOOD" if quality_ok else "CHECK", "OK")
