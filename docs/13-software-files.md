[13-software-files.md](https://github.com/user-attachments/files/28998059/13-software-files.md)
# 13 — Software Files & Distributed Code Package

<div class="git-buttons">

[Git: Distributed Software Architecture](software-platform/ROMR_Distributed_Software_Architecture_V1.md)
[Git: Core AI System](software/core_ai_system/main.py)
[Git: Decision Engine](software/core_ai_system/decision_engine.py)
[Git: Robot Path Planner](software/core_ai_system/robot_path_planner.py)
[Git: Motion Control](software/motion_control_system/twincat_motion_interface.py)
[Git: Robot Arm Control](software/robot_arm_control/kuka_robot_bridge.py)
[Git: Flow Control](software/flow_control_system/paint_flow_controller.py)
[Git: Induction Heat Control](software/induction_heat_control/induction_heat_controller.py)
[Git: Speed Synchronization](software/speed_synchronization/speed_synchronization_module.py)
[Git: HUD System](software/hud_system/hud_guidance_system.py)
[Git: Safety System](software/safety_system/safety_supervisor.py)
[Git: Quality Control AI](software/quality_control_ai/quality_control_module.py)

</div>

---

## 1. Purpose

This section provides a direct navigation map to the ROMR software files.

The system is not a single Python file. It is a distributed industrial software architecture where each software module runs on the correct target system.

---

## 2. Software Folder Structure

```text
docs/software/
│
├── core_ai_system/
│   ├── main.py
│   ├── mission_manager.py
│   ├── road_model_loader.py
│   ├── decision_engine.py
│   ├── robot_path_planner.py
│   ├── hud_generator.py
│   ├── quality_analyzer.py
│   ├── telemetry_system.py
│   ├── ai_inference_engine.py
│   └── ethercat_interface.py
│
├── motion_control_system/
│   └── twincat_motion_interface.py
│
├── robot_arm_control/
│   └── kuka_robot_bridge.py
│
├── flow_control_system/
│   └── paint_flow_controller.py
│
├── induction_heat_control/
│   └── induction_heat_controller.py
│
├── speed_synchronization/
│   └── speed_synchronization_module.py
│
├── hud_system/
│   └── hud_guidance_system.py
│
├── safety_system/
│   └── safety_supervisor.py
│
└── quality_control_ai/
    └── quality_control_module.py
```

---

## 3. Software-to-Hardware Mapping

| Software | Target Hardware | Role | Git |
|---|---|---|---|
| Core AI System | NVIDIA Jetson AGX Orin | high-level AI brain | [Git](software/core_ai_system/main.py) |
| Motion Control | Beckhoff TwinCAT IPC | deterministic motion interface | [Git](software/motion_control_system/twincat_motion_interface.py) |
| Robot Arm Control | KUKA Controller + Beckhoff | robot command bridge | [Git](software/robot_arm_control/kuka_robot_bridge.py) |
| Flow Control | Beckhoff IPC | paint flow regulation | [Git](software/flow_control_system/paint_flow_controller.py) |
| Induction Heat Control | Beckhoff IPC | multi-zone heating logic | [Git](software/induction_heat_control/induction_heat_controller.py) |
| Speed Synchronization | Beckhoff IPC | vehicle speed and flow sync | [Git](software/speed_synchronization/speed_synchronization_module.py) |
| Decision Engine | Jetson Orin | RMDE decision logic | [Git](software/core_ai_system/decision_engine.py) |
| HUD System | Jetson Orin | ghost-line and guidance | [Git](software/hud_system/hud_guidance_system.py) |
| Safety System | Beckhoff Safety PLC | safety permission layer | [Git](software/safety_system/safety_supervisor.py) |
| Quality Control AI | Jetson Orin | vision and quality analysis | [Git](software/quality_control_ai/quality_control_module.py) |

---

## 4. Main Rule

```text
AI layer decides.
Real-time layer executes.
Safety layer permits.
Quality layer validates.
Telemetry layer records.
```

This is the core software control principle of the ROMR platform.
