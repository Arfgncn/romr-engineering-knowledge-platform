"""
Existing Line Detector Module

Purpose:
Detects existing road markings, evaluates their condition, and prepares
reference data for RMDE decision logic.
"""

from dataclasses import dataclass
from enum import Enum


class LineCondition(str, Enum):
    NONE = "none"
    GOOD = "good"
    BROKEN = "broken"
    WORN = "worn"
    UNKNOWN = "unknown"


@dataclass
class ExistingLineResult:
    detected: bool
    condition: LineCondition
    confidence: float
    lateral_position_m: float | None = None
    color: str | None = None


class ExistingLineDetector:
    def evaluate(self, camera_frame=None, lidar_data=None) -> ExistingLineResult:
        # Prototype placeholder: real implementation will use computer vision.
        return ExistingLineResult(
            detected=False,
            condition=LineCondition.NONE,
            confidence=0.0,
        )
