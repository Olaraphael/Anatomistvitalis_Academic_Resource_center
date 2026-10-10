# Anatomistvitalis Academic Resource Center

A responsive, mobile-friendly educational website for anatomy and physiology learners. The starter release includes a searchable lesson library, topic filters, lesson explanations, high-yield summaries, local lesson completion tracking, and a self-marking knowledge quiz.

## Publish with GitHub Pages

This repository includes a GitHub Actions workflow that deploys the static website after pushes to `main`.

1. Open the repository's **Settings → Pages**.
2. Under **Build and deployment**, select **GitHub Actions** as the source.
3. Open the **Actions** tab and check the deployment workflow.
4. Once the workflow succeeds, the site should be available at:

   https://olaraphael.github.io/Anatomistvitalis_Academic_Resource_center/

If the workflow reports that the Pages site was not found, return to **Settings → Pages**, confirm **GitHub Actions** is selected, save the setting, and rerun the workflow from the **Actions** tab.

## Current release limitations

- This is a static front-end release; it does not yet have server-backed student accounts, cross-device synchronisation, an administrator dashboard or a persistent database.
- Lesson completion is saved only in the learner's current browser on the current device.
- The lessons and quiz are starter educational content and should be expanded and reviewed by qualified subject experts before being presented as a comprehensive medical curriculum.
- Educational content is not personal medical advice.
