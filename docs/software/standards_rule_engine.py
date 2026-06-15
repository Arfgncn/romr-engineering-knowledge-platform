"""
ROMR Standards Rule Engine

Purpose:
Loads region/country-specific road marking rules and provides the RMDE with
line geometry, color, thickness, visibility and quality parameters.

This is an engineering prototype, not a final legal standards database.
"""

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any


@dataclass
class StandardRule:
    region: str
    road_type: str
    line_type: str
    line_width_cm: str
    line_gap: str
    color: str
    thickness: str | None = None
    special_note: str | None = None


class StandardsRuleEngine:
    def __init__(self, library_path: str | Path = "docs/standards/international_standards_library_v1.json"):
        self.library_path = Path(library_path)
        self.library: dict[str, Any] = {}

    def load(self) -> None:
        if self.library_path.exists():
            self.library = json.loads(self.library_path.read_text(encoding="utf-8"))
        else:
            self.library = {"regions": {}}

    def get_region(self, region: str) -> dict[str, Any]:
        if not self.library:
            self.load()
        return self.library.get("regions", {}).get(region.lower(), {})

    def find_rule(self, region: str, road_type: str) -> StandardRule | None:
        data = self.get_region(region)
        for rule in data.get("rules", []):
            if rule.get("road_type") == road_type:
                return StandardRule(
                    region=region,
                    road_type=road_type,
                    line_type=rule.get("line_type", ""),
                    line_width_cm=rule.get("line_width_cm", ""),
                    line_gap=rule.get("line_gap", ""),
                    color=rule.get("color", ""),
                    thickness=rule.get("thickness_mm") or rule.get("thickness"),
                    special_note=data.get("architecture_note") or data.get("climate_profile"),
                )
        return None

    def select_ai_scenario(self, scenario_key: str) -> str:
        scenarios = {
            "turkiye_motorway": "15–20 cm motorway lane standard",
            "turkiye_urban": "3 m / 3 m urban lane structure",
            "usa_two_way": "Yellow centerline approach",
            "europe_urban": "10–12 cm urban lane standard",
            "gcc_desert_motorway": "Thick-film, UV-resistant, high-retroreflective marking",
            "canada_winter": "Wet-night visibility prioritized edge guidance",
            "airport_taxiway": "ICAO / FAA taxiway marking standard",
            "industrial_facility": "Heavy-wear-resistant safety marking",
        }
        return scenarios.get(scenario_key, "Manual engineering verification required")
