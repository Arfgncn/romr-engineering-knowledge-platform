"""Real-time road marking quality control module."""
from dataclasses import dataclass

@dataclass
class QualityResult:
    reference_start: str
    reference_end: str
    width_cm: float
    thickness_mm: float
    deviation_cm: float
    quality_score: float
    recommended_correction: str

class QualityControlModule:
    def evaluate(self, width_cm: float, thickness_mm: float, deviation_cm: float) -> QualityResult:
        score = 100.0
        if abs(width_cm - 14.0) > 0.5: score -= 10
        if abs(thickness_mm - 1.5) > 0.2: score -= 10
        if abs(deviation_cm) > 5: score -= 20
        rec = "No correction" if score >= 90 else "Adjust robot calibration / speed / flow"
        return QualityResult("P0", "P1", width_cm, thickness_mm, deviation_cm, score, rec)
