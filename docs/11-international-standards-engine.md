[11-international-standards-engine.md](https://github.com/user-attachments/files/28957935/11-international-standards-engine.md)
# 11 — International Standards Engine

<div class="git-buttons">

[Git: Sistem Genel Akışı](01-system-flow.md)
[Git: RMDE Yazılım Mimarisi](08-rmde-software-architecture.md)
[Git: Kalite Kontrol Sistemi](10-quality-control-system.md)
[Git: Yeni Nesil Termoplastik Tabanca](04-next-generation-thermoplastic-gun.md)
[Git: Robot Kol + X/Y Kızak](05-robot-arm-xy-rail.md)
[Git: Prototip BOM](12-prototype-bom.md)
[Git: Yazılım Dosyaları](13-software-files.md)

</div>

---

## 1. Modülün Sistemdeki Rolü

International Standards Engine, ROMR platformunun farklı ülke, bölge, iklim, yol tipi, havaalanı, endüstriyel saha ve özel uygulama standartlarına uyum sağlayabilmesini sağlayan dijital kural motorudur.

Bu modül, sistemi tek bir ülke standardına bağlı klasik yol çizgi makinesi olmaktan çıkarır ve **ülke/bölge seçimine göre çizgi geometrisi, renk, kalınlık, cam küreciği, görünürlük, kalite toleransı ve robot/proses parametrelerini otomatik belirleyen akıllı standart yönetim katmanı** haline getirir.

---

## 2. Standart Motorunun Ana İş Akışı

```text
Country / Region Selection
↓
Road Type Analysis
↓
Climate & Visibility Evaluation
↓
Traffic Density Analysis
↓
Applicable Standard Library
↓
Rule-Based Decision Engine
↓
Marking Geometry Selection
↓
Flow / Heat / Speed Targets
↓
RMDE Execution Approval
↓
Robot + PLC + Quality Control
```

Bu akış sayesinde sistem, yalnızca çizgi ölçülerini değil; termal proses, robot hareketi, kalite toleransı ve saha koşullarını da ülke standardı ile birlikte değerlendirir.

---

## 3. Standart Kütüphanesinin Kapsamı

Standart kütüphanesi aşağıdaki uygulama alanlarını destekleyecek şekilde tasarlanmalıdır:

- şehir içi yollar,
- şehirler arası yollar,
- bölünmüş yollar,
- otoyollar,
- ekspres yollar,
- banket / kenar çizgileri,
- tünel uygulamaları,
- geçici trafik uygulamaları,
- havaalanı pist, taksi yolu ve apron işaretlemeleri,
- lojistik ve endüstriyel saha işaretlemeleri,
- AGV / robotik yönlendirme çizgileri,
- yüksek güvenlikli operasyon alanları.

---

## 4. AI Standart Seçim Parametreleri

RMDE ve standart motoru birlikte şu verileri değerlendirir:

| Parametre | Kullanım Amacı |
|---|---|
| Ülke / bölge | Hangi standart tablosunun yükleneceği |
| Yol tipi | Şehir içi, otoyol, kırsal, tünel, havaalanı vb. |
| Yol sınıfı | Çizgi tipi ve geometrisi |
| Hız limiti | Çizgi uzunluğu, boşluk, görünürlük |
| Trafik yoğunluğu | Kalınlık ve dayanım ihtiyacı |
| Asfalt tipi | Malzeme ve tutunma uyumu |
| İklim | UV, kar, buz, yağmur, sıcaklık |
| Gece görünürlüğü | Retroreflectivity ve cam küreciği gereksinimi |
| Islak gece görünürlüğü | Yağmur ve nemli yüzey performansı |
| Proje tipi | Belediye, otoyol, havaalanı, endüstriyel saha |
| Operasyon güvenliği | Yüksek riskli alanlar, geçici uygulamalar |

---

## 5. Avrupa Standart Yaklaşımı

Avrupa’da yol çizgi standartları tek bir sabit geometri tablosu olarak değerlendirilmemelidir. Sistem iki katmanlı çalışmalıdır:

1. **EN Performans Standartları**  
   EN 1436, EN 1824, EN 13197 gibi görünürlük, retroreflectivity, renk, kayma direnci ve performans ölçüm kriterleri.

2. **Ülke Bazlı Yol Çizgi Yönetmelikleri**  
   Çizgi eni, kesikli çizgi uzunluğu, boşluk, yaya geçidi geometrisi ve yol tipine göre uygulama detayları.

### 5.1 Avrupa Referans Parametreleri

| Yol Tipi / Uygulama | Çizgi Tipi | Çizgi Eni | Kalınlık | Çizgi / Boşluk | Renk |
|---|---|---:|---|---|---|
| Şehir içi yollar | Şerit çizgisi | 10–12 cm | Proje/malzeme bazlı | 3 m / 3 m | Beyaz |
| Kırsal iki yönlü yollar | Kesikli merkez çizgisi | 10–15 cm | Proje/malzeme bazlı | 3 m / 9 m | Beyaz |
| Uyarı / kavşak yaklaşımı | Kesikli uyarı çizgisi | 10–15 cm | Proje/malzeme bazlı | 4/6 m veya 3/3 m | Beyaz |
| Çok şeritli yollar | Şerit ayırıcı | 10–15 cm | Proje/malzeme bazlı | 7 m / 2 m | Beyaz |
| Otoyol / yüksek hızlı yol | Şerit çizgisi | 15 cm | Proje/malzeme bazlı | 6 m / 9–12 m | Beyaz |
| Ana yol / otoyol kenarı | Sürekli kenar çizgisi | 15–25 cm | Proje/malzeme bazlı | Sürekli | Beyaz |

---

## 6. United States Standards

ABD için sistem, MUTCD, AASHTO ve ASTM referans katmanlarını ayrı ayrı değerlendirmelidir.

### 6.1 ABD Referans Parametreleri

| Yol Tipi | Çizgi Tipi | Çizgi Eni | Çizgi / Boşluk | Renk |
|---|---|---:|---|---|
| Şehir içi yollar | Şerit çizgisi | 10–15 cm | 3 m / 9 m | Beyaz |
| İki yönlü yollar | Merkez çizgisi | 10–15 cm | 3 m / 9 m | Sarı |
| Interstate kenar | Kenar çizgisi | 20–25 cm | Sürekli | Beyaz |
| Geçiş yasağı | Çift sürekli merkez çizgisi | 10–15 cm ×2 | Sürekli | Sarı |
| Yaya geçidi | Zebra / enine çizgi | 30–60 cm | Değişken | Beyaz |

### 6.2 ABD Renk Mantığı

| Kullanım | Renk |
|---|---|
| Aynı yöndeki trafik şeritleri | Beyaz |
| Karşı yön trafiği ayrımı | Sarı |
| Yol kenarı / edge line | Beyaz |
| Geçici işaretlemeler | Turuncu |
| Engelli erişim / özel alan | Mavi |

---

## 7. Türkiye Standart Yaklaşımı

Türkiye için sistem, Karayolları ve ilgili yerel idare şartnamelerine göre ülke modülü olarak yapılandırılmalıdır.

### 7.1 AI Karar Örnekleri

| Senaryo | AI Standart Kararı |
|---|---|
| Türkiye otoyol | 15–20 cm otoyol şerit standardı |
| Türkiye şehir içi yol | 3 m / 3 m şehir içi şerit yapısı |
| Kavşak yaklaşımı | Standartlara göre yön oku, dur çizgisi ve yaklaşım çizgileri |
| Yaya geçidi | Yerel şartnameye göre zebra blokları ve dur çizgisi |

Final veri tabanı, ilgili güncel resmi standartlar ve idare şartnamelerine göre tamamlanmalıdır.

---

## 8. Hindistan Standart Yaklaşımı

Hindistan modülü IRC, ulusal otoyol ve yerel idare standartlarını destekleyecek şekilde kurgulanmalıdır.

Sistem, Hindistan pazarı için:

- şehir içi yol,
- ana arter,
- ulusal otoyol,
- yüksek trafik yoğunluğu,
- sıcak iklim,
- yoğun UV etkisi,
- kavşak / yaya geçidi

senaryolarını ayrı ayrı değerlendirmelidir.

---

## 9. GCC / Körfez Bölgesi

Körfez ülkeleri için sistemin temel değerlendirme alanları:

- yüksek sıcaklık,
- yüksek UV etkisi,
- kum/toz etkisi,
- uzun ve geniş otoyol ağları,
- gece görünürlüğü,
- yüksek retroreflectivity gereksinimi.

### AI Karar Örneği

| Senaryo | AI Kararı |
|---|---|
| GCC çöl otoyolu | Kalın film, UV dayanımlı, yüksek retroreflective işaretleme |

---

## 10. Kanada ve Soğuk İklim Modülü

Kanada, TAC ve eyalet otoyol standartlarıyla birlikte ağır kış şartlarına göre değerlendirilmelidir.

### 10.1 Kanada Referans Parametreleri

| Yol Tipi | Çizgi Tipi | Çizgi Eni | Kalınlık | Çizgi / Boşluk | Renk |
|---|---|---:|---:|---|---|
| Şehir içi yollar | Şerit çizgisi | 10–15 cm | 1.5–3 mm | 3 m / 3 m | Beyaz |
| Kırsal yollar | Merkez çizgisi | 10–15 cm | 2–4 mm | 3 m / 9 m | Sarı |
| Eyalet otoyolu | Kenar çizgisi | 20 cm | 3–5 mm | Sürekli | Beyaz |
| Freeway / motorway | Şerit ayırıcı | 15–20 cm | 3–5 mm | 6 m / 12 m | Beyaz |
| Kar riski yüksek alan | Yüksek görünürlük kenar | 20–25 cm | 4–5 mm | Sürekli | Beyaz |

Öncelikler:

- ıslak gece görünürlüğü,
- kar altında yönlendirme,
- kar küreme dayanımı,
- yüksek retroreflectivity,
- kenar çizgisi görünürlüğü.

---

## 11. Rusya / Sert Kış Modülü

Rusya ve benzeri sert kış bölgelerinde sistem şu kriterleri yüksek öncelikli değerlendirir:

- soğuk hava dayanımı,
- kar altında görünürlük,
- uzun gece sürüş şartları,
- buzlanma,
- kar küreme dayanımı,
- aşınma direnci,
- kenar rehberliği.

Yapay zekâ modülü sıcaklık profili, kar yoğunluğu, gece sürüş süresi, yol sınıfı, görüş mesafesi ve aşınma koşullarını birlikte değerlendirmelidir.

---

## 12. Japonya, Güney Kore ve Çin Senaryoları

| Bölge | AI Karar Mantığı |
|---|---|
| Japonya şehir içi yol | Hassas geometri ve dar alanlı kentsel işaretleme modu |
| Güney Kore smart city | ITS uyumlu yüksek görünürlüklü çizgi modu |
| Çin ekspres yol | Yüksek hızlı yol rehberliği standardı |

Bu ülkelerde standart motoru, yerel resmi veri tabanları yüklendikten sonra ülke alt modülleriyle çalışmalıdır.

---

## 13. Havaalanı İşaretleme Modülü

Havaalanı uygulamaları, karayolu standardı gibi ele alınmamalıdır. Ayrı bir uygulama profili gerekir.

Desteklenecek alanlar:

- runway,
- taxiway,
- apron,
- gate guidance,
- aircraft stand markings,
- safety zones.

Referans standart aileleri:

- ICAO,
- FAA,
- yerel sivil havacılık otoritesi.

AI karar örneği:

| Senaryo | AI Kararı |
|---|---|
| Airport taxiway | ICAO / FAA taxiway marking standard |

---

## 14. Endüstriyel Tesis ve AGV / AMR Modülü

Bu modül klasik trafik çizgisi dışındaki zemin işaretlemelerini kapsar.

Kapsam:

- fabrika güvenlik çizgileri,
- lojistik alan çizgileri,
- forklift yolları,
- yaya güvenlik alanları,
- AGV / AMR robot yönlendirme hatları,
- yüksek aşınma dayanımlı zemin işaretlemeleri.

AI karar örneği:

| Senaryo | AI Kararı |
|---|---|
| Endüstriyel tesis | Ağır aşınma dayanımlı güvenlik işaretlemesi |
| AGV hattı | Robotik algılamaya uygun yüksek kontrastlı yönlendirme çizgisi |

---

## 15. RMDE Entegrasyonu

Standart motoru RMDE ile doğrudan çalışır.

```text
Country Selection
↓
Road Type
↓
Standard Rule Loading
↓
Reference Point Generation
↓
Line Geometry Decision
↓
Robot Target Coordinates
↓
PLC Process Parameters
↓
Quality Tolerance
```

RMDE bu modülden şu değerleri alır:

- çizgi eni,
- çizgi tipi,
- renk,
- boşluk mesafesi,
- çizgi kalınlığı,
- cam küreciği miktarı,
- kalite toleransı,
- retroreflectivity hedefi,
- uygulama hızı,
- termal/proses önerileri.

<div class="git-buttons">

[Git: RMDE Yazılım Mimarisi](08-rmde-software-architecture.md)
[Git: Yazılım: standards_rule_engine.py](software/standards_rule_engine.py)

</div>

---

## 16. Kalite Kontrol Entegrasyonu

Standart motoru yalnızca uygulama öncesi karar vermez; uygulama sonrası kalite kontrol modülüne kabul kriterlerini de sağlar.

Kalite kontrol kriterleri:

- çizgi eni toleransı,
- çizgi kalınlığı toleransı,
- süreklilik,
- sapma limiti,
- renk kontrolü,
- gece görünürlüğü,
- cam küreciği dağılımı,
- aşınma dayanımı,
- proje bazlı kabul değerleri.

<div class="git-buttons">

[Git: Kalite Kontrol Sistemi](10-quality-control-system.md)

</div>

---

## 17. Uzaktan Güncelleme ve Bulut Entegrasyonu

Standart veri tabanı şu yeteneklere sahip olmalıdır:

- yeni ülke standardı ekleme,
- mevcut standartları güncelleme,
- belediye/otorite özel şartname yükleme,
- AI model güncelleme,
- merkezi görev yönetimi,
- filo yönetimi,
- operasyon sonrası veri tabanı güncelleme.

Bu yapı sayesinde sistem, standart değişikliklerinde yeniden yazılım geliştirmeden güncellenebilir.

---

## 18. Standart Veri Dosyaları

Bu modül için ilk veri dosyaları:

```text
docs/standards/international_standards_library_v1.json
docs/standards/standards_rule_table_v1.csv
```

[Git: Standards JSON](standards/international_standards_library_v1.json)  
[Git: Standards CSV](standards/standards_rule_table_v1.csv)

---

## 19. Git Kısa Yol Haritası

```text
[Git: Sistem Genel Akışı] → 01-system-flow.md
[Git: RMDE Yazılım Mimarisi] → 08-rmde-software-architecture.md
[Git: Kalite Kontrol Sistemi] → 10-quality-control-system.md
[Git: Yeni Nesil Termoplastik Tabanca] → 04-next-generation-thermoplastic-gun.md
[Git: Robot Kol + X/Y Kızak] → 05-robot-arm-xy-rail.md
[Git: Prototip BOM] → 12-prototype-bom.md
[Git: Yazılım Dosyaları] → 13-software-files.md
[Git: Source Document] → source-documents/ROMR_International_Standards_Engine_V1.md
```

---

## 20. Teknik Sonuç

International Standards Engine, ROMR platformunu yerel bir yol çizgi makinesi olmaktan çıkarıp **ülke, iklim, yol sınıfı, havaalanı, endüstriyel tesis ve AGV uygulamalarına uyarlanabilir global bir işaretleme platformu** haline getirir.

Bu modül sayesinde sistem:

- farklı ülkelerde yazılımı yeniden geliştirmeden çalışabilir,
- ülke/bölge standardına göre çizgi geometrisini seçebilir,
- iklim ve görünürlük koşullarına göre uygulama parametresi değiştirebilir,
- RMDE, robot, PLC ve kalite kontrol modülleriyle kapalı döngü çalışabilir,
- gelecekte uzaktan güncellenebilir standart veri tabanına dönüşebilir.

Bu nedenle standart motoru, ROMR platformunun uluslararası ölçeklenebilirliğini sağlayan merkezi yazılım ve veri mimarisi olarak değerlendirilmelidir.
