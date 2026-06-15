# ROMR Master System Architecture V1

## Document Purpose

This master architecture defines the integrated engineering structure of the ROMR Engineering Knowledge Platform. The purpose is not to display five separate documents, but to transform the complete technical package into a connected engineering knowledge system where every subsystem is linked to its related equipment, software, PLC signals, sensors, BOM items, validation logic, and source documents.

---

# 0. Platform Principle

The ROMR platform must be understood as a single integrated industrial system:

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

The system is not a conventional thermoplastic road marking truck. It is a coordinated platform integrating pellet-form thermoplastic paint technology, staged induction heating, controlled flow-rate management, robot-arm-assisted marking, next-generation rotary bell / dual-disc thermoplastic paint application, AI-supported RMDE, HUD ghost-line driver guidance, real-time quality control, adaptive standards library, and PLC-based energy/safety/process control.

---

# 1. Ana Sistem Haritası

## 1.1 System Role

The Ana Sistem Haritası is the central navigation layer of the knowledge platform. It gives engineers a top-level map of the whole system and provides shortcut buttons to every connected subsystem.

## 1.2 Git Shortcut Buttons

Each main block must include these standard shortcut groups:

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

## 1.3 Main System Blocks

```text
ROMR Engineering Knowledge Platform
│
├── 1. Sistem Genel Akışı
├── 2. Pellet Boya Sistemi
├── 3. İndüksiyon Isıtma Sistemi
├── 4. Yeni Nesil Termoplastik Boya Tabancası
├── 5. Robot Kol + X/Y Kızak
├── 6. Güç ve Elektrik Mimarisi
├── 7. PLC ve Kontrol Sistemi
├── 8. RMDE Yazılım Mimarisi
├── 9. HUD ve Sürücü Rehberliği
├── 10. Kalite Kontrol Sistemi
├── 11. Uluslararası Standart Motoru
├── 12. Prototip BOM
└── 13. Yazılım Dosyaları
```

---

# 2. Pellet Boya Sistemi

## 2.1 System Role
The pellet paint system converts the thermoplastic material supply approach from irregular powder/block feeding into a controlled, homogeneous, repeatable pellet-based material flow.

## 2.2 Engineering Objective
- stabilize material feed
- reduce clogging risk
- improve heat transfer controllability
- reduce pressure fluctuations
- improve flow-rate stability
- support staged induction heating
- support robotic application repeatability

## 2.3 Pellet Production Process

```text
Powder thermoplastic paint
↓
Melting and homogenization at approximately 150°C
↓
Filament / rod formation
↓
Water-bath cooling
↓
Paraffin-based anti-sticking coating
↓
Cutting / pelletizing
↓
Controlled pellet storage
```

## 2.4 Target Pellet Geometry

| Parameter | Target |
|---|---|
| Diameter | approx. 5 mm |
| Length | approx. 5–15 mm |
| Form | cylindrical |
| Surface | smooth / anti-sticking |
| Internal structure | homogeneous, crack-free |

## 2.5 Connected Equipment
- pellet paint tank
- low-speed internal mixer
- bottom feeding screw
- screw pump / screw feeder
- heated transfer line
- humidity protection
- service hatch
- discharge / purge outlet

## 2.6 Connected Sensors
- tank level sensor
- material bridge detection sensor
- screw torque / load sensor
- inlet temperature sensor
- humidity sensor
- pressure sensor after screw pump

## 2.7 Connected PLC Functions
- mixer start/stop
- screw speed control
- torque overload protection
- low material alarm
- clogging alarm
- purge sequence control
- feed synchronization with RMDE line command

## 2.8 Git Shortcuts

```text
[Git: Induction Heating System]
[Git: Screw Pump System]
[Git: Pellet Tank BOM]
[Git: PLC Feed Control]
[Git: Flow Sensors]
[Git: Source: Section 1]
```

---

# 3. İndüksiyon Isıtma Sistemi

## 3.1 System Role
The induction heating system heats pellet-form thermoplastic paint progressively while the material is moving through the transfer line.

## 3.2 Engineering Objective
- controlled staged heating
- prevention of localized overheating
- stable outlet temperature
- lower energy loss
- fast response to flow changes
- reduction of paint degradation
- compatibility with robotic application speed

## 3.3 Baseline Design Values

| Parameter | Reference |
|---|---|
| Transfer line length | approx. 4 m design reference |
| Operating paint temperature | approx. 200–220°C |
| Workshop prototype supply | 3-phase 380–400 VAC |
| Real machine supply | onboard generator system |
| Reference application speed | 5 km/h |
| Reference line width | 0.14 m |
| Reference thickness | 1.5 mm |
| Reference density | approx. 2000 kg/m³ |
| Reference flow | approx. 2100 kg/h |

## 3.4 Heating Zone Logic

```text
Zone 1 — Preheating
Zone 2 — Controlled softening
Zone 3 — Melting / flow formation
Zone 4 — Temperature stabilization
Zone 5 — Gun inlet temperature maintenance
```

## 3.5 Connected Equipment
- induction inverter modules
- induction coils
- insulated heated transfer pipe
- temperature feedback sensors
- cooling fans / electronics cooling
- thermal insulation
- emergency thermal bypass / shutdown

## 3.6 Connected PLC Functions
- multi-zone PID control
- temperature ramp control
- inverter enable/disable
- overtemperature alarm
- flow-temperature synchronization
- generator load coordination
- emergency thermal shutdown

## 3.7 Git Shortcuts

```text
[Git: Thermal Power Calculator]
[Git: Generator System]
[Git: PLC PID Control]
[Git: Paint Flow Sensors]
[Git: Next-Generation Paint Gun]
[Git: Source: Section 1 / Section 3]
```

---

# 4. Yeni Nesil Termoplastik Boya Tabancası

## 4.1 System Role
The next-generation thermoplastic paint gun is the application endpoint of the platform. It is not a conventional narrow-nozzle thermoplastic gun. It is intended as a rotary bell / dual-disc inspired application head designed for high-temperature, high-flow thermoplastic material.

## 4.2 Core Principle
Instead of forcing high-temperature thermoplastic paint through a narrow nozzle, the system aims to create a wider, more stable, more controllable flow geometry using rotary bell operating principles, dual-disc distribution, circular flow guidance, compressed-air-assisted stabilization, induction-assisted temperature maintenance, large-flow channels, and automatic internal cleaning.

## 4.3 Main Engineering Objectives
- reduce clogging risk
- stabilize flow geometry
- improve line edge quality
- support robotic motion
- reduce maintenance difficulty
- maintain application temperature near the outlet
- allow controlled flow start/stop
- support synchronized glass bead application

## 4.4 Conceptual Internal Architecture

```text
Heated paint inlet
↓
Wide internal flow channel
↓
Temperature-maintained gun body
↓
Dual-disc distribution chamber
↓
Rotary bell / circular spread zone
↓
Compressed-air stabilization ring
↓
Controlled outlet geometry
↓
Road marking line formation
```

## 4.5 Key Subsystems

| Subsystem | Function |
|---|---|
| Heated inlet body | prevents thermal drop at gun entry |
| Internal distribution chamber | distributes paint before outlet |
| Dual-disc structure | forms controlled paint spread |
| Rotary bell surface | helps flow expansion and distribution |
| Air stabilization ring | shapes and stabilizes outlet flow |
| Induction-assisted body heating | maintains working temperature |
| Cleaning channel | supports internal purge / cleaning |
| Robot wrist mount | connects the gun to robot arm end-effector |

## 4.6 Robot Arm Integration
The gun must be integrated as a robotic end-effector. The robot command layer must control lateral position, gun height, application angle, start/stop timing, end-of-line lift/withdrawal, purge/cleaning position, and safe standby pose.

## 4.7 PLC / Control Integration
The PLC must monitor and control gun body temperature, inlet pressure, paint flow enable, air stabilization pressure, purge valve, cleaning sequence, overtemperature alarm, clogging pressure rise, and emergency shutoff.

## 4.8 Required Sensors
- gun body temperature sensor
- inlet paint temperature sensor
- pressure sensor before gun
- air pressure sensor
- flow verification sensor
- nozzle/gun height sensor
- robot position feedback

## 4.9 Maintenance and Service Logic
- wide flow channels should be accessible
- internal cleaning/purge should be automated
- service cover should allow inspection
- replaceable wear surfaces should be considered
- heating elements/coils should be serviceable
- robot-mounted quick-release interface is recommended

## 4.10 Technical Concept Diagram Requirement
A technical diagram must be produced showing:

```text
Paint inlet
→ heated body
→ dual-disc chamber
→ rotary bell spread zone
→ air stabilization ring
→ road line output
→ purge/cleaning path
```

## 4.11 Git Shortcuts

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

# 5. Robot Kol + X/Y Kızak Sistemi

## 5.1 System Role
The robot arm and X/Y linear slide system physically execute the road marking commands generated by the RMDE system.

## 5.2 Engineering Objective
- coordinate-based nozzle/gun positioning
- line width and position control
- dynamic correction against vehicle movement
- nozzle height control
- application of different line geometries
- integration with laser line removal module if required

## 5.3 Main Equipment
- industrial robot arm or custom robotic arm
- X/Y linear slide
- robot base frame
- vibration-isolated mounting platform
- end-effector mounting bracket
- cable carrier
- servo drives
- limit switches
- safety interlock zone

## 5.4 Input Data
- reference point ID
- line type
- start coordinate
- end coordinate
- target Y position
- vehicle speed
- line width
- paint temperature
- flow rate
- gun height

## 5.5 Output Actions
- position gun over target line
- maintain height
- start paint command
- synchronize with vehicle speed
- stop at end point
- move to safe standby
- trigger purge when required

## 5.6 Git Shortcuts

```text
[Git: RMDE Software Architecture]
[Git: New Generation Paint Gun]
[Git: Robot Command Layer]
[Git: PLC Safety System]
[Git: Quality Control]
[Git: Robot / Rail BOM]
[Git: Source: Section 2 / Section 3 / Section 4]
```

---

# 6. Güç ve Elektrik Mimarisi

## 6.1 System Role
The power system supplies high-power induction heating, robot systems, PLC, AI computers, compressor, cooling, sensors, and auxiliary loads.

## 6.2 Generator Architecture

| Parameter | Value |
|---|---|
| Generator type | turbine-engine generator |
| Quantity | 2 |
| Single generator power | 180 kW |
| Total design basis | 360 kW |
| Output | 400–480 VAC |
| Phase | 3-phase |
| Operation | parallel via main power bus |

## 6.3 Energy Flow

```text
Turbine Generators
↓
Main Power Distribution Panel
↓
Load Management Module
↓
Induction Inverter System
↓
Sub Power Distribution Panels
↓
Robot / PLC / Compressor / Sensors / AI Computer
```

## 6.4 Load Priority

```text
1. PLC and safety systems
2. Induction control system
3. Robot arm system
4. Compressor
5. Auxiliary equipment
```

## 6.5 Git Shortcuts

```text
[Git: Thermal Power Center]
[Git: Induction Heating System]
[Git: Main Electrical Panel BOM]
[Git: PLC Control System]
[Git: Safety Supervisor]
[Git: Source: Section 2 / Section 3]
```

---

# 7. PLC ve Kontrol Sistemi

## 7.1 System Role
The PLC system synchronizes the physical process: energy, heating, flow, pneumatics, robot interlocks, safety, alarms, and purge sequences.

## 7.2 PLC-Controlled Subsystems
- pellet tank mixer
- screw pump / feeder
- induction inverter zones
- generator load states
- compressor system
- air valves
- gun heating
- purge valves
- glass bead dosing
- safety interlocks
- emergency stop system
- alarms and telemetry

## 7.3 Main Sensor Inputs
- temperature sensors
- pressure sensors
- flow sensors
- level sensors
- vibration sensors
- air pressure sensors
- robot safe-zone sensors
- generator status signals
- E-stop feedback
- fire detection sensors

## 7.4 Main Outputs
- inverter enable signals
- pump speed references
- valve open/close commands
- compressor enable
- alarm outputs
- emergency shutdown
- purge start/stop
- robot-permission interlock

## 7.5 Git Shortcuts

```text
[Git: PLC Signal Matrix]
[Git: Electrical Architecture]
[Git: Safety System]
[Git: Induction Heating]
[Git: Paint Gun Control]
[Git: Software: plc_process_interface.py]
[Git: Source: Section 2 / Section 3 / Section 4]
```

---

# 8. RMDE Yazılım Mimarisi

## 8.1 System Role
The Road Marking Decision Engine is the software brain that transforms road data and country standards into executable marking commands.

## 8.2 Main Software Flow

```text
Pre-Survey Data Acquisition
↓
Road Classification
↓
Existing Line Detection
↓
Digital Road Model
↓
50 cm Reference Point Generation
↓
Standards-Based Line Decision Engine
↓
Robot Command Layer
↓
HUD Guidance
↓
Quality Feedback
```

## 8.3 Main Input Data
- road width
- lane count
- lane widths
- road type
- road length
- existing line status
- line condition
- surface condition
- country standard
- GPS / RTK coordinates
- camera data
- LiDAR data
- road slope
- traffic zone type

## 8.4 Main Output Data
- line type
- line width
- line thickness
- line color
- start coordinate
- end coordinate
- robot target Y
- vehicle target speed
- paint flow rate
- glass bead flow rate
- driver command
- quality tolerance

## 8.5 Git Shortcuts

```text
[Git: Reference Point Generator]
[Git: Standards Rule Engine]
[Git: Robot Command Layer]
[Git: HUD Guidance]
[Git: Quality Control Module]
[Git: Software Files]
[Git: Source: Section 4]
```

---

# 9. HUD ve Sürücü Rehberliği

## 9.1 System Role
The HUD system guides the driver according to the digital road model instead of visual estimation.

## 9.2 HUD Layers
- green target path
- blue ghost line
- white actual line
- red deviation zone
- yellow next movement arrow
- speed display
- temperature display
- flow stability display
- next action message

## 9.3 Example Driver Commands

```text
Alignment is correct. Maintain current path.
Make a slight right correction after five meters.
Reduce speed.
Approaching line end point.
Application will be terminated automatically.
```

## 9.4 Git Shortcuts

```text
[Git: RMDE Software]
[Git: Digital Road Model]
[Git: Driver Guidance Code]
[Git: Quality Control]
[Git: HMI / HUD BOM]
[Git: Source: Section 4]
```

---

# 10. Kalite Kontrol Sistemi

## 10.1 System Role
The quality control system verifies whether the applied road marking complies with the target digital road model and applicable standards.

## 10.2 Quality Parameters
- line width accuracy
- line thickness accuracy
- alignment deviation
- line continuity
- glass bead distribution
- speed stability
- paint temperature stability
- flow stability
- robot application precision

## 10.3 Error Logging

```text
Error Type: Line deviation
Location: P420 – P438
Deviation: 6 cm
Recommended correction: robot calibration / vehicle speed correction
```

## 10.4 Git Shortcuts

```text
[Git: Camera System]
[Git: RMDE Reference Points]
[Git: Quality Code]
[Git: Standards Library]
[Git: Robot Calibration]
[Git: Source: Section 4]
```

---

# 11. Uluslararası Standart Motoru

## 11.1 System Role
The international standards engine allows the same machine architecture to operate under different country, regional, airport, industrial, and special-purpose marking standards.

## 11.2 Standards Scope
- Türkiye
- India
- Europe / country-specific European rules
- United States
- Gulf region
- airport runway / apron markings
- industrial facility markings
- logistics area markings
- AGV / robotic guidance lines
- temporary traffic applications
- tunnel applications
- high-security operational areas

## 11.3 Rule Parameters
- line width
- line length
- gap distance
- line color
- line type
- edge line rules
- centerline rules
- pedestrian crossing geometry
- stop line distance
- retroreflectivity class
- glass bead quantity
- climate adaptation
- wet-night visibility
- road classification
- speed limit
- surface condition

## 11.4 Git Shortcuts

```text
[Git: Standards Database]
[Git: RMDE Decision Engine]
[Git: Country Rule Tables]
[Git: Quality Tolerances]
[Git: Software: standards_rule_engine.py]
[Git: Source: Section 5]
```

---

# 12. Prototip BOM

## 12.1 System Role
The prototype BOM defines all major machine equipment, electrical components, sensors, actuators, safety units, and software-relevant hardware needed for the prototype.

## 12.2 BOM Categories

```text
Carrier Platform
Power Generation
Electrical Distribution
Induction Heating
Paint Storage
Glass Bead Storage
Screw Pump / Transfer
Robot Arm
X/Y Linear Slide
Paint Application Gun
Pneumatics
PLC / Automation
Sensors
AI Computer
HUD / HMI
Safety
Cooling / Filtration
Cable and Pipe Routing
Service / Maintenance
```

## 12.3 Initial Critical BOM Items

| Category | Item | Reference |
|---|---|---|
| Carrier | heavy-duty multi-axle truck chassis | 8x4 or equivalent |
| Power | turbine generator | 2 × 180 kW |
| Material | pellet paint tank | approx. 4000 kg |
| Material | glass bead tank | approx. 750 kg |
| Transfer | screw pump / feeder | 3–8 bar target |
| Heating | staged induction line | approx. 4 m reference |
| Application | robot arm + X/Y rail | coordinate-based |
| Application | rotary bell / dual-disc paint gun | next-generation endpoint |
| Pneumatic | screw compressor | 6 bar |
| Control | PLC + safety control | industrial grade |
| Perception | LiDAR / camera / RTK / IMU | AI + QC |
| Safety | fire detection / E-stop | mandatory |

## 12.4 Git Shortcuts

```text
[Git: Equipment Library]
[Git: Electrical BOM]
[Git: Sensor BOM]
[Git: Robot BOM]
[Git: Paint Gun BOM]
[Git: Source: Section 2 / Section 3]
```

---

# 13. Yazılım Dosyaları

## 13.1 Required Software Files

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

## 13.2 Software-to-Hardware Links

| Software File | Hardware / Subsystem |
|---|---|
| pre_survey_module.py | camera, LiDAR, RTK, IMU |
| road_classifier.py | RMDE decision core |
| reference_point_generator.py | digital road model |
| standards_rule_engine.py | country standards library |
| rmde_decision_engine.py | line decision engine |
| robot_command_layer.py | robot arm, X/Y rail, paint gun |
| plc_interface.py | PLC, sensors, valves, induction, pump |
| hud_guidance_system.py | HUD / HMI |
| quality_control_module.py | camera, reference points, standards |
| safety_supervisor.py | E-stop, fire, overtemperature, robot safety |

## 13.3 Git Shortcuts

```text
[Git: RMDE Architecture]
[Git: PLC Control System]
[Git: Robot Command Layer]
[Git: Standards Library]
[Git: Quality Feedback]
[Git: Source: Section 4]
```

---

# 14. Source Document Map

| Source Document | Platform Role |
|---|---|
| Section 1 – Prototype Working Method | process logic, pellet technology, induction heating, paint gun innovation |
| Section 2 – Mechanical Architecture | chassis layout, generator, tank, robot, compressor, mechanical integration |
| Section 3 – Prototype Manufacturing Package | validation objectives, BOM, manufacturing requirements |
| Section 4 – RMDE Software | digital road model, decision engine, HUD, quality feedback, software files |
| Section 5 – Standards Library | international standards, adaptive AI rule engine |

---

# 15. Next Implementation Step

After this architecture is approved, the next deliverable should be:

```text
ROMR Engineering Knowledge Platform V1
│
├── docs/
├── software/
├── standards/
├── bom/
├── diagrams/
└── mkdocs.yml or app.py
```

The platform must not be a summary application. It must be an engineering navigation system where each subsystem is connected through shortcut buttons to its mechanical, electrical, software, sensor, BOM, validation, and source-document layers.
