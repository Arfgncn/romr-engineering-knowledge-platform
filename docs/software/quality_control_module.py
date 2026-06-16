"""
Quality Control Module

Evaluates applied marking geometry against reference-point-based targets.
"""

from dataclasses import dataclass


@dataclass
class QualityResult:
    reference_point_id: str
    target_width_cm: float
    measured_width_cm: float
    width_error_cm: float
    alignment_error_cm: float
    status: str
    recommended_correction: str


class QualityControlModule:
    def evaluate(
        self,
        reference_point_id: str,
        target_width_cm: float,
        measured_width_cm: float,
        alignment_error_cm: float,
        width_tolerance_cm: float = 1.0,
        alignment_tolerance_cm: float = 5.0,
    ) -> QualityResult:
        width_error = measured_width_cm - target_width_cm

        if abs(width_error) <= width_tolerance_cm and abs(alignment_error_cm) <= alignment_tolerance_cm:
            status = "ok"
            correction = "No correction required."
        elif abs(alignment_error_cm) > alignment_tolerance_cm:
            status = "out_of_tolerance"
            correction = "Check robot Y-offset, vehicle alignment, and reference point matching."
        elif width_error < -width_tolerance_cm:
            status = "out_of_tolerance"
            correction = "Increase paint flow, reduce speed, or verify gun height."
        else:
            status = "out_of_tolerance"
            correction = "Reduce paint flow, increase speed, or verify rotary bell geometry."

        return QualityResult(
            reference_point_id=reference_point_id,
            target_width_cm=target_width_cm,
            measured_width_cm=measured_width_cm,
            width_error_cm=width_error,
            alignment_error_cm=alignment_error_cm,
            status=status,
            recommended_correction=correction,
        )
