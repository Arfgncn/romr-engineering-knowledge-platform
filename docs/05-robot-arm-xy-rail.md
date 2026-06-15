[05-robot-arm-xy-rail.md](https://github.com/user-attachments/files/28956115/05-robot-arm-xy-rail.md)
# 05 — Industrial Robotic Application System / Robot Arm + X/Y Rail

<div class="git-buttons">

[Git: Sistem Genel Akışı](01-system-flow.md)
[Git: Pellet Boya Sistemi](02-pellet-paint-system.md)
[Git: İndüksiyon Isıtma Sistemi](03-induction-heating-system.md)
[Git: Yeni Nesil Termoplastik Boya Tabancası](04-next-generation-thermoplastic-gun.md)
[Git: Güç ve Elektrik Mimarisi](06-power-electrical-architecture.md)
[Git: PLC ve Kontrol Sistemi](07-plc-control-system.md)
[Git: RMDE Yazılım Mimarisi](08-rmde-software-architecture.md)
[Git: Kalite Kontrol Sistemi](10-quality-control-system.md)
[Git: Prototip BOM](12-prototype-bom.md)
[Git: Yazılım Dosyaları](13-software-files.md)

</div>

---

## 1. Modülün Sistemdeki Rolü

Industrial Robotic Application System, ROMR platformunun fiziksel uygulama hareket merkezidir. Bu sistem, RMDE tarafından üretilen koordinatları, ülke standart kütüphanesinden gelen çizgi geometrilerini, PLC süreç izinlerini ve kalite kontrol geri bildirimlerini kullanarak termoplastik yol çizgisini asfalt yüzeyine uygular.

Bu modül yalnızca bir robot kol taşıyıcısı değildir. Aynı zamanda:

- yeni nesil dual-bell rotary thermoplastic paint gun sistemini taşır,
- ısıtılmış boya transfer hattını yönetir,
- son indüksiyon ısıtma bölümünü uygulama noktasına taşır,
- boya tozu emiş hortumunu taşır,
- hava, purge, sensör ve iletişim hatlarını üzerinde barındırır,
- RMDE komutlarını gerçek robot hareketine dönüştürür,
- tabanca yüksekliğini sabit tutar,
- titreşim ve darbe etkilerini mekanik ve yazılımsal olarak bastırır.

ROMR platformunda robotik sistem, klasik operatör kontrollü çizgi uygulama yaklaşımını koordinat kontrollü, sensör destekli ve kapalı döngü çalışan bir uygulama mimarisine dönüştürür.

---

## 2. Sistem Mimarisi

```text
Digital Road Model
↓
50 cm Reference Points
↓
RMDE Decision Engine
↓
Robot Command Layer
↓
PLC Permission / Safety Interlock
↓
Industrial Robot Controller
↓
X/Y Linear Rail + 6-Axis Robot
↓
Dual-Bell Rotary Thermoplastic Gun
↓
Road Marking Application
↓
Quality Control Feedback
```

Robotik sistem, RMDE tarafından üretilen her referans noktası için hedef konumu, hedef çizgi tipini, tabanca yüksekliğini, boya debisini, uygulama hızını ve başlangıç/bitiş komutlarını uygular.

---

## 3. Endüstriyel Robot Seçim Felsefesi

ROMR platformunda kullanılacak robot, hobi sınıfı veya hafif hizmet tipi bir robot kol olarak değerlendirilmemelidir. Sistem; yüksek sıcaklık, titreşim, ağır uç ekipman, ısıtılmış boya hattı, emiş hortumu ve sürekli saha operasyonu altında çalışacak endüstriyel sınıf bir robot mimarisi gerektirir.

### 3.1 Tercih Edilen Referans Platform

```text
Preferred Reference Platform:
KUKA KR Series Industrial Robot
```

### 3.2 Alternatif Endüstriyel Robot Platformları

```text
Alternative Platforms:
ABB IRB Series
FANUC M-Series
Yaskawa Motoman Series
```

KUKA KR serisi referans platform olarak belirtilir; ancak nihai marka seçimi prototip mühendisliği, tedarik, servis ağı, kontrol entegrasyonu ve yük hesabına göre üretici firma tarafından doğrulanmalıdır.

---

## 4. Robot Taşıma Kapasitesi ve Uç Yük Analizi

Robot kol yalnızca boya tabancasını taşımayacaktır. Robot bileği ve kol hattı üzerinde sıcak boya hattı, indüksiyon destekli son ısıtma bölümü, hava hatları, purge hattı, boya tozu emiş hortumu, sensör kablo demeti ve mekanik adaptörler de bulunacaktır.

### 4.1 Tahmini Uç Yük Dağılımı

| Bileşen | Tahmini Ağırlık |
|---|---:|
| Dual-bell rotary thermoplastic paint gun | 8–12 kg |
| Rotary / hydraulic drive system | 3–5 kg |
| Final induction heating section | 3–6 kg |
| Heated paint transfer line with material inside | 2–4 kg |
| Atomizing air / purge / cleaning lines | 1–2 kg |
| Paint dust extraction hose and capture ring | 2–4 kg |
| Sensors and wiring harness | 1–2 kg |
| Robot wrist adapter / mechanical bracket | 2–4 kg |

### 4.2 Estimated Total Payload

```text
Estimated active payload: 22–39 kg
```

Bu hesap yalnızca statik uç yükü temsil eder. Gerçek robot seçiminde:

- dinamik hareket yükleri,
- ivmelenme etkileri,
- hortum sürükleme kuvvetleri,
- sıcak boya hattının rijitliği,
- tabanca titreşimi,
- acil duruş momentleri,
- güvenlik katsayısı

dikkate alınmalıdır.

### 4.3 Önerilen Robot Sınıfı

| Parametre | Öneri |
|---|---|
| Minimum payload | 50 kg |
| Tercih edilen payload aralığı | 50–70 kg |
| Eksen sayısı | 6 eksen |
| Robot sınıfı | Endüstriyel manipülatör |
| Referans marka sınıfı | KUKA KR / ABB IRB / FANUC M / Yaskawa Motoman |
| Çalışma tipi | Sürekli saha operasyonu |
| Entegrasyon | PLC + robot controller + RMDE |

50 kg altındaki robotlar, tabanca ve servis hatlarını taşısa bile dinamik güvenlik payı açısından yetersiz kalabilir. Bu nedenle sistemin 50–70 kg payload aralığında endüstriyel robot sınıfında değerlendirilmesi önerilir.

---

## 5. Robot Üzerinde Taşınacak Entegre Servis Hatları

Robot kol, yalnızca mekanik bir taşıyıcı değil; uygulama uç ekipmanına enerji, boya, hava, sensör ve güvenlik bağlantılarını ulaştıran entegre bir servis taşıyıcıdır.

```text
Robot Arm Integrated Services
│
├── Heated Paint Transfer Line
├── Final Induction Heating Section
├── Dual-Bell Rotary Thermoplastic Gun
├── Atomizing Air Line
├── Purge / Cleaning Line
├── Paint Dust Extraction Hose
├── Gun Height Sensor Cable
├── Temperature / Pressure Sensor Harness
├── Industrial Ethernet / Fieldbus Line
└── Emergency Stop / Safety Circuit
```

Bu hatlar robot hareketini engellemeyecek şekilde:

- endüstriyel kablo taşıyıcılarla,
- yüksek sıcaklığa dayanıklı hortumlarla,
- esnek ama kontrollü yönlendirme elemanlarıyla,
- titreşimden etkilenmeyecek bağlantı noktalarıyla,
- kolay sökülebilir bakım bağlantılarıyla

tasarlanmalıdır.

---

## 6. X-Ekseni Lineer Ray Sistemi

X ekseni lineer ray sistemi, robotun araç şasisi üzerinde ileri-geri hareket etmesini sağlar.

### 6.1 Görevleri

- robotun çalışma alanını uzatmak,
- uzun kesintisiz çizgi uygulamasını desteklemek,
- robot kolun sürekli maksimum erişim sınırında çalışmasını önlemek,
- tabancanın hedef uygulama bölgesinde daha stabil kalmasını sağlamak,
- farklı çizgi başlangıç/bitiş pozisyonlarına otomatik geçiş sağlamak.

### 6.2 Teknik Gereksinimler

| Gereksinim | Açıklama |
|---|---|
| Taşıma kapasitesi | Robot + end-effector + servis hatları toplam yükü |
| Rijitlik | Robot hassasiyetini bozmayacak şasi bağlantısı |
| Koruma | Toz, sıcaklık, titreşim ve saha koşullarına dayanım |
| Sürücü sistemi | Servo motor / endüstriyel lineer hareket tahriki |
| Geri bildirim | Encoder veya lineer cetvel |
| Güvenlik | Limit switch, safe zone, mechanical stop |

---

## 7. Y-Ekseni Lineer Ray Sistemi

Y ekseni lineer ray sistemi, robotun sağ-sol ofset düzeltmesi yapmasını sağlar.

### 7.1 Görevleri

- omuz çizgisi uygulaması,
- orta çizgi uygulaması,
- şerit çizgisi uygulaması,
- yol genişliği değişimlerine uyum,
- RMDE tarafından verilen lateral hedeflerin uygulanması,
- robot kolun daha küçük hareketlerle daha hassas pozisyon alması.

Y ekseni, RMDE'nin hesapladığı çizgi konumunu robotun erişim alanı içinde optimum noktaya taşır.

---

## 8. Sabit Tabanca Yüksekliği Kontrol Sistemi

Uygulama sırasında tabanca ile asfalt yüzeyi arasındaki mesafe sabit tutulmalıdır. Bu mesafe değişirse çizgi eni, boya dağılımı, kenar geometrisi ve tabanca püskürtme karakteristiği bozulabilir.

### 8.1 Gerekli Sensörler

```text
Laser Distance Sensor
LiDAR / Road Profile Sensor
Robot Wrist Position Feedback
IMU / Vibration Data
Quality Camera Feedback
```

### 8.2 Kontrol Prensibi

```text
Road surface height measurement
↓
Nozzle height error calculation
↓
Robot Z / wrist correction
↓
PLC safety permission
↓
Continuous height stabilization
```

### 8.3 Hedef Hassasiyet

| Parametre | Hedef |
|---|---|
| Nozzle height deviation | ±5 mm hedef sınıfı |
| Correction type | Continuous / dynamic |
| Feedback source | Distance sensor + robot feedback |
| Safety action | height fault alarm / stop marking |

Bu değer nihai prototip testleriyle doğrulanmalıdır.

---

## 9. Titreşim ve Darbe Kompanzasyon Sistemi

Araç saha koşullarında çalışırken şasi üzerinde titreşimler, yol birleşimleri, çukur etkileri, kasisler ve ani salınımlar oluşabilir. Bu etkiler doğrudan tabanca ucuna aktarılırsa çizgi geometrisi bozulur.

### 9.1 Titreşim Kaynakları

- yol yüzeyi düzensizlikleri,
- şasi burulması,
- jeneratör titreşimi,
- kompresör titreşimi,
- robot ray hareketi,
- ani frenleme / hız değişimi,
- sıcak boya hattı ve hortum hareketi.

### 9.2 Kompanzasyon Yaklaşımı

```text
Mechanical vibration isolation
+
Robot motion filtering
+
IMU / vibration sensor feedback
+
Nozzle height sensor correction
+
Quality control feedback
```

### 9.3 Güvenlik Davranışı

Aşırı darbe veya yükseklik sapması algılanırsa:

```text
Paint flow disabled
↓
Gun lifted to safe height
↓
Robot moves to standby pose
↓
Error logged by quality control module
↓
Operator receives HUD / HMI warning
```

---

## 10. Boya Tozu Emiş Sistemi Entegrasyonu

Yeni nesil rotary bell tabancada uygulama bölgesinde oluşabilecek ince boya tozları ve partiküller robot kol ile birlikte hareket eden emiş sistemiyle toplanacaktır.

### 10.1 Sistem Akışı

```text
Dual-Bell Spray Zone
↓
Capture Ring / Suction Mouth
↓
Flexible Extraction Hose on Robot Arm
↓
Industrial Jet Fan
↓
Dust Separator
↓
Under-Truck Collection Tank
```

### 10.2 Amaçlar

- robot kolun kirlenmesini azaltmak,
- kalite kontrol kameralarının görüşünü korumak,
- sensör yüzeylerinde boya birikmesini azaltmak,
- çevresel partikül yayılımını düşürmek,
- uygulama bölgesini daha temiz tutmak.

### 10.3 Robot Hareketine Etkisi

Emiş hortumu robot hareketinde ek sürükleme kuvveti oluşturacağı için robot seçimi ve payload hesabında dikkate alınmalıdır. Hortum güzergâhı robot hareketini sınırlamayacak şekilde kablo taşıyıcı veya özel hortum yönlendirme sistemi ile planlanmalıdır.

---

## 11. RMDE Entegrasyonu

Robotik sistemin hareketleri RMDE tarafından üretilen 50 cm referans noktalarıyla ilişkilidir.

### 11.1 RMDE'den Gelen Veriler

| Veri | Robotik Kullanım |
|---|---|
| Reference Point ID | hareket komutunun dijital düğümü |
| Start coordinate | çizgi başlangıç noktası |
| End coordinate | çizgi bitiş noktası |
| Robot target Y | lateral robot hedefi |
| Line type | sürekli / kesikli / kenar / merkez çizgi |
| Line width | tabanca / debi / hız ayarı |
| Thickness | boya debisi ve hız koordinasyonu |
| Vehicle speed | robot hareket zamanlaması |
| Paint flow rate | PLC ile akış senkronizasyonu |
| Driver command | HUD ve uygulama kontrolü |

### 11.2 Komut Zinciri

```text
RMDE Decision Engine
↓
Reference Point Command List
↓
Robot Command Layer
↓
Industrial Robot Controller
↓
Robot + X/Y Rail Motion
↓
Paint Gun Application
```

Robot doğrudan “çizgi çiz” komutu almaz. Her hareket, referans noktası, çizgi standardı, tabanca yüksekliği, boya debisi ve kalite toleransı ile ilişkilendirilmiş komutlar üzerinden çalışır.

---

## 12. PLC Entegrasyonu

PLC, robot hareketine uygulama izni veren, boya akışı ve güvenliği senkronize eden ana saha kontrol katmanıdır.

### 12.1 PLC'den Robota Giden Sinyaller

| Sinyal | Tip | Açıklama |
|---|---|---|
| robot_motion_enable | digital output | Robot hareket izni |
| application_enable | digital output | Boya uygulama izni |
| gun_ready | digital output | Tabanca sıcaklık ve basınç hazır bilgisi |
| purge_position_request | digital output | Temizlik pozisyonu talebi |
| emergency_stop | safety signal | Acil durdurma |
| safe_zone_clear | safety signal | Robot alanı güvenli |

### 12.2 Robottan PLC'ye Gelen Sinyaller

| Sinyal | Tip | Açıklama |
|---|---|---|
| robot_in_position | digital input | Robot hedef pozisyonda |
| robot_fault | digital input | Robot arızası |
| robot_safe_pose | digital input | Güvenli bekleme pozisyonu |
| gun_height_actual | analog input | Gerçek tabanca yüksekliği |
| rail_position_x | analog / fieldbus | X ray pozisyonu |
| rail_position_y | analog / fieldbus | Y ray pozisyonu |
| collision_detected | safety input | Çarpışma / darbe algısı |

---

## 13. Sensör Mimarisi

Robotik uygulama sistemi aşağıdaki sensörlerle desteklenmelidir:

| Sensör | Görev |
|---|---|
| Robot encoder feedback | eksen konumu ve hareket doğrulama |
| Linear rail encoder | X/Y ray pozisyonu |
| Laser distance sensor | tabanca-yol yüksekliği |
| LiDAR / road profile sensor | yol yüzeyi ve geometri izleme |
| IMU / vibration sensor | şasi ve robot titreşimi |
| Gun body temperature sensor | tabanca sıcaklığı |
| Paint pressure sensor | tabanca öncesi boya basıncı |
| Air pressure sensor | atomize / stabilizasyon havası |
| Vacuum sensor | toz emiş hattı kontrolü |
| Quality camera | çizgi eni, kenar ve sapma analizi |

---

## 14. Güvenlik Sistemi

Robotik sistem yüksek sıcaklık, hareketli mekanik yapı, boya basıncı, hava basıncı ve saha personeli riski içerdiği için safety layer zorunludur.

### 14.1 Zorunlu Güvenlik Fonksiyonları

- emergency stop,
- robot safe zone monitoring,
- collision detection,
- overtemperature shutdown,
- overpressure shutdown,
- rail limit protection,
- cable/hose strain monitoring,
- gun safe lift position,
- maintenance lockout mode.

### 14.2 Güvenli Davranış

```text
Fault detected
↓
Paint flow disabled
↓
Robot motion stopped or slowed
↓
Gun lifted to safe height
↓
Induction gun heating reduced or disabled
↓
Alarm sent to HMI / HUD
↓
Fault logged
```

---

## 15. Robot Komut Katmanı

Robot hareketlerinin yazılım tarafındaki ana dosyası:

```text
robot_command_layer.py
```

### 15.1 Görevleri

- RMDE referans noktalarını robot hareket komutlarına dönüştürmek,
- X/Y ray pozisyonlarını hesaplamak,
- robot bilek pozisyonunu belirlemek,
- tabanca yüksekliğini korumak,
- çizgi başlangıç/bitiş hareketlerini yönetmek,
- purge ve cleaning pozisyonlarını yürütmek,
- kalite kontrol düzeltmelerini robota aktarmak.

### 15.2 Bağlı Yazılım Dosyaları

```text
rmde_decision_engine.py
reference_point_generator.py
plc_process_interface.py
quality_control_module.py
safety_supervisor.py
telemetry_logger.py
```

---

## 16. Robotik Sistem BOM

| Kategori | Bileşen |
|---|---|
| Robot | 6 eksenli endüstriyel robot kol |
| Referans robot sınıfı | KUKA KR series industrial robot |
| Alternatif robot sınıfı | ABB IRB / FANUC M / Yaskawa Motoman |
| Taşıma kapasitesi | minimum 50 kg, önerilen 50–70 kg |
| Ray sistemi | X ekseni lineer ray |
| Ray sistemi | Y ekseni lineer ray |
| Tahrik | servo motor / endüstriyel lineer tahrik |
| Geri bildirim | encoder / lineer cetvel |
| End-effector | dual-bell rotary thermoplastic gun |
| Bağlantı | robot bilek adaptörü |
| Isıtma | son indüksiyon ısıtma bölümü |
| Boya hattı | yüksek sıcaklık boya transfer hattı |
| Hava hattı | atomizing air / purge line |
| Emiş | boya tozu emiş hortumu |
| Kablo taşıma | endüstriyel kablo taşıyıcı |
| Sensör | laser distance / height sensor |
| Sensör | IMU / vibration sensor |
| Sensör | pressure / temperature / vacuum sensors |
| Güvenlik | safe zone sensor / E-stop / collision detection |

---

## 17. Test ve Doğrulama Planı

### 17.1 Mekanik Doğrulama

- robot payload doğrulaması,
- X/Y ray rijitlik testi,
- kablo/hortum hareket testi,
- tabanca bilek adaptörü yük testi,
- titreşim izolasyon testi.

### 17.2 Hareket Doğrulama

- sabit yükseklik testi,
- düz çizgi takip testi,
- kesikli çizgi başlangıç/bitiş testi,
- lateral ofset geçiş testi,
- robot + araç hızı senkronizasyon testi.

### 17.3 Süreç Doğrulama

- boya akışı ile robot hareket senkronizasyonu,
- tabanca sıcaklığı ile robot hareket uyumu,
- emiş hortumu performansı,
- purge / cleaning pozisyon testi,
- hata durumunda safe pose testi.

---

## 18. Git Kısa Yol Haritası

```text
[Git: Sistem Genel Akışı] → 01-system-flow.md
[Git: Pellet Boya Sistemi] → 02-pellet-paint-system.md
[Git: İndüksiyon Isıtma Sistemi] → 03-induction-heating-system.md
[Git: Yeni Nesil Termoplastik Boya Tabancası] → 04-next-generation-thermoplastic-gun.md
[Git: Güç ve Elektrik Mimarisi] → 06-power-electrical-architecture.md
[Git: PLC ve Kontrol Sistemi] → 07-plc-control-system.md
[Git: RMDE Yazılım Mimarisi] → 08-rmde-software-architecture.md
[Git: Kalite Kontrol Sistemi] → 10-quality-control-system.md
[Git: Prototip BOM] → 12-prototype-bom.md
[Git: Yazılım Dosyaları] → 13-software-files.md
```

---

## 19. Teknik Sonuç

Industrial Robotic Application System, ROMR platformunda tabanca, indüksiyon hattı, toz emiş sistemi, RMDE, PLC ve kalite kontrol mimarilerini fiziksel uygulamada birleştiren ana hareket katmanıdır.

Bu sistemin endüstriyel sınıfta tasarlanması zorunludur. Robot kolun üzerinde yalnızca bir boya tabancası değil; sıcak boya hattı, son indüksiyon ısıtma bölümü, hava hatları, purge hattı, toz emiş hortumu, sensörler ve güvenlik bağlantıları bulunacaktır.

Bu nedenle tercih edilen robot sınıfı minimum 50 kg taşıma kapasiteli, tercihen 50–70 kg payload aralığında, KUKA KR serisi veya eşdeğer ABB / FANUC / Yaskawa endüstriyel robot sınıfıdır.

Robotik sistem, ROMR platformunu klasik operatör bağımlı yol çizgi makinesinden; koordinat kontrollü, sensör destekli, RMDE yönlendirmeli ve kalite geri bildirimiyle çalışan robotik uygulama sistemine dönüştüren temel modüldür.
