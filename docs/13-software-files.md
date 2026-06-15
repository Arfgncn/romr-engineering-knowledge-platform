[13-software-files.md](https://github.com/user-attachments/files/28957647/13-software-files.md)
# 13 — Software Files & Code Package

<div class="git-buttons">

[Git: Sistem Genel Akışı](01-system-flow.md)
[Git: RMDE Yazılım Mimarisi](08-rmde-software-architecture.md)
[Git: Robot Kol + X/Y Kızak](05-robot-arm-xy-rail.md)
[Git: Yeni Nesil Termoplastik Tabanca](04-next-generation-thermoplastic-gun.md)
[Git: PLC ve Kontrol Sistemi](07-plc-control-system.md)
[Git: HUD ve Sürücü Rehberliği](09-hud-driver-guidance.md)
[Git: Kalite Kontrol Sistemi](10-quality-control-system.md)
[Git: Uluslararası Standart Motoru](11-international-standards-engine.md)
[Git: Prototip BOM](12-prototype-bom.md)

</div>

---

## 1. Yazılım Paketinin Rolü

Software Files & Code Package, ROMR Engineering Knowledge Platform içindeki tüm yazılım katmanlarının dosya bazlı mimarisini tanımlar.

Bu bölümdeki dosyalar nihai ticari yazılım paketi değildir. Bunlar:

- sistem mimarisini açıklayan,
- veri yapılarını tanımlayan,
- modüller arası görev paylaşımını gösteren,
- prototip simülasyonu için başlangıç çekirdeği sağlayan,
- üretici yazılım ekibinin geliştirme sürecini yönlendiren

mühendislik yazılım dosyalarıdır.

---

## 2. Ana Yazılım Dosya Ağacı

```text
docs/software/
│
├── pre_survey_module.py
├── road_classifier.py
├── existing_line_detector.py
├── digital_road_model.py
├── reference_point_generator.py
├── standards_rule_engine.py
├── rmde_decision_engine.py
├── robot_command_layer.py
├── plc_process_interface.py
├── hud_guidance_system.py
├── quality_control_module.py
├── safety_supervisor.py
├── telemetry_logger.py
└── induction_heat_controller.py
```

---

## 3. Yazılım Katmanları

| Katman | Dosyalar | Görev |
|---|---|---|
| Sensor / Survey Layer | `pre_survey_module.py`, `existing_line_detector.py`, `digital_road_model.py` | Yol verisini ve mevcut çizgiyi işler |
| Classification Layer | `road_classifier.py` | Yol tipini ve uygulama senaryosunu belirler |
| Standards Layer | `standards_rule_engine.py` | Ülke/bölge/proje standartlarını yükler |
| Decision Layer | `reference_point_generator.py`, `rmde_decision_engine.py` | 50 cm noktalar ve çizgi kararları üretir |
| Execution Layer | `robot_command_layer.py`, `plc_process_interface.py` | Robot ve PLC komutlarını oluşturur |
| Guidance Layer | `hud_guidance_system.py` | Sürücüye ghost-line ve yönlendirme verir |
| Feedback Layer | `quality_control_module.py`, `telemetry_logger.py` | Kalite ve kayıt sistemini yönetir |
| Safety Layer | `safety_supervisor.py` | Güvenlik izinleri ve acil durum mantığı |
| Thermal Layer | `induction_heat_controller.py` | İndüksiyon sıcaklık ve PID mantığı |

---

## 4. Modüller Arası Ana Veri Akışı

```text
pre_survey_module.py
        ↓
road_classifier.py
        ↓
digital_road_model.py
        ↓
reference_point_generator.py
        ↓
standards_rule_engine.py
        ↓
rmde_decision_engine.py
        ↓
robot_command_layer.py
        ↓
plc_process_interface.py
        ↓
hud_guidance_system.py
        ↓
quality_control_module.py
        ↓
telemetry_logger.py
```

Güvenlik katmanı olan `safety_supervisor.py`, tüm proses boyunca paralel olarak çalışır ve kritik durumlarda robot, tabanca, indüksiyon, pompa, emiş ve jeneratör sistemlerini güvenli duruma geçirir.

---

## 5. Dosya Açıklamaları

### 5.1 `pre_survey_module.py`

Görevleri:

- kamera, LiDAR, RTK-GNSS ve IMU verilerini almak,
- yol genişliği, şerit sayısı, kenar/orta eksen bilgilerini çıkarmak,
- ham veriyi RMDE’ye uygun ön veri haline getirmek.

[Git: RMDE Yazılım Mimarisi](08-rmde-software-architecture.md)

---

### 5.2 `road_classifier.py`

Görevleri:

- şehir içi yol,
- otoyol,
- iki yönlü yol,
- kavşak yaklaşımı,
- yaya geçidi,
- tünel,
- havaalanı,
- endüstriyel saha

gibi uygulama senaryolarını sınıflandırmak.

---

### 5.3 `digital_road_model.py`

Görevleri:

- yol segmentini dijital geometri modeline dönüştürmek,
- sağ/sol kenar, orta eksen, şerit merkezleri ve uygulama koridorunu tanımlamak,
- referans noktası üretimi için temel modeli hazırlamak.

---

### 5.4 `reference_point_generator.py`

Görevleri:

- yol güzergâhını 50 cm aralıklarla bölmek,
- P0, P1, P2... veri düğümlerini oluşturmak,
- her nokta için konum, hız, çizgi tipi ve robot hedef verilerini saklamak.

---

### 5.5 `standards_rule_engine.py`

Görevleri:

- ülke / bölge standart dosyasını yüklemek,
- çizgi eni, renk, boşluk, kalınlık ve toleransları belirlemek,
- RMDE’ye standart parametre sağlamak.

[Git: Uluslararası Standart Motoru](11-international-standards-engine.md)

---

### 5.6 `rmde_decision_engine.py`

Görevleri:

- yol modeli + standart + mevcut çizgi + uygulama durumunu birlikte değerlendirmek,
- hangi çizginin uygulanacağını belirlemek,
- robot, PLC, HUD ve kalite kontrol modüllerine karar paketi üretmek.

---

### 5.7 `robot_command_layer.py`

Görevleri:

- RMDE kararlarını robot pozisyon komutlarına çevirmek,
- X/Y ray, robot bilek, tabanca yüksekliği ve purge pozisyonlarını yönetmek.

[Git: Robot Kol + X/Y Kızak](05-robot-arm-xy-rail.md)

---

### 5.8 `plc_process_interface.py`

Görevleri:

- boya akışı,
- tabanca ısıtma,
- indüksiyon setpoint,
- hava basıncı,
- emiş fanı,
- purge valfi,
- rotary bell rpm,
- güvenlik izinleri

gibi proses komutlarını PLC’ye aktarmak.

[Git: PLC ve Kontrol Sistemi](07-plc-control-system.md)

---

### 5.9 `hud_guidance_system.py`

Görevleri:

- ghost-line katmanını oluşturmak,
- sürücüye yön düzeltmesi vermek,
- hız ve hizalama uyarısı üretmek,
- çizgi başlangıç/bitiş mesajları göstermek.

[Git: HUD ve Sürücü Rehberliği](09-hud-driver-guidance.md)

---

### 5.10 `quality_control_module.py`

Görevleri:

- çizgi eni,
- çizgi kalınlığı,
- hizalama sapması,
- renk / süreklilik,
- cam küreciği dağılımı

parametrelerini değerlendirmek ve referans nokta bazlı hata kaydı üretmek.

[Git: Kalite Kontrol Sistemi](10-quality-control-system.md)

---

### 5.11 `safety_supervisor.py`

Görevleri:

- robot güvenlik alanı,
- acil stop,
- tabanca sıcaklığı,
- boya basıncı,
- yangın,
- emiş sistemi,
- jeneratör durumu,
- insan/araç yakınlığı

gibi kritik durumları izlemek.

---

### 5.12 `telemetry_logger.py`

Görevleri:

- RMDE kararlarını,
- robot komutlarını,
- PLC durumunu,
- kalite verisini,
- hata kayıtlarını

saha raporu ve geliştirme analizi için kaydetmek.

---

### 5.13 `induction_heat_controller.py`

Görevleri:

- indüksiyon bölge sıcaklıklarını yönetmek,
- PID hedeflerini üretmek,
- akış-sıcaklık koordinasyonunu sağlamak,
- aşırı ısınma durumunda güvenli duruş komutu hazırlamak.

[Git: İndüksiyon Isıtma Sistemi](03-induction-heating-system.md)

---

## 6. Yazılım-Donanım Bağlantı Matrisi

| Yazılım Dosyası | Donanım / Sistem |
|---|---|
| `pre_survey_module.py` | Kamera, LiDAR, RTK-GNSS, IMU |
| `road_classifier.py` | RMDE çekirdeği |
| `digital_road_model.py` | Dijital yol modeli |
| `reference_point_generator.py` | 50 cm referans noktaları |
| `standards_rule_engine.py` | Ülke/bölge standart kütüphanesi |
| `rmde_decision_engine.py` | Ana karar motoru |
| `robot_command_layer.py` | Endüstriyel robot, X/Y ray, tabanca |
| `plc_process_interface.py` | PLC, sensörler, valfler, pompa, indüksiyon |
| `hud_guidance_system.py` | HUD / HMI |
| `quality_control_module.py` | Kamera, kalite sensörleri |
| `safety_supervisor.py` | Safety PLC, acil stop, yangın, robot güvenliği |
| `telemetry_logger.py` | Veri kayıt sistemi |
| `induction_heat_controller.py` | İndüksiyon inverterleri ve sıcaklık sensörleri |

---

## 7. Prototip Geliştirme Sırası

```text
1. RoadInput, RoadStandard, ReferencePoint veri sınıfları
2. 50 cm referans noktası üretimi
3. Standart kütüphanesi okuma
4. Basit RMDE karar motoru
5. Robot komut paketi üretimi
6. PLC proses komut paketi
7. HUD mesajları
8. Kalite kontrol hata kaydı
9. Safety supervisor izin zinciri
10. Telemetry logger
```

---

## 8. Örnek Çalışma Senaryosu

```text
Input:
Country = Türkiye
Road Type = Urban Road
Road Width = 7.00 m
Lane Count = 2
Existing Line = Broken
Road Length = 100 m

Process:
Standards engine loads Turkish urban road rules
Reference point generator creates 200 points
RMDE decides broken centerline completion
Robot command layer creates target positions
PLC interface activates paint / heat / air / suction
HUD shows ghost line
Quality control checks applied line

Output:
Reference-point-based robot and PLC command list
```

---

## 9. Git Kısa Yol Haritası

```text
[Git: RMDE Yazılım Mimarisi] → 08-rmde-software-architecture.md
[Git: Robot Kol + X/Y Kızak] → 05-robot-arm-xy-rail.md
[Git: PLC ve Kontrol Sistemi] → 07-plc-control-system.md
[Git: HUD ve Sürücü Rehberliği] → 09-hud-driver-guidance.md
[Git: Kalite Kontrol Sistemi] → 10-quality-control-system.md
[Git: Uluslararası Standart Motoru] → 11-international-standards-engine.md
[Git: Prototip BOM] → 12-prototype-bom.md
[Git: Source Document] → source-documents/ROMR_Software_Files_Code_Package_V1.md
```

---

## 10. Teknik Sonuç

Software Files & Code Package, ROMR platformunun yazılım mimarisini dosya düzeyinde görünür hale getirir.

Bu bölüm sayesinde:

- üretici yazılım ekibi hangi dosyanın ne iş yaptığını anlar,
- RMDE, robot, PLC, HUD ve kalite kontrol bağlantısı netleşir,
- prototip simülasyonu için başlangıç çekirdeği oluşur,
- gerçek saha yazılımına geçiş için katmanlı mimari korunur,
- sistem tek büyük ve anlaşılmaz Python dosyası yerine profesyonel modüllere ayrılır.

Bu nedenle yazılım dosyaları, ROMR platformunun mühendislik bilgi ağında bağımsız ama tüm sistemle bağlantılı bir ana modül olarak ele alınmalıdır.
