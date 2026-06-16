"""
ROMR Core AI System Main Entry

Target: NVIDIA Jetson AGX Orin Industrial
Role: High-level mission orchestration. Does not perform deterministic servo control.
"""

from mission_manager import MissionManager


def main() -> None:
    mission = MissionManager(mission_id="ROMR-DEMO-001")
    mission.initialize()
    mission.run_demo_cycle()


if __name__ == "__main__":
    main()
