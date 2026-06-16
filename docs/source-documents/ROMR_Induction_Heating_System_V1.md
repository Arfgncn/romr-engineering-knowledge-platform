# ROMR Multi-Stage Induction Heating System V1

> Source technical module for the ROMR Engineering Knowledge Platform.

# 03 — Multi-Stage Induction Heating System

<div class="git-buttons">

[Git: Sistem Genel Akışı](01-system-flow.md)
[Git: Pellet Boya Sistemi](02-pellet-paint-system.md)
[Git: Yeni Nesil Termoplastik Tabanca](04-next-generation-thermoplastic-gun.md)
[Git: Robot Kol + X/Y Kızak](05-robot-arm-xy-rail.md)
[Git: Güç ve Elektrik Mimarisi](06-power-electrical-architecture.md)
[Git: PLC ve Kontrol Sistemi](07-plc-control-system.md)
[Git: RMDE Yazılım Mimarisi](08-rmde-software-architecture.md)
[Git: Prototip BOM](12-prototype-bom.md)
[Git: Yazılım Dosyaları](13-software-files.md)

</div>

---

## 1. Modülün Sistemdeki Rolü

Multi-Stage Induction Heating System, pellet formdaki termoplastik boyayı hareket halindeyken kademeli olarak ısıtan ve uygulama sıcaklığına ulaştıran termal proses sistemidir.

Bu sistem klasik tank içinde sürekli yüksek sıcaklıkta bekletme yaklaşımından farklıdır. Amaç, enerjiyi yalnızca gerekli bölgelerde kullanmak, boya akışını hareketli hat içinde kontrollü şekilde ısıtmak, yerel yanma veya bozunmayı azaltmak ve tabanca girişine kadar sıcaklık kararlılığını korumaktır.

İndüksiyon hattı şu alt sistemlerle doğrudan bağlantılıdır:

- pellet boya besleme sistemi,
- screw pump / transfer sistemi,
- güç ve elektrik mimarisi,
- PLC PID kontrol sistemi,
- yeni nesil termoplastik tabanca,
- robot üzerinde taşınan son ısıtma bölümü,
- kalite kontrol ve debi doğrulama sistemi.

---

## 2. Ana Proses Akışı

```text
Pellet Paint Tank
↓
Low-Speed Mixer
↓
Screw Pump / Controlled Feeder
↓
Insulated Transfer Line
↓
Induction Zone 1 — Preheating
↓
Induction Zone 2 — Controlled Softening
↓
Induction Zone 3 — Melting / Flow Formation
↓
Induction Zone 4 — Temperature Stabilization
↓
Induction Zone 5 — Gun Inlet / Body Temperature Maintenance
↓
Dual-Bell Rotary Thermoplastic Paint Gun
```

---

## 3. Tasarım Amacı

İndüksiyon ısıtma sisteminin mühendislik hedefleri:

- pellet boyayı kontrollü ve kademeli şekilde ısıtmak,
- ani sıcaklık şoklarını azaltmak,
- yerel aşırı ısınma ve boya yanmasını engellemek,
- sürekli akış altında sıcaklık kararlılığı sağlamak,
- tabanca girişindeki viskoziteyi sabit tutmak,
- enerji tüketimini klasik sistemlere göre optimize etmek,
- PLC ile kapalı döngü PID kontrol sağlamak,
- debi değişimlerinde sıcaklık setpointlerini adapte etmek.

---

## 4. Referans Prototip Değerleri

| Parametre | Referans |
|---|---|
| Hat uzunluğu | yaklaşık 4 m tasarım referansı |
| Prototip enerji beslemesi | 3 faz 380–400 VAC workshop supply |
| Gerçek makine beslemesi | onboard generator system |
| Hedef boya sıcaklığı | yaklaşık 200–220°C |
| Referans araç hızı | 5 km/h |
| Referans çizgi eni | 0.14 m |
| Referans çizgi kalınlığı | 1.5 mm |
| Boya yoğunluğu | yaklaşık 2000 kg/m³ |
| Hesaplanan referans debi | yaklaşık 2100 kg/h |
| İlk rotary bell prototip hedef debisi | 120–200 kg/h |

Not: 2100 kg/h değeri yüksek kapasiteli referans uygulama hesabıdır. Prototip rotary bell testlerinde daha düşük debi aralıklarıyla doğrulama yapılması beklenir.

---

## 5. Termal Güç Hesabı Yaklaşımı

Temel akış hesabı:

```text
Volumetric flow rate:
Q = v × b × h

Mass flow rate:
m_dot = density × Q

Thermal power:
P = m_dot × c × ΔT
```

Burada:

| Sembol | Açıklama |
|---|---|
| `v` | araç hızı |
| `b` | çizgi eni |
| `h` | çizgi kalınlığı |
| `density` | boya yoğunluğu |
| `c` | özgül ısı |
| `ΔT` | sıcaklık artışı |

Bu hesap, 360 kW güç mimarisinin doğrulanmasında kullanılacak ana mühendislik yaklaşımıdır.

---

## 6. Isıtma Zone Mimarisi

### Zone 1 — Preheating

Görev:

- pellet malzemeyi ön ısıtmak,
- ani termal şoku azaltmak,
- sonraki bölgelerde daha kararlı ısıtma sağlamak.

### Zone 2 — Controlled Softening

Görev:

- malzemeyi kontrollü yumuşatma bölgesine taşımak,
- screw pump sonrası akış kararlılığını korumak,
- basınç dalgalanmasını azaltmak.

### Zone 3 — Melting / Flow Formation

Görev:

- pellet formun akışkan termoplastik boya fazına geçişini tamamlamak,
- sıcaklık dağılımını homojenleştirmek,
- tıkanma riskini azaltmak.

### Zone 4 — Temperature Stabilization

Görev:

- hedef uygulama sıcaklığına yakın sabit değer oluşturmak,
- debi değişimlerinde sıcaklığı dengelemek,
- tabancaya giden akışı kararlı hale getirmek.

### Zone 5 — Gun Inlet / Body Maintenance

Görev:

- robot üzerinde taşınan son ısıtma bölgesini desteklemek,
- tabanca girişinde donma/sertleşme riskini azaltmak,
- dual-bell rotary gun gövde sıcaklığıyla senkron çalışmak.

---

## 7. PLC PID Kontrol Mantığı

Her zone bağımsız PID kontrol mantığıyla yönetilmelidir.

```text
Temperature Setpoint
↓
Actual Temperature Feedback
↓
Flow Rate Compensation
↓
PID Output
↓
Induction Inverter Power
↓
Temperature Stabilization
```

PLC şu verileri izler:

- her zone gerçek sıcaklığı,
- her zone setpoint değeri,
- boya debisi,
- pompa hızı,
- tabanca giriş sıcaklığı,
- gövde sıcaklığı,
- basınç durumu,
- aşırı sıcaklık alarmı,
- enerji yük durumu.

---

## 8. Debi-Sıcaklık Senkronizasyonu

Boya debisi arttığında, indüksiyon sistemi daha fazla termal güç gerektirir. Debi azaldığında ise aşırı ısınma riski oluşur.

Bu nedenle kontrol mantığı:

```text
Flow rate increases
↓
Thermal demand increases
↓
Induction power increases within safe limits
```

```text
Flow rate decreases
↓
Residence time increases
↓
Induction power reduces
↓
Overheating prevented
```

---

## 9. Tabanca ile Entegrasyon

İndüksiyon hattının son bölgesi, yeni nesil dual-bell rotary tabanca ile birlikte çalışır.

Bağlantılı parametreler:

- tabanca gövde sıcaklığı,
- tabanca giriş sıcaklığı,
- boya basıncı,
- rotary bell rpm,
- hava stabilizasyon basıncı,
- nozzle/gun height,
- robot hareket hızı.

<div class="git-buttons">

[Git: Yeni Nesil Termoplastik Tabanca](04-next-generation-thermoplastic-gun.md)

</div>

---

## 10. Robot Kol Üzerindeki Son Isıtma Bölümü

Robot kol üzerinde taşınan boya hattında sıcaklık kaybı oluşmaması için son ısıtma ve izolasyon bölümü gereklidir.

Robot üzerindeki hatlar:

- ısıtılmış boya transfer hattı,
- son indüksiyon / sıcaklık koruma bölgesi,
- termal izolasyon,
- sıcaklık sensörü,
- esnek yüksek sıcaklık bağlantıları,
- kablo/hortum taşıyıcı zincir sistemi.

Bu bölüm robot payload hesabında da dikkate alınmalıdır.

<div class="git-buttons">

[Git: Robot Kol + X/Y Kızak](05-robot-arm-xy-rail.md)

</div>

---

## 11. Güç ve Elektrik Bağlantısı

İndüksiyon sistemi yüksek güçlü yük grubudur. Bu nedenle ayrı koruma, ayrı inverter, EMC ayrımı ve ana güç panosu bağlantısı gerektirir.

Gerekenler:

- her zone için inverter koruması,
- ana güç panosu bağlantısı,
- kontaktör / sigorta grupları,
- aşırı akım koruması,
- sıcaklık emniyet rölesi,
- kablo ekranlama,
- soğutma ve havalandırma,
- sensör kablolarından fiziksel ayrım.

<div class="git-buttons">

[Git: Güç ve Elektrik Mimarisi](06-power-electrical-architecture.md)

</div>

---

## 12. Sensör Gereksinimleri

| Sensör | Görev |
|---|---|
| Zone temperature sensor | her indüksiyon bölgesi sıcaklığı |
| Gun inlet temperature sensor | tabanca giriş sıcaklığı |
| Paint outlet temperature sensor | hat çıkış sıcaklığı |
| Flow sensor | gerçek boya debisi |
| Pressure sensor | boya hattı basıncı |
| Pump torque / current sensor | tıkanma ve yük artışı |
| Inverter status feedback | indüksiyon inverter durumu |
| Overtemperature sensor | güvenlik limiti |
| Cooling fan status | elektronik soğutma durumu |

---

## 13. Güvenlik Mantığı

Aşağıdaki durumlarda sistem kontrollü duruşa geçmelidir:

- aşırı sıcaklık,
- düşük debide yüksek güç,
- yüksek basınç,
- tıkanma ihtimali,
- inverter alarmı,
- soğutma arızası,
- tabanca giriş sıcaklık sapması,
- acil stop,
- yangın alarmı.

Güvenlik fonksiyonları yalnızca Python/RMDE’ye bırakılmamalıdır. PLC ve safety katmanıyla doğrulanmalıdır.

---

## 14. Test ve Doğrulama Planı

### 14.1 Boş Hat Isıtma Testi

- hat üzerinde boya olmadan sensör ve inverter kontrolü doğrulanır,
- sıcaklık rampası izlenir,
- overtemperature korumaları test edilir.

### 14.2 Düşük Debi Pellet Testi

- düşük debide pellet boya ilerletilir,
- preheating ve softening bölgeleri gözlenir,
- tıkanma ve basınç davranışı izlenir.

### 14.3 Sürekli Akış Testi

- belirli debide boya sürekli akıtılır,
- zone sıcaklıkları kaydedilir,
- çıkış sıcaklığı kararlılığı ölçülür.

### 14.4 Rotary Bell Gun Entegrasyon Testi

- tabanca takılı halde gerçek akış testi yapılır,
- püskürtülen boya tartılır,
- saatlik debi hesaplanır,
- sıcaklık sürekliliği ve püskürtme kararlılığı gözlenir.

### 14.5 Yüksek Debi Simülasyonu

- sistem hedef kapasiteye doğru kademeli yükseltilir,
- güç tüketimi,
- sıcaklık dalgalanması,
- basınç,
- tabanca çıkış kalitesi

birlikte değerlendirilir.

---

## 15. Yazılım Bağlantıları

```text
induction_heat_controller.py
plc_process_interface.py
safety_supervisor.py
rmde_decision_engine.py
quality_control_module.py
telemetry_logger.py
```

<div class="git-buttons">

[Git: Yazılım: induction_heat_controller.py](software/induction_heat_controller.py)
[Git: PLC ve Kontrol Sistemi](07-plc-control-system.md)
[Git: Kalite Kontrol Sistemi](10-quality-control-system.md)

</div>

---

## 16. Git Kısa Yol Haritası

```text
[Git: Pellet Boya Sistemi] → 02-pellet-paint-system.md
[Git: Yeni Nesil Termoplastik Tabanca] → 04-next-generation-thermoplastic-gun.md
[Git: Robot Kol + X/Y Kızak] → 05-robot-arm-xy-rail.md
[Git: Güç ve Elektrik Mimarisi] → 06-power-electrical-architecture.md
[Git: PLC ve Kontrol Sistemi] → 07-plc-control-system.md
[Git: Prototip BOM] → 12-prototype-bom.md
[Git: Source Document] → source-documents/ROMR_Induction_Heating_System_V1.md
```

---

## 17. Teknik Sonuç

Multi-Stage Induction Heating System, ROMR platformunda pellet boyayı kontrollü şekilde uygulama sıcaklığına ulaştıran ana termal proses katmanıdır.

Bu sistem:

- klasik tank bazlı sürekli ısıtmadan farklıdır,
- enerjiyi kademeli ve kontrollü bölgelerde kullanır,
- debi, sıcaklık ve basıncı birlikte izler,
- tabanca girişinde viskozite kararlılığı sağlar,
- PLC PID kontrolüyle fiziksel proses güvenliğini korur,
- robot ve tabanca üzerindeki son ısıtma bölümüyle entegre çalışır,
- 360 kW referans güç mimarisinin doğrulanmasında temel hesap modülüdür.

Bu nedenle indüksiyon ısıtma sistemi, ROMR platformunun enerji verimliliği, akış kararlılığı ve uygulama kalitesi açısından merkezi mühendislik bileşenlerinden biridir.
