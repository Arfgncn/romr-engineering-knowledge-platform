"""
Quality Control Module

Evaluates applied marking geometry against reference-point-based targets.
"""

from dataclasses import dataclass


@dataclass
class QualityResult:
    reference_point_id: str
    width_error_cm: float
    alignment_error_cm: float
    status: str


class QualityControlModule:
    def evaluate(self, reference_point_id: str, target_width_cm: float, measured_width_cm: float, alignment_error_cm: float) -> QualityResult:
        width_error = measured_width_cm - target_width_cm
        status = "ok" if abs(width_error) <= 1.0 and abs(alignment_error_cm) <= 5.0 else "out_of_tolerance"
        return QualityResult(reference_point_id, width_error, alignment_error_cm, status)
