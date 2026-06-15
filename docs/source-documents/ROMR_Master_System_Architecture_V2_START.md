# ROMR Master System Architecture V2 — Development Draft

> Status: V2 development draft. This document is the master source for the ROMR Engineering Knowledge Platform. It is not a summary portal. It is the integration map that will be expanded module by module from the five technical source documents.

---

## 0. Platform Definition

ROMR is an integrated AI-supported autonomous road-marking industrial platform. The system combines pellet-form thermoplastic paint feeding, staged induction heating, controlled flow-rate management, robotic application, a next-generation rotary bell / dual-disc thermoplastic paint gun, RMDE software, HUD guidance, quality feedback, safety architecture, PLC control, and international standards adaptation.

### Core System Flow

```text
Road Survey
↓
Digital Road Model
↓
RMDE Decision Engine
↓
50 cm Reference Points
↓
Robot Arm Commands
↓
Pellet Paint Feeding
↓
Multi-Stage Induction Heating
↓
Next-Generation Thermoplastic Paint Gun
↓
Road Marking Application
↓
Quality Control and Feedback
↓
International Standards Validation
```

---

## 1. Knowledge Platform Navigation Model

Every module must include shortcut buttons to related engineering layers.

```text
[Git: Mechanical Architecture]
[Git: Equipment / BOM]
[Git: Electrical Architecture]
[Git: PLC Signals]
[Git: Software File]
[Git: Sensors]
[Git: Validation Plan]
[Git: Source Document]
```

These buttons are not decorative. They are cross-links that allow an engineer to move directly from a subsystem to its related machine equipment, PLC logic, software module, sensor set, BOM item, validation rule, and source document.

---

## 2. Main Module Tree

```text
ROMR Engineering Knowledge Platform
│
├── 01 System Flow
├── 02 Pellet Paint System
├── 03 Multi-Stage Induction Heating System
├── 04 Next-Generation Thermoplastic Paint Gun
├── 05 Robot Arm + X/Y Linear Rail System
├── 06 Power and Electrical Architecture
├── 07 PLC and Control System
├── 08 RMDE Software Architecture
├── 09 HUD and Driver Guidance System
├── 10 Quality Control System
├── 11 International Standards Engine
├── 12 Prototype BOM
├── 13 Software Files
├── 14 Safety and Emergency Stop System
├── 15 Sensor Architecture
├── 16 Validation Plan
└── 17 Source Document Map
```

---

## 3. Next-Generation Thermoplastic Paint Gun — Required Full Module

### 3.1 Role

The next-generation thermoplastic paint gun is the physical application endpoint of the platform. It must not be treated as a conventional narrow-nozzle thermoplastic gun. It is a robotic end-effector designed around high-temperature, high-flow thermoplastic material behavior.

### 3.2 Core Concept

Instead of forcing thermoplastic material through a small nozzle hole, the concept uses:

- rotary bell operating principles,
- dual-disc distribution,
- wide internal flow geometry,
- circular flow guidance,
- compressed-air-assisted stabilization,
- induction-assisted temperature maintenance,
- automatic internal cleaning / purge logic,
- robot-arm-mounted end-effector architecture.

### 3.3 Required Engineering Pages

```text
04-next-generation-thermoplastic-gun.md
│
├── Operating Principle
├── Thermal Flow Path
├── Rotary Bell / Dual-Disc Geometry
├── Air Stabilization Ring
├── Induction-Assisted Body Heating
├── Purge and Internal Cleaning Circuit
├── Robot Wrist Mount
├── PLC Gun Control
├── Gun Sensors
├── Maintenance and Service Access
├── Gun BOM
├── Gun Validation Tests
└── Technical Concept Diagram
```

### 3.4 Git Shortcuts

```text
[Git: Robot Arm + X/Y Rail]
[Git: Induction Heating System]
[Git: PLC Gun Control]
[Git: Air Compressor System]
[Git: Paint Flow Sensors]
[Git: Application End-Effector BOM]
[Git: Software: robot_command_layer.py]
[Git: Software: plc_process_interface.py]
[Git: Source: Section 1]
```

---

## 4. Prototype BOM — Required Full Module

### 4.1 Purpose

The BOM must become an engineering equipment library, not a short table. Each item must be linked to its subsystem, control method, PLC signal, safety dependency, validation purpose, and source section.

### 4.2 BOM Categories

```text
Carrier Platform
Power Generation
Main Electrical Distribution
Load Management
Induction Heating
Pellet Paint Storage
Glass Bead Storage
Screw Pump / Transfer Line
Robot Arm
X/Y Linear Rail
Thermoplastic Paint Gun
Pneumatics / Compressor
PLC / Automation
Safety PLC
Sensors
AI Computer
HUD / HMI
Quality Control Hardware
Cooling / Filtration
Cable and Pipe Routing
Fire Safety
Maintenance Equipment
```

### 4.3 Initial Critical BOM Items

| Category | Item | Reference Data | Integration Role |
|---|---|---|---|
| Carrier | Heavy-duty multi-axle truck chassis | 8x4 or equivalent, ≥30 tons | Mechanical base |
| Power | Turbine generator system | 2 × 180 kW, 400–480 VAC, 3-phase | Main energy supply |
| Material | Pellet paint tank | approx. 4000 kg | Pellet storage |
| Material | Glass bead tank | approx. 750 kg | Bead storage and dosing |
| Transfer | Screw pump / feeder | 3–8 bar target | Controlled material flow |
| Heating | Staged induction line | approx. 4 m reference | Continuous-flow heating |
| Application | Robot arm + X/Y rail | coordinate-based | Marking position control |
| Application | Rotary bell / dual-disc gun | next-generation endpoint | Line formation |
| Pneumatics | Screw compressor | 6 bar | Air support and cleaning |
| Control | PLC + safety PLC | industrial grade | Process and safety execution |
| Perception | LiDAR / camera / RTK / IMU | AI + QC layer | Digital road model and verification |

---

## 5. RMDE Software Architecture — Required Full Module

### 5.1 Principle

The system must not be developed as a single Python file. It must be treated as a distributed industrial control ecosystem consisting of AI computer, PLC, robot controller, EtherCAT or fieldbus network, field sensors, safety PLC, HMI/HUD, and quality-control hardware.

### 5.2 Software File Tree

```text
software/
│
├── pre_survey_module.py
├── road_classifier.py
├── existing_line_detector.py
├── digital_road_model.py
├── reference_point_generator.py
├── standards_rule_engine.py
├── rmde_decision_engine.py
├── robot_command_layer.py
├── plc_interface.py
├── hud_guidance_system.py
├── quality_control_module.py
├── safety_supervisor.py
├── telemetry_logger.py
└── config/
    ├── turkey_standards.yaml
    ├── india_standards.yaml
    ├── usa_mutcd.yaml
    ├── europe_standards.yaml
    ├── gulf_region.yaml
    ├── airport_markings.yaml
    └── industrial_agv_markings.yaml
```

### 5.3 Software-to-Hardware Matrix

| Software File | Hardware / Subsystem | Function |
|---|---|---|
| pre_survey_module.py | Camera, LiDAR, RTK, IMU | Raw survey data acquisition |
| road_classifier.py | RMDE | Road class verification |
| digital_road_model.py | Survey data + road geometry | Digital route model |
| reference_point_generator.py | Digital road model | 50 cm control point generation |
| standards_rule_engine.py | Standards database | Country and project rule selection |
| rmde_decision_engine.py | AI computer | Line decision generation |
| robot_command_layer.py | Robot arm, X/Y rail, paint gun | Executable motion and application commands |
| plc_interface.py | PLC, sensors, valves, induction, pump | Deterministic process control interface |
| hud_guidance_system.py | HUD / HMI | Driver guidance and warnings |
| quality_control_module.py | Cameras, laser profile sensors | Real-time quality monitoring |
| safety_supervisor.py | Safety PLC | Safety states and emergency logic |

---

## 6. PLC / Safety Architecture — Required Full Module

### 6.1 Separation Rule

AI must not make final safety decisions. AI may evaluate, predict, and warn, but final authority must remain with the Safety PLC.

### 6.2 Safety Chain

```text
Emergency Stop OK
↓
Covers Closed
↓
Phase Protection OK
↓
Grounding OK
↓
Cooling Flow OK
↓
Cooling Level OK
↓
No Inverter Fault
↓
Line Pressure Safe
↓
Main Contactor Permission
```

### 6.3 Emergency Stop Response

```text
Stop robot motion
↓
Cut servo torque / STO
↓
Stop auger / screw feed
↓
Reduce or cut induction power
↓
Release pressure
↓
Stop application process
↓
Continue logging and fault analysis
```

---

## 7. International Standards Engine — Required Full Module

The standards engine must include every country, region, and application environment defined in the source documents. It must not be limited to Türkiye, India, Europe, and the United States.

### 7.1 Standards Scope

```text
Türkiye
India
Europe / country-specific European rules
United States / MUTCD
Gulf region
Airport runway / apron markings
Industrial facility markings
Logistics area markings
AGV / robotic guidance lines
Temporary traffic applications
Tunnel applications
High-security operational areas
```

### 7.2 Rule Parameters

```text
line width
line length
gap distance
line color
line type
edge line rules
centerline rules
pedestrian crossing geometry
stop line distance
retroreflectivity class
glass bead quantity
climate adaptation
wet-night visibility
road classification
speed limit
surface condition
```

---

## 8. Next Work Package

The next work package is not interface design. It is content extraction from the five technical documents into the knowledge architecture:

```text
WP-1: Thermoplastic paint gun full module
WP-2: Full prototype BOM extraction
WP-3: PLC signal matrix
WP-4: Sensor architecture
WP-5: RMDE software files
WP-6: International standards tables
WP-7: Module cross-link network
WP-8: MkDocs deployment correction
```

