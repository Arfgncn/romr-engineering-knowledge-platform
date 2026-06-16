[02-pellet-paint-system.md](https://github.com/user-attachments/files/28995637/02-pellet-paint-system.md)
# 02 — Pellet Paint Feed System

## 1. System Purpose

The Pellet Paint Feed System is the starting point of the ROMR platform.

Process flow:

Pellet Storage → Agitator → Anti-Bridging System → Servo Screw Feeder →
Flow Conditioning Chamber → Multi-Stage Induction Heating →
Dual-Bell Rotary Gun → Robotic Application

## 2. Pellet Storage Tank

- Moisture protected tank
- Conical hopper geometry
- Inspection hatch
- Filling port
- Level sensors
- Low level alarm
- Service access

## 3. Anti-Bridging Architecture

Potential issues:
- Bridging
- Rat-holing
- Material compaction

Countermeasures:
- Vibrator motors
- Internal agitator
- Conical hopper
- Level monitoring
- Torque monitoring

## 4. Servo Screw Feeder

Functions:
- Closed-loop feed control
- Flow stabilization
- Torque monitoring
- Jam detection
- Automatic reverse sequence

## 5. Flow Conditioning Chamber

Located between feeder and induction system.

Functions:
- Flow stabilization
- Pressure equalization
- Thermal monitoring
- Feed smoothing

## 6. Sensors

- Pellet level sensor
- Agitator current sensor
- Screw torque sensor
- Flow sensor
- Pressure sensor
- Temperature sensor

## 7. PLC Signals

Inputs:
- tank_low_level
- bridge_detected
- screw_overload
- flow_low
- flow_high

Outputs:
- feed_enable
- feed_speed_reference
- agitator_enable
- anti_bridge_vibrator_enable

## 8. Integration with Induction Heating

Pellet Feed
↓
Induction Zone 1
↓
Induction Zone 2
↓
Induction Zone 3
↓
Induction Zone 4
↓
Gun Inlet

## 9. Integration with Robot System

Pellet System
↓
Induction Line
↓
Dual-Bell Rotary Gun
↓
Industrial Robot
↓
Road Application

## 10. Design Principle

The pellet feed system shall operate in closed-loop mode.

Screw speed, flow rate, line pressure and induction temperature shall be evaluated together and adjusted in real time.

## 11. Git Links

[Git: Induction Heating](03-induction-heating-system.md)

[Git: Thermoplastic Gun](04-next-generation-thermoplastic-gun.md)

[Git: PLC System](07-plc-control-system.md)

[Git: BOM](12-prototype-bom.md)
