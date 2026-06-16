"""
HUD Guidance System

Generates driver guidance, speed correction, process status, and safety messages
from RMDE path, vehicle deviation, robot state, PLC state, and quality feedback.
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

    def speed_message(self, target_speed_kmh: float, current_speed_kmh: float) -> HUDMessage:
        delta = current_speed_kmh - target_speed_kmh
        if abs(delta) <= 0.3:
            return HUDMessage("Speed is correct. Maintain current speed.", "good")
        if delta > 0.3:
            return HUDMessage("Reduce speed.", "warning")
        return HUDMessage("Increase speed slightly.", "warning")

    def process_message(self, robot_state: str, paint_ready: bool, heat_ready: bool) -> HUDMessage:
        if not heat_ready:
            return HUDMessage("Paint heating system is not ready. Wait.", "warning", False)
        if not paint_ready:
            return HUDMessage("Paint flow is not ready. Wait.", "warning", False)
        if robot_state == "tracking":
            return HUDMessage("Robot is active. Maintain stable path.", "info")
        if robot_state == "standby":
            return HUDMessage("Robot is in standby position.", "info")
        if robot_state == "alarm":
            return HUDMessage("Robot alarm. Stop operation.", "critical", False)
        return HUDMessage("System state unknown. Verify operation.", "warning", False)

    def safety_message(self, emergency_stop: bool, fire_alarm: bool, overtemperature: bool) -> HUDMessage | None:
        if emergency_stop:
            return HUDMessage("Emergency stop activated.", "critical", False)
        if fire_alarm:
            return HUDMessage("Fire alarm. Stop operation immediately.", "critical", False)
        if overtemperature:
            return HUDMessage("Overtemperature warning. Verify heating system.", "critical", False)
        return None
