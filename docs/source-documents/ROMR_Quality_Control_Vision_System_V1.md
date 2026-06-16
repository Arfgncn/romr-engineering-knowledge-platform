# ROMR Quality Control & Vision Feedback System V1

> Source technical module for the ROMR Engineering Knowledge Platform.

# 10 — Quality Control & Vision Feedback System

<div class="git-buttons">

[Git: Sistem Genel Akışı](01-system-flow.md)
[Git: RMDE Yazılım Mimarisi](08-rmde-software-architecture.md)
[Git: Robot Kol + X/Y Kızak](05-robot-arm-xy-rail.md)
[Git: Yeni Nesil Termoplastik Tabanca](04-next-generation-thermoplastic-gun.md)
[Git: PLC ve Kontrol Sistemi](07-plc-control-system.md)
[Git: Uluslararası Standart Motoru](11-international-standards-engine.md)
[Git: Prototip BOM](12-prototype-bom.md)
[Git: Yazılım Dosyaları](13-software-files.md)

</div>

---

## 1. Modülün Sistemdeki Rolü

Quality Control & Vision Feedback System, ROMR platformunun uygulama sonrası doğrulama ve kapalı döngü geri bildirim katmanıdır.

Bu sistemin amacı, uygulanan yol çizgisini sadece operatör gözüyle kontrol etmek değil; kamera, sensör, referans nokta kayıtları, RMDE kararları ve ülke standartları ile karşılaştırarak ölçülebilir kalite verisi üretmektir.

Bu modül sayesinde sistem çizgi eni doğruluğunu, hizalama sapmasını, çizgi sürekliliğini, başlangıç/bitiş geometrisini, cam küreciği dağılımını, robot hareket doğruluğunu, sıcaklık/akış/hız verilerini ve referans nokta bazlı hata haritasını yönetir.

---

## 2. Ana Kalite Kontrol Akışı

```text
RMDE Reference Points
↓
Applied Road Marking
↓
Rear / Side Vision Cameras
↓
Line Geometry Measurement
↓
Thickness / Material Estimation
↓
Glass Bead Distribution Check
↓
Deviation Analysis
↓
Standards Tolerance Comparison
↓
Reference Point Error Logging
↓
Robot / PLC / RMDE Feedback
↓
Digital Quality Report
```

---

## 3. Kalite Kontrol Donanım Katmanı

| Donanım | Görev |
|---|---|
| Arka kalite kontrol kamerası | Uygulanan çizgiyi araç geçtikten sonra izler |
| Robot bölgesi kamerası | Tabanca çıkışı ve uygulama anını gözlemler |
| Yan kamera / line scan kamera | Çizgi kenarlarını ve hizalamayı ölçer |
| Nozzle height sensor | Tabanca-yol mesafesini kaydeder |
| Boya sıcaklık sensörleri | Uygulama sıcaklığını kaliteyle ilişkilendirir |
| Boya basınç sensörü | Akış sürekliliği ve tıkanma riskini izler |
| Boya debi sensörü | Gerçek boya sarfiyatını doğrular |
| Cam küreciği debi sensörü | Bead uygulama miktarını izler |
| Robot pozisyon geri bildirimi | Gerçek robot hedef sapmasını hesaplar |
| RTK-GNSS / IMU | Yol konumu ve araç hareketini kalite kaydına bağlar |
| Aydınlatma sistemi | Gece ve düşük görünürlük kalite görüntüsü sağlar |

---

## 4. Ölçülecek Kalite Parametreleri

| Parametre | Açıklama |
|---|---|
| Line width accuracy | Çizgi eninin hedef standarda uygunluğu |
| Line thickness estimation | Et kalınlığının hedef değere yakınlığı |
| Alignment deviation | Çizginin referans yoldan sapması |
| Edge sharpness | Çizgi kenar düzgünlüğü |
| Continuity | Kesinti, kırılma, kopukluk kontrolü |
| Start / finish geometry | Çizgi başlangıç ve bitiş formu |
| Glass bead distribution | Cam küreciği dağılımı |
| Color consistency | Renk ve yüzey bütünlüğü |
| Paint temperature stability | Sıcaklık dalgalanması |
| Flow stability | Boya akış kararlılığı |
| Vehicle speed stability | Uygulama hızı değişimleri |
| Robot precision | Robot hedef koordinat doğruluğu |

---

## 5. Referans Nokta Bazlı Kalite Analizi

ROMR sistemi, kalite kontrolü her 50 cm referans noktasıyla eşleştirir.

```text
P420
Target line width: 14 cm
Measured line width: 13.2 cm
Alignment error: 2.1 cm
Paint temperature: 214°C
Vehicle speed: 5.1 km/h
Quality status: OK
```

Örnek hata kaydı:

```text
Error Type: Line deviation
Location: P420 – P438
Deviation Value: 6 cm
Recommended Correction:
- Robot calibration check
- Vehicle speed correction
- Nozzle height verification
```

---

## 6. Kamera Tabanlı Görüntü İşleme Mantığı

```text
Image Capture
↓
Perspective Correction
↓
Road Surface Segmentation
↓
Line Edge Detection
↓
Width Measurement
↓
Continuity Check
↓
Color / Contrast Check
↓
Reference Point Matching
↓
Tolerance Evaluation
↓
Error Logging
```

İlk prototipte kural tabanlı görüntü işleme kullanılabilir. Sonraki aşamada AI destekli kalite sınıflandırma ve otomatik hata tipi tanıma eklenebilir.

---

## 7. Çizgi Eni Ölçüm Sistemi

Çizgi eni ölçümü, ülke standart motorundan gelen hedef değerle karşılaştırılır.

```text
Country: Türkiye
Road type: Urban road
Target width: 14 cm
Measured width: 13.1 cm
Tolerance: ±1 cm
Result: OK
```

---

## 8. Çizgi Kalınlığı / Malzeme Miktarı Doğrulaması

Gerçek saha koşullarında çizgi kalınlığını doğrudan sürekli ölçmek zor olabilir. İlk prototipte et kalınlığı şu verilerden tahmin edilebilir:

- boya debisi,
- araç hızı,
- çizgi eni,
- boya yoğunluğu,
- tabanca çıkış geometrisi,
- sıcaklık ve viskozite,
- uygulama süresi.

---

## 9. Cam Küreciği Dağılım Kontrolü

Kontrol edilecek veriler:

- cam küreciği debisi,
- bead dağıtıcı çalışma durumu,
- çizgi üzerine düşme alanı,
- görsel yoğunluk,
- yüzey homojenliği,
- retroreflectivity beklentisi.

İleri aşamada retroreflectometer entegrasyonu yapılabilir. İlk prototipte kamera + debi + saha numunesi yaklaşımı kullanılabilir.

---

## 10. Robot / PLC / RMDE Geri Bildirim Zinciri

| Hata | Önerilen Düzeltme |
|---|---|
| Yanal sapma | Robot Y-offset kalibrasyonu |
| Genişlik düşük | Boya debisi / tabanca hızı / araç hızı kontrolü |
| Genişlik fazla | Debi azaltma veya hız artırma |
| Kenar bozuk | Tabanca yüksekliği / bell rpm / hava basıncı kontrolü |
| Çizgi kopuk | Boya basıncı, tıkanma, sıcaklık kontrolü |
| Başlangıç bozuk | Robot start timing / gun enable timing düzeltmesi |
| Bitiş bozuk | Stop timing / purge sequence kontrolü |

Kalite modülü PLC’ye doğrudan acil komut göndermemelidir; kalite durumunu proses kontrol katmanına bildirir.

---

## 11. Kalite Raporu Formatı

```text
Project ID
Road Segment ID
Country Standard
Total Marking Length
Average Line Width
Average Alignment Error
Out-of-Tolerance Segments
Temperature Stability
Flow Stability
Robot Precision
Glass Bead Status
Recommended Corrections
Digital Quality Map
```

---

## 12. Yazılım Bağlantıları

```text
quality_control_module.py
telemetry_logger.py
rmde_decision_engine.py
reference_point_generator.py
robot_command_layer.py
plc_process_interface.py
standards_rule_engine.py
```

<div class="git-buttons">

[Git: Yazılım: quality_control_module.py](software/quality_control_module.py)
[Git: Yazılım: telemetry_logger.py](software/telemetry_logger.py)
[Git: RMDE Yazılım Mimarisi](08-rmde-software-architecture.md)

</div>

---

## 13. Kalite Kontrol Test Planı

### 13.1 Statik Görüntü Testi

- çizgi görseli alınır,
- kenar algılama yapılır,
- çizgi eni ölçülür,
- toleransla karşılaştırılır.

### 13.2 Hareketli Uygulama Testi

- araç 5 km/h hızda ilerler,
- tabanca aktif çalışır,
- kalite kamerası çizgiyi kaydeder,
- referans noktalarla eşleşme yapılır.

### 13.3 Hata Senaryosu Testi

- düşük boya debisi,
- fazla hız,
- tabanca yüksekliği sapması,
- sıcaklık düşüşü,
- robot yanal sapma.

### 13.4 Kapalı Döngü Testi

- kalite hatası algılanır,
- düzeltme önerisi üretilir,
- robot / PLC parametreleri revize edilir,
- yeni uygulama sonucu karşılaştırılır.

---

## 14. Git Kısa Yol Haritası

```text
[Git: Sistem Genel Akışı] → 01-system-flow.md
[Git: RMDE Yazılım Mimarisi] → 08-rmde-software-architecture.md
[Git: Robot Kol + X/Y Kızak] → 05-robot-arm-xy-rail.md
[Git: Yeni Nesil Termoplastik Tabanca] → 04-next-generation-thermoplastic-gun.md
[Git: PLC ve Kontrol Sistemi] → 07-plc-control-system.md
[Git: Uluslararası Standart Motoru] → 11-international-standards-engine.md
[Git: Prototip BOM] → 12-prototype-bom.md
[Git: Yazılım Dosyaları] → 13-software-files.md
[Git: Source Document] → source-documents/ROMR_Quality_Control_Vision_System_V1.md
```

---

## 15. Teknik Sonuç

Quality Control & Vision Feedback System, ROMR platformunun uygulama doğruluğunu ölçülebilir, izlenebilir ve geliştirilebilir hale getiren ana doğrulama katmanıdır.

Bu modül; çizgi kalitesini referans nokta bazlı ölçer, standart motorundan gelen toleransları kullanır, RMDE kararlarını saha sonucuyla karşılaştırır, robot ve PLC proseslerine düzeltme önerisi üretir, uygulama sonrası dijital kalite raporu oluşturur ve gelecekte AI tabanlı kalite öğrenmesi için veri üretir.
