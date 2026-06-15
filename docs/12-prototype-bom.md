# 12. Prototip BOM

<div class="gitbar"><a href="../06-power-electrical-architecture/">Git: Güç Mimarisi</a><a href="../07-plc-control-system/">Git: PLC Kontrol</a><a href="../04-next-generation-thermoplastic-gun/">Git: Termoplastik Tabanca</a><a href="../13-software-files/">Git: Yazılım Dosyaları</a></div>

## Amaç

Bu bölüm prototip için ana ekipman, devre elemanları, sensörler, makine ekipmanları, kontrol donanımı ve güvenlik bileşenlerini sistem bağlantılarıyla birlikte gösterir. Liste nihai üretim BOM’u değildir; prototip mühendisliği, maliyet analizi, tedarik ve entegrasyon çalışmalarına temel oluşturur.

## Carrier Platform

| Bileşen | Referans Özellik | Entegrasyon |
|---|---|---|
| Heavy-duty multi-axle truck chassis | 8x4 veya eşdeğer, ≥30 ton | bütün sistemin taşıyıcı tabanı |
| Modular superstructure frame | ST52 / yüksek dayanımlı çelik | tank, robot, jeneratör, kompresör |
| Service platform | kaymaz yürüyüş alanı | bakım erişimi |

## Power Generation and Distribution

| Bileşen | Referans Özellik | Entegrasyon |
|---|---|---|
| Turbine generator | 2 × 180 kW | ana güç kaynağı |
| Main distribution panel | 400–480 VAC, 3 phase | jeneratör çıkışları ve yük yönetimi |
| Load management module | PLC-linked | yük önceliklendirme |
| Sub power panels | robot, PLC, sensör, kompresör | alt sistem beslemesi |
| Insulation leakage protection | mandatory | elektrik güvenliği |

## Pellet Paint and Glass Bead System

| Bileşen | Referans Özellik | Entegrasyon |
|---|---|---|
| Pellet paint tank | ~4000 kg | paint storage |
| Glass bead tank | ~750 kg | synchronized bead dosing |
| Low-speed mixer | anti-bridging | tank içi akış stabilitesi |
| Moisture control | dry material handling | cam küreciği ve pellet stabilitesi |
| Level sensors | tank monitoring | PLC/HMI |

## Paint Transfer and Flow

| Bileşen | Referans Özellik | Entegrasyon |
|---|---|---|
| Screw pump / screw feeder | 3–8 bar target | boyayı indüksiyon hattına aktarır |
| Heated transfer line | 200–220°C compatible | paint line continuity |
| Pressure sensor | high-temperature | tıkanma ve basınç izleme |
| Flow monitoring | closed-loop target | debi kararlılığı |
| Drainage valves | service points | shutdown / fault evacuation |
| Purge ports | cleaning line | bakım ve restart kabiliyeti |

## Induction Heating and Thermal Control

| Bileşen | Referans Özellik | Entegrasyon |
|---|---|---|
| Induction inverter | multi-zone | hat ısıtma güç kontrolü |
| Induction coils | staged line + gun body | lokal ısıtma |
| Thermocouples / IR sensors | multi-point | PID feedback |
| Thermal insulation | high-temp | enerji kaybını azaltma |
| Cooling system | inverter/electronics | termal güvenlik |

## Robotic Application System

| Bileşen | Referans Özellik | Entegrasyon |
|---|---|---|
| Robot arm | 6-axis / industrial or custom | coordinate-based marking |
| X/Y linear rail | heavy-duty enclosed | reach and correction |
| Robot controller | KUKA / equivalent | motion execution |
| Servo drives | EtherCAT-compatible | motion axes |
| Laser distance sensor | nozzle height | closed-loop height correction |

## Application End Effector

| Bileşen | Referans Özellik | Entegrasyon |
|---|---|---|
| Rotary bell / dual-disc thermoplastic gun | primary long-term target | wide controlled flow |
| High-temp valve group | 200–220°C | paint on/off control |
| Induction-heated gun body | viscosity maintenance | gun thermal stability |
| Compressed-air stabilization | 6 bar system | flow edge support |
| Automatic internal cleaning line | air + controlled fluid | cleaning mode |
| Optional laser removal head | advanced phase | line removal / surface prep |
| Head selection mechanism | servo / pneumatic | paint vs laser head selection |

## Sensor and AI Integration

| Bileşen | Görev |
|---|---|
| Camera system | existing line detection + quality control |
| LiDAR | road edge / obstacle / geometry reference |
| RTK-GNSS | centimeter-level location reference |
| IMU | slope, vibration, vehicle attitude |
| Laser profile sensor | line width / thickness profile |
| Thermal camera / IR | heat risk and line thermal state |

## PLC, Safety and HMI

| Bileşen | Görev |
|---|---|
| Beckhoff TwinCAT IPC | motion/process control |
| Beckhoff Safety PLC | safety authority |
| NVIDIA Jetson AGX Orin Industrial | AI + RMDE + vision + HUD |
| Industrial HMI panel | operator interface |
| AR-HUD / display interface | driver guidance |
| Emergency stop chain | hardwired safety |
| Fire detection and suppression | generator/hot-zone protection |
| Laser scanner safety | human detection and robot zone protection |
