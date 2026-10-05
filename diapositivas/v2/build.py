# Genera las diapositivas simplificadas en español y turco a partir de un mismo diseño.
import os, json
D = os.path.dirname(os.path.abspath(__file__))

T = {
 "es": {
  "lang":"es","title":"Agarres y usuario ideal",
  "s1_title":"¿Qué agarre es mejor para la artritis?",
  "s1_sub":"Comparamos 5 formas de usar un salero.",
  "grips":[
   ("girar","Girar","Girar y pellizcar es lo que más duele (AAOS, s. f.).","8"),
   ("sacudir","Sacudir","La muñeca se mueve una y otra vez y no controlas la dosis.","9"),
   ("pinza","Pinza con el pulgar","La base del pulgar carga 12 veces la fuerza (Cooney y Chao, 1977).","11"),
   ("palma","Empujar con la palma","Mejor, pero carga la muñeca doblada.","14"),
   ("cuatro","Apretar con 4 dedos","Reparte la fuerza y solo pide un 2–3 % de la fuerza de la mano (Mathiowetz et al., 1985).","19"),
  ],
  "best":"Mejor opción",
  "s1_concl":"Conclusión: apretar con 4 dedos sosteniendo el salero es lo que menos duele. Por eso Dosis 5 funciona así.",
  "refs":"Referencias",
  "s1_refs":[
   "American Academy of Orthopaedic Surgeons. (s. f.). <i>Arthritis of the thumb</i>. OrthoInfo. https://orthoinfo.aaos.org/en/diseases--conditions/arthritis-of-the-thumb/",
   "Cooney, W. P., III, &amp; Chao, E. Y. S. (1977). Biomechanical analysis of static forces in the thumb during hand function. <i>The Journal of Bone and Joint Surgery. American Volume, 59</i>(1), 27–36.",
   "Mathiowetz, V., Kashman, N., Volland, G., Weber, K., Dowe, M., &amp; Rogers, S. (1985). Grip and pinch strength: Normative data for adults. <i>Archives of Physical Medicine and Rehabilitation, 66</i>(2), 69–74.",
  ],
  "s2_title":"Usuario ideal: una pareja recién casada que recibe a la familia",
  "s2_family":"Ellos compran el salero; lo usan también sus padres y sus sobrinos. Si funciona para el que más le cuesta, funciona para todos (Microsoft, 2016).",
  "needs":[
   ("abuelos","Los padres: fácil de usar","Casi la mitad de quienes tienen artritis tiene más de 65 años (Fallon et al., 2023).","Se aprieta con 4 dedos, sin girar."),
   ("ninos","Los niños: higiene","Los gérmenes pasan de las superficies a los dedos (Winther et al., 2007).","Hermético: nadie toca la sal."),
   ("dosis","Todos: la dosis","La OMS recomienda menos de 5 g de sal al día (WHO, 2012).","0,5 g por presión: 10 presiones = el máximo del día."),
  ],
  "s2_refs":[
   "Fallon, E. A., Boring, M. A., Foster, A. L., Stowe, E. W., Lites, T. D., Odom, E. L., &amp; Seth, P. (2023). Prevalence of diagnosed arthritis — United States, 2019–2021. <i>Morbidity and Mortality Weekly Report, 72</i>(41), 1101–1107. https://doi.org/10.15585/mmwr.mm7241a1",
   "Microsoft. (2016). <i>Inclusive design toolkit</i>. Microsoft Design. https://inclusive.microsoft.design/",
   "Winther, B., McCue, K., Ashe, K., Rubino, J. R., &amp; Hendley, J. O. (2007). Environmental contamination with rhinovirus and transfer to fingers of healthy individuals by daily life activity. <i>Journal of Medical Virology, 79</i>(10), 1606–1610. https://doi.org/10.1002/jmv.20956",
   "World Health Organization. (2012). <i>Guideline: Sodium intake for adults and children</i>. https://www.who.int/publications/i/item/9789241504836",
  ],
  "ph":"Foto",
 },
 "tr": {
  "lang":"tr","title":"Tutuş ve ideal kullanıcı",
  "s1_title":"Artrit için en iyi tutuş hangisi?",
  "s1_sub":"Bir tuzluğu kullanmanın 5 yolunu karşılaştırdık.",
  "grips":[
   ("girar","Çevirmek","Çevirmek ve sıkıştırmak en çok ağrıtan hareketlerdir (AAOS, t.y.).","8"),
   ("sacudir","Sallamak","Bilek tekrar tekrar hareket eder ve doz kontrol edilemez.","9"),
   ("pinza","Başparmakla sıkıştırmak","Başparmağın tabanı uygulanan kuvvetin 12 katını taşır (Cooney ve Chao, 1977).","11"),
   ("palma","Avuçla bastırmak","Daha iyi, ama bileği bükülü hâlde zorlar.","14"),
   ("cuatro","4 parmakla sıkmak","Kuvveti dağıtır ve elin gücünün sadece %2–3'ünü ister (Mathiowetz vd., 1985).","19"),
  ],
  "best":"En iyi seçenek",
  "s1_concl":"Sonuç: tuzluğu tutarken 4 parmakla sıkmak en az ağrıtan yoldur. Dosis 5 bu yüzden böyle çalışır.",
  "refs":"Kaynakça",
  "s1_refs":None,
  "s2_title":"İdeal kullanıcı: aileyi ağırlayan yeni evli bir çift",
  "s2_family":"Tuzluğu onlar satın alır; ama anne babaları ve yeğenleri de kullanır. En çok zorlanan için çalışıyorsa, herkes için çalışır (Microsoft, 2016).",
  "needs":[
   ("abuelos","Anne babalar: kolay kullanım","Artriti olanların neredeyse yarısı 65 yaşın üzerindedir (Fallon vd., 2023).","4 parmakla sıkılır, çevirmek yok."),
   ("ninos","Çocuklar: hijyen","Mikroplar yüzeylerden parmaklara geçer (Winther vd., 2007).","Hava geçirmez: kimse tuza dokunmaz."),
   ("dosis","Herkes: doz","DSÖ günde 5 g'dan az tuz önerir (WHO, 2012).","Her basışta 0,5 g: 10 basış = günlük sınır."),
  ],
  "s2_refs":None,
  "ph":"Fotoğraf",
 },
}
T["tr"]["s1_refs"] = [r.replace("(s. f.)","(t.y.)").replace("&amp;","&amp;") for r in T["es"]["s1_refs"]]
T["tr"]["s2_refs"] = T["es"]["s2_refs"]

CSS = open(os.path.join(D,"style.css")).read()

# Escenas ilustradas: (imagen, izquierda %, arriba %, ancho %, estilo extra) + zonas de dolor (x %, y %, tamaño %, color)
RED, GREEN = "230,40,40", "40,170,90"
SCENES = {
 "girar":  dict(bg="#fdecec", items=[("270a",16,26,68,""),("1f504",62,6,30,""),("1f623",6,70,24,"")], glows=[(66,52,34,RED),(48,74,26,RED)]),
 "sacudir":dict(bg="#fdecec", items=[("1f9c2",54,10,34,"transform:rotate(28deg)"),("1f44b",6,28,64,""),("1f623",68,70,24,"")], glows=[(44,72,30,RED)]),
 "pinza":  dict(bg="#fdecec", items=[("1f90f",12,22,74,""),("1f623",6,72,24,"")], glows=[(62,62,30,RED),(76,30,18,RED)]),
 "palma":  dict(bg="#fdf3e6", items=[("1f9c2",34,46,32,""),("1faf3",8,18,74,""),("1f615",70,72,24,"")], glows=[(16,40,30,RED)]),
 "cuatro": dict(bg="#e8f6ee", items=[("1f9c2",30,14,40,""),("270a",20,40,58,""),("2705",68,6,26,""),("1f60a",6,72,24,"")], glows=[]),
 "familia":dict(bg="#fff4e0", items=[("1f474",2,10,28,""),("1f475",22,4,28,""),("1f46b",46,2,30,""),("1f467",56,54,20,""),("1f9d2",76,48,22,""),("1f37d-fe0f",12,56,30,""),("1f9c2",40,58,13,"")], glows=[]),
 "abuelos":dict(bg="#fdecec", items=[("1f475",6,6,58,""),("1f590-fe0f",44,44,52,""),("1f623",6,74,22,"")], glows=[(70,80,30,RED),(60,58,22,RED)]),
 "ninos":  dict(bg="#eaf3fb", items=[("1f9d2",4,8,54,""),("1f9a0",50,6,30,""),("1f9c2",54,44,32,""),("1f512",30,64,26,"")], glows=[]),
 "dosis":  dict(bg="#eef1f6", items=[("1f9c2",8,12,44,""),("1f944",44,30,50,"transform:rotate(10deg)")], glows=[], label="0,5 g"),
}

def img(name, t, cls=""):
    sc = SCENES[name]
    out = f'<div class="scene {cls}" style="background:{sc["bg"]}">'
    for x,y,size,col in sc["glows"]:
        out += f'<span class="glow" style="left:{x}%;top:{y}%;width:{size}%;background:radial-gradient(circle,rgba({col},.85) 0,rgba({col},.45) 35%,rgba({col},0) 70%)"></span>'
    for src,l,tp,w,extra in sc["items"]:
        out += f'<img src="img/{src}.webp" alt="" style="left:{l}%;top:{tp}%;width:{w}%;{extra}">'
    for x,y,size,col in sc["glows"]:
        if col == RED:
            out += f'<span class="ring" style="left:{x}%;top:{y}%;width:{size*0.55}%"></span>'
    if sc.get("label"):
        out += f'<span class="lbl">{sc["label"]}</span>'
    return out + '</div>'

def build(code):
    t = T[code]
    cards = ""
    for key,name,why,score in t["grips"]:
        win = key=="cuatro"
        cards += f'''<figure class="card{' win' if win else ''}">{img(key,t)}
  <figcaption><b>{name}</b><span class="score">{score}/20</span>{f'<em class="best">{t["best"]}</em>' if win else ''}<p>{why}</p></figcaption></figure>'''
    needs = ""
    for key,head,data,sol in t["needs"]:
        needs += f'''<figure class="need">{img(key,t)}<figcaption><b>{head}</b><p>{data}</p><p class="sol">→ {sol}</p></figcaption></figure>'''
    refs = lambda L: "".join(f"<p>{r}</p>" for r in L)
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
 <div class="s2grid"><figure class="family">{img('familia',t)}<figcaption>{t['s2_family']}</figcaption></figure>
 <div class="needs">{needs}</div></div>
</div></section>
</main><script>
function fit(){{document.querySelectorAll('.frame').forEach(f=>{{f.querySelector('.slide').style.transform='scale('+(f.clientWidth/1920)+')';}});}}
new ResizeObserver(fit).observe(document.body);fit();
</script></body></html>'''
    open(os.path.join(D,f"diapositivas-{code}.html"),"w").write(html)

for c in T: build(c)
