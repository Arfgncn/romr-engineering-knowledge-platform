"""
Paint Flow Controller

Target: Beckhoff IPC
Role: Paint flow, screw pump and glass bead command generation.
"""

from dataclasses import dataclass


@dataclass
class FlowCommand:
    paint_flow_kg_h: float
    glass_bead_ratio: float
    pump_enable: bool


class PaintFlowController:
    def calculate_flow(self, line_width_cm: float, thickness_mm: float, speed_kmh: float, density_kg_m3: float = 2000.0) -> FlowCommand:
        v = speed_kmh / 3.6
        b = line_width_cm / 100
        h = thickness_mm / 1000
        kg_h = v * b * h * density_kg_m3 * 3600
        return FlowCommand(round(kg_h, 2), 0.30, True)
