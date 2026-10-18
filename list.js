(()=>{const ID=u=>{const m=u&&String(u).match(/(?:youtu\.be\/|[?&]v=|\/shorts\/|\/embed\/)([\w-]{11})|^([\w-]{11})$/);return m&&(m[1]||m[2])},T="https://i.ytimg.com/vi/";
const io="IntersectionObserver"in window?new IntersectionObserver(es=>es.forEach(n=>{if(!n.isIntersecting)return;const e=n.target,m=e.style.getPropertyValue("--img").match(/vi\/([\w-]{11})\//);io.unobserve(e);if(!m)return;
const i=new Image();i.onload=()=>{if(i.naturalWidth>120)e.style.setProperty("--img","url("+i.src+")")};i.src=T+m[1]+"/sddefault.jpg"}),{rootMargin:"300px"}):null;
const mark=(e,id)=>{e.classList.add("th");e.style.setProperty("--img","url("+T+id+"/hqdefault.jpg)");if(io)io.observe(e)};
document.querySelectorAll("li.th").forEach(e=>io&&io.observe(e));
fetch("videos.json",{cache:"no-cache"}).then(r=>r.json()).then(j=>{document.querySelectorAll("li[data-k]:not(.th)").forEach(e=>{const id=ID(j[e.dataset.k]);if(id)mark(e,id)})}).catch(()=>{})})();
