# ROMR HUD & Driver Guidance System V1

> Source technical module for the ROMR Engineering Knowledge Platform.

# 09 — HUD & Driver Guidance System

<div class="git-buttons">

[Git: Sistem Genel Akışı](01-system-flow.md)
[Git: RMDE Yazılım Mimarisi](08-rmde-software-architecture.md)
[Git: Robot Kol + X/Y Kızak](05-robot-arm-xy-rail.md)
[Git: Yeni Nesil Termoplastik Tabanca](04-next-generation-thermoplastic-gun.md)
[Git: PLC ve Kontrol Sistemi](07-plc-control-system.md)
[Git: Kalite Kontrol Sistemi](10-quality-control-system.md)
[Git: Uluslararası Standart Motoru](11-international-standards-engine.md)
[Git: Yazılım Dosyaları](13-software-files.md)

</div>

---

## 1. Modülün Sistemdeki Rolü

HUD & Driver Guidance System, ROMR platformunda sürücünün aracı doğru hatta, doğru hızda ve doğru uygulama koridorunda tutmasını sağlayan görsel ve sesli rehberlik katmanıdır.

Bu sistem klasik “operatör göz kararıyla çizgi takip eder” mantığını ortadan kaldırır. Sürücü, RMDE tarafından üretilen dijital yol modeli, 50 cm referans noktaları, ghost-line hedef çizgisi, sapma uyarıları, hız komutları, robot durumu, boya/ısıtma durumu ve kalite geri bildirimleriyle yönlendirilir.

HUD sistemi aracı otonom yapmaz; ancak sürücüyü dijital çizgi rehberliği ile destekleyerek robot kolun ve boya tabancasının doğru uygulama koridorunda çalışmasını sağlar.

---

## 2. Ana Veri Akışı

```text
Pre-Survey Data
↓
Digital Road Model
↓
RMDE Decision Engine
↓
50 cm Reference Points
↓
HUD Target Path
↓
Ghost Line Projection
↓
Driver Correction Commands
↓
Vehicle Path Stabilization
↓
Robot + Paint Application
↓
Quality Feedback
↓
HUD Warning / Correction Update
```

HUD, RMDE ile sürücü arasında çalışan insan-makine arayüzüdür.

---

## 3. HUD Görsel Katmanları

HUD ekranında ayrı katmanlar bulunmalıdır:

| Katman | Açıklama |
|---|---|
| Green Target Path | Sürücünün takip etmesi gereken ideal yol |
| Blue Ghost Line | Uygulanacak çizginin sanal ön gösterimi |
| White Applied Line | Gerçek uygulanan çizgi bilgisi |
| Red Deviation Zone | Hedef dışına çıkılan risk bölgesi |
| Yellow Correction Arrow | Sürücünün düzeltmesi gereken yön |
| Speed Indicator | Hedef ve mevcut hız |
| Robot Status | Robot hazır / aktif / standby / alarm |
| Paint Status | Boya akışı, sıcaklık, basınç |
| Thermal Status | İndüksiyon ve tabanca sıcaklık durumu |
| Quality Status | Anlık kalite toleransı / sapma bilgisi |

---

## 4. Ghost Line Sistemi

Ghost Line, sürücünün gerçek yol üzerinde göremeyeceği dijital hedef çizgiyi HUD üzerinde sanal olarak göstermeyi amaçlar.

```text
Digital Road Model
↓
Reference Point Path
↓
Screen Projection / HUD Overlay
↓
Ghost Line Visualization
```

Ghost Line şu amaçlarla kullanılır:

- çizgi başlangıç noktasını göstermek,
- çizgi bitiş noktasını göstermek,
- şerit merkezini göstermek,
- kenar çizgisi hedefini göstermek,
- sürücünün aracı doğru yanal pozisyonda tutmasını sağlamak,
- robot kolun erişim alanını aşmadan çalışmasını desteklemek.

---

## 5. Sapma Ölçümü

HUD sistemi sürücünün hedef hatta göre sapmasını sürekli izler.

Sapma verileri:

- yanal sapma,
- açı sapması,
- hız sapması,
- yol merkezinden uzaklık,
- robot erişim sınırına yaklaşma,
- çizgi başlangıç/bitiş zamanlaması.

Örnek:

```text
Target lateral offset: 0.00 cm
Current vehicle offset: +6.00 cm
Correction: Move slightly left
Severity: Warning
```

---

## 6. Sürücü Komutları

HUD sistemi sürücüye kısa, anlaşılır ve operasyonel komutlar vermelidir.

Örnek komutlar:

```text
Alignment is correct. Maintain current path.
Make a slight left correction.
Make a slight right correction.
Reduce speed.
Increase speed slightly.
Approaching line start point.
Approaching line end point.
Robot is active. Maintain speed.
Paint system not ready. Wait.
Emergency stop activated.
```

Sesli uyarılar da aynı komut mantığıyla üretilebilir.

---

## 7. Hız Rehberliği

ROMR uygulama kalitesi için araç hızı kritik parametredir. HUD, hedef hız ile mevcut hız arasındaki farkı sürücüye gösterir.

```text
Target Speed: 5.0 km/h
Current Speed: 5.6 km/h
Command: Reduce speed
```

Hız verisi şu kaynaklardan alınabilir:

- teker enkoderi,
- RTK-GNSS,
- araç CAN verisi,
- IMU destekli hareket analizi.

---

## 8. Robot ve Uygulama Durumu

HUD yalnızca araç yönlendirmesi değil, robotik uygulama durumunu da göstermelidir:

| Durum | Açıklama |
|---|---|
| Robot Ready | Robot başlangıç pozisyonunda |
| Robot Tracking | Robot RMDE koordinatlarını takip ediyor |
| Gun Active | Boya akışı aktif |
| Gun Standby | Tabanca güvenli bekleme konumunda |
| Purge Mode | Temizlik/purge işlemi aktif |
| Height Error | Tabanca yüksekliği tolerans dışında |
| Robot Limit Warning | Robot erişim sınırına yaklaşıldı |
| Emergency Stop | Güvenlik duruşu aktif |

---

## 9. Boya / Isıtma / Emiş Durumu

HUD üzerinde proses durumları özet olarak gösterilmelidir:

- boya sıcaklığı,
- tabanca gövde sıcaklığı,
- indüksiyon hat sıcaklığı,
- boya basıncı,
- rotary bell rpm,
- hava basıncı,
- emiş fanı durumu,
- tank seviyesi,
- cam küreciği seviyesi.

Bu veriler PLC’den alınır ve sürücüye sadece anlamlı durum mesajı olarak gösterilir.

---

## 10. Kalite Geri Bildirimi

Kalite kontrol modülü hata algıladığında HUD sürücüyü uyarabilir.

Örnek:

```text
Line deviation detected between P420–P438.
Correction: reduce lateral offset.
```

Ancak kalite sistemi her küçük hatada sürücüyü yormamalıdır. HUD sadece operasyonu etkileyen veya tekrarlayan hataları göstermelidir.

---

## 11. Sensör Entegrasyonu

HUD şu sensör ve sistemlerden veri alır:

| Kaynak | HUD’da Kullanımı |
|---|---|
| RTK-GNSS | Konum ve yol segmenti |
| IMU | araç yönü, eğim, titreşim |
| Kamera | yol/çizgi algılama |
| LiDAR | yol kenarı, mesafe, profil |
| Teker enkoderi | düşük hız doğrulama |
| RMDE | ghost-line ve referans noktalar |
| Robot controller | robot durumu |
| PLC | proses ve güvenlik durumu |
| Quality module | hata ve kalite durumu |

---

## 12. PLC ve Safety Bağlantısı

HUD, güvenlik kararını kendisi vermez. Safety PLC ve ana PLC’den gelen durumları sürücüye anlaşılır hale getirir.

Örnek safety durumları:

```text
Emergency stop active
Fire alarm
Overtemperature
Paint pressure high
Robot safety zone violation
Generator alarm
Suction system failure
```

---

## 13. HUD Yazılım Mantığı

HUD yazılımı üç temel karar üretir:

1. **Navigation Message**  
   Aracın yön ve hız düzeltmesi.

2. **Process Message**  
   Boya, ısıtma, robot ve PLC durumu.

3. **Safety Message**  
   Acil veya kritik uyarılar.

Yazılım dosyası:

```text
docs/software/hud_guidance_system.py
```

---

## 14. Örnek HUD Mesaj Üretimi

```text
Input:
deviation_cm = +6
target_speed = 5.0
current_speed = 5.7
robot_state = tracking
paint_ready = true

Output:
Message 1: Make a slight left correction.
Message 2: Reduce speed.
Message 3: Robot is active. Maintain stable path.
```

---

## 15. Test ve Doğrulama Planı

### 15.1 Statik HUD Testi

- manuel sapma değeri girilir,
- sistem doğru yön komutunu üretir,
- hız farkına göre uyarı üretilir.

### 15.2 Simülasyon Testi

- 100 metrelik yol modeli oluşturulur,
- ghost-line üretilir,
- sürücü sapmaları simüle edilir,
- HUD mesajları kaydedilir.

### 15.3 Saha Testi

- araç 5 km/h hızla ilerler,
- HUD ghost-line gösterir,
- sürücü komutları takip eder,
- robot ve kalite sistemiyle sonuç karşılaştırılır.

---

## 16. Git Kısa Yol Haritası

```text
[Git: Sistem Genel Akışı] → 01-system-flow.md
[Git: RMDE Yazılım Mimarisi] → 08-rmde-software-architecture.md
[Git: Robot Kol + X/Y Kızak] → 05-robot-arm-xy-rail.md
[Git: Yeni Nesil Termoplastik Tabanca] → 04-next-generation-thermoplastic-gun.md
[Git: PLC ve Kontrol Sistemi] → 07-plc-control-system.md
[Git: Kalite Kontrol Sistemi] → 10-quality-control-system.md
[Git: Yazılım Dosyaları] → 13-software-files.md
[Git: Source Document] → source-documents/ROMR_HUD_Driver_Guidance_System_V1.md
```

---

## 17. Teknik Sonuç

HUD & Driver Guidance System, ROMR platformunda sürücüyü dijital yol modeliyle uyumlu hale getiren rehberlik katmanıdır.

Bu sistem sayesinde:

- sürücü çizgiyi göz kararıyla takip etmez,
- RMDE’nin ürettiği hedef yol ekranda görünür,
- ghost-line ile doğru uygulama koridoru takip edilir,
- hız ve yanal sapma kontrol edilir,
- robot ve boya sistemi durumu izlenir,
- kalite hataları sürücüye anlamlı şekilde bildirilir,
- sistem operatör destekli yarı-otonom uygulama mimarisine yaklaşır.

Bu nedenle HUD, ROMR platformunun insan-makine arayüzü ve saha operasyon güvenliği açısından kritik bir modüldür.
