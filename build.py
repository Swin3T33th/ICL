# Uso: python3 build.py   (cambia SITE por tu URL real antes de publicar)
import html, os, re
SITE = "https://swin3t33th.github.io/ICL"
DATA = """Midnight sun|Akhanas|68366977|
WORLD DESTRUCTION|MagiYT|68602457|2p
HELL NO|KaiGuy|66711620|2p
Enigma|Akhanas|67609666|
5 seconds AGONY|TheRealQueney|67482292|2p
Tokyo Beach|TheRealQueney|67523895|
Ultradeath|NickGeoDash, uploaded by Euphormic|66572754|
PREPOSTEROUS|KaiGuy|66479556|2p
Cyan Hell|ItzVersen|66104376|
Never Die|Haxorras|65903599|
Punk God|igoldboi551|67762963|
TH331|TheSpy|67823109|
Easy For KaiGuy|FlinnMod750|68509314|2p
THISHURTS|Doodsureta|66791314|
BR1MST0N3|Haxorras|65839219|
Iodized|Akhanas|67709391|
Cyber|JonGamingGD|68228449|
Diym|Visionary, uploaded by Ignignokt|65083058|
Ocean Caverns|gooseUNDERSCORE|68395172|2p
spongebob chamber X|kJang, yoot16 and graded|66689000|
Step to heaven|Oskir|68544614|
yYyYyYyYy|kJang|64304553|
THISISTHEWAYTODIE|NickGeoDash|65706022|
Veri|||
Abyssal S|HaellM|65123554|
RedStorm|zLunar and more||
Speedcowore|Markiiuz|65191915|
Silent Sheol Burger|elliotidk|65107016|
A5 sqql|Akhanas|68039472|
FOO WUH|atomano|6511522|
Quantum Break|n618|63411342|
2011|LaLiK24, uploaded by kJang|66622302|
Silent Lava Temple|ItzVersen|64417985|
hheh|ItzVersen|66687957|
16 seconds of MURKA|AgiLityGMD||
HelpThisMan|Akhanas|68686237|
9074|Izofdoors|67262123|
Cyber|JonGamingGD|68228449|
Z|yoot16 and kJang|66688480|
ZERO|HaydenDom|66481331|unnerfed
Pure Terror|ItzVersen|66367069|
very list worthy|JonGamingGD|69165357|
Never give up|Akhanas|66937168|
Last Stop|Knali2001|64815983|
Glaz Diavola|Convindix|61425553|
You So Defeated|Spike|65601075|
Default Block Trial|Electrolyte99|62843279|
Misery|Radarthefox|64108968|
Script|Maxfs|66972591|
Neglected|kaic and Akyse|69212853|
Nerve Crusher|Queney|66177833|
VPC|Akhanas|66749748|
Easy For Jang|Pixelation|67772911|
Willow|TheSpy|67669693|
vsc in china|IndielsTaken|66700276|
W4v3 Ch4ll3ng3r|JonGamingGD|66930531|
CORRUPTED|10daemon26|67829767|
Me When Unnerfed|unregistered222|66102320|
SUPERULTRABUFFEDWAVE|NickGeoDash|65399716|
Toxic Tides|USSRtrew|66572311|
Chamber 11|Akhanas|67580159|
Amizade|Akhanas|67581180|
Thunder|Tomato|6486452|
Illusion of Hell|Exen|38230726|
Silent Venom Challen|HaellM|65121137|
Vicious|DefThLow|63257989|
Inctoolimun|Akhanas|66669660|
Sharkboy Challenge|Temzzz|66423506|
Bo|Fwuffles|65668232|
Heart Attack|JonGamingGD|68119787|
Symball|realhutoew|62843279|fixed
Mecha|JonGamingGD|68000090|
Lemonade|338|65451448|
PleaseDoNotTheCat|ILit, fixed and uploaded by JonGamingGD|69900082|
SideFlip Unnerfed|LGenoxyde|67757646|
O4ko diavola|Flori|67722766|
Falling Illusion|Exen|50542904|
Shipping Container|LegendNeedsHelp|68646694|
hexplate|zBing|67002351|
Wyoming Corridor|MBOD, uploaded by Euphormic|66572032|
Illusion|BuoiToNhatGD|67265931|
Strautniek Chamber|AgiLity GMD|67110540|
AnarchoPrimitivism|TheRealQueney|66967570|
Glata chamber|Akhanas|68064486|
Ultranim|winbo|66521201|
MIND|Neon|67868404|
Drugs|Akhanas|67462276|
You So Acropolis|Vsus|66270674|
Neurosis my part|kJang, uploaded by Temzzz|66398750|
greek yogurt challen|MBOD||
Distortion|AceroGD|67562132|
Shiverthorn|Cybreon||
Chamber 7|Akhanas|67316034|
Hell|realhutoew|65394692|
Toxic Saws|USSRtrew||
bobux challenge|CookieD|66400965|
Jang is Trash|ItzPixelation|66745396|
ao8yeg|DenseCabbageGD|68699343|
hi spike psychopath|Taste|67280577|
Waver|Exen|57463253|"""
L = []
for i, line in enumerate(DATA.split("\n"), 1):
    n, c, d, f = line.split("|")
    L.append(dict(o=i, r=i, n=n, c=c, id=d, f=f))
REMOVED = {24, 35, 38, 95}  # puestos del PDF original que no se muestran: Veri, MURKA, Cyber repetido, Toxic Saws
L = [x for x in L if x["o"] not in REMOVED]
for i, x in enumerate(L, 1):
    x["r"] = i
    x["s"] = re.sub(r"[^a-z0-9]+", "-", x["n"].lower()).strip("-")
assert len({x["s"] for x in L}) == len(L)
E = html.escape
FL = {"2p": "2 jugadores", "unnerfed": "Sin nerfear", "fixed": "Requiere versión corregida"}
TITLE = "Impossible Challenge List (ICL): niveles imposibles de Geometry Dash"
CSS = """:root{color-scheme:dark;--bg:#171220;--s:#1d1728;--ink:#e6e0f2;--mute:#9a8fb3;--line:#2d2540;--acc:#b295ec}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 system-ui,sans-serif}
main{max-width:900px;margin:0 auto;padding:28px 16px 56px}a{color:var(--acc)}
h1{font-size:clamp(1.8rem,6vw,2.5rem);line-height:1.1;margin:0 0 8px}.sub{color:var(--mute);max-width:60ch}
input[type=search]{width:100%;font:inherit;color:var(--ink);background:var(--s);border:1px solid var(--line);border-radius:12px;padding:10px 12px;margin:14px 0 8px}
label.ck{display:inline-flex;gap:6px;align-items:center;color:var(--mute)}.count{color:var(--mute);margin:8px 0}
ol{list-style:none;margin:0;padding:0;display:grid;gap:8px}
li a.it{display:flex;gap:14px;align-items:center;background:var(--s);border:1px solid var(--line);border-radius:12px;padding:12px 14px;text-decoration:none;color:inherit}
li a.it:hover{border-color:var(--acc)}.rk{min-width:48px;text-align:center;font-weight:700;color:var(--acc)}
.nm{font-weight:700;display:block;overflow-wrap:anywhere}.by{color:var(--mute);font-size:.92rem}
.tg{display:inline-block;margin-left:6px;border:1px solid var(--acc);color:var(--acc);border-radius:99px;padding:0 8px;font-size:.75rem}
dl{display:grid;grid-template-columns:auto 1fr;gap:8px 20px;background:var(--s);border:1px solid var(--line);border-radius:12px;padding:16px}
dt{color:var(--mute)}dd{margin:0;font-weight:600;overflow-wrap:anywhere}.nav{display:flex;justify-content:space-between;gap:10px;margin-top:24px}
.vid{position:relative;margin:16px 0 6px;aspect-ratio:16/9;border-radius:14px;overflow:hidden;background:#000}.vid iframe,.vid button{position:absolute;inset:0;width:100%;height:100%;border:0}.vid button{padding:0;cursor:pointer;background:center/cover no-repeat}.vid button::after{content:"▶";position:absolute;inset:0;margin:auto;width:68px;height:68px;border-radius:50%;background:rgba(0,0,0,.65);color:#fff;font-size:28px;display:grid;place-items:center;padding-left:4px}.btns{display:flex;gap:8px;flex-wrap:wrap;margin:14px 0}.btn{font:inherit;color:var(--ink);background:var(--s);border:1px solid var(--line);border-radius:10px;padding:8px 14px;cursor:pointer}.btn:hover{border-color:var(--acc)}.tg.t-2p{border-color:#6c8cff;color:#8fa6ff}.tg.t-unnerfed{border-color:#e0b04a;color:#e0b04a}.tg.t-fixed{border-color:#e07a7a;color:#e07a7a}li.th a.it{background:linear-gradient(90deg,rgba(29,23,40,.97) 30%,rgba(29,23,40,.55)),var(--img) center/cover}footer{margin-top:36px;color:var(--mute);font-size:.9rem}:focus-visible{outline:3px solid var(--acc);outline-offset:2px}"""
FOOT = '<footer>Sitio no oficial. La lista original es de KaiGuy y está moderada por Akhanas. <a href="https://discord.gg/u2D73R7" rel="noopener">Discord de la ICL</a>.</footer>'
def page(title, desc, canon, body, extra=""):
    return f'''<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{SITE}/{canon}">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:type" content="website"><meta property="og:url" content="{SITE}/{canon}">
<link rel="stylesheet" href="style.css">{extra}</head><body><main>{body}{FOOT}</main></body></html>'''
def tags(x):
    return "".join(f'<span class="tg t-{t}">{FL[t]}</span>' for t in x["f"].split(",") if t)
open("style.css", "w").write(CSS)
items = "".join(f'<li data-k="{x["s"]}" data-s="{E((x["n"]+" "+x["c"]).lower())}" data-2p="{int("2p" in x["f"])}"><a class="it" href="nivel-{x["r"]}.html"><span class="rk">#{x["r"]}</span><span><span class="nm">{E(x["n"])}{tags(x)}</span><span class="by">{"de "+E(x["c"]) if x["c"] else "creador sin indicar"}</span></span></a></li>' for x in L)
js = """<script>const q=document.getElementById("q"),p=document.getElementById("p"),li=[...document.querySelectorAll("li")],c=document.getElementById("c");
function f(){const s=q.value.toLowerCase().trim();let n=0;li.forEach(e=>{const ok=e.dataset.s.includes(s)&&(!p.checked||e.dataset["2p"]==="1");e.hidden=!ok;if(ok)n++});c.textContent=n+" niveles"}
q.oninput=p.onchange=f;f()</script>"""
body = f'<h1>Impossible Challenge List</h1><p class="sub">Los {len(L)} niveles más difíciles de Geometry Dash, ordenados del más difícil al más accesible. Toca un nivel para ver su ficha.</p><input id="q" type="search" placeholder="Buscar por nivel o creador" aria-label="Buscar"><label class="ck"><input id="p" type="checkbox"> Solo 2 jugadores</label><p class="count" id="c" aria-live="polite"></p><ol>{items}</ol>{js}<script src="list.js"></script>'
ld = '<script type="application/ld+json">{"@context":"https://schema.org","@type":"ItemList","name":"Impossible Challenge List","itemListElement":[' + ",".join(f'{{"@type":"ListItem","position":{x["r"]},"name":"{x["n"]}","url":"{SITE}/nivel-{x["r"]}.html"}}' for x in L).replace("\\", "") + ']}</script>'
open("index.html", "w").write(page(TITLE, f"Lista completa de los {len(L)} niveles de la Impossible Challenge List de Geometry Dash, con creador e ID, ordenados por dificultad. Busca por nombre o creador.", "", body, ld))
if not os.path.exists('videos.json'): open('videos.json','w').write('{}')
urls = [SITE + "/"]
for i, x in enumerate(L):
    r = x["r"]; pv = L[i-1] if i else None; nx = L[i+1] if i < len(L)-1 else None
    rows = f'<dt>Posición</dt><dd>#{r} de {len(L)}</dd><dt>Creador</dt><dd>{E(x["c"]) or "Sin indicar"}</dd><dt>ID del nivel</dt><dd>{x["id"] or "No disponible"}</dd>'
    if x["f"]: rows += "<dt>Notas</dt><dd>" + ", ".join(FL[t] for t in x["f"].split(",")) + "</dd>"
    nav = f'<div class="nav"><span>{f"<a href=nivel-{pv[chr(114)]}.html>← {pv[chr(114)]}. {E(pv[chr(110)])}</a>" if pv else ""}</span><span>{f"<a href=nivel-{nx[chr(114)]}.html>{nx[chr(114)]}. {E(nx[chr(110)])} →</a>" if nx else ""}</span></div>'
    b = f'<p><a href="index.html">← Volver a la lista</a></p><h1>#{r} {E(x["n"])}</h1><div id="v"></div><dl>{rows}</dl><div class="btns">' + (f'<button class="btn" data-c="{x["id"]}">Copiar ID</button>' if x["id"] else '') + '<button class="btn" data-c="">Copiar enlace</button></div>' + f'<script src="level.js" data-k="{x["s"]}"></script>' + nav
    d = f'{x["n"]}' + (f' de {x["c"]}' if x["c"] else "") + f', puesto #{r} de la Impossible Challenge List de Geometry Dash' + (f'. ID del nivel: {x["id"]}.' if x["id"] else ".")
    open(f"nivel-{r}.html", "w").write(page(f'{x["n"]} (#{r}) | Impossible Challenge List', d, f"nivel-{r}.html", b))
    urls.append(f"{SITE}/nivel-{r}.html")
for r in range(len(L) + 1, 101):
    open(f"nivel-{r}.html", "w").write('<!DOCTYPE html><meta charset="utf-8"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url=index.html"><title>Redirigiendo</title><a href="index.html">Volver a la lista</a>')
open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{u}</loc></url>" for u in urls) + "</urlset>")
open("robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
print(len(urls), "paginas")
