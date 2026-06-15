"""
Telemetry Logger Module

Purpose:
Records RMDE decisions, PLC process states, robot commands, HUD messages,
and quality-control results for traceability and future optimization.
"""

from dataclasses import dataclass, asdict
from datetime import datetime
import csv
from pathlib import Path


@dataclass
class TelemetryRecord:
    timestamp: str
    reference_point_id: str
    event_type: str
    payload: dict


class TelemetryLogger:
    def __init__(self, output_path: str = "romr_telemetry.csv"):
        self.output_path = Path(output_path)

    def log(self, reference_point_id: str, event_type: str, payload: dict):
        record = TelemetryRecord(
            timestamp=datetime.utcnow().isoformat(),
            reference_point_id=reference_point_id,
            event_type=event_type,
            payload=payload,
        )
        write_header = not self.output_path.exists()
        with self.output_path.open("a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["timestamp", "reference_point_id", "event_type", "payload"])
            if write_header:
                writer.writeheader()
            writer.writerow(asdict(record))
