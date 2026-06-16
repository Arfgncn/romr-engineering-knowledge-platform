# ROMR Industrial Robot Selection & Payload Validation V1

## 1. Purpose

This file validates the required industrial robot payload class for the ROMR robotic application system.

The robot arm is not expected to carry only a paint gun. It must carry the full application end-effector package:

```text
Dual-Bell Rotary Thermoplastic Gun
+
Hydraulic rotary drive
+
Final induction heating section
+
Heated paint transfer line with paint inside
+
Air stabilization line
+
Purge / cleaning line
+
Paint dust extraction hose
+
Sensors and cable harness
+
Robot wrist adapter
```

---

## 2. Recommended Robot Class

Preferred reference platform:

```text
KUKA KR Series Industrial Robot
```

Alternative industrial platforms:

```text
ABB IRB Series
FANUC M-Series
Yaskawa Motoman Series
```

The documentation should avoid locking the design to one vendor, but KUKA KR class may be used as the preferred reference platform.

---

## 3. Payload Result Summary

| Parameter | Result |
|---|---:|
| Estimated total working mass | 46.0 kg |
| Maximum estimated end-effector mass | 67.0 kg |
| Safety factor | 1.5 |
| Recommended minimum robot payload | 100.5 kg |
| Recommended practical robot class | 50–70 kg class |
| Preferred reference platform | KUKA KR 50 class or equivalent |

---

## 4. Engineering Interpretation

The estimated maximum end-effector system mass is approximately **67.0 kg** before dynamic safety allowance.

With a safety factor of **1.5**, the recommended payload class becomes approximately **100.5 kg**.

Therefore, the robot should not be selected from small/light-duty robotic arms. It should be selected from the **50–70 kg industrial payload class**.

This class provides:

- payload reserve,
- better rigidity,
- better wrist torque margin,
- compatibility with hot paint line routing,
- improved resistance to vibration,
- safer operation under field conditions,
- capacity for future sensor and tooling additions.

---

## 5. Payload Table

| Load Category | Component | Estimated Mass kg | Max Mass kg | Distance from Wrist m | Moment kg·m | Engineering Note |
|---|---|---:|---:|---:|---:|---|
| End Effector | Dual-bell rotary thermoplastic paint gun | 12 | 16 | 0.18 | 2.88 | Main application tool; high-temperature metal body |
| Drive | Hydraulic rotary bell drive / motor group | 5 | 7 | 0.15 | 1.05 | Rotary bell torque system |
| Thermal | Final induction heating section on robot arm | 6 | 9 | 0.25 | 2.25 | Last heating / temperature maintenance zone |
| Paint Line | Heated paint transfer hose with paint inside | 4 | 6 | 0.3 | 1.80 | Includes hot thermoplastic material inside line |
| Pneumatic | Atomizing / stabilization air lines | 2 | 3 | 0.22 | 0.66 | Air lines and fittings |
| Cleaning | Purge / cleaning line | 2 | 3 | 0.22 | 0.66 | Cleaning fluid / purge path |
| Extraction | Paint dust extraction hose | 4 | 6 | 0.35 | 2.10 | Flexible hose and suction interface |
| Sensors | Height, temperature, pressure and RPM sensors | 2 | 3 | 0.2 | 0.60 | Sensor package and brackets |
| Cabling | Sensor harness, Ethernet, safety wiring | 2 | 3 | 0.3 | 0.90 | Cable bundle along robot arm |
| Adapter | Robot wrist adapter / mounting bracket | 4 | 6 | 0.12 | 0.72 | Heavy-duty quick-mount plate |
| Protection | Thermal shields and vibration isolation parts | 3 | 5 | 0.18 | 0.90 | Protective covers and dampers |

---

## 6. Key Mechanical Considerations

### 6.1 Payload

The robot must carry both static mass and dynamic effects. The selected robot should have enough payload margin for:

- hot paint inside transfer line,
- additional heat shields,
- future sensor packages,
- suction hose drag,
- vibration forces,
- field operation shocks,
- dynamic robot acceleration.

### 6.2 Wrist Moment

The payload rating alone is not enough. The robot wrist moment capacity must also be checked.

The dual-bell gun, heated pipe, suction hose and adapter form an offset load. Therefore, center-of-gravity distance must be measured during prototype CAD design.

### 6.3 Hose and Cable Drag

Robot arm payload analysis must include:

- heated paint hose stiffness,
- suction hose drag,
- air line bending resistance,
- cable carrier force,
- purge hose movement,
- thermal expansion.

### 6.4 X/Y Rail Integration

The X/Y rail extends the working envelope and reduces extreme robot reach. This improves:

- line following stability,
- wrist angle control,
- robot life,
- vibration behavior,
- application repeatability.

---

## 7. Recommended Robot Specification

| Requirement | Recommended Value |
|---|---|
| Robot type | 6-axis industrial robot |
| Preferred reference | KUKA KR 50 class |
| Payload class | 50–70 kg |
| Wrist torque | To be verified with CAD center of gravity |
| Outdoor protection | Industrial protection required |
| Controller | Industrial robot controller with PLC interface |
| Communication | Industrial Ethernet / fieldbus |
| Safety | Safety-rated robot controller + safety PLC interlock |
| Mounting | Rigid frame on X/Y rail platform |
| Environment | Heat, dust, vibration, outdoor-duty adaptation |

---

## 8. Validation Tests Required

1. Static payload mount test  
2. Wrist moment and center-of-gravity verification  
3. Hose drag test  
4. Heated paint line flexibility test  
5. Suction hose movement test  
6. X/Y rail motion test  
7. Robot repeatability test under load  
8. Gun height stability test  
9. Vibration and road-shock test  
10. Integrated robot + gun + PLC safety interlock test  

---

## 9. Technical Conclusion

The ROMR robotic application system should be designed around a **50–70 kg industrial robot payload class**, with **KUKA KR 50 class or equivalent** as the preferred reference.

The robot is not merely a paint-gun holder. It is a mobile industrial application platform carrying thermal, pneumatic, extraction, sensor, safety and communication subsystems.

Final robot selection must be confirmed through CAD mass properties, wrist moment calculations, hose routing analysis, vibration testing and prototype validation.
