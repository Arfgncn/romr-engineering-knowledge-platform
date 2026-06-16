# ROMR Dual-Bell Rotary Gun Flow & Spray Validation V1

## 1. Purpose

This document defines the first engineering validation method for the ROMR next-generation dual-bell rotary thermoplastic paint gun.

The goal is to validate:

```text
Paint flow rate
+
temperature stability
+
rotary bell speed
+
air stabilization pressure
+
circular spray geometry
+
robotic application compatibility
+
clogging resistance
```

---

## 2. Why This Test Is Critical

The dual-bell rotary gun is one of the most distinctive ROMR technologies. The system does not depend on a narrow fan-type nozzle. Instead, spray geometry is created by:

- controlled rotational movement,
- centrifugal force,
- dual-bell / dual-disc flow geometry,
- air-assisted stabilization,
- wide flow channels,
- induction-assisted temperature maintenance.

Therefore, validation must measure not only free-flow capacity, but the actual spray behavior while the rotary bell is active.

---

## 3. Core Flow Measurement Method

The test method is simple and physically direct:

```text
Heat the system to operating temperature
↓
Activate rotary bell gun
↓
Spray paint for a measured duration
↓
Collect sprayed paint in a controlled container
↓
Weigh collected paint
↓
Calculate hourly flow rate
```

Formula:

```text
Flow Rate kg/h = Collected Paint kg / Test Duration min × 60
```

---

## 4. Target Prototype Range

Initial prototype target:

```text
120–200 kg/h
```

This range is suitable for early validation of:

- rotary bell flow behavior,
- heating continuity,
- clogging resistance,
- spray pattern stability,
- robotic motion compatibility.

The earlier 2100 kg/h value should be treated as a high-capacity system-level reference and not as the first rotary gun prototype target.

---

## 5. Test Variables

| Parameter | Purpose |
|---|---|
| Paint temperature | controls viscosity and flow stability |
| Bell RPM | controls angular momentum and spray pattern |
| Air pressure | stabilizes circular spray geometry |
| Paint pressure | shows flow resistance and clogging risk |
| Duration | validates continuous operation |
| Collected mass | gives real flow capacity |
| Line width | validates standards compatibility |
| Thickness | validates material output per meter |
| Robot speed | validates motion compatibility |

---

## 6. Preliminary Test Table

| Test ID | Test Mode | Duration min | Collected Paint kg | Flow Rate kg/h | Paint Temp C | Bell RPM | Air Pressure bar | Line Width cm | Thickness mm | Status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| GUN-001 | Static warm flow | 1 | 2.0 | 120.0 | 210 | 150 | 2.0 | 12 | 1.5 | Prototype target |
| GUN-002 | Static warm flow | 1 | 3.0 | 180.0 | 215 | 250 | 2.5 | 14 | 1.5 | Prototype target |
| GUN-003 | Static warm flow | 1 | 3.5 | 210.0 | 220 | 350 | 3.0 | 15 | 1.7 | Prototype target |
| GUN-004 | Robot motion test | 2 | 5.0 | 150.0 | 220 | 300 | 2.8 | 14 | 1.5 | To validate |
| GUN-005 | Longer continuous test | 5 | 15.0 | 180.0 | 218 | 300 | 2.8 | 14 | 1.5 | To validate |

---

## 7. Acceptance Criteria

### 7.1 Flow Stability

Acceptable:

- flow does not suddenly drop,
- no rapid pressure spike,
- no thermal freezing at the outlet,
- collected mass follows expected trend.

### 7.2 Spray Geometry

Acceptable:

- circular pattern remains stable,
- no severe thick-center / thin-edge defect,
- no severe thick-edge / thin-center defect,
- line edges remain controllable.

### 7.3 Robotic Compatibility

Acceptable:

- robot motion does not break spray geometry,
- gun height remains stable,
- line width remains within tolerance,
- start/finish transitions are repeatable.

---

## 8. Required Measurements

Each test should record:

```text
test_id
test_duration
collected_paint_kg
calculated_flow_rate_kg_h
paint_temperature
gun_body_temperature
paint_pressure
bell_rpm
air_pressure
line_width
line_thickness
robot_speed
quality_observation
```

---

## 9. Engineering Conclusion

The dual-bell gun should not be approved only by visual spray appearance. It must be validated by measured paint mass flow, thermal stability, pressure behavior, spray geometry, robot motion behavior and quality-control results.

This validation file provides the first structured test layer for converting the gun concept into a measurable industrial prototype.
