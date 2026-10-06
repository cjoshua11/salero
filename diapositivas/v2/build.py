# Genera las diapositivas en español y turco a partir de un mismo diseño.
import os
D = os.path.dirname(os.path.abspath(__file__))

T = {
 "es": {
  "lang": "es", "title": "Agarres y usuario ideal",
  "s1_title": "¿Qué agarre es mejor para la artritis?",
  "s1_sub": "De los métodos convencionales a nuestro método.",
  "grips": [
   ("pulgar.jpg", "Molinillo: girar con las dos manos", "Girar duele en la base del pulgar (AAOS, s. f.), que carga 12 veces la fuerza aplicada (Cooney y Chao, 1977).", False),
   ("hombro.jpg", "Salero tradicional: sacudir", "No controla la dosis: con un salero común se echaron 7,86 g de media en una sola servida, más de lo recomendado para todo un día (Goffe et al., 2016).", False),
   ("muneca.jpg", "Dispensador de bomba: empujar con la palma", "Empuja con la muñeca doblada hacia atrás: así la presión dentro de la muñeca sube de 2,5 a 30 mmHg, 12 veces más (Gelberman et al., 1981).", False),
   ("producto.png", "Dosis 5: apretar con 4 dedos", "Reparte la fuerza: solo pide un 2–3 % de la fuerza de la mano (Mathiowetz et al., 1985).", True),
  ],
  "best": "Nuestro método",
  "s1_concl": "Conclusión: Dosis 5 se agarra con la muñeca recta y un ancho de 5 a 6 cm, la posición en la que la mano tiene más fuerza (Fransson y Winkel, 1991; O'Driscoll et al., 1992). Por eso cuesta menos y duele menos.",
  "s2_title": "Usuario ideal: una pareja recién casada que recibe a la familia",
  "facts": [
   "En 2024 se casaron <b>568.395 parejas</b> en Turquía, con 26 a 28 años de media (TÜİK, 2025).",
   "La familia se ve seguido: el <b>56,7 %</b> de los mayores de 60 recibe a sus hijos varias veces por semana (TÜİK, 2022).",
  ],
  "needs": [
   ("padres.jpg", "Los padres: sin dolor", "Casi la mitad de las personas con artritis tiene más de 65 años (Fallon et al., 2023).", "Se aprieta con 4 dedos, sin girar."),
   ("hermetico.jpg", "Los niños: higiene", "Los gérmenes pasan de las superficies a los dedos (Winther et al., 2007).", "Hermético: nadie toca la sal."),
   (None, "Todos: la dosis", "En Turquía se comen 14,8 g de sal al día y el 41 % se añade en casa (Erdem et al., 2017). La OMS pide menos de 5 g (WHO, 2012).", "0,5 g por presión: 10 presiones = máximo del día."),
  ],
  "salt": ("14,8 g", "al día en Turquía", "5 g", "máximo OMS"),
 },
 "tr": {
  "lang": "tr", "title": "Tutuş ve ideal kullanıcı",
  "s1_title": "Artrit için en iyi tutuş hangisi?",
  "s1_sub": "Geleneksel yöntemlerden bizim yöntemimize.",
  "grips": [
   ("pulgar.jpg", "Değirmen: iki elle çevirmek", "Çevirmek başparmağın tabanını ağrıtır (AAOS, t.y.); bu eklem uygulanan kuvvetin 12 katını taşır (Cooney ve Chao, 1977).", False),
   ("hombro.jpg", "Geleneksel tuzluk: sallamak", "Doz kontrol edilemez: sıradan bir tuzlukla tek seferde ortalama 7,86 g tuz döküldü; bu, bir günlük önerilen miktardan fazladır (Goffe vd., 2016).", False),
   ("muneca.jpg", "Pompalı kap: avuçla bastırmak", "Bilek geriye bükülü hâlde bastırır: bu pozisyonda bilek içindeki basınç 2,5'ten 30 mmHg'ye, yani 12 kat artar (Gelberman vd., 1981).", False),
   ("producto.png", "Dosis 5: 4 parmakla sıkmak", "Kuvveti dağıtır: elin gücünün sadece %2–3'ünü ister (Mathiowetz vd., 1985).", True),
  ],
  "best": "Bizim yöntemimiz",
  "s1_concl": "Sonuç: Dosis 5 düz bilekle ve 5–6 cm genişlikte tutulur; elin en güçlü olduğu pozisyon budur (Fransson ve Winkel, 1991; O'Driscoll vd., 1992). Bu yüzden daha az zorlar ve daha az ağrıtır.",
  "s2_title": "İdeal kullanıcı: aileyi ağırlayan yeni evli bir çift",
  "facts": [
   "2024'te Türkiye'de <b>568.395 çift</b> evlendi; ortalama evlenme yaşı 26 ile 28 arası (TÜİK, 2025).",
   "Aile sık görüşür: 60 yaş üstü kişilerin <b>%56,7</b>'si çocukları tarafından haftada birkaç kez ziyaret edilir (TÜİK, 2022).",
  ],
  "needs": [
   ("padres.jpg", "Anne babalar: ağrısız", "Artriti olanların neredeyse yarısı 65 yaşın üzerindedir (Fallon vd., 2023).", "4 parmakla sıkılır, çevirmek yok."),
   ("hermetico.jpg", "Çocuklar: hijyen", "Mikroplar yüzeylerden parmaklara geçer (Winther vd., 2007).", "Hava geçirmez: kimse tuza dokunmaz."),
   (None, "Herkes: doz", "Türkiye'de günde 14,8 g tuz tüketiliyor ve bunun %41'i evde ekleniyor (Erdem vd., 2017). DSÖ günde 5 g'dan azını önerir (WHO, 2012).", "Her basışta 0,5 g: 10 basış = günlük sınır."),
  ],
  "salt": ("14,8 g", "Türkiye'de günlük", "5 g", "DSÖ sınırı"),
 },
}

CSS = open(os.path.join(D, "style.css")).read()


def build(code):
    t = T[code]
    cards = ""
    for src, name, why, win in t["grips"]:
        badge = f'<em class="best">{t["best"]}</em>' if win else ""
        cards += (f'<figure class="card{" win" if win else ""}">{badge}<img class="photo{" product" if win else ""}" src="img/{src}" alt="">'
                  f'<figcaption><b>{name}</b><p>{why}</p></figcaption></figure>')
    needs = ""
    for src, head, data, sol in t["needs"]:
        if src:
            pic = f'<img class="photo" src="img/{src}" alt="">'
        else:
            a, al, b, bl = t["salt"]
            pic = (f'<div class="photo salt"><div><span class="big bad">{a}</span><span>{al}</span></div>'
                   f'<div><span class="big ok">{b}</span><span>{bl}</span></div></div>')
        needs += f'<figure class="need">{pic}<figcaption><b>{head}</b><p>{data}</p><p class="sol">→ {sol}</p></figcaption></figure>'
    facts = "".join(f"<li>{f}</li>" for f in t["facts"])
    html = f'''<!doctype html>
<html lang="{t['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t['title']}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;800&display=swap">
<style>{CSS}</style></head><body><main class="deck">
<section class="frame"><div class="slide s1" id="s1">
 <h1>{t['s1_title']}</h1><p class="sub">{t['s1_sub']}</p>
 <div class="grips">{cards}</div>
 <p class="concl">{t['s1_concl']}</p>
</div></section>
<section class="frame"><div class="slide s2" id="s2">
 <h1>{t['s2_title']}</h1>
 <div class="s2grid"><figure class="family"><img class="photo" src="img/pareja.png" alt=""><ul>{facts}</ul></figure>
 <div class="needs">{needs}</div></div>
</div></section>
</main><script>
function fit(){{document.querySelectorAll('.frame').forEach(f=>{{f.querySelector('.slide').style.transform='scale('+(f.clientWidth/1920)+')';}});}}
new ResizeObserver(fit).observe(document.body);fit();
</script></body></html>'''
    open(os.path.join(D, f"diapositivas-{code}.html"), "w").write(html)


for c in T:
    build(c)
