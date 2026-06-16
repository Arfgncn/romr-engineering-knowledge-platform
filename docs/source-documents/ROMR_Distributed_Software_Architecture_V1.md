# ROMR Distributed Software Architecture V1

<div class="git-buttons">

[Git: Core AI System](../software/core_ai_system/main.py)
[Git: Mission Manager](../software/core_ai_system/mission_manager.py)
[Git: Road Model Loader](../software/core_ai_system/road_model_loader.py)
[Git: Decision Engine](../software/core_ai_system/decision_engine.py)
[Git: Robot Path Planner](../software/core_ai_system/robot_path_planner.py)
[Git: HUD Generator](../software/core_ai_system/hud_generator.py)
[Git: Quality Analyzer](../software/core_ai_system/quality_analyzer.py)
[Git: Telemetry System](../software/core_ai_system/telemetry_system.py)
[Git: AI Inference Engine](../software/core_ai_system/ai_inference_engine.py)
[Git: EtherCAT Interface](../software/core_ai_system/ethercat_interface.py)

</div>

---

## 1. Purpose

This software architecture module separates the ROMR system into real industrial software layers.

The system must not be developed as a single Python file. It is a distributed robotic road marking software ecosystem consisting of:

- AI computer,
- real-time motion controller,
- robot controller,
- Beckhoff TwinCAT IPC,
- EtherCAT network,
- safety PLC,
- field sensors,
- HMI / HUD interface,
- quality-control AI,
- telemetry and data logging infrastructure.

---

## 2. Distributed Software Layer Table

| Section | Software Layer | Target System | Git |
|---|---|---|---|
| 1 | Core AI System | NVIDIA Jetson AGX Orin Industrial | [Git](../software/core_ai_system/main.py) |
| 2 | Motion Control System | Beckhoff TwinCAT IPC | [Git](../software/motion_control_system/twincat_motion_interface.py) |
| 3 | Robot Arm Control | KUKA Controller + Beckhoff | [Git](../software/robot_arm_control/kuka_robot_bridge.py) |
| 4 | Flow Control System | Beckhoff IPC | [Git](../software/flow_control_system/paint_flow_controller.py) |
| 5 | Induction Heat Control | Beckhoff IPC | [Git](../software/induction_heat_control/induction_heat_controller.py) |
| 6 | Speed Synchronization | Beckhoff IPC | [Git](../software/speed_synchronization/speed_synchronization_module.py) |
| 7 | Decision Engine | NVIDIA Jetson AGX Orin | [Git](../software/core_ai_system/decision_engine.py) |
| 8 | HUD System | NVIDIA Jetson AGX Orin | [Git](../software/hud_system/hud_guidance_system.py) |
| 9 | Safety System | Beckhoff Safety PLC | [Git](../software/safety_system/safety_supervisor.py) |
| 10 | Quality Control AI | NVIDIA Jetson AGX Orin | [Git](../software/quality_control_ai/quality_control_module.py) |

---

## 3. Core Architectural Rule

```text
AI generates decisions
↓
Real-time controller executes
↓
Quality system validates
↓
AI system learns and corrects
```

The AI layer must not directly control servo motion. Real-time motion execution must remain inside Beckhoff TwinCAT / robot controller / safety PLC layers.

---

## 4. Main Software Flow

```text
Road Model Loader
↓
Road Classification
↓
Standards Rule Engine
↓
Decision Engine
↓
Reference Point Planner
↓
Robot Path Planner
↓
Flow / Heat / Speed Targets
↓
PLC / EtherCAT Interface
↓
Robot Execution
↓
HUD Guidance
↓
Quality Analysis
↓
Telemetry Logger
```

---

## 5. Core AI System

Target hardware:

```text
NVIDIA Jetson AGX Orin Industrial
```

Primary functions:

- digital road model processing,
- RMDE execution,
- robot target coordinate generation,
- HUD management,
- quality-analysis infrastructure,
- AI inference processing,
- mission management,
- telemetry and logging,
- high-level EtherCAT communication.

Folder:

```text
docs/software/core_ai_system/
```

Files:

```text
main.py
mission_manager.py
road_model_loader.py
decision_engine.py
robot_path_planner.py
hud_generator.py
quality_analyzer.py
telemetry_system.py
ai_inference_engine.py
ethercat_interface.py
```

---

## 6. Beckhoff / TwinCAT Real-Time Layer

Target hardware:

```text
Beckhoff TwinCAT IPC
```

Primary responsibilities:

- deterministic motion control,
- flow control,
- induction heat control,
- speed synchronization,
- EtherCAT fieldbus operation,
- PLC interface,
- process readiness signals.

Folders:

```text
docs/software/motion_control_system/
docs/software/flow_control_system/
docs/software/induction_heat_control/
docs/software/speed_synchronization/
```

---

## 7. Robot Arm Control Layer

Target systems:

```text
KUKA Controller
+
Beckhoff TwinCAT IPC
```

Responsibilities:

- robot target pose receiving,
- KUKA command bridge,
- robot safe-zone check,
- X/Y rail coordination,
- gun height control,
- paint-gun enable interlock.

Folder:

```text
docs/software/robot_arm_control/
```

---

## 8. Safety System

Target hardware:

```text
Beckhoff Safety PLC
```

Responsibilities:

- emergency stop,
- fire alarm,
- overtemperature,
- pressure alarm,
- robot safety zone,
- service covers,
- generator alarm,
- suction system alarm.

Folder:

```text
docs/software/safety_system/
```

---

## 9. HUD System

Target hardware:

```text
NVIDIA Jetson AGX Orin Industrial
```

Responsibilities:

- ghost line rendering,
- speed guidance,
- alignment correction messages,
- process status,
- safety warnings,
- quality status display.

Folder:

```text
docs/software/hud_system/
```

---

## 10. Quality Control AI

Target hardware:

```text
NVIDIA Jetson AGX Orin Industrial
```

Responsibilities:

- application camera processing,
- line width analysis,
- thickness estimation,
- glass bead distribution estimation,
- quality report generation,
- defect detection,
- correction recommendation.

Folder:

```text
docs/software/quality_control_ai/
```

---

## 11. Git Navigation Map

```text
[Git: Core AI System] → ../software/core_ai_system/main.py
[Git: Mission Manager] → ../software/core_ai_system/mission_manager.py
[Git: Road Model Loader] → ../software/core_ai_system/road_model_loader.py
[Git: Decision Engine] → ../software/core_ai_system/decision_engine.py
[Git: Robot Path Planner] → ../software/core_ai_system/robot_path_planner.py
[Git: EtherCAT Interface] → ../software/core_ai_system/ethercat_interface.py
[Git: Motion Control] → ../software/motion_control_system/twincat_motion_interface.py
[Git: Robot Arm Control] → ../software/robot_arm_control/kuka_robot_bridge.py
[Git: Paint Flow Control] → ../software/flow_control_system/paint_flow_controller.py
[Git: Induction Heat Control] → ../software/induction_heat_control/induction_heat_controller.py
[Git: Speed Synchronization] → ../software/speed_synchronization/speed_synchronization_module.py
[Git: HUD System] → ../software/hud_system/hud_guidance_system.py
[Git: Safety System] → ../software/safety_system/safety_supervisor.py
[Git: Quality Control AI] → ../software/quality_control_ai/quality_control_module.py
```

---

## 12. Technical Conclusion

This software architecture converts the ROMR platform from a document-level concept into a distributed industrial software system.

The architecture clearly separates:

```text
AI decision-making
from
real-time motion control
from
PLC process control
from
safety control
from
quality validation
```

This separation is essential for stability, maintainability, real-time performance, safety and industrial scalability.
