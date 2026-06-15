# 13. Yazılım Dosyaları

<div class="gitbar"><a href="../08-rmde-software-architecture/">Git: RMDE Yazılım</a><a href="../07-plc-control-system/">Git: PLC Kontrol</a><a href="../11-international-standards-engine/">Git: Standart Motoru</a></div>

## Amaç

Bu bölüm, yazılım mimarisinin tek Python dosyası değil; ayrı donanım ve görev katmanlarına bölünmüş modüler dosyalardan oluşması gerektiğini gösterir.

## Yazılım Dosya Listesi

| Dosya | Görev | Git |
|---|---|---|
| `pre_survey_module.py` | yol ve sensör veri paketi | [Git](../software/pre_survey_module.py) |
| `road_classifier.py` | yol sınıflandırma | [Git](../software/road_classifier.py) |
| `standards_rule_engine.py` | ülke/senaryo standardı seçimi | [Git](../software/standards_rule_engine.py) |
| `reference_point_generator.py` | 50 cm referans noktaları | [Git](../software/reference_point_generator.py) |
| `rmde_decision_engine.py` | çizgi karar motoru | [Git](../software/rmde_decision_engine.py) |
| `robot_command_layer.py` | robot hedef koordinatları | [Git](../software/robot_command_layer.py) |
| `plc_process_interface.py` | PLC veri paketi | [Git](../software/plc_process_interface.py) |
| `hud_guidance_system.py` | ghost line + sürücü rehberliği | [Git](../software/hud_guidance_system.py) |
| `quality_control_module.py` | kalite kontrol | [Git](../software/quality_control_module.py) |
| `safety_supervisor.py` | safety izleme | [Git](../software/safety_supervisor.py) |
| `induction_heat_controller.py` | indüksiyon hedefleri | [Git](../software/induction_heat_controller.py) |

## Modülerlik Kuralı

Her modül şu bilgileri ayrı taşımalıdır:

1. Software title,
2. target device,
3. communication protocol,
4. functional responsibility,
5. core data structure,
6. test / simulation logic.
