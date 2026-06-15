# 8. RMDE Yazılım Mimarisi

<div class="gitbar"><a href="../13-software-files/">Git: Yazılım Dosyaları</a><a href="../11-international-standards-engine/">Git: Standart Motoru</a><a href="../05-robot-arm-xy-rail/">Git: Robot Komut Katmanı</a><a href="../09-hud-driver-guidance/">Git: HUD</a><a href="../10-quality-control-system/">Git: Kalite Kontrol</a></div>

## RMDE Tanımı

Road Marking Decision Engine, dijital yol verisini ülke standartları, yol sınıflandırması, mevcut çizgi durumu ve operasyon parametreleriyle karşılaştırarak çizgi tipi, ölçü, renk, koordinat, robot hedefi, araç hızı ve akış komutlarını üretir.

## Ana Yazılım Akışı

```mermaid
flowchart TB
    pre[Pre-Survey Data Acquisition] --> class[Road Classification]
    class --> standards[Country Standards Library]
    standards --> decision[Line Decision Engine]
    decision --> ref[50 cm Reference Point Generator]
    ref --> robot[Robotic Application Command Layer]
    robot --> hud[HUD Guidance]
    robot --> plc[PLC Process Interface]
    plc --> qc[Quality Control Feedback]
    qc --> decision
```

## Yazılım Modülleri

| Dosya | Görev | Hedef Katman |
|---|---|---|
| `pre_survey_module.py` | kamera, LiDAR, RTK, IMU veri paketi | AI computer |
| `road_classifier.py` | yol tipini ve sınıfını belirler | AI computer |
| `standards_rule_engine.py` | ülke/senaryo standardını seçer | AI computer |
| `reference_point_generator.py` | 50 cm nokta haritası üretir | AI computer |
| `rmde_decision_engine.py` | çizgi kararlarını üretir | AI computer |
| `robot_command_layer.py` | robot hedef koordinatlarını hazırlar | AI + robot interface |
| `plc_process_interface.py` | PLC’ye hız, akış, sıcaklık hedeflerini iletir | PLC interface |
| `hud_guidance_system.py` | ghost line ve sürücü komutlarını üretir | HUD/HMI |
| `quality_control_module.py` | görüntü/sensör geri bildirimiyle kaliteyi ölçer | AI quality layer |
| `safety_supervisor.py` | safety durumlarını izler, AI kararlarını sınırlar | Safety PLC interface |

## 50 cm Referans Noktası

Her referans noktası şunları içermelidir:

- P_ID,
- distance_m,
- road_width,
- right_edge_position,
- left_edge_position,
- center_line_allowed,
- edge_line_required,
- line_type,
- robot_target_y,
- vehicle_speed,
- paint_flow_rate,
- glass_bead_flow_rate,
- driver_command.
