(()=>{const ID=u=>{const m=u&&String(u).match(/(?:youtu\.be\/|[?&]v=|\/shorts\/|\/embed\/)([\w-]{11})|^([\w-]{11})$/);return m&&(m[1]||m[2])};
const box=document.getElementById("v"),K=document.currentScript.dataset.k;
const play=d=>{const id=d.dataset.id,b=d.querySelector("button");b.onclick=()=>{const f=document.createElement("iframe");f.src="https://www.youtube-nocookie.com/embed/"+id+"?autoplay=1";f.title="Video del nivel";f.allow="autoplay; encrypted-media; picture-in-picture";f.allowFullscreen=true;d.replaceChildren(f)}};
const baked=box&&box.querySelector(".vid");
if(baked)play(baked);
else if(box)fetch("videos.json",{cache:"no-cache"}).then(r=>r.json()).then(j=>{const id=ID(j[K]);if(!id)return;
box.innerHTML='<div class="vid" data-id="'+id+'"><button aria-label="Reproducir video" style="background-image:url(https://i.ytimg.com/vi/'+id+'/hqdefault.jpg)"></button></div><p><a rel="noopener" href="https://youtu.be/'+id+'">Ver en YouTube</a></p>';play(box.querySelector(".vid"))}).catch(()=>{});
document.querySelectorAll("[data-c]").forEach(e=>e.onclick=async()=>{const t=e.dataset.c||location.href,o=e.textContent;
try{await navigator.clipboard.writeText(t);e.textContent="¡Copiado!"}catch(_){e.textContent="No se pudo copiar"}
setTimeout(()=>e.textContent=o,1500)})})();
