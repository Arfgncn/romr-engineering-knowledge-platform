# 14. Kaynak Doküman Haritası

<div class="gitbar"><a href="01-system-flow/">Git: Sistem Akışı</a><a href="12-prototype-bom/">Git: BOM</a><a href="13-software-files/">Git: Yazılım Dosyaları</a><a href="14-source-document-map/">Git: Kaynak Haritası</a></div>

## Amaç

Bu sayfa, platformdaki her ana modülün hangi teknik dokümandan beslendiğini gösterir. Böylece üretici veya tasarım ekibi, bir modülün kök açıklamasına hızlıca dönebilir.

| Platform Modülü | Birincil Kaynak | İkincil Kaynak | Not |
|---|---|---|---|
| Sistem genel akışı | Roadmap Guide | Section 4 | tüm dokümanları bağlayan ana akış |
| Pellet boya sistemi | Section 1 | Section 3 | proses ve prototip doğrulama |
| İndüksiyon ısıtma | Section 1 | Section 3, Section 2 | termal ve güç mimarisi |
| Yeni nesil termoplastik tabanca | Section 1 | Roadmap, Section 2 | rotary bell / dual-disc uygulama ucu |
| Robot kol + X/Y kızak | Section 2 | Section 3, Section 4 | mekanik ve komut entegrasyonu |
| Güç ve elektrik | Section 2 | Section 3 | 2 × 180 kW, pano, yük yönetimi |
| PLC ve kontrol | Section 4 | Section 2, Section 3 | process + safety + motion kontrol |
| RMDE yazılım | Section 4 | Section 5 | karar motoru ve standart bağlantısı |
| HUD rehberliği | Section 4 | Roadmap | ghost line ve sesli uyarı |
| Kalite kontrol | Section 4 | Section 5 | kapalı çevrim doğrulama |
| Standart motoru | Section 5 | Section 4 | ülke/senaryo bazlı karar |
| Prototip BOM | Section 3 | Section 2 | üretim ve tedarik temeli |

## Dokümanları Okuma Sırası

1. Section 1 — Prototype Working Method Technical Progress
2. Section 2 — Mechanical Architecture and Mobile Industrial Platform Systems
3. Section 3 — Prototype Manufacturing Package and Engineering Requirements
4. Section 4 — Road Marking Decision Engine
5. Section 5 — International Standards Library and Adaptive AI Rule Engine
6. Roadmap Guide — navigation and integration guide
