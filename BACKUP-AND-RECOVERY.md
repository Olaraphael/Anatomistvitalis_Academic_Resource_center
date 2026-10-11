# Website backup and recovery guide

The live website is published with GitHub Pages from this repository. GitHub stores the source files and version history, but the live hosting service and repository are separate risks: an outage could temporarily make the site unavailable, and account or repository access problems could affect your ability to update or restore it.

## Recommended low-cost backup routine

1. Open the repository: https://github.com/Olaraphael/Anatomistvitalis_Academic_Resource_center
2. Choose **Code → Download ZIP** and save the ZIP to a computer or trusted cloud drive. Repeat after substantial changes and at least monthly.
3. Keep a second copy somewhere independent of GitHub, such as an external drive or a separate cloud-storage account with two-factor authentication.
4. Secure the GitHub account with a unique password and two-factor authentication; keep recovery codes safe and maintain a verified recovery email.
5. Do not store passwords, private keys, API tokens, student records, or sensitive personal data in this public repository.

## Restore the website

- To recover a deleted or damaged file, inspect the repository's **Commits** history and restore the appropriate previous version.
- To restore the whole project, use a known-good ZIP backup or clone a separate mirror repository. Re-enable GitHub Pages from the correct branch and folder in **Settings → Pages**.
- If GitHub Pages is temporarily unavailable, the source files can be published to another static host. Keep your backup intact until the replacement site is tested.
- If the project grows beyond a simple static educational site, review current GitHub Pages terms and limits before adding commercial or transaction features.

## Important limitation

A backup reduces the risk of permanent loss; it does not guarantee uninterrupted hosting. GitHub Pages may experience temporary interruptions, and account or repository deletion can require recovery from another copy. Keep a separate backup outside GitHub.
