"""
Telemetry System

Records operational history, temperature, flow, GPS and quality data.
"""

from dataclasses import dataclass, asdict
from datetime import datetime
import json


@dataclass
class TelemetryEvent:
    timestamp: str
    point_id: str
    event_type: str
    payload: dict


class TelemetrySystem:
    def create_event(self, point_id: str, event_type: str, payload: dict) -> TelemetryEvent:
        return TelemetryEvent(datetime.utcnow().isoformat(), point_id, event_type, payload)

    def export_event(self, event: TelemetryEvent, file_path: str) -> None:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(asdict(event), f, ensure_ascii=False, indent=2)
