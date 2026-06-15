"""
Pre-Survey Module
Target device: NVIDIA Jetson AGX Orin Industrial
Purpose: collect and normalize camera, LiDAR, RTK-GNSS and IMU data before RMDE.
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class SurveyPacket:
    road_width_m: float
    lane_count: int
    lane_width_m: float
    road_type_hint: str
    existing_line_detected: bool
    gps_lat: Optional[float] = None
    gps_lon: Optional[float] = None
    imu_pitch_deg: float = 0.0
    imu_roll_deg: float = 0.0
    surface_condition: str = "unknown"

class PreSurveyModule:
    def collect(self) -> SurveyPacket:
        # Placeholder for real camera/LiDAR/RTK/IMU acquisition.
        return SurveyPacket(
            road_width_m=5.8,
            lane_count=2,
            lane_width_m=2.9,
            road_type_hint="two_way",
            existing_line_detected=False,
            surface_condition="new_asphalt",
        )
