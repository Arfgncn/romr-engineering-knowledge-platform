"""Safety supervisor interface. Final safety authority belongs to Safety PLC."""
from dataclasses import dataclass

@dataclass
class SafetyStatus:
    emergency_stop_active: bool
    robot_zone_clear: bool
    pressure_within_limit: bool
    temperature_within_limit: bool
    safety_permissive: bool

class SafetySupervisor:
    def evaluate(self, e_stop: bool, zone_clear: bool, pressure_ok: bool, temp_ok: bool) -> SafetyStatus:
        permissive = (not e_stop) and zone_clear and pressure_ok and temp_ok
        return SafetyStatus(e_stop, zone_clear, pressure_ok, temp_ok, permissive)
