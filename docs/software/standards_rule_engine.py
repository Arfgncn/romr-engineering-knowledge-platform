"""International standards and adaptive AI rule engine."""
from dataclasses import dataclass

@dataclass
class StandardProfile:
    name: str
    line_width_cm: float
    thickness_mm: float
    dash_m: float | None
    gap_m: float | None
    color: str
    notes: str

class StandardsRuleEngine:
    PROFILES = {
        "turkiye_motorway": StandardProfile("Türkiye motorway", 15, 1.5, 6, 9, "white", "15–20 cm motorway lane reference"),
        "turkiye_urban": StandardProfile("Türkiye urban", 12, 1.5, 3, 3, "white", "3 m / 3 m urban lane structure"),
        "usa_two_way": StandardProfile("U.S. two-way", 10, 1.5, 3, 9, "yellow", "MUTCD yellow centerline approach"),
        "europe_urban": StandardProfile("European urban", 10, 1.5, 3, 3, "white", "country-specific database required"),
        "gcc_desert_motorway": StandardProfile("GCC desert motorway", 20, 2.0, 6, 9, "white", "UV-resistant high-retroreflective marking"),
        "canada_winter": StandardProfile("Canadian winter road", 15, 1.8, 3, 9, "white", "wet-night visibility prioritized"),
        "scandinavia_motorway": StandardProfile("Scandinavian motorway", 15, 1.8, 6, 9, "white", "snow-resistant high-visibility marking"),
        "japan_urban": StandardProfile("Japanese urban", 10, 1.5, 3, 3, "white", "precision-geometry urban mode"),
        "south_korea_smart_city": StandardProfile("South Korea smart city", 12, 1.5, 3, 3, "white", "ITS-compatible marking"),
        "china_expressway": StandardProfile("China expressway", 15, 1.5, 6, 9, "white", "high-speed guidance standard"),
        "airport_taxiway": StandardProfile("Airport taxiway", 15, 1.5, None, None, "yellow", "ICAO/FAA taxiway marking scenario"),
        "industrial_facility": StandardProfile("Industrial facility", 10, 2.0, None, None, "yellow", "heavy-wear-resistant safety marking"),
    }
    def select(self, scenario: str) -> StandardProfile:
        return self.PROFILES.get(scenario, self.PROFILES["europe_urban"])
