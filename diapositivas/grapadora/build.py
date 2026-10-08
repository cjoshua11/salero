# Genera las diapositivas de las partes de la grapadora en español y turco.
# Usa el mismo estilo base que diapositivas/v2.
import os
D = os.path.dirname(os.path.abspath(__file__))

T = {
 "es": {
  "lang": "es", "title": "Partes de la grapadora",
  "s1_title": "Partes de la grapadora",
  "s1_sub": "Vista explosionada: cada pieza agrupada por la función que cumple.",
  "groups": [
   ("1", "Carcasa exterior", "Üst gövde + Alt dış gövde"),
   ("2", "Mecanismo de grapado", "Zımba haznesi, Zımba iticisi, Örs, Alt metal gövde"),
   ("3", "Sistema de resortes", "İtici yay + Geri dönüş yayı"),
   ("4", "Soporte estructural", "Bağlantı pimi + Kaymaz kauçuk taban"),
  ],
  "k_mat": "Material", "k_why": "Por qué", "k_fn": "Función",
  "s2_title": "La carcasa y el mecanismo",
  "s3_title": "Los resortes y el soporte",
  "parts": [
   ("1", "Carcasa exterior (cuerpo)", [("carcasa.jpg", None)],
    "Plástico de ingeniería (ABS o policarbonato).",
    "Es económico y resiste golpes. Se moldea por inyección, lo que permite paredes con nervaduras internas y formas curvas.",
    "Es la parte que toca la mano: sin aristas vivas, no deja puntos de presión dolorosos. Protege el mecanismo interno."),
   ("2", "Mecanismo de grapado (carril, empujador y yunque)", [("mecanismo.jpg", None)],
    "Acero estampado con recubrimiento de zinc o níquel contra la corrosión.",
    "Es muy rígido: aguanta la compresión sin deformarse. El estampado produce perfiles precisos en grandes cantidades.",
    "El carril aloja y alinea la tira de grapas. El empujador separa cada grapa y el yunque, con sus hendiduras, guía y dobla las patas para cerrarla."),
   ("3", "Sistema de resortes (empuje y retorno)", [("resorte-empuje.jpg", "Empuje"), ("resorte-retorno.jpg", "Retorno")],
    "Acero de alto carbono (acero para resortes).",
    "Tiene excelente memoria elástica: soporta miles de ciclos sin fatigarse ni perder su forma.",
    "El muelle lineal empuja las grapas con fuerza constante para que siempre haya una lista. El muelle de torsión del eje guarda energía al presionar y reabre la grapadora tras cada uso."),
   ("4", "Componentes de soporte (eje y base)", [("eje.jpg", "Eje"), ("base.jpg", "Base")],
    "Eje de acero macizo y base de elastómero o goma.",
    "El eje soporta las grandes fuerzas de cizalladura de la palanca. La goma aumenta la fricción con la mesa.",
    "El eje es el pivote principal sobre el que gira la grapadora. La base la mantiene quieta al presionar y absorbe la vibración y el ruido del golpe."),
  ],
 },
 "tr": {
  "lang": "tr", "title": "Zımbanın parçaları",
  "s1_title": "Zımbanın parçaları",
  "s1_sub": "Patlatılmış görünüm: her parça gördüğü işe göre gruplandı.",
  "groups": [
   ("1", "Dış gövde", "Üst gövde + Alt dış gövde"),
   ("2", "Zımbalama mekanizması", "Zımba haznesi, Zımba iticisi, Örs, Alt metal gövde"),
   ("3", "Yay sistemi", "İtici yay + Geri dönüş yayı"),
   ("4", "Taşıyıcı parçalar", "Bağlantı pimi + Kaymaz kauçuk taban"),
  ],
  "k_mat": "Malzeme", "k_why": "Neden", "k_fn": "İşlevi",
  "s2_title": "Gövde ve mekanizma",
  "s3_title": "Yaylar ve taşıyıcı parçalar",
  "parts": [
   ("1", "Dış gövde", [("carcasa.jpg", None)],
    "Mühendislik plastiği (ABS veya polikarbonat).",
    "Ucuzdur ve darbeye dayanıklıdır. Enjeksiyonla kalıplanır; bu sayede iç nervürlü duvarlar ve kavisli formlar yapılabilir.",
    "Elin dokunduğu kısımdır: keskin kenar olmadığı için ağrılı baskı noktası oluşmaz. İç mekanizmayı korur."),
   ("2", "Zımbalama mekanizması (ray, itici ve örs)", [("mecanismo.jpg", None)],
    "Korozyona karşı çinko veya nikel kaplı preslenmiş çelik.",
    "Çok rijittir: basınç altında şekli bozulmaz. Presleme, hassas profilleri seri üretmeyi sağlar.",
    "Ray, zımba tellerini taşır ve hizalar. İtici her teli tek tek ayırır; örs, oluklarıyla telin bacaklarını yönlendirir ve bükerek kapatır."),
   ("3", "Yay sistemi (itme ve geri dönüş)", [("resorte-empuje.jpg", "İtme"), ("resorte-retorno.jpg", "Geri dönüş")],
    "Yüksek karbonlu çelik (yay çeliği).",
    "Elastik hafızası çok iyidir: binlerce kullanımda yorulmaz ve şeklini kaybetmez.",
    "Düz yay, telleri sabit kuvvetle iter; böylece her zaman bir tel hazırdır. Mildeki burulma yayı basarken enerji depolar ve her kullanımdan sonra zımbayı açar."),
   ("4", "Taşıyıcı parçalar (mil ve taban)", [("eje.jpg", "Mil"), ("base.jpg", "Taban")],
    "Dolu çelik mil ve elastomer veya kauçuk taban.",
    "Mil, kaldıraç etkisinin yarattığı büyük kesme kuvvetlerine dayanır. Kauçuk, masayla sürtünmeyi artırır.",
    "Mil, zımbanın döndüğü ana eksendir. Taban, basarken zımbayı sabit tutar; darbenin titreşimini ve sesini emer."),
  ],
 },
}

CSS = open(os.path.join(D, "..", "v2", "style.css")).read() + open(os.path.join(D, "style.css")).read()


def part(t, p):
    num, name, pics, mat, why, fn = p
    imgs = "".join(
        f'<figure class="pic">{"<figcaption>" + cap + "</figcaption>" if cap else ""}<img class="photo" src="img/{src}" alt=""></figure>'
        for src, cap in pics)
    return (f'<article class="part"><div class="pics n{len(pics)}">{imgs}</div>'
            f'<h2><span class="num">{num}</span>{name}</h2><dl>'
            f'<dt>{t["k_mat"]}</dt><dd>{mat}</dd><dt>{t["k_why"]}</dt><dd>{why}</dd><dt>{t["k_fn"]}</dt><dd>{fn}</dd></dl></article>')


def build(code):
    t = T[code]
    groups = "".join(f'<li><span class="num">{n}</span><div><b>{g}</b><span>{l}</span></div></li>' for n, g, l in t["groups"])
    s2 = "".join(part(t, p) for p in t["parts"][:2])
    s3 = "".join(part(t, p) for p in t["parts"][2:])
    html = f'''<!doctype html>
<html lang="{t['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t['title']}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;800&display=swap">
<style>{CSS}</style></head><body><main class="deck">
<section class="frame"><div class="slide g1" id="s1">
 <h1>{t['s1_title']}</h1><p class="sub">{t['s1_sub']}</p>
 <div class="g1grid"><img class="diagram" src="img/despiece.jpg" alt=""><ol class="groups">{groups}</ol></div>
</div></section>
<section class="frame"><div class="slide gp" id="s2"><h1>{t['s2_title']}</h1><div class="parts">{s2}</div></div></section>
<section class="frame"><div class="slide gp" id="s3"><h1>{t['s3_title']}</h1><div class="parts">{s3}</div></div></section>
</main><script>
function fit(){{document.querySelectorAll('.frame').forEach(f=>{{f.querySelector('.slide').style.transform='scale('+(f.clientWidth/1920)+')';}});}}
new ResizeObserver(fit).observe(document.body);fit();
</script></body></html>'''
    open(os.path.join(D, f"grapadora-{code}.html"), "w").write(html)


for c in T:
    build(c)
