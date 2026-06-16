# ROMR PLC, Safety & Process Control System V1

> Source technical module for the ROMR Engineering Knowledge Platform.

# 07 — PLC, Safety & Process Control System

<div class="git-buttons">

[Git: Sistem Genel Akışı](01-system-flow.md)
[Git: Pellet Boya Sistemi](02-pellet-paint-system.md)
[Git: İndüksiyon Isıtma Sistemi](03-induction-heating-system.md)
[Git: Yeni Nesil Termoplastik Tabanca](04-next-generation-thermoplastic-gun.md)
[Git: Robot Kol + X/Y Kızak](05-robot-arm-xy-rail.md)
[Git: Güç ve Elektrik Mimarisi](06-power-electrical-architecture.md)
[Git: RMDE Yazılım Mimarisi](08-rmde-software-architecture.md)
[Git: HUD ve Sürücü Rehberliği](09-hud-driver-guidance.md)
[Git: Kalite Kontrol Sistemi](10-quality-control-system.md)
[Git: Yazılım Dosyaları](13-software-files.md)

</div>

---

## 1. Modülün Sistemdeki Rolü

PLC, Safety & Process Control System, ROMR platformunun fiziksel proses kontrol omurgasıdır.

RMDE karar üretir; robot hareketi uygular; ancak boya besleme, indüksiyon ısıtma, tabanca, rotary bell, hava, purge, emiş, jeneratör yük durumu, acil durdurma ve güvenlik izinleri PLC katmanı tarafından yönetilmelidir.

Bu sistem şu prensiple çalışır:

```text
RMDE karar verir
↓
PLC proses izinlerini kontrol eder
↓
Safety PLC güvenlik doğrulaması yapar
↓
Robot / pompa / indüksiyon / tabanca / hava sistemleri çalışır
↓
Sensör geri bildirimi izlenir
↓
Alarm veya kalite hatası varsa proses düzeltmesi yapılır
```

---

## 2. Kontrol Mimarisinin Ana Katmanları

| Katman | Görev |
|---|---|
| Main PLC | Proses kontrolü, sensör okuma, pompa, valf, ısıtma ve alarm yönetimi |
| Safety PLC | Acil stop, yangın, aşırı sıcaklık, robot güvenlik alanı, enerji kesme |
| Robot Controller | 6 eksen robot ve X/Y ray hareket kontrolü |
| RMDE Computer | Karar motoru, yol modeli, standart motoru, robot komut paketi |
| HMI / HUD | Operatör ve sürücü bilgi ekranları |
| Sensor Network | Sıcaklık, basınç, debi, seviye, titreşim, vakum, kamera, LiDAR |
| Power Management | Jeneratör ve ana güç yük yönetimi |

---

## 3. Ana Kontrol Akışı

```text
Operator Start Command
↓
Safety PLC Check
↓
Generator and Power Status Check
↓
PLC Process Readiness Check
↓
Tank / Paint / Air / Heat / Robot Ready
↓
RMDE Application Command
↓
Robot Permission
↓
Paint Flow Enable
↓
Induction Heating Enable
↓
Gun / Air / Suction Enable
↓
Application
↓
Quality Feedback
↓
Correction or Safe Stop
```

---

## 4. PLC Tarafından Kontrol Edilen Alt Sistemler

| Alt Sistem | PLC Fonksiyonu |
|---|---|
| Pellet paint tank | mikser, seviye, köprüleşme, düşük malzeme alarmı |
| Screw pump / feeder | hız, tork, basınç, tıkanma alarmı |
| Induction heating | bölgesel PID, sıcaklık setpoint, inverter enable |
| Paint transfer line | sıcaklık, basınç, purge, akış doğrulama |
| Dual-bell paint gun | gövde ısıtma, rotary rpm, boya akışı, hava basıncı |
| Dust extraction | emiş fanı, vakum sensörü, toz haznesi seviyesi |
| Glass bead system | dozaj, seviye, akış doğrulama |
| Compressor | basınç, tank durumu, air dryer alarmı |
| Robot interlock | robot çalışabilir izin, safe zone, standby/purge pozisyonu |
| Generator system | yük durumu, alarm, yakıt, sıcaklık |
| Fire and emergency | acil durdurma, yangın, izolasyon, alarm |

---

## 5. PLC I/O Signal Matrix

### 5.1 Analog Inputs

| Signal | Source | Purpose |
|---|---|---|
| `paint_tank_temp` | tank temperature sensor | boya tank sıcaklığı |
| `paint_line_temp_z1` | induction zone 1 | ön ısıtma sıcaklığı |
| `paint_line_temp_z2` | induction zone 2 | yumuşama bölgesi |
| `paint_line_temp_z3` | induction zone 3 | ergime bölgesi |
| `paint_line_temp_z4` | induction zone 4 | stabilizasyon |
| `gun_body_temp` | gun body sensor | tabanca gövde sıcaklığı |
| `paint_pressure_before_gun` | pressure sensor | tabanca öncesi boya basıncı |
| `paint_flow_rate` | flow sensor | gerçek boya debisi |
| `atomizing_air_pressure` | air pressure sensor | 45° hava kanalları basıncı |
| `suction_vacuum_level` | vacuum sensor | emiş sistemi performansı |
| `rotary_bell_rpm` | RPM sensor | dış bell dönüş hızı |
| `gun_height` | laser / LiDAR height sensor | tabanca-yol mesafesi |
| `glass_bead_flow_rate` | bead flow sensor | cam küreciği debisi |
| `hydraulic_pressure` | hydraulic pressure sensor | rotary tahrik hidrolik basıncı |

### 5.2 Digital Inputs

| Signal | Source | Purpose |
|---|---|---|
| `e_stop_ok` | emergency stop circuit | acil stop zinciri sağlıklı mı |
| `fire_alarm_ok` | fire detection | yangın alarmı yok |
| `robot_safe_zone_ok` | robot controller | robot güvenli bölgede |
| `generator_ready` | generator controller | jeneratör hazır |
| `compressor_ready` | compressor controller | hava sistemi hazır |
| `tank_low_level` | level switch | boya düşük seviye |
| `bead_low_level` | level switch | cam küreciği düşük seviye |
| `dust_tank_full` | dust tank switch | toz haznesi dolu |
| `service_cover_closed` | safety switch | kapaklar kapalı |
| `overtemperature_alarm` | thermal safety relay | aşırı sıcaklık alarmı |

### 5.3 Analog Outputs

| Signal | Target | Purpose |
|---|---|---|
| `screw_pump_speed_ref` | pump drive | boya besleme hızı |
| `induction_power_z1` | induction inverter | zone 1 güç setpoint |
| `induction_power_z2` | induction inverter | zone 2 güç setpoint |
| `induction_power_z3` | induction inverter | zone 3 güç setpoint |
| `induction_power_z4` | induction inverter | zone 4 güç setpoint |
| `rotary_speed_setpoint` | hydraulic / motor drive | bell RPM hedefi |
| `atomizing_air_pressure_ref` | proportional valve | hava basınç hedefi |
| `glass_bead_dosing_ref` | dosing drive | cam küreciği debisi |

### 5.4 Digital Outputs

| Signal | Target | Purpose |
|---|---|---|
| `paint_flow_enable` | valve / pump | boya akışı aktif |
| `gun_heat_enable` | gun heating controller | tabanca ısıtma aktif |
| `induction_enable` | induction inverter | indüksiyon aktif |
| `atomizing_air_enable` | air valve | hava stabilizasyonu aktif |
| `suction_fan_enable` | jet fan | emiş sistemi aktif |
| `purge_valve_enable` | purge valve | temizlik hattı aktif |
| `robot_motion_permission` | robot controller | robot hareket izni |
| `glass_bead_enable` | bead dosing | cam küreciği aktif |
| `alarm_beacon` | warning light | görsel alarm |
| `safe_shutdown` | main contactor / safety | güvenli kapatma |

---

## 6. İndüksiyon PID Kontrol Mantığı

İndüksiyon sistemi tek noktalı ısıtma değil, çok bölgeli kademeli kontrol sistemi olarak ele alınmalıdır.

```text
Zone 1 — Preheating
Zone 2 — Controlled softening
Zone 3 — Melting / flow formation
Zone 4 — Temperature stabilization
Zone 5 — Gun inlet / body maintenance
```

PLC, her bölge için:

- sıcaklık setpoint,
- gerçek sıcaklık,
- akış hızı,
- güç yüzdesi,
- aşırı sıcaklık limiti,
- boya durumu

verilerini izler.

---

## 7. Boya Besleme ve Akış Kontrolü

Boya besleme sistemi şu mantıkla çalışır:

```text
RMDE line_required = True
↓
Safety OK
↓
Paint temperature OK
↓
Gun ready
↓
Screw pump speed reference
↓
Paint pressure check
↓
Paint flow enable
↓
Quality feedback
```

Eğer boya basıncı yükselir ve debi düşerse:

```text
Possible clogging
↓
Reduce pump speed
↓
Trigger warning
↓
Prepare purge sequence
```

---

## 8. Dual-Bell Tabanca Kontrolü

PLC, yeni nesil termoplastik tabancanın şu fonksiyonlarını yönetir:

- gövde sıcaklığı,
- rotary bell rpm,
- boya akışı,
- atomizing air pressure,
- purge / cleaning sequence,
- emiş fanı,
- tabanca yüksekliği alarmı,
- acil kapatma.

Tabanca, robot ve PLC arasında karşılıklı izin zinciri olmalıdır.

```text
Robot in target pose
AND gun height OK
AND paint temp OK
AND pressure OK
AND safety OK
THEN paint_flow_enable = True
```

---

## 9. Robot Interlock Sistemi

Robot hareketi yalnızca aşağıdaki koşullarda izinli olmalıdır:

- emergency stop OK,
- robot safety zone OK,
- service covers closed,
- gun and hose carrier clear,
- paint pressure within safe range,
- thermal status OK,
- suction hose not blocked,
- X/Y rail limit OK,
- RMDE command valid.

Robot herhangi bir nedenle limit dışına çıkarsa boya akışı otomatik olarak durdurulmalıdır.

---

## 10. Toz Emiş Kontrolü

Püskürtme aktif olduğunda emiş sistemi de otomatik devreye girmelidir.

```text
paint_flow_enable = True
↓
suction_fan_enable = True
↓
vacuum level monitored
↓
dust tank level monitored
```

Vakum düşerse:

```text
Suction warning
↓
Quality risk flag
↓
Operator notification
```

---

## 11. Purge / Otomatik Temizlik Sırası

Tabanca ve boya hattı için temizlik süreci PLC tarafından yönetilir.

```text
Application stop
↓
Paint flow disabled
↓
Robot moves to purge position
↓
Gun heat maintained
↓
Purge valve opens
↓
Air / cleaning fluid sequence
↓
Rotary bell low-speed rotation
↓
Discharge to safe collection container
↓
System standby
```

---

## 12. Safety PLC Görevleri

Safety PLC veya bağımsız safety controller şu görevleri üstlenmelidir:

- acil stop zinciri,
- robot güvenli bölge,
- yangın algılama,
- aşırı sıcaklık,
- yüksek basınç,
- servis kapağı açık uyarısı,
- jeneratör acil kapatma,
- ana kontaktör kesme,
- robot hareket yetkisi kesme.

Güvenlik fonksiyonları Python/RMDE yazılımına bırakılmamalıdır. RMDE karar üretir; safety PLC fiziksel güvenliği doğrular.

---

## 13. PLC-RMDE Haberleşmesi

RMDE ile PLC arasında veri alışverişi aşağıdaki paketlerle yapılmalıdır:

### 13.1 RMDE → PLC

| Veri | Açıklama |
|---|---|
| `line_required` | çizgi uygulanacak mı |
| `paint_flow_target` | boya debisi hedefi |
| `line_width` | çizgi eni |
| `vehicle_speed_target` | araç hızı |
| `gun_enable_request` | tabanca açma isteği |
| `purge_request` | temizlik isteği |
| `country_standard_id` | standart kuralı |
| `robot_pose_valid` | robot hedef geçerli mi |

### 13.2 PLC → RMDE

| Veri | Açıklama |
|---|---|
| `process_ready` | proses hazır |
| `paint_temperature_ok` | boya sıcaklığı uygun |
| `paint_pressure_ok` | basınç uygun |
| `gun_ready` | tabanca hazır |
| `air_ready` | hava basıncı uygun |
| `suction_ready` | emiş sistemi uygun |
| `safety_ok` | güvenlik zinciri tamam |
| `alarm_code` | alarm durumu |

---

## 14. Alarm ve Hata Kodları

| Alarm | Açıklama | Etki |
|---|---|---|
| `E_STOP_ACTIVE` | Acil stop aktif | tüm proses durur |
| `FIRE_ALARM` | Yangın algılandı | güvenli kapatma |
| `OVER_TEMP` | sıcaklık limit dışı | ısıtma durur |
| `HIGH_PAINT_PRESSURE` | boya basıncı yüksek | pompa durur |
| `LOW_AIR_PRESSURE` | hava basıncı düşük | tabanca açılmaz |
| `SUCTION_FAILURE` | emiş yetersiz | kalite riski |
| `ROBOT_LIMIT` | robot limitte | boya akışı kesilir |
| `GUN_HEIGHT_ERROR` | tabanca yüksekliği hatalı | uygulama durur |
| `GENERATOR_ALARM` | jeneratör alarmı | yük yönetimi / duruş |

---

## 15. Yazılım Bağlantıları

```text
plc_process_interface.py
safety_supervisor.py
induction_heat_controller.py
robot_command_layer.py
rmde_decision_engine.py
quality_control_module.py
hud_guidance_system.py
```

<div class="git-buttons">

[Git: Yazılım: plc_process_interface.py](software/plc_process_interface.py)
[Git: Yazılım: safety_supervisor.py](software/safety_supervisor.py)
[Git: Yazılım: induction_heat_controller.py](software/induction_heat_controller.py)

</div>

---

## 16. Test ve Doğrulama Planı

### 16.1 I/O Simülasyon Testi

- tüm analog ve dijital sinyaller simüle edilir,
- alarm koşulları test edilir,
- güvenlik izin zinciri doğrulanır.

### 16.2 Termal PID Testi

- her indüksiyon zone ayrı ayrı test edilir,
- sıcaklık rampası izlenir,
- aşırı sıcaklık durumunda shutdown doğrulanır.

### 16.3 Robot-PLC Interlock Testi

- robot hedef pozisyonda değilken boya akışı engellenir,
- robot güvenlik alarmında paint_flow_enable kapanır.

### 16.4 Purge Testi

- robot purge pozisyonuna gider,
- boya akışı kapanır,
- purge valfi ve hava sırası çalışır,
- sistem standby moduna döner.

### 16.5 Safety PLC Testi

- acil stop,
- yangın,
- kapak açık,
- aşırı sıcaklık,
- yüksek basınç

senaryoları ayrı ayrı doğrulanır.

---

## 17. Git Kısa Yol Haritası

```text
[Git: Pellet Boya Sistemi] → 02-pellet-paint-system.md
[Git: İndüksiyon Isıtma Sistemi] → 03-induction-heating-system.md
[Git: Yeni Nesil Termoplastik Tabanca] → 04-next-generation-thermoplastic-gun.md
[Git: Robot Kol + X/Y Kızak] → 05-robot-arm-xy-rail.md
[Git: Güç ve Elektrik Mimarisi] → 06-power-electrical-architecture.md
[Git: RMDE Yazılım Mimarisi] → 08-rmde-software-architecture.md
[Git: Kalite Kontrol Sistemi] → 10-quality-control-system.md
[Git: Yazılım Dosyaları] → 13-software-files.md
[Git: Source Document] → source-documents/ROMR_PLC_Control_System_V1.md
```

---

## 18. Teknik Sonuç

PLC, Safety & Process Control System, ROMR platformunun fiziksel dünyadaki güvenli ve kararlı çalışmasını sağlayan ana kontrol katmanıdır.

Bu modül sayesinde:

- RMDE kararları fiziksel proses komutlarına dönüştürülür,
- indüksiyon, boya, hava, tabanca, robot ve emiş sistemleri senkronize edilir,
- safety PLC ile güvenlik yazılımdan bağımsız doğrulanır,
- kalite kontrol geri bildirimi proses düzeltmelerine bağlanır,
- tabanca, robot ve boya akışı yalnızca güvenli koşullarda çalışır.

Bu nedenle PLC sistemi, ROMR platformunda mekanik ekipmanları, yazılım kararlarını ve saha güvenliğini birleştiren merkezi endüstriyel kontrol omurgasıdır.
