# Anatomistvitalis Academic Resource Center

A responsive educational website for anatomy, neuroanatomy, embryology, histology and physiology learners. The current curriculum contains 130 topic articles, 73 topic-based question-bank items, original schematic diagrams, a dedicated memory-aid library, topic pages with shareable URLs, local lesson completion tracking, and a Progressive Web App (PWA) manifest with offline caching.

## Publish with GitHub Pages

This repository includes a GitHub Actions workflow that deploys the static website after pushes to `main`.

1. Open the repository's **Settings → Pages**.
2. Under **Build and deployment**, select **GitHub Actions** as the source.
3. Open the **Actions** tab and check the deployment workflow.
4. Once the workflow succeeds, the site should be available at:

   https://olaraphael.github.io/Anatomistvitalis_Academic_Resource_center/

If the workflow reports that the Pages site was not found, return to **Settings → Pages**, confirm **GitHub Actions** is selected, save the setting, and rerun the workflow from the **Actions** tab.

## Learning content and visual aids

- Neuroanatomy now progresses from foundational organisation to sensory and motor pathways, brainstem nuclei, cerebellum, basal ganglia, limbic circuits, CSF flow, spinal cord localisation and stroke anatomy.
- Embryology progresses from history and developmental principles through gametogenesis, weeks 1–4, organogenesis, fetal circulation, placenta and teratology.
- Each of the 109 lessons has an individual topic page; the sitemap lists the homepage, topic directory, memory-aid library and all topic URLs.
- Original diagrams are stored as SVG files in `diagrams/`. Mnemonics and retrieval cues are available in lesson modals and at `memory-aids/`.
- The app manifest includes 192px and 512px PNG icons as well as SVG fallbacks. The service worker caches core files and selected new lessons, and caches other visited pages as they are opened. Installation availability still depends on browser/device support and must be tested on the target device.
- Google Analytics 4 is configured with Measurement ID `G-MS73LHJC9D`. Verify collection in the GA4 Realtime report and apply any privacy or consent requirements relevant to your audience.

## Hosting elsewhere

The site is a static HTML/CSS/JavaScript project and can be copied to another static host. Upload the complete repository output—including `index.html`, `topics/`, `diagrams/`, `icons/`, `memory-aids/`, `manifest.webmanifest`, `service-worker.js`, `sitemap.xml` and `robots.txt`—and serve it over HTTPS. If the public base URL changes, update canonical URLs, Open Graph URLs, sitemap URLs, robots.txt and any absolute links. For a custom domain while staying on GitHub Pages, configure the domain in repository **Settings → Pages** and add the required DNS records.

## Current release limitations

- This is a static front-end release; it does not yet have server-backed student accounts, cross-device synchronisation, an administrator dashboard or a persistent database.
- Lesson completion is saved only in the learner's current browser on the current device.
- The lessons and quiz are starter educational content and should be expanded and reviewed by qualified subject experts before being presented as a comprehensive medical curriculum.
- Educational content is not personal medical advice.
