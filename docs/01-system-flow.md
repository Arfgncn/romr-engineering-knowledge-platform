[01-system-flow.md](https://github.com/user-attachments/files/28995859/01-system-flow.md)
# 01 — ROMR Integrated System Flow

<div class="git-buttons">

[Git: Pellet Boya Sistemi](02-pellet-paint-system.md)
[Git: İndüksiyon Isıtma Sistemi](03-induction-heating-system.md)
[Git: Yeni Nesil Termoplastik Tabanca](04-next-generation-thermoplastic-gun.md)
[Git: Robot Kol + X/Y Kızak](05-robot-arm-xy-rail.md)
[Git: Güç ve Elektrik Mimarisi](06-power-electrical-architecture.md)
[Git: PLC ve Kontrol Sistemi](07-plc-control-system.md)
[Git: RMDE Yazılım Mimarisi](08-rmde-software-architecture.md)
[Git: HUD ve Sürücü Rehberliği](09-hud-driver-guidance.md)
[Git: Kalite Kontrol Sistemi](10-quality-control-system.md)
[Git: Uluslararası Standart Motoru](11-international-standards-engine.md)
[Git: Prototip BOM](12-prototype-bom.md)
[Git: Yazılım Dosyaları](13-software-files.md)

</div>

---

## 1. Platformun Ana Mantığı

ROMR platformu, klasik termoplastik yol çizgi kamyonu değildir. Sistem; mekanik platform, pellet boya besleme, çok kademeli indüksiyon ısıtma, endüstriyel robot uygulaması, yeni nesil dual-bell rotary thermoplastic gun, RMDE yazılım mimarisi, HUD sürücü rehberliği, kalite kontrol, PLC/safety kontrolü ve uluslararası standart motorunu tek bir entegre mühendislik ağı altında birleştirir.

Ana çalışma akışı:

```text
Road Survey
↓
Digital Road Model
↓
RMDE Decision Engine
↓
50 cm Reference Points
↓
Robot Command Layer
↓
Industrial Robot + X/Y Rail
↓
Pellet Paint Feed System
↓
Multi-Stage Induction Heating
↓
Dual-Bell Rotary Thermoplastic Gun
↓
Road Marking Application
↓
Quality Control & Vision Feedback
↓
Standards Validation
↓
Telemetry & Improvement Loop
```

---

## 2. Ana Sistem Blokları

| Sistem Bloğu | Görev | Git |
|---|---|---|
| Pellet Paint Feed System | Boyayı pelet formda kontrollü besler | [Git](02-pellet-paint-system.md) |
| Multi-Stage Induction Heating | Boyayı hareketli hatta kademeli ısıtır | [Git](03-induction-heating-system.md) |
| Next-Generation Paint Gun | Boyayı dual-bell rotary prensiple uygular | [Git](04-next-generation-thermoplastic-gun.md) |
| Industrial Robot + X/Y Rail | Tabancayı koordinat bazlı konumlandırır | [Git](05-robot-arm-xy-rail.md) |
| Power & Electrical Architecture | Jeneratör, pano, yük ve güvenli enerji dağıtımı | [Git](06-power-electrical-architecture.md) |
| PLC & Safety Control | Fiziksel proses ve güvenlik izinlerini yönetir | [Git](07-plc-control-system.md) |
| RMDE Software Architecture | Yol verisinden çizgi kararları üretir | [Git](08-rmde-software-architecture.md) |
| HUD Driver Guidance | Sürücüyü ghost-line ve sapma uyarılarıyla yönlendirir | [Git](09-hud-driver-guidance.md) |
| Quality Control System | Uygulamayı ölçer ve geri bildirim üretir | [Git](10-quality-control-system.md) |
| International Standards Engine | Ülke/bölge standartlarını uygular | [Git](11-international-standards-engine.md) |
| Prototype BOM | Tüm ekipman ve donanım ağını listeler | [Git](12-prototype-bom.md) |
| Software Files | Yazılım dosyalarını ve kod mimarisini gösterir | [Git](13-software-files.md) |

---

## 3. Fiziksel Proses Akışı

```text
Pellet Tank
↓
Anti-Bridging / Agitator
↓
Servo Screw Feeder
↓
Flow Conditioning Chamber
↓
Induction Heating Zones
↓
Heated Robot-Mounted Transfer Line
↓
Dual-Bell Rotary Gun
↓
Circular Thermoplastic Application
↓
Dust Extraction
↓
Quality Vision Check
```

<div class="git-buttons">

[Git: Pellet Boya Sistemi](02-pellet-paint-system.md)
[Git: İndüksiyon Isıtma Sistemi](03-induction-heating-system.md)
[Git: Yeni Nesil Termoplastik Tabanca](04-next-generation-thermoplastic-gun.md)
[Git: Kalite Kontrol Sistemi](10-quality-control-system.md)

</div>

---

## 4. Yazılım ve Karar Akışı

```text
Pre-Survey Module
↓
Road Classifier
↓
Digital Road Model
↓
Reference Point Generator
↓
Standards Rule Engine
↓
RMDE Decision Engine
↓
Robot Command Layer
↓
PLC Process Interface
↓
HUD Guidance
↓
Quality Feedback
↓
Telemetry Logger
```

<div class="git-buttons">

[Git: RMDE Yazılım Mimarisi](08-rmde-software-architecture.md)
[Git: Uluslararası Standart Motoru](11-international-standards-engine.md)
[Git: Yazılım Dosyaları](13-software-files.md)

</div>

---

## 5. Robotik Uygulama Akışı

```text
RMDE Reference Point
↓
Robot Target Pose
↓
X/Y Rail Position
↓
6-Axis Industrial Robot
↓
Constant Gun Height
↓
Dual-Bell Gun Activation
↓
Line Application
↓
Quality Feedback
```

<div class="git-buttons">

[Git: Robot Kol + X/Y Kızak](05-robot-arm-xy-rail.md)
[Git: Yeni Nesil Termoplastik Tabanca](04-next-generation-thermoplastic-gun.md)
[Git: RMDE Yazılım Mimarisi](08-rmde-software-architecture.md)

</div>

---

## 6. Enerji ve Kontrol Akışı

```text
Turbine Generators
↓
Main Electrical Panel
↓
Load Management
↓
Induction Inverters
↓
Robot Controller
↓
PLC / Safety PLC
↓
AI Computer / Sensors / HUD
```

<div class="git-buttons">

[Git: Güç ve Elektrik Mimarisi](06-power-electrical-architecture.md)
[Git: PLC ve Kontrol Sistemi](07-plc-control-system.md)
[Git: Prototip BOM](12-prototype-bom.md)

</div>

---

## 7. Standart ve Kalite Döngüsü

```text
Country / Region Selection
↓
Standards Rule Engine
↓
RMDE Line Geometry
↓
Robot + PLC Execution
↓
Quality Vision Measurement
↓
Tolerance Comparison
↓
Correction Recommendation
↓
Telemetry Record
```

<div class="git-buttons">

[Git: Uluslararası Standart Motoru](11-international-standards-engine.md)
[Git: Kalite Kontrol Sistemi](10-quality-control-system.md)
[Git: HUD ve Sürücü Rehberliği](09-hud-driver-guidance.md)

</div>

---

## 8. Ana Entegrasyon Mantığı

ROMR platformunda hiçbir sistem bağımsız çalışmaz.

Örnek:

```text
RMDE line decision
requires:
- country standard
- road model
- reference points
- robot reach
- PLC process readiness
- paint temperature
- safety approval
```

Başka örnek:

```text
Gun activation
requires:
- robot target pose valid
- gun height OK
- paint temperature OK
- paint pressure OK
- air pressure OK
- suction system ready
- safety PLC OK
```

Bu nedenle platformun gerçek değeri tek tek ekipmanlarda değil, bu ekipmanların kontrollü mühendislik ağı içinde birlikte çalışmasındadır.

---

## 9. Kritik Sistem Bağlantıları

| Kaynak Sistem | Bağlı Sistemler |
|---|---|
| Pellet System | Induction, PLC, BOM |
| Induction System | Power, PLC, Gun, Robot |
| Gun System | Robot, PLC, Dust Extraction, Quality |
| Robot System | RMDE, PLC, Gun, Quality |
| RMDE | Standards, Reference Points, Robot, HUD, Quality |
| PLC | Power, Sensors, Gun, Pump, Induction, Safety |
| HUD | RMDE, PLC, Robot, Quality |
| Quality | RMDE, Standards, Robot, PLC |
| BOM | All hardware modules |
| Software Files | RMDE, PLC, Robot, HUD, Quality |

---

## 10. Geliştirme Sırası

ROMR platformu aşağıdaki sırayla geliştirilmelidir:

```text
1. Pellet feed and induction prototype
2. Rotary gun flow validation
3. Robot + gun motion validation
4. PLC process and safety validation
5. RMDE simulation
6. HUD guidance simulation
7. Quality vision feedback
8. Integrated vehicle prototype
9. Field testing
10. Standards-based deployment
```

---

## 11. Teknik Sonuç

ROMR Integrated System Flow, platformdaki tüm alt sistemlerin birbirine nasıl bağlandığını gösteren ana navigasyon ve entegrasyon haritasıdır.

Bu dosya sayesinde üretici firma:

- hangi modülün hangi sistemle bağlantılı olduğunu,
- yazılımın fiziksel ekipmana nasıl komut verdiğini,
- PLC’nin hangi prosesleri yönettiğini,
- robotun RMDE ile nasıl çalıştığını,
- tabancanın indüksiyon, robot ve kalite sistemleriyle nasıl entegre edildiğini,
- standart motorunun çizgi geometrisini nasıl etkilediğini

tek bir ana sistem haritası üzerinden görebilir.

Bu nedenle bu dosya, ROMR Engineering Knowledge Platform’un ana giriş ve yönlendirme sayfasıdır.
