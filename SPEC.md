# Spec: Cambridge Institute Website Redesign (cambriz.com)

## Objective

Redesign the entire web presence for **Cambridge Institute** (https://www.cambriz.com) — a premier English and foreign-language education, visa consultancy, coaching, and study-abroad institute based in Ahmedabad, Gujarat. 

The redesigned site faithfully implements the official **Cambridge Institute Frontend Design System** (`design.md` and `cambridge-institute-design-system (1).png`), replacing the dated legacy theme with a modern, authoritative, accessible, responsive, and trustworthy digital experience.

### Target Audiences & Personas
1. **Aspiring Study Abroad Students:** Seeking admission and student visas for USA, UK, Canada, Australia, Europe, New Zealand, Singapore.
2. **Language & Coaching Aspirants:** Seeking IELTS Band 7+, TOEFL iBT, Spoken English fluency, Cambridge BEC certifications, and French/German DELF/Goethe training.
3. **Immigration & Visa Applicants:** Seeking professional guidance for PR (Express Entry, PNP, SkillSelect), visitor/tourist visas, and legal documentation.
4. **Prospective Franchisees & Associates:** Entrepreneurs seeking institutional partnerships, franchise models, and curriculum support.
5. **Corporate & Educational Tour Participants:** Groups seeking international university delegations and academic tours.

---

## Assumptions Made

1. **Architecture:** Multi-Page Application (MPA) with component-driven architecture powered by Vite, HTML5, CSS3 with strict Design System custom property tokens, and TypeScript for interactive controls (navigation drawer, modal consultation, country filters, FAQ accordions, testimonial carousel, form validations).
2. **Design Tokens:** Strict adherence to color palette (Primary Navy `#0C1A45`, Teal Green `#0B6A56`, Mustard Gold `#C99712`, Ink `#151515`, Canvas `#F7F6F2`, Surface `#FFFFFF`, Border `#E6E8EC`), 8px spacing grid, Inter typography hierarchy, and subtle elevation tokens.
3. **Responsive Target:** Pixel-perfect across Mobile (<768px), Tablet (768px–1279px), and Desktop (≥1280px).
4. **Data Fidelity:** 100% preservation and enrichment of genuine institutional data (Ahmedabad headquarters, branch centers, exact phone numbers `+91 99988 06666` / `8866232322`, email `info@cambriz.com`, course syllabi, visa criteria, testimonials, and authorization credentials).

---

## Tech Stack

- **Build Tool:** Vite 6 / Node.js
- **Markup & Layout:** Semantic HTML5, CSS Grid (12-column desktop, 6-column tablet, 1-column mobile), Flexbox
- **Design Tokens & Styling:** CSS Custom Properties (`--color-navy-900`, `--color-teal-700`, `--color-gold-600`, `--space-*`, `--radius-*`, `--shadow-*`), Tailwind CSS utility layer for rapid layout composition, Lucide line iconography
- **Interactivity:** Vanilla TypeScript for lightweight, accessible, zero-bloat state management (drawer menus, modal inquiries, filter tabs, interactive tabs, form verification, responsive sliders)
- **Asset Pipeline:** Optimized SVGs, WebP responsive photography with documentary grayscale/contrast treatments, Google Fonts (Inter)

---

## Commands

- **Install Dependencies:** `npm install`
- **Development Server:** `npm run dev` (starts live hot-reloading server on `http://localhost:5173`)
- **Production Build:** `npm run build` (bundles optimized HTML, CSS, JS, and static assets to `dist/`)
- **Preview Production Build:** `npm run preview`
- **Lint & Format:** `npm run lint` / `npm run format`
- **Test / Verification:** `npm run test` (verifies HTML link integrity, responsive markup, accessibility attributes, and token compliance)

---

## Project Structure

```
cambridge-institute-redesign/
├── index.html                           # Home Page
├── aboutcambridge.html                  # About Cambridge Institute
├── testimonials.html                    # Student & Visa Testimonials
├── franchisee.html                      # Franchisee & Associate Opportunities
├── cambridgeinmedia.html                # Media Coverage, Press & News
├── certificatesofauthorizations.html    # Official Authorizations & Accreditations
├── immigrationvisa.html                 # PR & Immigration Visa Services
├── studentvisa.html                     # Student Visa Roadmap & Guidance
├── visitorvisa.html                     # Visitor & Tourist Visa Services
├── internationaltours.html              # University Delegations & Educational Tours
├── usastudent.html                      # USA Study Abroad & F-1 Visa
├── ukstudy.html                         # UK Higher Education & Graduate Route
├── australiastudy.html                  # Australia Study & Subclass 500 Visa
├── newzealandstudy.html                 # New Zealand Study & Post-Study Work
├── canadastudy.html                     # Canada Study, SDS & PGWP
├── europestudy.html                     # Europe & Germany (Tuition-Free) Study
├── singaporestudy.html                  # Singapore Study & Fast-Track Degrees
├── TOEFL.html                           # TOEFL iBT Coaching & Lab Training
├── IELTS.html                           # IELTS Academic & General (Band 7+)
├── spokenenglish.html                   # Spoken English & Fluency Mastery
├── englishexams.html                    # Cambridge English Qualifications & BEC
├── french.html                          # French Language Classes (DELF / TEF)
├── german.html                          # German Language Classes (Goethe / TestDaF)
├── inquiry.html                         # Quick Inquiry & Profile Assessment
├── center.html                          # Branch Centers & Satellite Office Directory
├── privacypolicy.html                   # Privacy Policy & Legal Disclosures
├── src/
│   ├── css/
│   │   ├── tokens.css                   # Brand Tokens (Colors, Typography, Spacing, Radii, Shadows)
│   │   ├── components.css               # Header, Footer, Hero, Cards, Forms, Modals
│   │   └── main.css                     # Global styles, resets, utility classes
│   ├── js/
│   │   ├── main.ts                      # Navigation, Mobile Menu, Sticky Header, Analytics hook
│   │   ├── inquiry-form.ts              # Interactive multi-field validation & submission
│   │   ├── testimonials-slider.ts       # Accessible carousel / filter tabs
│   │   └── components/                  # Shared web components / layout helpers
│   └── data/
│       ├── navigation.json              # Nav menu structure & active routes
│       ├── courses.json                 # Coaching courses & curricula
│       ├── countries.json               # Study abroad destinations & requirements
│       ├── visas.json                   # Visa category details
│       ├── centers.json                 # Branch centers, addresses & maps
│       └── testimonials.json            # Verified student reviews & scores
├── public/
│   ├── images/                          # Brand imagery, student avatars, documentary classroom photos
│   └── favicon.svg                      # Cambridge Institute emblem
├── tasks/
│   ├── plan.md                          # Phase-by-phase implementation plan
│   └── todo.md                          # Granular checklist with acceptance criteria
├── package.json                         # Build & dev dependencies
├── tsconfig.json                        # TypeScript configuration
├── vite.config.ts                       # Multi-page Vite configuration
└── SPEC.md                              # This specification
```

---

## Code Style & Conventions

- **Semantic HTML5:** Every page uses semantic landmarks `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`.
- **CSS Architecture:** Variables prefixed with `--color-`, `--space-`, `--radius-`, `--font-`, `--shadow-`.
- **Naming Conventions:** BEM-inspired / component utility classes (`site-header`, `utility-bar`, `hero-banner`, `service-card--teal`, `service-card--gold`, `inquiry-form`).
- **Accessibility:** Explicit `<label>` for every form input, `aria-expanded` on accordion and mobile drawers, `aria-current="page"` on active navigation items, visible `focus-visible` rings with `--color-navy-900` outline.

### Example Component Code Pattern

```html
<!-- Service Category Card Example -->
<div class="service-card service-card--teal">
  <div class="service-card__header">
    <svg class="service-card__icon" aria-hidden="true" width="24" height="24"><use href="#icon-globe"/></svg>
    <h3 class="service-card__title">Study Abroad</h3>
  </div>
  <p class="service-card__description">Comprehensive admission and student visa guidance for world-leading institutions.</p>
  <ul class="service-card__list" role="list">
    <li><a href="usastudent.html">USA Student Visa <span class="arrow" aria-hidden="true">→</span></a></li>
    <li><a href="ukstudy.html">UK Study <span class="arrow" aria-hidden="true">→</span></a></li>
    <li><a href="canadastudy.html">Canada Study <span class="arrow" aria-hidden="true">→</span></a></li>
    <li><a href="australiastudy.html">Australia Study <span class="arrow" aria-hidden="true">→</span></a></li>
  </ul>
  <a href="usastudent.html" class="btn btn--teal-outline service-card__action">View all Study Abroad Programs →</a>
</div>
```

---

## Testing Strategy

1. **Multi-Page Build Integrity:** Vite production build must compile all 26 HTML entrypoints with zero missing asset errors or broken imports.
2. **Link Verification:** Automated verification script to test every internal link across all 26 HTML pages, ensuring 0 broken `404` hrefs.
3. **Accessibility (a11y):** WCAG AA contrast compliance on primary navy (`#0C1A45`), teal (`#0B6A56`), gold (`#C99712`), input labels, and interactive keyboard tab index.
4. **Responsive Layouts:** Viewport verification at 375px (iPhone), 768px (iPad portrait), 1024px (iPad landscape), 1280px (Desktop), and 1440px+ (Large desktop).
5. **Interactive Component Testing:** Verify mobile menu open/close, consultation inquiry form validation, country filter tabs, and FAQ accordions.

---

## Boundaries

- **Always:** Use design system tokens, preserve authentic contact and course information, ensure semantic HTML, support keyboard navigation, provide accessible form labels and error feedback.
- **Ask First:** Removing any existing core service or radically changing academic program structures.
- **Never:** Use neon gradients, unapproved fonts, broken external links, placeholder fake phone numbers, or unstyled raw templates.

---

## Success Criteria

- [x] All 26 pages completely redesigned with full, rich, authentic institutional content.
- [x] Design tokens accurately reflect the official Cambridge Institute design board (`design.md` & PNG).
- [x] Header utility bar, responsive navigation, and mobile hamburger drawer functional across all pages.
- [x] Service categories systematically color-coded: Navy (Visa & Core), Teal Green (Study Abroad), Mustard Gold (Coaching).
- [x] Value cards, interactive inquiry forms, testimonial sliders, associate split CTAs, and 4-column footer implemented.
- [x] Production build passes cleanly with zero errors and 100% link integrity.
