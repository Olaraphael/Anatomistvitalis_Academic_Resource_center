const CACHE_NAME = "anatomistvitalis-pwa-v5";
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
  "./memory-aids/",
  "./topics/embryology-history-introduction/",
  "./topics/gametogenesis-fertilisation/",
  "./topics/week-one-cleavage-blastocyst/",
  "./topics/week-two-implantation-bilaminar-disc/",
  "./topics/week-three-gastrulation-notochord/",
  "./topics/week-four-neurulation-folding/",
  "./topics/weeks-five-eight-organogenesis/",
  "./topics/fetal-period-placenta-circulation/",
  "./topics/congenital-anomalies-teratology/",
  "./topics/neuroanatomy-foundations/",
  "./topics/brainstem-cranial-nerve-nuclei/",
  "./topics/ascending-sensory-pathways-advanced/",
  "./topics/descending-motor-pathways-advanced/",
  "./topics/cerebellum-basal-ganglia/",
  "./topics/limbic-system-memory/",
  "./topics/ventricles-csf-hydrocephalus/",
  "./topics/neurovascular-stroke-localisation/",
  "./topics/spinal-cord-tract-lesion-localisation/"
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
        .catch(() => caches.match(request).then(cached => cached || (url.pathname.endsWith("/") ? caches.match("./index.html") : caches.match("./"))))
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
