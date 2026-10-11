const CACHE_NAME = "anatomistvitalis-pwa-v6";
const CORE_ASSETS = [
  "./",
  "./index.html",
  "./manifest.webmanifest",
  "./icons/icon-192.svg",
  "./icons/icon-512.svg",
  "./icons/icon-192.png",
  "./icons/icon-512.png",
  "./diagrams/cardiac-conduction.svg",
  "./diagrams/nephron.svg",
  "./diagrams/anatomical-planes.svg",
  "./diagrams/regional-anatomy-map.svg",
  "./diagrams/neuroanatomy-pathways.svg",
  "./diagrams/embryology-timeline.svg",
  "./diagrams/neural-tube-development.svg",
  "./diagrams/germ-layer-derivatives.svg",
  "./memory-aids/index.html",
  "./topics/index.html",
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
  "./topics/spinal-cord-tract-lesion-localisation/index.html"
];

self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(CORE_ASSETS))
      .then(() => self.skipWaiting())
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
        .then(response => {
          if (response && response.ok) {
            const copy = response.clone();
            caches.open(CACHE_NAME).then(cache => cache.put(request, copy));
          }
          return response;
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
