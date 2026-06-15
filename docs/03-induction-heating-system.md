# 3. İndüksiyon Isıtma Sistemi

<div class="gitbar"><a href="../06-power-electrical-architecture/">Git: Güç Mimarisi</a><a href="../07-plc-control-system/">Git: PLC PID Kontrol</a><a href="../04-next-generation-thermoplastic-gun/#induction-assisted-temperature-maintenance">Git: Tabanca Isıtması</a><a href="../12-prototype-bom/#induction-heating-and-thermal-control">Git: BOM: Induction</a><a href="../software/induction_heat_controller.py">Git: Yazılım: induction_heat_controller.py</a></div>

## Sistem Tanımı

İndüksiyon ısıtma sistemi, pellet formundaki termoplastik boyayı büyük bir kazan içinde sürekli yüksek sıcaklıkta bekletmek yerine, hareket halindeki transfer hattı üzerinde kademeli olarak ısıtır. Bu yaklaşım enerji tüketimini, lokal yanma riskini ve boya bozulmasını azaltmayı hedefler.

## Referans Isıtma Hattı

- Tasarım referansı: yaklaşık **4 m** ısıtma hattı.
- Uygulama sıcaklığı: **200–220°C**.
- Besleme: vida pompa / screw transfer sistemi.
- Kontrol: çok bölgeli sıcaklık kontrolü + PLC PID döngüleri.

```mermaid
flowchart LR
    tank[Pellet Tank] --> screw[Screw Pump]
    screw --> z1[Zone 1\nPreheating]
    z1 --> z2[Zone 2\nMelting]
    z2 --> z3[Zone 3\nStabilization]
    z3 --> z4[Zone 4\nFinal Heating]
    z4 --> gun[Heated Gun Body]
```

## Isıl Kontrol Katmanları

| Katman | Amaç | Kontrol Verisi |
|---|---|---|
| Ön ısıtma | Pellet yapısını akışa hazırlama | sıcaklık, vida hızı |
| Erime bölgesi | malzemeyi sürekli akış fazına getirme | hat sıcaklığı, basınç |
| Stabilizasyon | viskoziteyi kararlı tutma | sıcaklık farkı, basınç dalgalanması |
| Final ısıtma | tabanca öncesi hedef sıcaklık | 200–220°C aralığı |
| Tabanca gövdesi | uç noktada donmayı engelleme | indüksiyon bobini, gövde sensörü |

## Güç ve Enerji Yönetimi

İndüksiyon hattı, sistemdeki ana enerji tüketicilerden biridir. Bu nedenle jeneratör, ana pano, yük yönetimi ve indüksiyon inverterleri ile doğrudan bağlıdır.

Öncelik sırası:

1. PLC ve safety sistemleri,
2. indüksiyon kontrol sistemi,
3. robot kol sistemi,
4. kompresör,
5. yardımcı ekipmanlar.

## PLC Sinyalleri

- her bölge için sıcaklık geri bildirimi,
- indüksiyon inverter güç komutu,
- coil sıcaklık limiti,
- hat basınç limiti,
- akış düşüş / aşırı basınç alarmı,
- purge ve drainage valf durumları,
- emergency stop kesme sinyali.
