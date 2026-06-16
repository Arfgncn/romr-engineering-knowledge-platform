# ROMR Electrical Power Budget & Energy Validation V1

## 1. Purpose

This validation file estimates the electrical power budget of the ROMR platform and evaluates whether the reference **2 × 180 kW = 360 kW** onboard generator architecture is technically justified.

This is not a final certified electrical design. It is an engineering validation layer intended to guide prototype sizing, generator selection, induction heating verification, and load-management strategy.

---

## 2. Key Question

```text
Is 360 kW really required?
```

Preliminary answer:

```text
360 kW appears to be a conservative reference architecture.
The real required power depends mainly on:
- paint mass flow rate,
- required temperature rise,
- induction efficiency,
- insulation losses,
- operating speed,
- line width and thickness,
- simultaneous load profile.
```

---

## 3. Load Budget Summary

| Metric | Value |
|---|---:|
| Reference generator architecture | 2 × 180 kW |
| Total reference generator power | 360.0 kW |
| Estimated effective operating load | 190.8 kW |
| Estimated simultaneous peak load | 284.5 kW |
| Effective-load margin | 169.2 kW |
| Peak-load margin | 75.5 kW |

---

## 4. Preliminary Load Table

| Load Group | Subsystem | Estimated kW | Peak kW | Duty Factor | Effective kW | Status | Notes |
|---|---|---:|---:|---:|---:|---|---|
| Thermal | Multi-stage induction heating line | 90 | 180 | 0.7 | 126 | To validate | Dominant load; depends on paint flow, ΔT, insulation, and efficiency |
| Thermal | Gun body / final heating section | 5 | 12 | 0.7 | 8.4 | To validate | Maintains gun inlet and dual-bell body temperature |
| Material Flow | Screw pump / pellet feed | 4 | 10 | 0.6 | 6 | Estimate | Depends on viscosity, pressure, and screw geometry |
| Material Flow | Tank agitator / anti-bridging | 2 | 5 | 0.5 | 2.5 | Estimate | Intermittent operation |
| Pneumatic | 6 bar screw compressor | 15 | 30 | 0.6 | 18 | Estimate | Air stabilization, purge, pneumatic valves |
| Dust Extraction | Jet fan / suction system | 5 | 12 | 0.7 | 8.4 | Estimate | Paint dust capture and underbody collection |
| Robotics | Industrial robot controller + arm | 4 | 12 | 0.5 | 6 | Estimate | KUKA/ABB/FANUC/Yaskawa class robot |
| Robotics | X/Y rail servo drives | 2 | 8 | 0.4 | 3.2 | Estimate | Motion dependent |
| Control | PLC + Safety PLC + I/O | 0.8 | 1.5 | 1.0 | 1.5 | Estimate | Critical always-on load |
| AI / Vision | RMDE industrial computer + cameras + LiDAR | 1.5 | 3 | 1.0 | 3 | Estimate | AI computer, sensors, networking |
| HMI / HUD | HUD, HMI, displays, communication | 0.8 | 2 | 1.0 | 2 | Estimate | Driver guidance and operator interface |
| Auxiliary | Cooling, panel ventilation, lighting, service loads | 3 | 8 | 0.6 | 4.8 | Estimate | Electronics cooling and maintenance loads |
| Safety | Fire detection / emergency systems | 0.5 | 1 | 1.0 | 1 | Estimate | Always-on safety layer |

---

## 5. Thermal Power Validation Logic

The induction heating requirement must be calculated from the real mass flow rate.

```text
Q = v × b × h
m_dot = density × Q
P_thermal = m_dot × c × ΔT / efficiency
```

Where:

| Symbol | Meaning |
|---|---|
| `v` | vehicle speed |
| `b` | line width |
| `h` | line thickness |
| `density` | thermoplastic paint density |
| `c` | specific heat |
| `ΔT` | required temperature rise |
| `efficiency` | total thermal efficiency |

---

## 6. Important Engineering Observation

If the platform is designed around a very high paint flow rate such as approximately **2100 kg/h**, the thermal system becomes the dominant energy consumer.

If the first prototype is validated at **120–200 kg/h** rotary bell flow, the required induction power may be much lower.

Therefore, the system should be validated in two stages:

```text
Stage 1 — Rotary gun prototype flow validation
120–200 kg/h

Stage 2 — Scaled vehicle system validation
500–1000+ kg/h

Stage 3 — Full-capacity road-marking architecture
up to reference capacity, if required
```

---

## 7. Generator Architecture Interpretation

The 360 kW architecture should not be presented as a fixed absolute requirement before testing.

It should be described as:

```text
Reference high-capacity onboard generation architecture
subject to thermal-flow validation.
```

Possible alternatives:

- single generator architecture,
- dual generator architecture,
- generator + battery buffer,
- separate induction power bus,
- reduced-power prototype architecture.

---

## 8. Load Management Strategy

Recommended load priority:

```text
Priority 1 — Safety PLC / Emergency systems
Priority 2 — Main PLC / sensors / communication
Priority 3 — RMDE computer / HUD / quality cameras
Priority 4 — Robot controller and X/Y rail
Priority 5 — Pump / compressor / suction
Priority 6 — Induction heating zones
Priority 7 — auxiliary service loads
```

During overload:

```text
Disable paint flow
↓
Stop application motion
↓
Reduce induction power
↓
Maintain control and safety systems
↓
Move to safe shutdown if required
```

---

## 9. Validation Tests Required

1. No-load generator test  
2. PLC/control power stability test  
3. Induction zone heating test  
4. Pellet flow heating test  
5. Rotary bell gun flow test  
6. Compressor + suction simultaneous load test  
7. Robot + X/Y rail motion load test  
8. Full simulated application cycle  
9. Emergency shutdown under load  
10. Thermal efficiency measurement  

---

## 10. Technical Conclusion

The 360 kW architecture is technically plausible as a high-capacity reference architecture, but it must be validated against real thermal-flow data.

The most critical unknown is not the robot, PLC, sensors or HUD; it is the **thermal energy required to heat the target thermoplastic paint mass flow continuously**.

Therefore, the final generator sizing should be based on:

```text
measured paint flow
+
measured induction efficiency
+
measured heat losses
+
simultaneous load profile
+
required safety margin
```

Until those values are measured, 360 kW should be kept as a conservative engineering reference, not as an unavoidable final requirement.
