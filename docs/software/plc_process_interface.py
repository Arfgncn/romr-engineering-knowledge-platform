"""PLC process interface packet definitions."""
from dataclasses import dataclass

@dataclass
class ProcessTargetPacket:
    timestamp_ms: int
    source_module: str
    target_module: str
    paint_temp_target_c: float
    flow_target_kg_min: float
    screw_speed_percent: float
    valve_open: bool
    induction_power_percent: float
    safety_permissive: bool

class PLCProcessInterface:
    def build_marking_packet(self, flow_kg_min: float, temp_c: float, safety_ok: bool) -> ProcessTargetPacket:
        return ProcessTargetPacket(
            timestamp_ms=0, source_module="RMDE", target_module="Beckhoff_TwinCAT_IPC",
            paint_temp_target_c=temp_c, flow_target_kg_min=flow_kg_min,
            screw_speed_percent=50.0, valve_open=safety_ok,
            induction_power_percent=65.0, safety_permissive=safety_ok,
        )
