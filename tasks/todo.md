# Task List: Cambridge Institute Website Redesign

- [x] Task 1: Initialize Project Configuration and Design System Tokens
  - Acceptance: `package.json`, `vite.config.ts`, `tsconfig.json`, `src/css/tokens.css`, and `src/css/main.css` are configured with exact colors, typography, spacing, radii, and shadows from `design.md`.
  - Verify: Run `npm install` and verify CSS tokens match `#0C1A45`, `#0B6A56`, `#C99712`, `#151515`, `#F7F6F2`, `#FFFFFF`, `#E6E8EC`.
  - Files: `package.json`, `vite.config.ts`, `tsconfig.json`, `src/css/tokens.css`, `src/css/components.css`, `src/css/main.css`

- [x] Task 2: Build Shared Layout Components & Global Script Engine
  - Acceptance: Shared header with utility bar, desktop navigation, active states, mobile responsive drawer, 4-column footer, modal inquiry dialog, and Lucide SVG icon system are implemented.
  - Verify: Load test page in browser/dev-server and test mobile menu toggle, sticky header scroll, and footer responsiveness.
  - Files: `src/js/main.ts`, `src/js/inquiry-form.ts`, `src/css/components.css`

- [x] Task 3: Redesign Home & Core Institutional Pages (6 Pages)
  - Acceptance: `index.html`, `aboutcambridge.html`, `testimonials.html`, `franchisee.html`, `cambridgeinmedia.html`, `certificatesofauthorizations.html` are created with authentic content, hero banners, value cards, category cards, and responsive layouts.
  - Verify: Build check & visual inspection of each page across desktop and mobile viewports.
  - Files: `index.html`, `aboutcambridge.html`, `testimonials.html`, `franchisee.html`, `cambridgeinmedia.html`, `certificatesofauthorizations.html`

- [x] Task 4: Redesign Study Abroad Destination Pages [Teal Theme] (7 Pages)
  - Acceptance: `usastudent.html`, `ukstudy.html`, `australiastudy.html`, `canadastudy.html`, `newzealandstudy.html`, `europestudy.html`, `singaporestudy.html` redesigned with country statistics, admission criteria, visa roadmaps, university lists, and teal accent actions.
  - Verify: Validate internal links, breadcrumbs, inquiry modal triggers, and responsive grids.
  - Files: `usastudent.html`, `ukstudy.html`, `australiastudy.html`, `canadastudy.html`, `newzealandstudy.html`, `europestudy.html`, `singaporestudy.html`

- [x] Task 5: Redesign Coaching & Language Course Pages [Gold Theme] (6 Pages)
  - Acceptance: `IELTS.html`, `TOEFL.html`, `spokenenglish.html`, `englishexams.html`, `french.html`, `german.html` redesigned with module breakdown, syllabus, CEFR levels, batch schedules, mock test info, and gold accent actions.
  - Verify: Verify course card layouts, level tables, demo class booking triggers, and responsive typography.
  - Files: `IELTS.html`, `TOEFL.html`, `spokenenglish.html`, `englishexams.html`, `french.html`, `german.html`

- [x] Task 6: Redesign Visa Services, Tours & Contact Pages (7 Pages)
  - Acceptance: `immigrationvisa.html`, `studentvisa.html`, `visitorvisa.html`, `internationaltours.html`, `inquiry.html`, `center.html`, `privacypolicy.html` redesigned with step-by-step checklists, tour itineraries, branch cards with Google Maps, interactive inquiry engine, and legal terms.
  - Verify: Test inquiry form validation on submit, branch phone/map links, and tour itinerary accordions.
  - Files: `immigrationvisa.html`, `studentvisa.html`, `visitorvisa.html`, `internationaltours.html`, `inquiry.html`, `center.html`, `privacypolicy.html`

- [x] Task 7: Comprehensive Verification, Link Integrity & Production Build
  - Acceptance: Run automated link checking across all 26 HTML files (0 broken links), run `npm run build` with 100% clean output, verify WCAG contrast and responsive viewport rendering.
  - Verify: Execute test scripts and `npm run build`.
  - Files: `scripts/verify-links.js`, `dist/`
