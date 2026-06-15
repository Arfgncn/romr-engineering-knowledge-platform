# 08 — RMDE Software Architecture

<div class="git-buttons">

[Git: Sistem Genel Akışı](01-system-flow.md)
[Git: Robot Kol + X/Y Kızak](05-robot-arm-xy-rail.md)
[Git: Yeni Nesil Termoplastik Tabanca](04-next-generation-thermoplastic-gun.md)
[Git: PLC ve Kontrol Sistemi](07-plc-control-system.md)
[Git: HUD ve Sürücü Rehberliği](09-hud-driver-guidance.md)
[Git: Kalite Kontrol Sistemi](10-quality-control-system.md)
[Git: Uluslararası Standart Motoru](11-international-standards-engine.md)
[Git: Prototip BOM](12-prototype-bom.md)
[Git: Yazılım Dosyaları](13-software-files.md)

</div>

---

## 1. RMDE'nin Sistemdeki Rolü

Road Marking Decision Engine (RMDE), ROMR platformunun yazılım beynidir. Bu modül, ön keşif aracından veya sensör sisteminden gelen dijital yol verisini; ülke bazlı çizgi standartları, yol sınıflandırması, mevcut çizgi durumu, araç hızı, boya debisi, robot erişim alanı ve kalite toleranslarıyla birlikte değerlendirerek uygulanacak çizginin tipini, geometrisini, koordinatlarını ve proses parametrelerini belirler.

RMDE doğrudan "çizgi çiz" komutu veren basit bir yazılım değildir. Sistem; yol modelini, standartları, robot komutlarını, PLC proses sinyallerini, HUD sürücü rehberliğini ve kalite kontrol geri bildirimlerini tek bir karar zinciri içinde yönetir.

---

## 2. Ana Yazılım Akışı

```text
Pre-Survey Data Acquisition
↓
Digital Road Model
↓
Road Classification
↓
Existing Line Detection
↓
Country / Region Standards Library
↓
50 cm Reference Point Generator
↓
RMDE Decision Engine
↓
Robot Command Layer
↓
PLC Process Interface
↓
HUD Guidance System
↓
Quality Control Feedback
↓
Adaptive Parameter Update
```

Bu yapı sayesinde sistem, operatörün görsel tahminine değil, sayısal yol modeline ve standart doğrulama katmanına göre çalışır.

---

## 3. RMDE Ana Modülleri

| Modül | Görev | Bağlı Sistem |
|---|---|---|
| `pre_survey_module.py` | Kamera, LiDAR, RTK-GNSS, IMU ve yol geometrisi verilerini toplar | Sensör sistemi |
| `road_classifier.py` | Yol tipi, şerit sayısı, yön, bölge ve uygulama senaryosunu sınıflandırır | RMDE çekirdeği |
| `existing_line_detector.py` | Mevcut çizgileri ve çizgi durumunu değerlendirir | Kamera / AI vision |
| `digital_road_model.py` | Yol segmentini dijital geometri modeline dönüştürür | Referans nokta sistemi |
| `reference_point_generator.py` | Her 50 cm için P0, P1, P2... kontrol noktalarını üretir | Robot + HUD + kalite |
| `standards_rule_engine.py` | Ülke ve bölge standartlarını yükler | Standart kütüphanesi |
| `rmde_decision_engine.py` | Nihai çizgi kararlarını üretir | Tüm yazılım katmanı |
| `robot_command_layer.py` | Robot kol ve X/Y ray için hedef komutları üretir | Robot kontrolcü |
| `plc_process_interface.py` | Boya, hava, indüksiyon, tabanca, emiş ve purge proseslerini PLC'ye aktarır | PLC |
| `hud_guidance_system.py` | Sürücüye ghost-line ve düzeltme komutları üretir | HMI / HUD |
| `quality_control_module.py` | Uygulama sonrası ölçüm ve hata kaydı yapar | Kamera + sensör |
| `safety_supervisor.py` | Güvenlik, acil durdurma ve proses kilitlerini izler | Safety PLC / PLC |

---

## 4. Girdi Veri Modeli

RMDE'nin işlediği ana girdiler aşağıdaki veri gruplarından oluşur:

### 4.1 Yol Geometrisi

- yol genişliği,
- şerit sayısı,
- şerit genişlikleri,
- yol tipi,
- yol uzunluğu,
- sağ yol kenarı,
- sol yol kenarı,
- orta eksen,
- banket / kaldırım / refüj bilgisi,
- eğim ve yol yüzeyi bilgisi.

### 4.2 Mevcut Çizgi Verisi

- mevcut çizgi var/yok,
- çizgi kondisyonu,
- kırık / silinmiş / eksik segmentler,
- çizgi rengi,
- çizgi konumu,
- önceki ve sonraki çizgi segmentleri.

### 4.3 Standart Verisi

- ülke / bölge seçimi,
- yol sınıfı,
- çizgi tipi,
- çizgi eni,
- çizgi kalınlığı,
- çizgi uzunluğu,
- boşluk mesafesi,
- renk,
- cam küreciği miktarı,
- kalite toleransı,
- retroreflectivity gereksinimi.

### 4.4 Makine ve Proses Verisi

- araç hızı,
- robot erişim alanı,
- tabanca yüksekliği,
- boya sıcaklığı,
- boya basıncı,
- boya debisi,
- cam küreciği debisi,
- bell dönüş hızı,
- hava basıncı,
- emiş sistemi durumu.

---

## 5. Çıktı Veri Modeli

RMDE aşağıdaki çıktı komutlarını üretir:

| Çıktı | Açıklama |
|---|---|
| `line_required` | İlgili referans noktasında çizgi uygulanacak mı? |
| `line_type` | Sürekli, kesikli, kenar, merkez, yaya, ok, sembol vb. |
| `line_width` | Ülke standardına göre çizgi eni |
| `line_thickness` | Malzeme ve standart bazlı et kalınlığı |
| `line_color` | Beyaz, sarı, kırmızı, mavi vb. |
| `start_coordinate` | Çizgi başlangıç koordinatı |
| `end_coordinate` | Çizgi bitiş koordinatı |
| `robot_target_pose` | Robot kol hedef pozisyonu |
| `vehicle_target_speed` | Araç hedef hızı |
| `paint_flow_rate` | Hesaplanan boya debisi |
| `glass_bead_flow_rate` | Cam küreciği debisi |
| `gun_height` | Tabanca-asfalt mesafesi |
| `hud_command` | Sürücüye görsel/sesli komut |
| `quality_tolerance` | Kabul edilebilir sapma sınırı |

---

## 6. 50 cm Reference Point Architecture

RMDE mimarisinin ana kontrol birimi 50 cm referans noktasıdır. Yol segmenti her 0.50 m'de bir bağımsız dijital karar noktasına ayrılır.

```text
P0 = 0.00 m
P1 = 0.50 m
P2 = 1.00 m
P3 = 1.50 m
P4 = 2.00 m
...
```

Her referans noktası, hem yazılım hem de fiziksel uygulama için bağımsız bir veri düğümüdür.

### 6.1 Referans Noktası Veri Alanları

| Alan | Açıklama |
|---|---|
| `point_id` | P0, P1, P2... |
| `distance_m` | Başlangıçtan uzaklık |
| `gps_coordinate` | RTK-GNSS koordinatı |
| `road_width` | Yol genişliği |
| `left_edge_position` | Sol kenar konumu |
| `right_edge_position` | Sağ kenar konumu |
| `lane_center_position` | Şerit merkezi |
| `center_line_allowed` | Orta çizgi uygulanabilir mi? |
| `edge_line_required` | Kenar çizgisi gerekiyor mu? |
| `line_type` | Uygulanacak çizgi tipi |
| `robot_target_y` | Robotun yanal hedefi |
| `gun_height` | Tabanca yüksekliği |
| `vehicle_speed` | Hedef hız |
| `paint_flow_rate` | Boya debisi |
| `glass_bead_flow_rate` | Cam küreciği debisi |
| `driver_command` | HUD komutu |
| `quality_status` | Uygulama sonrası kalite durumu |

---

## 7. Karar Kuralları

### 7.1 Dar Yol Senaryosu

```text
IF road_type = two_way
AND road_width < minimum_centerline_width
THEN center_line = False
AND edge_lines = True
```

Bu durumda sistem orta çizgi uygulamasını iptal eder ve yol güvenliği için kenar/omuz çizgilerine odaklanır.

### 7.2 Mevcut Çizgiyi Referans Alma

```text
IF existing_line = True
AND line_condition = good
THEN use_existing_line_as_reference = True
```

Bu durumda RMDE mevcut çizgiyi dijital yol modeline referans olarak dahil eder.

### 7.3 Kırık / Silinmiş Çizgi Tamamlama

```text
IF line_condition = broken
THEN estimate_reference_line_from_previous_and_next_segments = True
```

Sistem önceki ve sonraki segmentleri kullanarak eksik çizgi bölgesini tahmin eder.

### 7.4 Yeni Asfalt Senaryosu

```text
IF existing_line = False
AND road_surface = new_asphalt
THEN generate_new_digital_road_model = True
```

Bu durumda çizgi geometrisi doğrudan yol kenarları, şerit genişliği ve ülke standardına göre oluşturulur.

---

## 8. Robot Command Layer Entegrasyonu

RMDE, robot kola doğrudan basit aç/kapat komutu göndermez. Her 50 cm referans noktası için koordinat tabanlı, parametreli komut üretir.

### 8.1 Robot Komut Paketi

| Alan | Açıklama |
|---|---|
| `reference_point_id` | P numarası |
| `line_type` | Çizgi türü |
| `target_x` | Boyuna hedef |
| `target_y` | Yanal hedef |
| `target_z` | Tabanca yüksekliği |
| `wrist_angle` | Robot bilek açısı |
| `gun_start` | Boya başlangıç komutu |
| `gun_stop` | Boya bitiş komutu |
| `purge_position` | Temizlik pozisyonu |
| `safe_standby_pose` | Güvenli bekleme pozisyonu |

### 8.2 Robot Sistemiyle Bağlantılar

<div class="git-buttons">

[Git: Robot Kol + X/Y Kızak](05-robot-arm-xy-rail.md)
[Git: Yeni Nesil Termoplastik Tabanca](04-next-generation-thermoplastic-gun.md)
[Git: Yazılım: robot_command_layer.py](software/robot_command_layer.py)

</div>

---

## 9. PLC Process Interface Entegrasyonu

RMDE çizgi kararını üretir; PLC ise fiziksel prosesin güvenli şekilde uygulanmasını sağlar.

PLC'ye aktarılan ana parametreler:

- boya akışı aktif/pasif,
- tabanca ısıtma aktif/pasif,
- induction zone setpoint,
- purge sequence,
- atomizing air pressure,
- rotary bell speed setpoint,
- suction fan enable,
- emergency interlock,
- cam küreciği dozaj komutu.

<div class="git-buttons">

[Git: PLC ve Kontrol Sistemi](07-plc-control-system.md)
[Git: Yazılım: plc_process_interface.py](software/plc_process_interface.py)

</div>

---

## 10. HUD Guidance Entegrasyonu

RMDE'nin ürettiği yol modeli ve çizgi hedefleri sürücüye HUD üzerinden aktarılır.

HUD göstergeleri:

- yeşil hedef sürüş yolu,
- mavi ghost line,
- beyaz uygulanan çizgi,
- kırmızı sapma bölgesi,
- sarı yön düzeltme oku,
- hız komutu,
- yaklaşan çizgi sonu uyarısı,
- proses durumu.

Örnek komutlar:

```text
Alignment is correct. Maintain current path.
Make a slight right correction after five meters.
Reduce speed.
Approaching line end point.
Application will be terminated automatically.
```

<div class="git-buttons">

[Git: HUD ve Sürücü Rehberliği](09-hud-driver-guidance.md)
[Git: Yazılım: hud_guidance_system.py](software/hud_guidance_system.py)

</div>

---

## 11. Quality Feedback Loop

Kalite kontrol modülü, uygulama sonrası çizgiyi dijital referans modeliyle karşılaştırır.

Kontrol edilen parametreler:

- çizgi eni,
- çizgi kalınlığı,
- çizgi geometrisi,
- hizalama sapması,
- cam küreciği dağılımı,
- boya sıcaklığı,
- araç hızı,
- robot pozisyon doğruluğu,
- akış kararlılığı.

### 11.1 Hata Kaydı

```text
Error Type: Line deviation
Location: P420 – P438
Deviation: 6 cm
Recommended Correction: Robot calibration / vehicle speed correction
```

Bu geri bildirim şu sistemlere aktarılır:

- robot kalibrasyonu,
- RMDE karar parametreleri,
- PLC proses ayarları,
- sürücü rehberliği,
- kalite raporu.

<div class="git-buttons">

[Git: Kalite Kontrol Sistemi](10-quality-control-system.md)
[Git: Yazılım: quality_control_module.py](software/quality_control_module.py)

</div>

---

## 12. Standards Rule Engine Entegrasyonu

RMDE'nin standart doğrulama katmanı yalnızca Türkiye, ABD veya Hindistan ile sınırlı değildir. Sistem, ülke/bölge/proje bazlı veri tabloları üzerinden çalışmalıdır.

Desteklenecek standart kapsamı:

- Türkiye,
- Hindistan,
- Avrupa ülke alt standartları,
- Amerika Birleşik Devletleri,
- Körfez / GCC bölgesi,
- havaalanı pist ve apron işaretlemeleri,
- endüstriyel tesis işaretlemeleri,
- lojistik alanlar,
- AGV / robotik yönlendirme çizgileri,
- geçici trafik uygulamaları,
- tünel uygulamaları.

<div class="git-buttons">

[Git: Uluslararası Standart Motoru](11-international-standards-engine.md)
[Git: Yazılım: standards_rule_engine.py](software/standards_rule_engine.py)

</div>

---

## 13. Safety Supervisor

RMDE karar üretir, ancak güvenlik kararı safety supervisor ve PLC katmanı tarafından doğrulanmadan fiziksel proses çalıştırılmamalıdır.

Safety Supervisor izleme alanları:

- robot çalışma alanı,
- tabanca sıcaklığı,
- boya basıncı,
- hidrolik tahrik durumu,
- emiş sistemi durumu,
- acil stop hattı,
- yangın algılama,
- jeneratör ve elektrik güvenliği,
- insan/araç yakınlık algılama,
- robot çarpışma riski,
- yüksek sıcaklık bölgeleri.

<div class="git-buttons">

[Git: PLC ve Kontrol Sistemi](07-plc-control-system.md)
[Git: Yazılım: safety_supervisor.py](software/safety_supervisor.py)

</div>

---

## 14. Yazılım Dosya Ağacı

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
└── telemetry_logger.py
```

Bu dosyalar nihai ticari yazılım değildir. İlk aşamada sistem mimarisini, veri modellerini, karar zincirini ve modüller arası bağlantıları tanımlayan mühendislik çekirdeği olarak hazırlanmalıdır.

---

## 15. RMDE Veri Akış Diyagramı

```text
[Sensor Data]
     ↓
[Pre-Survey Module]
     ↓
[Road Classifier]
     ↓
[Standards Rule Engine]
     ↓
[Reference Point Generator]
     ↓
[RMDE Decision Engine]
     ↓
[Robot Command Layer] → [Industrial Robot + X/Y Rail]
     ↓
[PLC Process Interface] → [Paint / Heat / Air / Gun / Suction]
     ↓
[HUD Guidance]
     ↓
[Quality Control Module]
     ↓
[Adaptive Feedback]
```

---

## 16. Test ve Doğrulama Planı

### 16.1 Simülasyon Testi

- manuel yol genişliği girişi,
- şerit sayısı seçimi,
- ülke standardı seçimi,
- mevcut çizgi var/yok durumu,
- 50 cm referans noktası üretimi,
- robot komut listesinin oluşturulması.

### 16.2 Sensör Entegrasyon Testi

- kamera verisi,
- LiDAR verisi,
- RTK-GNSS doğruluğu,
- IMU eğim kompanzasyonu,
- yol kenarı algılama.

### 16.3 Robot Komut Testi

- P noktası hedef koordinatları,
- tabanca yüksekliği,
- bilek açısı,
- start/stop komutları,
- purge pozisyonu.

### 16.4 PLC Proses Testi

- boya akışı,
- indüksiyon sıcaklık setpoint,
- tabanca gövde ısıtması,
- rotary bell rpm,
- hava basıncı,
- emiş fanı,
- acil durdurma.

### 16.5 Kalite Geri Bildirim Testi

- çizgi eni ölçümü,
- çizgi kalınlık kontrolü,
- sapma ölçümü,
- referans nokta bazlı hata kaydı,
- düzeltme önerisi üretimi.

---

## 17. Git Kısa Yol Haritası

```text
[Git: Sistem Genel Akışı] → 01-system-flow.md
[Git: Yeni Nesil Termoplastik Tabanca] → 04-next-generation-thermoplastic-gun.md
[Git: Robot Kol + X/Y Kızak] → 05-robot-arm-xy-rail.md
[Git: PLC ve Kontrol Sistemi] → 07-plc-control-system.md
[Git: HUD ve Sürücü Rehberliği] → 09-hud-driver-guidance.md
[Git: Kalite Kontrol Sistemi] → 10-quality-control-system.md
[Git: Uluslararası Standart Motoru] → 11-international-standards-engine.md
[Git: Prototip BOM] → 12-prototype-bom.md
[Git: Yazılım Dosyaları] → 13-software-files.md
```

---

## 18. Teknik Sonuç

RMDE, ROMR platformunun yalnızca yazılım bölümü değil; mekanik uygulama, robotik hareket, termal proses, ülke standartları, PLC güvenliği, HUD rehberliği ve kalite kontrol zincirini birbirine bağlayan merkezi karar mimarisidir.

Bu nedenle RMDE olmadan sistem yalnızca mekanik bir çizgi makinesi olur. RMDE ile birlikte sistem:

- sayısal yol modeline dayalı,
- ülke standartlarına uyumlu,
- robotik olarak konumlandırılmış,
- PLC ile güvenli hale getirilmiş,
- HUD ile sürücüye rehberlik eden,
- kalite kontrol geri bildirimiyle kendini iyileştirebilen

entegre bir otonom yol çizgi uygulama platformuna dönüşür.
