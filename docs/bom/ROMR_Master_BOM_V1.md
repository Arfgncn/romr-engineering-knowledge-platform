# ROMR Master BOM V1

Engineering reference bill of materials for the ROMR Engineering Knowledge Platform prototype architecture.

> Status: Concept / reference BOM. Final suppliers, ratings, quantities and compliance must be validated during prototype engineering.

## BOM Table

| BOM ID | Category | Subsystem | Item | Reference Specification | Engineering Function | Qty | Unit | Priority | Status | Git / Related Module | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ROMR-BOM-001 | Carrier Platform | Vehicle Base | Heavy-duty multi-axle truck chassis | 8x4 or equivalent | Mobile carrier for complete ROMR superstructure | 1 | set | Critical | Concept | 05-robot-arm-xy-rail.md | Final chassis selection after weight and axle-load study |
| ROMR-BOM-002 | Carrier Platform | Superstructure | Modular steel superstructure frame | ST52/equivalent steel | Vibration-resistant frame for tanks, generator, robot, panels | 1 | set | Critical | Concept | 01-system-flow.md | Service access and torsional rigidity required |
| ROMR-BOM-003 | Power Generation | Generator | Industrial turbine generator system | 2 × 180 kW reference | Onboard high-power electrical supply | 2 | unit | Critical / Validate | Reference | 06-power-electrical-architecture.md | 360 kW must be validated by thermal/power budget |
| ROMR-BOM-004 | Power Generation | Fuel System | Main fuel tank and fuel delivery system | Industrial fuel architecture | Fuel storage and supply for onboard generators | 1 | set | Critical | Concept | 06-power-electrical-architecture.md | Include filtration, return line, leak detection |
| ROMR-BOM-005 | Electrical | Main Panel | Main AC distribution panel | 400–480 VAC 3-phase | Distributes generator power to high-power loads | 1 | set | Critical | Concept | 06-power-electrical-architecture.md | Include protection, isolators, load metering |
| ROMR-BOM-006 | Electrical | Load Management | Load management controller | PLC-linked | Prioritizes safety, control, induction, robot and auxiliaries | 1 | unit | Critical | Concept | 07-plc-control-system.md | Supports safe load shedding |
| ROMR-BOM-007 | Electrical | Cabling | EMI-separated cable channels | Industrial cable routing | Separates induction power from sensors and communication | 1 | set | Critical | Concept | 06-power-electrical-architecture.md | Use shielding and grounding strategy |
| ROMR-BOM-008 | Pellet Paint System | Storage | Pellet thermoplastic paint tank | ~4,000 kg reference | Stores thermoplastic paint pellets | 1 | tank | Critical | Concept | 02-pellet-paint-system.md | Moisture protection and access hatch |
| ROMR-BOM-009 | Pellet Paint System | Storage | Low-speed internal mixer / agitator | Tank-integrated | Prevents bridging and irregular pellet feeding | 1 | set | Critical | Concept | 02-pellet-paint-system.md | Torque monitoring recommended |
| ROMR-BOM-010 | Pellet Paint System | Feed | Servo screw feeder / screw pump | Closed-loop feed | Metered pellet feed into induction line | 1 | set | Critical | Concept | 02-pellet-paint-system.md | Jam detection and reverse sequence |
| ROMR-BOM-011 | Pellet Paint System | Conditioning | Flow conditioning chamber | Pre-induction chamber | Stabilizes feed before induction heating | 1 | unit | Critical | Concept | 02-pellet-paint-system.md | Pressure and temperature monitoring |
| ROMR-BOM-012 | Glass Bead System | Storage | Glass bead tank | ~750 kg reference | Stores reflective glass beads | 1 | tank | Critical | Concept | 12-prototype-bom.md | Level and dosing feedback |
| ROMR-BOM-013 | Glass Bead System | Dosing | Glass bead dosing unit | Servo / pneumatic dosing | Controlled bead application to line surface | 1 | set | Critical | Concept | 07-plc-control-system.md | Closed-loop bead flow target |
| ROMR-BOM-014 | Induction Heating | Thermal Line | Multi-stage induction transfer line | Approx. 4 m reference | Kademeli paint heating before gun | 1 | set | Critical | Concept | 03-induction-heating-system.md | Multi-zone PID architecture |
| ROMR-BOM-015 | Induction Heating | Power | Induction inverter modules | Per heating zone | Supplies controlled induction power to zones | 5 | unit | Critical | Concept | 03-induction-heating-system.md | Number of zones prototype-dependent |
| ROMR-BOM-016 | Induction Heating | Coils | Induction heating coils | Zone-specific | Applies heating energy to transfer line/gun body | 5 | unit | Critical | Concept | 03-induction-heating-system.md | Coil geometry after validation |
| ROMR-BOM-017 | Induction Heating | Insulation | High-temperature insulation system | Industrial insulation | Minimizes heat loss and protects surrounding equipment | 1 | set | Critical | Concept | 03-induction-heating-system.md | Robot arm final section included |
| ROMR-BOM-018 | Application System | Industrial Robot | 6-axis industrial robot | Preferred: KUKA KR class; alternatives ABB/FANUC/Yaskawa | Carries gun and executes RMDE coordinates | 1 | unit | Critical | Reference | 05-robot-arm-xy-rail.md | Recommended 50–70 kg payload class |
| ROMR-BOM-019 | Application System | Linear Motion | X/Y linear rail system | Industrial rail axes | Extends robot reach for longitudinal/lateral marking | 1 | set | Critical | Concept | 05-robot-arm-xy-rail.md | Include servo drives and limit switches |
| ROMR-BOM-020 | Application System | Mounting | Robot base and vibration-isolated mounting frame | Industrial-grade | Rigid and stable robot mounting on vehicle frame | 1 | set | Critical | Concept | 05-robot-arm-xy-rail.md | Vibration compensation strategy required |
| ROMR-BOM-021 | Application System | Paint Gun | Dual-bell rotary thermoplastic paint gun | Next-generation applicator | Circular homogeneous thermoplastic application | 1 | unit | Critical Innovation | Concept | 04-next-generation-thermoplastic-gun.md | Rotary bell + fixed inner bell + angled air channels |
| ROMR-BOM-022 | Application System | End Effector | Robot wrist adapter | Heavy-duty adapter | Carries gun, heated line, suction hose, air and sensors | 1 | unit | Critical | Concept | 05-robot-arm-xy-rail.md | Payload and CG validation required |
| ROMR-BOM-023 | Pneumatics | Compressor | 6 bar screw compressor | Industrial screw compressor | Supplies atomizing air, purge air and valves | 1 | unit | Critical | Concept | 07-plc-control-system.md | Size after gun air consumption test |
| ROMR-BOM-024 | Pneumatics | Air Handling | Air tank + dryer + regulator group | 6 bar system | Stabilizes and conditions air supply | 1 | set | Critical | Concept | 07-plc-control-system.md | Include moisture separator |
| ROMR-BOM-025 | Dust Extraction | Capture | Paint dust capture ring / suction manifold | Gun-mounted | Captures paint dust around spray zone | 1 | set | Prototype Required | Concept | 04-next-generation-thermoplastic-gun.md | Geometry after spray testing |
| ROMR-BOM-026 | Dust Extraction | Hose | High-temp flexible extraction hose | Abrasion/temperature resistant | Transfers paint dust from robot to collection tank | 1 | set | Prototype Required | Concept | 05-robot-arm-xy-rail.md | Must not overload robot wrist |
| ROMR-BOM-027 | Dust Extraction | Fan | Industrial jet fan / suction fan | High suction | Moves paint dust to underbody dust tank | 1 | unit | Prototype Required | Concept | 10-quality-control-system.md | Vacuum sensor feedback |
| ROMR-BOM-028 | Dust Extraction | Collection | Dust separator and collection tank | Underbody tank | Collects paint dust for disposal | 1 | set | Prototype Required | Concept | 12-prototype-bom.md | Level sensor required |
| ROMR-BOM-029 | Automation | PLC | Main industrial PLC | Industrial PLC platform | Controls process, I/O, alarms and PID loops | 1 | unit | Critical | Concept | 07-plc-control-system.md | PLC platform selected by integrator |
| ROMR-BOM-030 | Automation | Safety | Safety PLC / safety controller | TwinSAFE or equivalent class | Independent safety chain and safe shutdown | 1 | unit | Mandatory | Concept | 07-plc-control-system.md | Do not rely on Python for safety |
| ROMR-BOM-031 | Automation | Robot Controller | Robot manufacturer controller | KUKA/ABB/FANUC/Yaskawa class | Controls 6-axis robot and safety zones | 1 | unit | Critical | Reference | 05-robot-arm-xy-rail.md | Must support PLC communication |
| ROMR-BOM-032 | Automation | Drives | Servo drives / motor controllers | For pump, dosing, rail axes | Controls motion and feed equipment | 1 | set | Critical | Concept | 07-plc-control-system.md | Synchronized with PLC |
| ROMR-BOM-033 | AI / Compute | Industrial Computer | CPU/GPU industrial PC | RMDE compute platform | Runs RMDE, vision, telemetry and standards engine | 1 | unit | Critical | Concept | 08-rmde-software-architecture.md | Ruggedized enclosure |
| ROMR-BOM-034 | HMI / HUD | Operator HMI | Industrial HMI panel | Operator dashboard and system alarms | 1 | unit | Critical | Concept | 09-hud-driver-guidance.md | Integrate PLC and RMDE status |
| ROMR-BOM-035 | HMI / HUD | Driver HUD | Ghost-line display / driver guidance unit | Shows path, speed, deviation, alarms | 1 | unit | Critical Demo | Concept | 09-hud-driver-guidance.md | Driver-assist layer |
| ROMR-BOM-036 | Sensors | Road Perception | Front LiDAR | Road edge and geometry sensing | Inputs to pre-survey and RMDE | 1 | unit | Critical | Concept | 08-rmde-software-architecture.md | Outdoor rated |
| ROMR-BOM-037 | Sensors | Road Perception | Side LiDAR / distance sensors | Road edge and lateral distance | Y-position and curb/edge references | 2 | unit | Critical | Concept | 08-rmde-software-architecture.md | Left/right coverage |
| ROMR-BOM-038 | Sensors | Vision | Front road cameras | Existing line and road surface detection | Vision input for RMDE | 2 | unit | Critical | Concept | 10-quality-control-system.md | Lighting required |
| ROMR-BOM-039 | Sensors | Vision | Rear quality-control camera | Post-application verification | Line width, alignment and continuity measurement | 1 | unit | Critical | Concept | 10-quality-control-system.md | Calibrated field of view |
| ROMR-BOM-040 | Sensors | Positioning | RTK-GNSS module | Centimeter-grade positioning | Digital road model matching and geo-referenced reports | 1 | unit | Critical | Concept | 08-rmde-software-architecture.md | Final RTK provider TBD |
| ROMR-BOM-041 | Sensors | Motion | IMU | Vehicle attitude and vibration | Compensates slope, motion and platform dynamics | 1 | unit | Critical | Concept | 09-hud-driver-guidance.md | Synchronize with GNSS |
| ROMR-BOM-042 | Sensors | Thermal | Temperature sensors | Multi-point | Tank, line, zones, gun body and inlet temperatures | 1 | set | Critical | Concept | 03-induction-heating-system.md | High-temperature compatible |
| ROMR-BOM-043 | Sensors | Pressure / Flow | Paint pressure and flow sensors | High-temp compatible | Closed-loop paint transfer and clog detection | 1 | set | Critical | Concept | 07-plc-control-system.md | Before gun and line sections |
| ROMR-BOM-044 | Sensors | Air / Vacuum | Air pressure and vacuum sensors | 6 bar / suction feedback | Air stabilization and dust extraction monitoring | 1 | set | Critical | Concept | 07-plc-control-system.md | Triggers quality and process alarms |
| ROMR-BOM-045 | Safety | Emergency | Emergency stop system | Hardwired + PLC safety | Stops hazardous motion/processes | 1 | set | Mandatory | Concept | 07-plc-control-system.md | Multiple E-stop points |
| ROMR-BOM-046 | Safety | Fire | Fire detection and suppression | FM200/aerosol/waterless option | Protects generator, electrical and hot zones | 1 | set | Mandatory | Concept | 06-power-electrical-architecture.md | Final method per authority requirements |
| ROMR-BOM-047 | Safety | Thermal Guarding | Thermal shields and hot surface guards | Hot-zone protection | Protects operator and surrounding components | 1 | set | Mandatory | Concept | 06-power-electrical-architecture.md | Service access maintained |
| ROMR-BOM-048 | Cooling / Filtration | Electronics Cooling | Panel ventilation / AC | Industrial enclosure cooling | Protects PLC, drives, AI computer and inverters | 1 | set | Critical | Concept | 06-power-electrical-architecture.md | Filtered airflow |
| ROMR-BOM-049 | Installation | Cable/Hose Carrier | Cable and hose carrier chain | Robot + rail routing | Routes paint, air, power, signal and suction safely | 1 | set | Critical | Concept | 05-robot-arm-xy-rail.md | Robot dynamic load impact |
| ROMR-BOM-050 | Service | Maintenance Access | Openable service covers and platforms | Service design | Enables safe access to generators, pump, tank, panels | 1 | set | Recommended | Concept | 12-prototype-bom.md | Include lockout/tagout |

## GitHub Target Location

Upload these files under:

```text
docs/bom/
```

- `ROMR_Master_BOM_V1.xlsx`
- `ROMR_Master_BOM_V1.csv`
- `ROMR_Master_BOM_V1.md`
