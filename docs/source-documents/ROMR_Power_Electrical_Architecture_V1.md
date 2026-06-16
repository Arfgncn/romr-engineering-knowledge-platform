# ROMR Power & Electrical Architecture V1

> Source technical module for the ROMR Engineering Knowledge Platform.

# 06 — Power & Electrical Architecture

<div class="git-buttons">

[Git: Sistem Genel Akışı](01-system-flow.md)
[Git: Pellet Boya Sistemi](02-pellet-paint-system.md)
[Git: İndüksiyon Isıtma Sistemi](03-induction-heating-system.md)
[Git: Yeni Nesil Termoplastik Tabanca](04-next-generation-thermoplastic-gun.md)
[Git: Robot Kol + X/Y Kızak](05-robot-arm-xy-rail.md)
[Git: PLC ve Kontrol Sistemi](07-plc-control-system.md)
[Git: RMDE Yazılım Mimarisi](08-rmde-software-architecture.md)
[Git: Prototip BOM](12-prototype-bom.md)

</div>

---

## 1. Modülün Sistemdeki Rolü

Power & Electrical Architecture, ROMR platformundaki tüm yüksek güç, düşük güç, kontrol, haberleşme, güvenlik ve yardımcı sistem beslemelerini düzenleyen enerji omurgasıdır.

Bu modülün temel amacı:

- türbin jeneratör gücünü güvenli şekilde dağıtmak,
- indüksiyon ısıtma sisteminin yüksek güçlü yüklerini yönetmek,
- robot, PLC, AI bilgisayarı, sensörler ve HUD sistemlerini temiz ve kararlı beslemek,
- yüksek güçlü hatlarla hassas sinyal hatlarını birbirinden ayırmak,
- yük önceliği ve güvenli kapatma mantığını tanımlamak,
- bakım ve hata teşhis erişimini kolaylaştırmaktır.

---

## 2. Ana Enerji Akışı

```text
Turbine Generator System
↓
Main AC Distribution Panel
↓
Power Protection and Load Management
↓
High-Power Bus
    ├── Induction Heating Inverters
    ├── Compressor System
    ├── Robot Controller / X-Y Rail Drives
    └── Auxiliary High-Power Loads
↓
Control Power Supplies
    ├── PLC / Safety PLC
    ├── AI Computer
    ├── Sensors
    ├── HMI / HUD
    └── Communication Network
```

---

## 3. Jeneratör Mimarisi

Prototip referans mimaride 2 × 180 kW türbin jeneratör sistemi değerlendirilmiştir. Toplam nominal güç 360 kW seviyesindedir.

Bu değer, nihai doğrulama yapılmadan kesin ihtiyaç olarak kabul edilmemelidir. Özellikle boya debisi, indüksiyon ısıtma yükü, kompresör tüketimi, robot gücü, yardımcı sistemler ve eşzamanlı yük profili birlikte hesaplanmalıdır.

### 3.1 Referans Jeneratör Yapısı

| Bileşen | Referans |
|---|---|
| Jeneratör adedi | 2 |
| Birim güç | 180 kW |
| Toplam nominal güç | 360 kW |
| Çıkış | 400–480 VAC, 3 faz |
| Kullanım | indüksiyon + robot + kompresör + yardımcı sistemler |
| Not | nihai güç ihtiyacı termal hesapla doğrulanmalı |

### 3.2 Alternatif Değerlendirme

Prototip aşamasında aşağıdaki alternatifler ayrıca incelenmelidir:

- tek büyük jeneratör,
- iki paralel jeneratör,
- türbin jeneratör + batarya tampon sistemi,
- indüksiyon yükleri için ayrı güç hattı,
- robot/PLC/sensörler için izole yardımcı güç hattı.

---

## 4. Ana Elektrik Panosu

Ana elektrik panosu, jeneratör çıkışını güvenli şekilde dağıtan merkezdir.

İçermesi gereken ana bileşenler:

- ana şalter,
- jeneratör giriş korumaları,
- faz koruma rölesi,
- aşırı akım koruması,
- kaçak akım / izolasyon izleme,
- yük kontaktörleri,
- motor koruma şalterleri,
- indüksiyon inverter beslemeleri,
- robot kontrolcü beslemesi,
- kompresör beslemesi,
- PLC ve kontrol besleme güç kaynakları,
- acil durdurma ile kesilecek güç hatları,
- servis ve bakım güvenlik kilitleri.

---

## 5. Yük Önceliklendirme Mantığı

ROMR platformunda tüm yükler aynı öncelikte değildir. Güvenlik ve kontrol sistemleri her zaman birinci öncelikte olmalıdır.

```text
Priority 1 — Safety PLC, emergency stop, fire detection
Priority 2 — Main PLC, sensors, communication, HMI/HUD
Priority 3 — RMDE computer and data systems
Priority 4 — Robot controller and X/Y rail drives
Priority 5 — Paint pump, glass bead dosing, compressor
Priority 6 — Induction heating inverters
Priority 7 — Auxiliary service loads
```

Yük aşımı veya jeneratör alarmında sistem aşağıdaki sırayla güvenli duruma geçmelidir:

```text
Disable paint flow
↓
Disable robot application motion
↓
Maintain safe heat if required
↓
Stop induction heating
↓
Keep PLC / safety / alarm systems alive
↓
Move to safe shutdown
```

---

## 6. İndüksiyon Güç Beslemesi

İndüksiyon ısıtma sistemi, platformun en yüksek ve en hassas güç tüketicilerinden biridir.

İndüksiyon mimarisinde aşağıdaki prensipler kullanılmalıdır:

- her ısıtma bölgesi için ayrı inverter veya kontrollü güç çıkışı,
- ayrı sigorta ve kontaktör koruması,
- sıcaklık sensörü geri bildirimi,
- PLC PID kontrolü,
- aşırı sıcaklık güvenlik rölesi,
- EMI/EMC filtreleme,
- hassas sinyal kablolarından fiziksel ayrım,
- soğutma ve havalandırma kontrolü.

### 6.1 İndüksiyon Zone Besleme Yapısı

```text
Main AC Bus
↓
Induction Protection Group
↓
Zone Inverter 1
Zone Inverter 2
Zone Inverter 3
Zone Inverter 4
Zone Inverter 5
↓
Induction Coils
↓
Temperature Feedback to PLC
```

---

## 7. Robot ve X/Y Ray Beslemesi

Endüstriyel robot ve lineer ray sistemi ayrı korumalı güç hattından beslenmelidir.

Gereksinimler:

- robot kontrolcü için izole güç çıkışı,
- X/Y ray servo sürücüler için ayrı koruma,
- robot güvenlik devresi,
- fren kontrolü,
- encoder ve haberleşme kablo ayrımı,
- acil stop ile kontrollü duruş,
- mekanik limit switch bağlantıları.

Robotun üzerinde taşınacak boya hattı, indüksiyon son bölümü, emiş hortumu ve sensör kabloları nedeniyle kablo/hortum taşıyıcı zincir sistemi enerji mimarisinin parçası olarak düşünülmelidir.

---

## 8. PLC, Safety PLC ve Kontrol Gücü

PLC ve safety PLC, yüksek güçlü yüklerden bağımsız ve kararlı düşük voltaj beslemeyle çalışmalıdır.

Önerilen kontrol beslemeleri:

| Hat | Kullanım |
|---|---|
| 24 VDC Safety | Safety PLC, E-stop, güvenlik röleleri |
| 24 VDC Control | PLC I/O, sensörler, valfler |
| 12 VDC / 24 VDC auxiliary | kameralar, küçük elektronikler |
| UPS backed control line | PLC, HMI, veri kayıt sistemi |
| Isolated AI computer supply | RMDE bilgisayarı |

Kontrol gücü ani jeneratör yük değişimlerinden etkilenmemelidir.

---

## 9. Sensör ve Haberleşme Kablolaması

Hassas sensör ve haberleşme kabloları, yüksek güç hatlarından ayrı taşınmalıdır.

Ayrı güzergâh önerisi:

```text
High Power Cable Route:
generator → panel → induction / compressor / robot drives

Control Cable Route:
PLC → sensors → valves → robot interlock

Communication Route:
AI computer → PLC → robot controller → HMI/HUD

Vision/Data Route:
cameras → AI computer → storage / quality module
```

Özellikle indüksiyon kabloları ile kamera, LiDAR, RTK-GNSS, IMU ve Ethernet hatları fiziksel olarak ayrılmalıdır.

---

## 10. Topraklama ve EMC

ROMR platformunda yüksek güçlü indüksiyon sistemi, robot servo sürücüleri, jeneratör ve hassas AI/sensör sistemleri birlikte çalışacağı için EMC kritik önemdedir.

Gerekenler:

- ortak şasi topraklama noktası,
- jeneratör topraklama bağlantısı,
- indüksiyon inverterleri için ekranlı kablo,
- robot servo kabloları için uygun ekranlama,
- kontrol panosu için ayrı toprak barası,
- sensör kabloları için düşük gürültülü güzergâh,
- Ethernet/fieldbus izolasyonu,
- yıldırım ve transient koruma,
- filtreli güç kaynakları.

---

## 11. Acil Durdurma ve Güvenli Güç Kesme

Acil durdurma mantığı kademeli olmalıdır.

```text
E-Stop Activated
↓
Paint flow disabled
↓
Robot motion permission removed
↓
Induction disabled or safe heat mode
↓
Compressor output isolated if required
↓
Generator load reduced
↓
Alarm and safety systems remain active
```

Güvenlik fonksiyonları yalnızca yazılıma bırakılmamalıdır. Safety PLC, kontaktörler, röleler ve donanımsal güvenlik devreleriyle doğrulanmalıdır.

---

## 12. Yangın ve Termal Güvenlik

Sistemde yüksek sıcaklık, jeneratör, yakıt, indüksiyon, termoplastik boya ve elektrik panoları birlikte bulunduğu için yangın güvenliği ayrı ele alınmalıdır.

Gerekenler:

- jeneratör bölmesi sıcaklık sensörleri,
- yakıt kaçak sensörleri,
- elektrik panosu sıcaklık izleme,
- indüksiyon hat aşırı sıcaklık algılama,
- otomatik yangın söndürme sistemi,
- acil yakıt kesme valfi,
- tabanca ve boya hattı sıcak yüzey koruması,
- operatör uyarı sistemi.

---

## 13. Güç Hesabı Doğrulama Yaklaşımı

360 kW güç mimarisi, nihai karar olarak değil, doğrulanması gereken referans mimari olarak ele alınmalıdır.

Doğrulanacak yükler:

| Yük Grubu | Değerlendirme |
|---|---|
| İndüksiyon ısıtma | boya debisi, sıcaklık artışı, kayıp ve verime göre hesaplanmalı |
| Robot + raylar | hareket profili ve payload etkisine göre |
| Kompresör | rotary gun hava, purge ve yardımcı hava tüketimine göre |
| Pompa / feeder | boya viskozitesi ve basınca göre |
| Cam küreciği sistemi | dozaj motorları ve yardımcı sistemlere göre |
| AI / PLC / sensörler | düşük güç ama kritik yük |
| Emiş sistemi | jet fan ve vakum ihtiyacına göre |
| Yardımcı sistemler | soğutma, aydınlatma, HMI, bakım ekipmanları |

---

## 14. Elektrik Bakım ve Servis Erişimi

Tüm panolar ve güç modülleri saha bakımına uygun olmalıdır.

- modüler pano kapakları,
- etiketli kablo kanalları,
- kolay erişilebilir sigortalar,
- ayrı servis kesicileri,
- yüksek voltaj uyarıları,
- kilitleme / etiketleme prosedürü,
- yedek sigorta ve kritik modül erişimi,
- uzaktan alarm teşhisi.

---

## 15. Yazılım ve PLC Bağlantısı

Bu modül şu yazılım ve kontrol dosyalarıyla bağlantılıdır:

```text
plc_process_interface.py
safety_supervisor.py
induction_heat_controller.py
rmde_decision_engine.py
telemetry_logger.py
```

<div class="git-buttons">

[Git: PLC ve Kontrol Sistemi](07-plc-control-system.md)
[Git: Yazılım: plc_process_interface.py](software/plc_process_interface.py)
[Git: Yazılım: safety_supervisor.py](software/safety_supervisor.py)
[Git: Yazılım: induction_heat_controller.py](software/induction_heat_controller.py)

</div>

---

## 16. Test ve Doğrulama Planı

### 16.1 No-Load Electrical Test

- jeneratör çıkışı doğrulanır,
- ana pano beslenir,
- kontrol güçleri ölçülür,
- faz sırası ve korumalar kontrol edilir.

### 16.2 Partial Load Test

- PLC ve sensörler aktif edilir,
- robot kontrolcü beslenir,
- kompresör düşük yükte çalıştırılır,
- indüksiyon zone testleri ayrı yapılır.

### 16.3 Full Load Simulation

- indüksiyon, robot, pompa, kompresör ve yardımcı yükler senaryolu çalıştırılır,
- yük paylaşımı ve sıcaklık izlenir,
- jeneratör tepkisi kaydedilir.

### 16.4 Emergency Shutdown Test

- E-stop,
- yangın alarmı,
- aşırı sıcaklık,
- yüksek basınç,
- jeneratör alarmı

senaryoları ayrı ayrı test edilir.

---

## 17. Git Kısa Yol Haritası

```text
[Git: İndüksiyon Isıtma Sistemi] → 03-induction-heating-system.md
[Git: PLC ve Kontrol Sistemi] → 07-plc-control-system.md
[Git: Robot Kol + X/Y Kızak] → 05-robot-arm-xy-rail.md
[Git: Prototip BOM] → 12-prototype-bom.md
[Git: Source Document] → source-documents/ROMR_Power_Electrical_Architecture_V1.md
```

---

## 18. Teknik Sonuç

Power & Electrical Architecture, ROMR platformunun tüm alt sistemlerinin güvenli, kararlı ve sürdürülebilir şekilde çalışmasını sağlayan enerji omurgasıdır.

Bu modül; jeneratör, ana pano, yük yönetimi, indüksiyon inverterleri, robot güç hattı, PLC kontrol gücü, safety devreleri, sensör haberleşmesi, topraklama, EMC ve acil durdurma mantığını tek elektrik mimarisinde birleştirir.

Bu nedenle güç mimarisi yalnızca “jeneratör seçimi” değildir; ROMR platformunun termal, robotik, yazılım, güvenlik ve kalite kontrol sistemlerini aynı anda çalıştıran endüstriyel enerji yönetim sistemidir.
