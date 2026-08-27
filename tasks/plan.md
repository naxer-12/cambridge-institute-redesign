# Implementation Plan: Cambridge Institute Redesign

## 1. Architecture & Component Hierarchy

The project is structured as a high-performance modern Multi-Page Application (MPA) with a central design token system and shared modular components.

```
                    ┌────────────────────────┐
                    │     Design Tokens      │
                    │  (colors, type, space) │
                    └───────────┬────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        ▼                       ▼                       ▼
┌───────────────┐       ┌───────────────┐       ┌───────────────┐
│  Utility Bar  │       │  Site Header  │       │  Site Footer  │
│  & Top Strip  │       │ & Mobile Menu │       │ & Disclosures │
└───────┬───────┘       └───────┬───────┘       └───────┬───────┘
        │                       │                       │
        └───────────────────────┼───────────────────────┘
                                │
    ┌───────────────────────────┼───────────────────────────┐
    ▼                           ▼                           ▼
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│   Core / Brand   │    │   Study Abroad   │    │     Coaching     │
│   Pages (6)      │    │   Pages (7)      │    │     Pages (6)    │
│  (Navy Theme)    │    │  (Teal Theme)    │    │  (Gold Theme)    │
└──────────────────┘    └──────────────────┘    └──────────────────┘
    │                           │                           │
    └───────────────────────────┼───────────────────────────┘
                                │
    ┌───────────────────────────┴───────────────────────────┐
    ▼                                                       ▼
┌──────────────────┐                        ┌──────────────────┐
│   Visa & Tours   │                        │ Contact, Inquiry │
│   Pages (4)      │                        │  & Centers (3)   │
└──────────────────┘                        └──────────────────┘
```

---

## 2. Implementation Phases & Order

### Phase 1: Setup & Design Tokens Engine
- Initialize Vite + TypeScript multi-page configuration with all 26 page inputs.
- Construct `tokens.css` with CSS custom properties exact to `design.md` & design image.
- Construct global reset, responsive container (`width: min(100% - 48px, 1280px)`), typography scale (Inter), 8px spacing utility, elevation levels (1, 2, 3), and button/input variants.
- Place optimized SVG icons and brand assets in `/public`.

### Phase 2: Core Components & Layout Shells
- Build `SiteHeader` with desktop navigation, active states, dropdowns, and scrolled elevation.
- Build `UtilityBar` with verified phone numbers, email, WhatsApp link, and opening hours.
- Build `MobileMenu` full-screen responsive drawer with accordion submenus.
- Build `SiteFooter` 4-column layout with corporate address, quick links, category tags, and legal info.
- Build reusable `InquiryForm` component with field validation, dynamic course/country selectors, and submission feedback.
- Build `HeroBanner`, `ValueCard`, `ServiceCard`, `TestimonialCard`, `AssociateCTA`, and `PageHeader` modules.

### Phase 3: Vertical Page Slices

#### Slice 3.1: Home & Institutional Core (6 Pages)
- `index.html`: Complete homepage with hero, 4 value cards, 3 service category cards (Visa, Study Abroad, Coaching), interactive quick inquiry, associate split CTA, testimonial slider, partner badges, and stats counter.
- `aboutcambridge.html`: Institute overview, 20+ years heritage, mission, pedagogy, state-of-the-art audio-visual language lab, faculty qualifications.
- `testimonials.html`: Interactive filterable review matrix (IELTS 8+ scorers, visa approvals, foreign language graduates) with quote cards, video highlights, and verifiable student stories.
- `franchisee.html`: Franchise & Associate program, ROI breakdown, curriculum supply, faculty training, marketing assistance, associate inquiry form.
- `cambridgeinmedia.html`: Press coverage gallery, newspaper clippings, television interviews, academic seminar features, photo gallery with modal zoom.
- `certificatesofauthorizations.html`: IDP IELTS Partner, British Council, Pearson PTE, ETS TOEFL, Cambridge English Assessment credentials, interactive authorization cards with license IDs.

#### Slice 3.2: Study Abroad Category [Teal Theme] (7 Pages)
- `usastudent.html`: USA higher education guide, Ivy League vs State Universities, F-1 visa timeline, SEVIS, STEM OPT 3-year extension, financial documentation checklist, intake calendar.
- `ukstudy.html`: Russell Group universities, 1-year master's degrees, Graduate Route 2-year post-study work visa, CAS clearance, tuition fee & scholarship guide.
- `australiastudy.html`: Group of Eight (Go8), Subclass 500 visa, CRICOS course finder, Post-Study Work Stream (PSW 485), PR points pathways, cost of living.
- `canadastudy.html`: Designated Learning Institutions (DLIs), SDS vs Non-SDS visa streams, PGWP rules, Co-op work terms, Provincial Nominee Program (PNP) integration.
- `newzealandstudy.html`: NZQA 8 universities & polytechnics, Pathway Student Visa, Green List skills, post-study work visa rights, living costs.
- `europestudy.html`: Study in Germany (Tuition-free public universities, APS certificate, blocked account), France, Netherlands, Ireland, Schengen travel benefits.
- `singaporestudy.html`: Singapore education hub, top global universities (NUS, NTU, PSB Academy), tuition grant scheme, fast-track degrees.

#### Slice 3.3: Coaching & Languages Category [Gold Theme] (6 Pages)
- `IELTS.html`: Academic vs General Training, Band 7+ and 8+ strategies, 4 modules (Listening, Reading, Writing, Speaking), mock test schedules, batch timings, band score calculator.
- `TOEFL.html`: TOEFL iBT computer-based test format, score scale (0-120), audio-visual lab practice, speaking evaluation, certified test preparation.
- `spokenenglish.html`: Fluency mastery from Beginner to Advanced, public speaking, group discussions, accent neutralization, corporate English, grammar & vocabulary builder.
- `englishexams.html`: Cambridge English Qualifications (A2, B1, B2 First, C1 Advanced), Business English Certificate (BEC Preliminary/Vantage/Higher), Pearson PTE Academic, Duolingo English Test.
- `french.html`: CEFR Levels A1, A2, B1, B2, C1, DELF / DALF exam prep, Canada immigration TEF / TCF test coaching, French cultural immersion.
- `german.html`: Goethe-Zertifikat A1 to C1 preparation, TestDaF for German universities, medical professional track (Fachsprachenprüfung), grammar drills & conversational practice.

#### Slice 3.4: Visa Services & Tours Category [Navy Theme] (4 Pages)
- `immigrationvisa.html`: Permanent Residency pathways, Canada Express Entry CRS calculator, Australia SkillSelect (189/190/491), UK Skilled Worker, eligibility assessment.
- `studentvisa.html`: Step-by-step visa assistance roadmap, SOP & LOR editing, mock embassy interviews, financial verification, pre-departure orientation.
- `visitorvisa.html`: Tourist & business visa processing for USA (B1/B2), UK Standard Visitor, Schengen 27 countries, Canada, Australia, Singapore, invitation letters & travel insurance.
- `internationaltours.html`: Academic delegations, university immersion tours, youth leadership trips to UK, USA, Europe, Dubai, Singapore with complete day-by-day itineraries and inquiry.

#### Slice 3.5: Contact, Centers & Utilities (3 Pages)
- `inquiry.html`: Full interactive multi-step profile evaluation & booking form, program filter, visa category, target intake, branch selector.
- `center.html`: Branch center directory with Ahmedabad Satellite Head Office, Navrangpura, Maninagar, Nikol, Vadodara, Surat; addresses, direct phone numbers, hours, Google Maps directions.
- `privacypolicy.html`: Comprehensive privacy policy, student data security, GDPR/IT Act compliance, cookies disclosure, and terms of service.

### Phase 4: Interactivity, Scripts & State Engine
- Responsive navigation drawer toggle with trap-focus and keyboard ESC support.
- Scrolled header shadow observer.
- Quick inquiry client-side validation with instant visual feedback and success confirmation state.
- Testimonials filter tabs and accessible controls.
- FAQ accordion with accessible `aria-expanded` attributes.
- Mobile bottom floating quick-action bar (Call, WhatsApp, Apply).

### Phase 5: Verification, Testing & Build
- Automated multi-page link and route validator (verifies all 26 HTML files and every internal link).
- Vite production build execution (`npm run build`).
- Responsive and layout inspection across breakpoints.
- Design token audit against `design.md` and design board image.
