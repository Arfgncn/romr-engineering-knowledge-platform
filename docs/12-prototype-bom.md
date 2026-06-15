[12-prototype-bom.md](https://github.com/user-attachments/files/28956591/12-prototype-bom.md)
# 12 — Prototype BOM & Component Network

<div class="git-buttons">

[Git: Sistem Genel Akışı](01-system-flow.md)
[Git: Pellet Boya Sistemi](02-pellet-paint-system.md)
[Git: İndüksiyon Isıtma Sistemi](03-induction-heating-system.md)
[Git: Yeni Nesil Termoplastik Tabanca](04-next-generation-thermoplastic-gun.md)
[Git: Robot Kol + X/Y Kızak](05-robot-arm-xy-rail.md)
[Git: Güç ve Elektrik Mimarisi](06-power-electrical-architecture.md)
[Git: PLC ve Kontrol Sistemi](07-plc-control-system.md)
[Git: RMDE Yazılım Mimarisi](08-rmde-software-architecture.md)
[Git: Yazılım Dosyaları](13-software-files.md)

</div>

---

## 1. BOM Modülünün Rolü

Prototype BOM & Component Network, ROMR platformunda kullanılacak ana makine ekipmanlarını, elektrik/elektronik bileşenleri, sensörleri, aktüatörleri, güvenlik sistemlerini, robotik ekipmanları, proses bileşenlerini ve yazılımla ilişkili donanımları tek bir mühendislik ağı altında toplar.

Bu liste nihai seri üretim BOM'u değildir. Prototip üretim, tedarik planlama, maliyet analizi, güç hesabı, mekanik yerleşim, kablolama, montaj ve mühendislik doğrulama çalışmalarına başlangıç çerçevesi sağlar.

---

## 2. Seçim Kriterleri

Tüm ekipman seçimlerinde aşağıdaki kriterler esas alınmalıdır:

- endüstriyel saha dayanımı,
- yüksek sıcaklık uyumluluğu,
- titreşim dayanımı,
- sürekli çalışma kabiliyeti,
- modüler servis erişimi,
- yedek parça bulunabilirliği,
- PLC / AI entegrasyon uygunluğu,
- kablo/hortum yönlendirme güvenliği,
- yangın ve acil durdurma entegrasyonu,
- prototip doğrulama sürecinde ölçülebilirlik.

---

## 3. Kritik Sistem Kategorileri

```text
Carrier Platform
Power Generation
Electrical Distribution
Induction Heating
Paint Storage
Glass Bead Storage
Paint Transfer
Application System
Pneumatics
Dust Extraction
PLC / Automation
AI Computing
HUD / HMI
Sensors
Safety
Cooling / Filtration
Cable and Hose Routing
Service / Maintenance
```

---

## 4. Full Prototype BOM Table

| Category | Item | Reference Specification | Engineering Function | Priority | Source |
|---|---|---|---|---|---|
| Carrier Platform | Heavy-duty multi-axle truck chassis | 8x4 or equivalent | ≥30 tons; long wheelbase; rigid robotic superstructure base | Critical | Section 3 |
| Carrier Platform | Modular superstructure subframe | ST52/equivalent steel | Vibration-resistant, service-accessible, torsion-aware frame | Critical | Section 2/3 |
| Power Generation | Industrial turbine generator | 2 × 180 kW | 400–480 VAC, 3-phase; parallel bus; optional single-unit prototype evaluation | Critical / verify load | Section 2/3 |
| Power Generation | Main fuel tank and fuel delivery system | Industrial fuel architecture | Fuel filtration, air separator, pump, return line, leakage sensor, emergency shutoff | Critical | Section 2 |
| Electrical Distribution | Main power distribution panel | Industrial LV panel | Receives generator power, feeds induction, PLC, robot, sensors, compressor | Critical | Section 2 |
| Electrical Distribution | Load management module | PLC-linked | Priority: safety/PLC → induction → robot → compressor → auxiliaries | Critical | Section 2 |
| Electrical Distribution | Sub distribution panels | Robot/PLC/sensor panels | Separated power, signal, and communication routing | Critical | Section 2 |
| Electrical Distribution | EMI-separated cable channels | Industrial cable routing | Separate high-power induction cables from sensor/camera/communication lines | Critical | Section 2 |
| Induction Heating | Induction inverter modules | Multi-zone | Segment-based PID power control for staged heating | Critical | Section 1/3 |
| Induction Heating | Staged induction transfer line | Approx. 4 m reference | Insulated, multi-zone, high-temperature-compatible paint transfer | Critical | Section 1/3 |
| Induction Heating | Induction coils | Per heating zone | Coil layout sized after prototype validation | Critical | Section 1 |
| Induction Heating | Thermal insulation system | High-temperature insulation | Reduces heat loss and protects nearby equipment | Critical | Section 2/3 |
| Material Storage | Pellet paint tank | ~4,000 kg | Fixed-body/mixer-type tank, low-speed mixer, humidity control | Critical | Section 3 |
| Material Storage | Glass bead tank | ~750 kg | Integrated or separate dosing chamber | Critical | Section 3 |
| Material Storage | Low-speed internal mixer | Tank-integrated | Prevents bridging and irregular pellet feeding | Critical | Section 1/3 |
| Paint Transfer | Screw pump / screw feeder | 3–8 bar target | Servo or hydromechanical assisted, heated/insulated, purge-capable | Critical | Section 3 |
| Paint Transfer | Purge and drainage system | High-temperature safe | Dual valves, collection container, restart cleaning logic | Critical | Section 2/3 |
| Application | 6-axis industrial robot | KUKA KR class preferred; ABB/FANUC/Yaskawa alternatives | Recommended payload 50–70 kg; industrial controller; PLC integration | Critical | Robot module |
| Application | X/Y linear rail system | ~1.5 m rail range reference | Extends robot work envelope; left/right and forward/back application positioning | Critical | Section 2 |
| Application | Robot base and vibration-isolated mounting frame | Industrial-grade | Ensures repeatability, rigidity, and dynamic stability | Critical | Section 2 |
| Application | Dual-bell rotary thermoplastic paint gun | Next-generation endpoint | Rotary bell, dual-bell flow, induction-heated body, air stabilization | Critical innovation | Gun module |
| Application | Robot wrist adapter | Heavy-duty end-effector mount | Carries gun, heated line, air line, purge line, suction hose, sensors | Critical | Robot/Gun module |
| Pneumatics | 6 bar screw compressor | Industrial screw compressor | Application gun air, pneumatic valves, cleaning air, auxiliary air | Critical | Section 2 |
| Pneumatics | Air tank | Matched to compressor | Stabilizes air supply | Critical | Section 2 |
| Pneumatics | Moisture separator / air dryer | Industrial | Protects pneumatic and cleaning lines | Critical | Section 2 |
| Pneumatics | Pressure regulators and safety valves | 6 bar system | Air pressure control and overpressure safety | Critical | Section 2 |
| Dust Extraction | Paint dust capture ring / suction manifold | Robot/gun mounted | Captures paint dust near spray zone | Prototype-required | Gun/Robot module |
| Dust Extraction | Flexible extraction hose | High-temp / abrasion resistant | Routes dust from robot arm to vehicle dust system | Prototype-required | Gun/Robot module |
| Dust Extraction | Industrial jet fan system | High suction | Transfers paint dust to underbody dust tank | Prototype-required | Gun/Robot module |
| Dust Extraction | Dust separator and collection tank | Underbody tank | Collects particles for maintenance disposal | Prototype-required | Gun/Robot module |
| Automation | Main PLC | Industrial PLC | Process control, PID loops, interlocks, alarms, communication | Critical | Section 2/3/4 |
| Automation | Safety PLC / safety controller | Beckhoff TwinSAFE or equivalent class | Emergency stop, safe shutdown, robot/thermal safety independent from Python | Mandatory | Section 4 |
| Automation | Robot controller | Vendor controller | Executes robot motion commands and safety zones | Critical | Section 4 |
| Automation | Servo drives / motor controllers | For pump, dosing, rail axes | Synchronized speed/position control | Critical | Section 3 |
| AI Computing | Industrial computer | CPU/GPU option | RMDE, vision, telemetry, standards engine | Critical | Section 4 |
| HMI/HUD | Operator HMI panel | Industrial PC/panel | Process dashboard, alarms, system state | Critical | Section 2/4 |
| HMI/HUD | HUD ghost-line display | Driver guidance unit | Target path, ghost line, deviation warning, next action | Critical demo | Section 4 |
| Sensors | Front LiDAR | Road geometry/lane detection | Pre-survey and road model input | Critical for AI layer | Section 2/4 |
| Sensors | Side LiDAR / distance sensors | Road edge/curb/shoulder detection | Y-position and edge references | Critical | Section 2 |
| Sensors | Front cameras | Existing line and road surface detection | Vision input for RMDE | Critical | Section 2/4 |
| Sensors | Robot area cameras | Gun, line width, application tracking | Real-time application observation | Critical | Section 2 |
| Sensors | Rear quality-control camera | Post-application verification | Width, alignment, continuity, quality feedback | Critical | Section 2/4 |
| Sensors | RTK-GNSS | Centimeter-grade positioning | Digital road model matching | Critical for field expansion | Section 4 |
| Sensors | IMU | Vehicle attitude/slope | Motion and road slope compensation | Critical | Section 2/4 |
| Sensors | Temperature sensors | Multi-point | Induction line, paint outlet, gun body, tank zones | Critical | Section 2/3 |
| Sensors | Pressure sensors | Paint and air lines | Paint transfer pressure and air stabilization pressure | Critical | Section 2/3 |
| Sensors | Flow sensors | Paint and glass bead | Closed-loop flow and dosing verification | Critical | Section 2 |
| Sensors | Level sensors | Paint, glass bead, fuel, dust tank | Material availability and maintenance alarms | Critical | Section 2/3 |
| Sensors | Vibration sensors | Generator/robot/platform | Fatigue, vibration isolation, safety alarm | Critical | Section 2 |
| Safety | Emergency stop system | Hardwired + PLC safety | Robot, induction, pump, generator stop logic | Mandatory | Section 2/3 |
| Safety | Fire detection and suppression | FM200/aerosol option | Generator and hot-zone protection | Mandatory | Section 2 |
| Safety | Fuel leakage sensors | Fuel system | Leak detection and shutdown logic | Mandatory | Section 2 |
| Safety | Thermal shields and hot surface guards | Hot zones | Operator and component protection | Mandatory | Section 2 |
| Cooling/Filtration | Generator airflow system | Controlled intake/exhaust | Protects robot/sensors from hot exhaust | Critical | Section 2 |
| Cooling/Filtration | Electronics cooling / panel ventilation | Panel AC/fans | Protects PLC, inverters, computer | Critical | Section 2 |
| Cooling/Filtration | Paint/filtering system | High-temp compatible | Reduces contaminants entering gun/pump | Critical | Section 1/2 |
| Installation | Cable/hose carrier chain | Robot + rail + chassis | Routes paint, air, power, signal, suction safely | Critical | Section 2 |
| Installation | Flexible high-temp hoses | Paint/air/purge | Allows robot motion and thermal safety | Critical | Section 2 |
| Service | Openable service covers | All zones | Maintenance access for panels, generators, pump, tank, gun | Critical | Section 2/3 |
| Service | Non-slip maintenance platform | Generator/service zones | Field maintenance safety | Recommended | Section 2 |

---

## 5. Downloadable BOM Data

CSV verisi platform içinde ayrıca tutulur:

```text
docs/bom/prototype_bom_v1.csv
```

Bu dosya üretici firmaların Excel, maliyet analizi veya tedarik listesi hazırlaması için kullanılabilir.

[Git: Prototype BOM CSV](bom/prototype_bom_v1.csv)

---

## 6. BOM-to-System Integration

### 6.1 Tabanca Bağlantısı

<div class="git-buttons">

[Git: Yeni Nesil Termoplastik Tabanca](04-next-generation-thermoplastic-gun.md)
[Git: Robot Kol + X/Y Kızak](05-robot-arm-xy-rail.md)

</div>

Tabanca BOM'u; dual-bell rotary gun, indüksiyon ısıtmalı gövde, sabit iç bell, dönen dış bell, fan kanatları, hidrolik tahrik, hava kanalları, purge sistemi, emiş bağlantısı ve robot bilek adaptöründen oluşur.

### 6.2 Robot Bağlantısı

Robot BOM'u; endüstriyel 6 eksenli robot, X/Y ray sistemi, robot kontrolcü, kablo/hortum taşıyıcı, titreşim izoleli montaj platformu, robot bilek adaptörü ve güvenlik limit sensörlerinden oluşur.

### 6.3 PLC Bağlantısı

PLC BOM'u; ana PLC, safety PLC, I/O modülleri, sıcaklık/basınç/debi sensörleri, inverter kontrol çıkışları, valf sürücüleri, acil durdurma röleleri, HMI bağlantıları ve haberleşme altyapısını kapsar.

### 6.4 RMDE Bağlantısı

RMDE'nin donanım karşılığı; endüstriyel AI bilgisayarı, LiDAR, kamera, RTK-GNSS, IMU, kalite kontrol kamerası, HUD/HMI ve veri kayıt altyapısıdır.

---

## 7. Prototype Procurement Logic

Prototip satın alma ve üretim süreci aşağıdaki sıraya göre ilerlemelidir:

```text
1. Carrier chassis and superstructure frame
2. Power generation and electrical distribution
3. Paint tank, glass bead tank, screw pump and transfer line
4. Induction heating modules and thermal insulation
5. Industrial robot, X/Y rail and robot controller
6. Dual-bell thermoplastic gun and suction system
7. PLC, safety PLC, HMI and sensor network
8. RMDE computer, cameras, LiDAR, RTK-GNSS and IMU
9. Compressor, pneumatic distribution and purge system
10. Safety, fire suppression, cooling and service systems
```

---

## 8. Validation Relationship

Her BOM kalemi yalnızca fiziksel parça olarak değil, prototip doğrulama hedefiyle birlikte değerlendirilmelidir.

| Validation Target | Related BOM Groups |
|---|---|
| Controlled pellet feeding | Pellet tank, mixer, screw pump, level/torque sensors |
| Staged induction heating | Induction inverters, coils, thermal sensors, insulation |
| Robotic line application | Robot, X/Y rail, gun, height sensor, robot controller |
| Flow stability | Screw pump, pressure sensors, flow sensors, gun body heating |
| AI decision execution | RMDE computer, cameras, LiDAR, RTK, IMU, robot interface |
| Quality verification | Rear camera, robot area camera, quality module, reference points |
| Safety validation | Safety PLC, E-stop, fire detection, thermal shields, pressure relief |
| Energy continuity | Generators, main panel, load management, inverter bus |

---

## 9. Git Kısa Yol Haritası

```text
[Git: Sistem Genel Akışı] → 01-system-flow.md
[Git: Yeni Nesil Termoplastik Tabanca] → 04-next-generation-thermoplastic-gun.md
[Git: Robot Kol + X/Y Kızak] → 05-robot-arm-xy-rail.md
[Git: Güç ve Elektrik Mimarisi] → 06-power-electrical-architecture.md
[Git: PLC ve Kontrol Sistemi] → 07-plc-control-system.md
[Git: RMDE Yazılım Mimarisi] → 08-rmde-software-architecture.md
[Git: Yazılım Dosyaları] → 13-software-files.md
[Git: Source Document] → source-documents/ROMR_Prototype_BOM_Component_Network_V1.md
```

---

## 10. Teknik Sonuç

Prototype BOM yalnızca satın alma listesi değildir. Bu modül ROMR platformunun tüm alt sistemlerini birbirine bağlayan donanım omurgasıdır.

Doğru yapılandırılmış BOM sayesinde:

- üretici firma hangi ekipmanın neden gerektiğini görür,
- mekanik ve elektrik mühendisleri aynı referansa göre çalışır,
- yazılım ekibi hangi donanımla haberleşeceğini bilir,
- PLC I/O gereksinimleri netleşir,
- sensör ve kalite kontrol zinciri anlaşılır,
- prototip doğrulama planı donanımla eşleşir.

Bu nedenle BOM, ROMR Engineering Knowledge Platform içinde merkezi bir mühendislik modülü olarak ele alınmalıdır.
