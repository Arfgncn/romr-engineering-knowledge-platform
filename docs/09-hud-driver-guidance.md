# 9. HUD ve Sürücü Rehberliği

<div class="gitbar"><a href="../08-rmde-software-architecture/">Git: RMDE Yazılım</a><a href="../10-quality-control-system/">Git: Kalite Kontrol</a><a href="../07-plc-control-system/#safety-prensibi">Git: Safety PLC</a><a href="../software/hud_guidance_system.py">Git: Yazılım: hud_guidance_system.py</a></div>

## Sistem Tanımı

HUD sistemi, sürücünün yolu göz kararı takip etmesi yerine RMDE tarafından hesaplanan dijital yol modelini görsel ve sesli rehberlik olarak sürücü alanına taşır.

## HUD Katmanları

- real road view,
- AI ghost line,
- target path indicator,
- actual applied line,
- red deviation zone,
- speed / flow / temperature / quality status,
- safety alarm layer,
- voice guidance output.

## Veri Kaynakları

| Kaynak | HUD Kullanımı |
|---|---|
| Decision Engine | ghost line ve uygulama hedefleri |
| Speed Synchronization | hız durumu ve hız uyarıları |
| Robot Arm Control | robot pozisyonu ve yürütme durumu |
| Flow Control | boya akışı ve malzeme durumu |
| Induction Heat Control | boya sıcaklığı ve termal durum |
| Quality Control | canlı kalite bilgisi |
| Safety PLC | acil stop ve risk uyarıları |

## Tasarım Kuralı

HUD bilgi kalabalığı yaratmamalıdır. Sadece görev için kritik bilgi, öncelikli alarm, basitleştirilmiş durum ve güvenlik mesajları verilmelidir.
