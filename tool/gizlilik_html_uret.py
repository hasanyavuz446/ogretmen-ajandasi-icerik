# -*- coding: utf-8 -*-
"""GIZLILIK.md → docs/gizlilik.html.

Gizlilik metninin TEK kaynağı uygulama deposundaki GIZLILIK.md'dir. Sayfa
elle kopyalanırsa ikisi zamanla ayrışır (App Store'a verilen URL ile
uygulamanın söylediği şey farklı olur) — bu yüzden üretilir.

Kullanım: python3 tool/gizlilik_html_uret.py [GIZLILIK.md yolu]
"""
import html
import re
import sys

VARSAYILAN = '../ogretmen_ajandasi/GIZLILIK.md'


def satiric(s):
    s = html.escape(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<!\w)([\w.\-+]+@[\w.\-]+\.\w+)', r'<a href="mailto:\1">\1</a>', s)
    return s


def govde_uret(md):
    govde, liste, para = [], [], []

    def para_bitir():
        if para:
            govde.append('<p>' + satiric(' '.join(para)) + '</p>')
            para.clear()

    def liste_bitir():
        if liste:
            govde.append('<ul>' + ''.join(f'<li>{satiric(x)}</li>' for x in liste)
                         + '</ul>')
            liste.clear()

    for ln in md.splitlines():
        t = ln.rstrip()
        if t.startswith('# '):
            continue
        if t.startswith('## '):
            para_bitir(); liste_bitir()
            govde.append(f'<h2>{satiric(t[3:].strip())}</h2>')
            continue
        if t.startswith('- '):
            para_bitir(); liste.append(t[2:].strip()); continue
        if t.startswith('  ') and liste:      # önceki maddenin devamı
            liste[-1] += ' ' + t.strip(); continue
        if not t.strip():
            para_bitir(); liste_bitir(); continue
        liste_bitir(); para.append(t.strip())
    para_bitir(); liste_bitir()
    return govde


def main():
    kaynak = sys.argv[1] if len(sys.argv) > 1 else VARSAYILAN
    md = open(kaynak, encoding='utf-8').read()
    if '[e-posta' in md:
        raise SystemExit('HATA: GIZLILIK.md içinde doldurulmamış yer tutucu var.')
    sayfa = ('<!doctype html>\n<html lang="tr">\n<head>\n'
             '<meta charset="utf-8">\n'
             '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
             '<title>Öğretmen Ajandam — Gizlilik Politikası</title>\n'
             '<link rel="stylesheet" href="ortak.css">\n</head>\n<body>\n'
             '<header><div class="kap">\n  <h1>Gizlilik Politikası</h1>\n'
             '  <p>Öğretmen Ajandam</p>\n</div></header>\n\n<div class="kap">\n'
             + '\n'.join(govde_uret(md)) +
             '\n<footer>\n  <p><a href="index.html">Destek sayfası</a> ·\n'
             '     <a href="mailto:yavuzzhasan@gmail.com">İletişim</a></p>\n'
             '</footer>\n</div>\n</body>\n</html>\n')
    open('docs/gizlilik.html', 'w', encoding='utf-8').write(sayfa)
    print(f'✓ docs/gizlilik.html ({len(sayfa)} bayt) ← {kaynak}')


if __name__ == '__main__':
    main()
