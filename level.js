(()=>{const R=document.currentScript.dataset.k;
const ID=u=>{const m=u&&String(u).match(/(?:youtu\.be\/|[?&]v=|\/shorts\/|\/embed\/)([\w-]{11})|^([\w-]{11})$/);return m&&(m[1]||m[2])};
fetch("videos.json").then(r=>r.json()).then(j=>{const id=ID(j[R]);if(!id)return;
const box=document.getElementById("v"),d=document.createElement("div"),b=document.createElement("button");
d.className="vid";b.setAttribute("aria-label","Reproducir video");
b.style.backgroundImage="url(https://i.ytimg.com/vi/"+id+"/hqdefault.jpg)";
b.onclick=()=>{const f=document.createElement("iframe");f.src="https://www.youtube-nocookie.com/embed/"+id+"?autoplay=1";f.title="Video del nivel";f.allow="autoplay; encrypted-media; picture-in-picture";f.allowFullscreen=true;d.replaceChildren(f)};
const a=document.createElement("p");a.innerHTML='<a rel="noopener" href="https://youtu.be/'+id+'">Ver en YouTube</a>';
d.append(b);box.append(d,a)}).catch(()=>{});
document.querySelectorAll("[data-c]").forEach(e=>e.onclick=async()=>{const t=e.dataset.c||location.href,o=e.textContent;
try{await navigator.clipboard.writeText(t);e.textContent="¡Copiado!"}catch(_){e.textContent="No se pudo copiar"}
setTimeout(()=>e.textContent=o,1500)})})();
