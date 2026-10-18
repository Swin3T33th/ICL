(()=>{const ID=u=>{const m=u&&String(u).match(/(?:youtu\.be\/|[?&]v=|\/shorts\/|\/embed\/)([\w-]{11})|^([\w-]{11})$/);return m&&(m[1]||m[2])};
fetch("videos.json",{cache:"no-cache"}).then(r=>r.json()).then(j=>{document.querySelectorAll("li[data-k]:not(.th)").forEach(e=>{const id=ID(j[e.dataset.k]);
if(id){e.classList.add("th");e.style.setProperty("--img","url(https://i.ytimg.com/vi/"+id+"/mqdefault.jpg)")}})}).catch(()=>{})})();
