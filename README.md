# Öğretmen Ajandası — Müfredat İçeriği

Uygulamanın kazanım/yıllık plan içeriği. Uygulama açılışta `content/manifest.json`
sürümünü kontrol eder; daha yeni sürüm varsa indirir (mağaza güncellemesi gerekmez).

## Yıllık güncelleme
1. Uygulama deposunda planı ekle → `python3 tool/parse_plan.py && dart run tool/gen_content.dart`,
   `manifest.version`'ı artır.
2. Üretilen `assets/curriculum/*.json` dosyalarını buradaki `content/` klasörüne kopyala.
3. `git add -A && git commit && git push`. Uygulama bir sonraki açılışta çeker.
