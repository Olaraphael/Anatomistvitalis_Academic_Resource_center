const CACHE_NAME = "anatomistvitalis-pwa-v40";
const CORE_ASSETS = [
  "./diagrams/cerebral-arterial-circulation.svg",
  "./topics/bone/index.html",
  "./topics/anatomical-nomenclature/index.html",
  "./topics/anatomy-history/index.html",
  "./topics/radiological-anatomy/index.html",
  "./topics/reproductive-anatomy/index.html",
  "./topics/research-literacy-biomed/index.html",
  "./topics/sensory-motor-pathways/index.html",
  "./topics/skeletal-muscle-anatomy/index.html",
  "./topics/special-senses-anatomy/index.html",
  "./topics/spinal-cord-tract-lesion-localisation/index.html",
  "./topics/synovial-joints-regional/index.html",
  "./topics/urinary-gross-anatomy/index.html",
  "./topics/neurological-rehabilitation/index.html",
  "./topics/physiotherapy-assessment/index.html",
  "./topics/physiotherapy-foundations/index.html",
  "./topics/therapeutic-exercise/index.html",
  "./topics/renal-filtration-clearance/index.html",
  "./topics/respiratory-ventilation-perfusion/index.html",
  "./topics/meninges/index.html",
  "./topics/metabolism-energy/index.html",
  "./topics/homeostasis/index.html",
  "./topics/reproductive-physiology/index.html",
  "./topics/shoulder/index.html",
  "./topics/head/index.html",
  "./topics/pelvis-perineum-anatomy/index.html",
  "./topics/endocrine-axis-thyroid-adrenal/index.html",
  "./topics/epithelium/index.html",
  "./topics/connective-tissue/index.html",
  "./topics/nervous-system-map/index.html",
  "./topics/upper-limb-regional-anatomy/index.html",
  "./topics/vertebral-column-anatomy/index.html",
  "./topics/respiratory-mechanics/index.html",
  "./topics/ventricles-csf-hydrocephalus/index.html",
  "./topics/congenital-anomalies-teratology/index.html",
  "./topics/digestive-gross-anatomy/index.html",
  "./diagrams/four-basic-tissue-classes.svg",
  "./diagrams/thorax-lungs-schematic.svg",
  "./diagrams/physiology-homeostasis.svg",
  "./diagrams/dcml-decussation.svg",
  "./topics/physiology-course/index.html",
  "./image-credits/index.html",
  "./",
  "./index.html",
  "./manifest.webmanifest",
  "./question-bank/",
  "./question-bank/index.html",
  "./icons/icon-192.svg",
  "./icons/icon-512.svg",
  "./icons/icon-192.png",
  "./icons/icon-512.png",
  "./diagrams/cardiac-conduction.svg",
  "./diagrams/nephron.svg",
  "./diagrams/anatomical-planes.svg",
  "./diagrams/regional-anatomy-map.svg",
  "./diagrams/neuroanatomy-pathways.svg",
  "./diagrams/brain-cortex-functional-landmarks.svg",
  "./diagrams/brainstem-cranial-nerve-levels.svg",
  "./visual-atlas/index.html",
  "./diagrams/embryology-timeline.svg",
  "./diagrams/neural-tube-development.svg",
  "./diagrams/germ-layer-derivatives.svg",
  "./memory-aids/index.html",
  "./topics/index.html",
  "./research-methodology/",
  "./research-methodology/index.html",
  "./topics/pathology-foundations/index.html",
  "./study-guides/index.html",
  "./topics/embryology-history-introduction/index.html",
  "./topics/gametogenesis-fertilisation/index.html",
  "./topics/week-one-cleavage-blastocyst/index.html",
  "./topics/week-two-implantation-bilaminar-disc/index.html",
  "./topics/week-three-gastrulation-notochord/index.html",
  "./topics/week-four-neurulation-folding/index.html",
  "./topics/weeks-five-eight-organogenesis/index.html",
  "./topics/fetal-period-placenta-circulation/index.html",
  "./topics/congenital-anomalies-teratology/index.html",
  "./topics/neuroanatomy-foundations/index.html",
  "./topics/brainstem-cranial-nerve-nuclei/index.html",
  "./topics/ascending-sensory-pathways-advanced/index.html",
  "./topics/descending-motor-pathways-advanced/index.html",
  "./topics/cerebellum-basal-ganglia/index.html",
  "./topics/limbic-system-memory/index.html",
  "./topics/ventricles-csf-hydrocephalus/index.html",
  "./topics/neurovascular-stroke-localisation/index.html",
  "./topics/spinal-cord-tract-lesion-localisation/index.html",
  "./topics/embryology-principles/index.html",
  "./topics/gametogenesis-fertilisation/index.html",
  "./topics/germ-layers-organogenesis/index.html",
  "./topics/neuron/index.html",
  "./topics/general-physiology-homeostasis/index.html",
  "./topics/cardiovascular-physiology/index.html",
  "./topics/respiratory-physiology/index.html",
  "./topics/renal-physiology/index.html",
  "./topics/endocrine-physiology/index.html",
  "./topics/muscle-physiology/index.html",
  "./topics/autonomic-physiology/index.html",
  "./topics/digestive-physiology/index.html",
  "./topics/physiotherapy-foundations/index.html",
  "./topics/physiotherapy-assessment/index.html",
  "./topics/therapeutic-exercise/index.html",
  "./topics/musculoskeletal-rehabilitation/index.html",
  "./topics/neurological-rehabilitation/index.html",
  "./topics/cardiorespiratory-physiotherapy/index.html",
  "./pro/index.html",
  "./diagrams/physiotherapy-assessment-sketch.svg",
  "./diagrams/therapeutic-exercise-sketch.svg",
  "./diagrams/neuro-rehabilitation-sketch.svg",
  "./diagrams/cardiorespiratory-physiotherapy-sketch.svg",
  "./diagrams/knee-joint-anatomy-sketch.svg",
  "./diagrams/abdominal-quadrants.svg",
  "./diagrams/body-cavities-schematic.svg",
  "./diagrams/levels-of-organisation.svg",
  "./diagrams/membrane-transport-schematic.svg",
  "./diagrams/axial-appendicular-skeleton.svg",
  "./diagrams/animal-cell-organelles.svg",
  "./topics/anatomy-history/index.html",
  "./topics/anatomical-language/index.html",
  "./topics/directional-terms-regions/index.html",
  "./topics/body-divisions-cavities/index.html",
  "./topics/anatomical-movements/index.html",
  "./topics/levels-of-organisation/index.html",
  "./topics/anatomical-nomenclature/index.html",
  "./topics/gross-anatomy-methods/index.html",
  "./topics/planes-axes-sections/index.html",
  "./topics/four-tissue-classes/index.html",
  "./topics/cell/index.html",
  "./topics/cell-organelle/index.html",
  "./topics/skeletal-system-overview/index.html",
  "./topics/bone/index.html",
  "./topics/respiratory-gross-anatomy/index.html",
  "./topics/histology-introduction/index.html",
  "./diagrams/skull-regions-schematic.svg",
  "./diagrams/neuron-structure-schematic.svg",
  "./diagrams/blood-components-schematic.svg",
  "./diagrams/endocrine-feedback-axis.svg",
  "./diagrams/digestive-process-schematic.svg",
  "./diagrams/muscle-contraction-schematic.svg",
  "./diagrams/shoulder-joint-schematic.svg",
  "./diagrams/hand-carpal-tunnel-schematic.svg",
  "./diagrams/foot-arches-schematic.svg",
  "./diagrams/autonomic-outflow-comparison.svg",
  "./diagrams/anatomy-history-timeline.svg",
  "./diagrams/pathology-disease-process.svg",
  "./topics/shoulder/index.html",
  "./topics/thorax-abdomen-regional/index.html",
  "./topics/abdominal-regions-lines/index.html",
  "./topics/head/index.html",
  "./topics/skull/index.html",
  "./topics/neuron/index.html",
  "./topics/meninges/index.html",
  "./topics/brain/index.html",
  "./topics/cranial/index.html",
  "./topics/nervous-system-map/index.html",
  "./topics/spinal-cord/index.html",
  "./topics/brainstem-cranial-nerve-nuclei/index.html",
  "./topics/ascending-sensory-pathways-advanced/index.html",
  "./topics/descending-motor-pathways-advanced/index.html",
  "./topics/cerebral-blood-supply/index.html",
  "./topics/general-physiology-homeostasis/index.html",
  "./topics/homeostasis/index.html",
  "./topics/cardiac/index.html",
  "./topics/respiratory-physiology/index.html",
  "./topics/endocrine-physiology/index.html",
  "./topics/digestive-physiology/index.html",
  "./topics/upper-limb-regional-anatomy/index.html",
  "./topics/hand-anatomy/index.html",
  "./topics/foot-ankle-anatomy/index.html",
  "./topics/thoracic-organs-anatomy/index.html",
  "./topics/abdominal-wall-anatomy/index.html",
  "./topics/pelvis-perineum-anatomy/index.html",
  "./topics/cardiovascular-gross-anatomy/index.html",
  "./topics/blood-components/index.html",
  "./topics/haemostasis-coagulation/index.html",
  "./topics/cardiac-output-vascular-resistance/index.html",
  "./topics/respiratory-mechanics/index.html",
  "./topics/respiratory-ventilation-perfusion/index.html",
  "./topics/renal-filtration-clearance/index.html",
  "./topics/endocrine-axis-thyroid-adrenal/index.html",
  "./topics/digestion-absorption-physiology/index.html",
  "./topics/muscle-physiology/index.html",
  "./topics/autonomic-physiology/index.html",
  "./topics/reproductive-physiology/index.html",
  "./topics/acid-base-fluid-balance/index.html",
  "./topics/physiotherapy-foundations/index.html",
  "./topics/physiotherapy-assessment/index.html",
  "./topics/therapeutic-exercise/index.html",
  "./topics/musculoskeletal-rehabilitation/index.html",
  "./topics/neurological-rehabilitation/index.html",
  "./topics/cardiorespiratory-physiotherapy/index.html",
  "./topics/biochemistry-molecular/index.html",
  "./topics/metabolism-energy/index.html",
  "./topics/genetics-molecular-medicine/index.html",
  "./topics/blood-immunity/index.html",
  "./diagrams/neuron-structure-schematic.svg",
  "./topics/pregnancy-development/index.html",
  "./topics/connective-tissue/index.html",
  "./topics/muscle-histology/index.html",
  "./topics/lung-histology-gas-barrier/index.html",
  "./topics/bone-classification-landmarks/index.html",
  "./topics/joints-classification/index.html",
  "./topics/vertebral-column-anatomy/index.html",
  "./diagrams/abdominal-nine-regions.svg"
];

self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => Promise.allSettled(CORE_ASSETS.map(asset => cache.add(asset))))
      .then(results => {
        const failed = results.filter(result => result.status === "rejected").length;
        if (failed) console.warn("Some optional offline assets could not be cached:", failed);
        return self.skipWaiting();
      })
  );
});

self.addEventListener("activate", event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", event => {
  const request = event.request;
  if (request.method !== "GET") return;
  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return;

  if (request.mode === "navigate") {
    event.respondWith(
      fetch(request)
        .then(async response => {
          if (!response || !response.ok) return response;
          let finalResponse = response;
          const isTopicArticle = url.pathname.includes("/topics/") && !url.pathname.endsWith("/topics/") && !url.pathname.endsWith("/topics/index.html");
          if (isTopicArticle) {
            let html = await response.clone().text();
            if (!html.includes("Written by Ibine Oladipupo R.")) {
              const h1End = html.toLowerCase().indexOf("</h1>");
              if (h1End >= 0) html = html.slice(0,h1End+5) + '<div class="author-byline" style="margin:0 0 12px;padding:10px 13px;background:#eaf8f5;border-left:4px solid #087d70;border-radius:0 9px 9px 0;font-size:14px;color:#203747"><strong>Written by Ibine Oladipupo R.</strong> · Anatomistvitalis Academic Resource Center</div>' + html.slice(h1End+5);
            }
            if (!html.toLowerCase().includes(">introduction</h2>")) {
              const introPos = html.indexOf('class="intro"');
              if (introPos >= 0) { const pStart = html.lastIndexOf("<p",introPos); if(pStart>=0) html=html.slice(0,pStart)+'<h2 class="article-introduction" style="font-size:22px;color:#0a2034;margin:18px 0 8px">Introduction</h2>'+html.slice(pStart); }
            }
            if (!html.includes("Original educational line art created for Anatomistvitalis") && !/<img\b/i.test(html)) {
              const path = url.pathname.toLowerCase();
              let diagram = "";
              let label = "";
              if (path.includes("embry") || path.includes("gastrulation") || path.includes("germ-layer") || path.includes("fetal") || path.includes("week-one") || path.includes("week-two") || path.includes("week-three") || path.includes("week-four")) { diagram = "embryology-timeline.svg"; label = "Embryology development timeline"; }
              else if (path.includes("cranial")) { diagram = "brainstem-cranial-nerve-levels.svg"; label = "Brainstem and cranial nerve levels"; }
              else if (path.includes("neuro") || path.includes("brain") || path.includes("spinal") || path.includes("mening") || path.includes("neuron") || path.includes("cerebell") || path.includes("limbic") || path.includes("ventric") || path.includes("sensory-motor")) { diagram = "neuroanatomy-pathways.svg"; label = "Neuroanatomical pathways schematic"; }
              else if (path.includes("blood-components") || path.includes("haemostasis") || path.includes("blood-immunity")) { diagram = "blood-components-schematic.svg"; label = "Blood components schematic"; }
              else if (path.includes("endocrine") || path.includes("hormone")) { diagram = "endocrine-feedback-axis.svg"; label = "Endocrine feedback axis schematic"; }
              else if (path.includes("digestive") || path.includes("digestion")) { diagram = "digestive-process-schematic.svg"; label = "Digestive processing and absorption schematic"; }
              else if (path.includes("muscle-physiology")) { diagram = "muscle-contraction-schematic.svg"; label = "Skeletal muscle contraction schematic"; }
              else if (path.includes("respiratory")) { diagram = "thorax-lungs-schematic.svg"; label = "Thoracic respiratory anatomy schematic"; }
              else if (path.includes("renal") || path.includes("nephron") || path.includes("urinary")) { diagram = "nephron.svg"; label = "Nephron structure schematic"; }
              else if (path.includes("cardiac") || path.includes("cardiovascular") || path.includes("heart")) { diagram = "cardiac-conduction.svg"; label = "Cardiac conduction schematic"; }
              else if (path.includes("physiology") || path.includes("homeostasis")) { diagram = "physiology-homeostasis.svg"; label = "Physiological homeostasis schematic"; }
              else if (path.includes("physiotherapy-assessment") || path.includes("assessment")) { diagram = "physiotherapy-assessment-sketch.svg"; label = "Physiotherapy assessment schematic"; }
              else if (path.includes("therapeutic-exercise") || path.includes("rehabilitation") || path.includes("physiotherapy")) { diagram = "therapeutic-exercise-sketch.svg"; label = "Rehabilitation and therapeutic exercise schematic"; }
              else if (path.includes("plane") || path.includes("axis") || path.includes("section")) { diagram = "anatomical-planes.svg"; label = "Anatomical planes schematic"; }
              else if (path.includes("regional") || path.includes("upper-limb") || path.includes("lower-limb") || path.includes("head-neck") || path.includes("pelvis") || path.includes("thorax") || path.includes("abdominal")) { diagram = "regional-anatomy-map.svg"; label = "Regional anatomy overview"; }
              if (diagram) {
                const figure = '<figure style="margin:22px 0;background:#f6fafc;border:1px solid #dfe8ee;border-radius:16px;padding:12px"><img src="../../diagrams/' + diagram + '" alt="' + label + '" loading="lazy" style="display:block;width:100%;height:auto;border-radius:10px"><figcaption style="font-size:13px;color:#667b8b;margin:8px 4px 0">' + label + '. Educational schematic from Anatomistvitalis Academic Resource Center.</figcaption></figure>';
                const introStart = html.indexOf('class="intro"');
                const introEnd = introStart >= 0 ? html.indexOf("</p>", introStart) : -1;
                if (introEnd >= 0) html = html.slice(0, introEnd + 4) + figure + html.slice(introEnd + 4);
              }
            }
            if (!html.includes('id="lesson-quiz"') && !html.includes("Check your understanding")) {
              const footerPos = html.toLowerCase().lastIndexOf("<footer");
              const mainEnd = html.toLowerCase().lastIndexOf("</main>");
              const pos = footerPos >= 0 ? footerPos : mainEnd;
              if(pos>=0) html=html.slice(0,pos)+"<section id=\"lesson-quiz\" class=\"panel lesson-quiz\" style=\"background:#fff;border:1px solid #dfe8ee;border-radius:16px;padding:22px;margin:24px 0;box-shadow:0 8px 24px #0a203408\"><div style=\"font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:#087e74;font-weight:800\">Check your understanding</div><h2 style=\"margin:6px 0 4px;color:#0a2034\">Lesson quiz</h2><p style=\"margin-top:0\">Answer these five questions after studying this article. Reveal each answer to check your understanding. For more practice, use the separate Question Bank.</p><div id=\"lesson-quiz-items\"></div><p style=\"margin:18px 0 0\"><a href=\"../../question-bank/\" style=\"display:inline-block;background:#0a2034;color:#fff;text-decoration:none;padding:11px 16px;border-radius:10px;font-weight:700;margin:4px 6px 4px 0\">Open separate Question Bank →</a><a href=\"../../pro/\" style=\"display:inline-block;background:#e2f8f4;color:#0a2034;text-decoration:none;padding:11px 16px;border-radius:10px;font-weight:700;margin:4px 0\">Explore Pro question packs →</a></p></section><script>\n(function(){\n const host=document.getElementById('lesson-quiz-items'); if(!host||host.dataset.ready)return; host.dataset.ready='1';\n const clean=s=>(s||'').split(String.fromCharCode(10)).join(' ').replace(/\\s+/g,' ').trim();\n const title=clean((document.querySelector('main h1')||{}).textContent||document.title.split('|')[0]);\n const intro=clean((document.querySelector('main .intro, main p')||{}).textContent);\n const heads=Array.from(document.querySelectorAll('main h2'));\n function sectionText(words){for(const h of heads){if(words.some(w=>h.textContent.toLowerCase().includes(w))){let n=h.nextElementSibling,a=[];while(n&&!/^H[1-3]$/.test(n.tagName)){if(n.tagName==='P'||n.tagName==='LI')a.push(clean(n.textContent));n=n.nextElementSibling;}if(a.length)return a.join(' ');}}return '';}\n const bullets=Array.from(document.querySelectorAll('main li')).map(x=>clean(x.textContent)).filter(x=>x.length>25);\n const clinical=sectionText(['clinical','applied','relevance']);\n const memory=sectionText(['memory','mnemonic','revision','high-yield','key point']);\n const objectives=sectionText(['objective','learning outcome']);\n const qs=[\n ['What is the main focus of this lesson?',intro||('This lesson focuses on '+title+'.')],\n ['State one important point you should remember from this topic.',bullets[0]||memory||('Explain the central structures and concepts discussed in '+title+'.')],\n ['State another key fact or relationship covered in the article.',bullets[1]||bullets[0]||objectives||('Describe the main components and their functions in '+title+'.')],\n ['How can this topic be applied clinically or practically?',clinical||('Apply the principles from '+title+' to explain normal function and recognise relevant clinical findings; this lesson alone does not establish a diagnosis.')],\n ['What should you be able to explain after studying this article?',objectives||memory||('Summarise the central concepts of '+title+', define important terms, and explain a structure-function relationship.')]\n ];\n const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/\"/g,'&quot;');\n host.innerHTML=qs.map((x,i)=>'<article style=\"border-top:1px solid #dfe8ee;padding:14px 0\"><strong style=\"color:#12334b\">'+(i+1)+'. '+esc(x[0])+'</strong><details style=\"margin-top:8px\"><summary style=\"cursor:pointer;color:#087e74;font-weight:750\">Reveal answer</summary><p style=\"margin-bottom:0\">'+esc(x[1])+'</p></details></article>').join('');\n})();\n</script>"+html.slice(pos);
            }
            const headers = new Headers(response.headers);
            headers.delete("content-length"); headers.delete("content-encoding"); headers.delete("etag");
            finalResponse = new Response(html,{status:response.status,statusText:response.statusText,headers});
          }
          caches.open(CACHE_NAME).then(cache => cache.put(request, finalResponse.clone()));
          return finalResponse;
        })
        .catch(() => caches.match(request).then(cached => cached || caches.match(new URL("index.html", request.url).toString()).then(page => page || caches.match("./index.html"))))
    );
    return;
  }

  event.respondWith(
    caches.match(request).then(cached => {
      if (cached) return cached;
      return fetch(request).then(response => {
        if (response && response.ok && response.type === "basic") {
          const copy = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(request, copy));
        }
        return response;
      });
    })
  );
});
