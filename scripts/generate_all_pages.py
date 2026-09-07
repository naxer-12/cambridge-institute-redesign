import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SVG Icons dictionary
ICONS = {
    'phone': '''<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>''',
    'mail': '''<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>''',
    'whatsapp': '''<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>''',
    'clock': '''<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>''',
    'chevron-down': '''<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>''',
    'chevron-right': '''<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>''',
    'arrow-right': '''<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>''',
    'check': '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>''',
    'globe': '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" x2="22" y1="12" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>''',
    'award': '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>''',
    'book-open': '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>''',
    'shield': '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>''',
    'users': '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>''',
    'map-pin': '''<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>''',
    'menu': '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>''',
    'x': '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>''',
    'plane': '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"/></svg>''',
    'star': '''<svg width="18" height="18" viewBox="0 0 24 24" fill="#C99712" stroke="#C99712" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>''',
    'file-text': '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/><line x1="16" x2="8" y1="13" y2="13"/><line x1="16" x2="8" y1="17" y2="17"/><line x1="10" x2="8" y1="9" y2="9"/></svg>''',
    'gem': '''<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="6 3 18 3 22 9 12 22 2 9"/></svg>'''
}

def render_document(title, description, content_html, active_page='', canonical='index.html'):
    header_html = render_header(active_page)
    footer_html = render_footer()
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | Cambridge Institute</title>
  <meta name="description" content="{description}" />
  <link rel="canonical" href="https://www.cambriz.com/{canonical}" />
  
  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{title} | Cambridge Institute" />
  <meta property="og:description" content="{description}" />
  <meta property="og:url" content="https://www.cambriz.com/{canonical}" />
  <meta property="og:site_name" content="Cambridge Institute Ahmedabad" />
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- Main Application CSS -->
  <link rel="stylesheet" href="/src/css/main.css" />
  <link rel="stylesheet" href="/src/css/components.css" />
</head>
<body>
  {header_html}
  
  <main id="main-content">
    {content_html}
  </main>
  
  {footer_html}
  
  <!-- Main Script -->
  <script type="module" src="/src/js/main.ts"></script>
</body>
</html>'''

def render_header(active_page=''):
    return f'''
    <!-- Top Utility Bar -->
    <div class="utility-bar">
      <div class="container utility-bar__inner">
        <div class="utility-bar__contacts">
          <a href="tel:+919998806666" class="utility-bar__item">
            {ICONS['phone']}
            <span><strong>Call Us:</strong> +91 99988 06666, 8866232322</span>
          </a>
          <a href="mailto:info@cambriz.com" class="utility-bar__item">
            {ICONS['mail']}
            <span>info@cambriz.com</span>
          </a>
          <a href="https://api.whatsapp.com/send?phone=919998806666&text=Hi%20Cambridge%20Institute" target="_blank" rel="noopener noreferrer" class="utility-bar__item" style="color: #0B6A56; font-weight: 600;">
            {ICONS['whatsapp']}
            <span>WhatsApp Us</span>
          </a>
        </div>
        <div class="utility-bar__hours">
          {ICONS['clock']}
          <span>Mon - Sat: 8:00 AM - 8:00 PM | Sun: 10:30 AM - 1:30 PM</span>
        </div>
      </div>
    </div>

    <!-- Main Header -->
    <header class="site-header">
      <div class="container site-header__inner">
        <a href="index.html" class="brand-logo" aria-label="Cambridge Institute Home">
          <div class="brand-logo__wordmark">
            <span class="brand-logo__primary">Cambridge</span>
            <span class="brand-logo__secondary">Institute</span>
          </div>
        </a>

        <!-- Desktop Navigation -->
        <nav class="nav-desktop" aria-label="Main Navigation">
          <div class="nav-item">
            <a href="index.html" class="nav-link {'active' if active_page == 'home' else ''}">Home</a>
          </div>

          <div class="nav-item">
            <a href="aboutcambridge.html" class="nav-link {'active' if active_page in ['about', 'testimonials', 'franchisee', 'media', 'authorizations'] else ''}">
              About Us {ICONS['chevron-down']}
            </a>
            <div class="dropdown-menu">
              <a href="aboutcambridge.html" class="dropdown-item {'active' if active_page == 'about' else ''}">About Cambridge</a>
              <a href="testimonials.html" class="dropdown-item {'active' if active_page == 'testimonials' else ''}">Testimonials</a>
              <a href="franchisee.html" class="dropdown-item {'active' if active_page == 'franchisee' else ''}">Franchisee / Associate</a>
              <a href="cambridgeinmedia.html" class="dropdown-item {'active' if active_page == 'media' else ''}">Cambridge In Media</a>
              <a href="certificatesofauthorizations.html" class="dropdown-item {'active' if active_page == 'authorizations' else ''}">Certificates Of Authorizations</a>
            </div>
          </div>

          <div class="nav-item">
            <a href="usastudent.html" class="nav-link {'active' if active_page in ['study_usa', 'study_uk', 'study_australia', 'study_nz', 'study_canada', 'study_europe', 'study_singapore'] else ''}">
              Study Abroad {ICONS['chevron-down']}
            </a>
            <div class="dropdown-menu">
              <a href="usastudent.html" class="dropdown-item {'active' if active_page == 'study_usa' else ''}">USA Student Visa</a>
              <a href="ukstudy.html" class="dropdown-item {'active' if active_page == 'study_uk' else ''}">UK Study</a>
              <a href="australiastudy.html" class="dropdown-item {'active' if active_page == 'study_australia' else ''}">Australia Study</a>
              <a href="newzealandstudy.html" class="dropdown-item {'active' if active_page == 'study_nz' else ''}">New Zealand Study</a>
              <a href="canadastudy.html" class="dropdown-item {'active' if active_page == 'study_canada' else ''}">Canada Study</a>
              <a href="europestudy.html" class="dropdown-item {'active' if active_page == 'study_europe' else ''}">Europe Study</a>
              <a href="singaporestudy.html" class="dropdown-item {'active' if active_page == 'study_singapore' else ''}">Singapore Study</a>
            </div>
          </div>

          <div class="nav-item">
            <a href="IELTS.html" class="nav-link {'active' if active_page in ['ielts', 'toefl', 'spoken_english', 'english_exams', 'french', 'german'] else ''}">
              Coaching {ICONS['chevron-down']}
            </a>
            <div class="dropdown-menu">
              <a href="IELTS.html" class="dropdown-item {'active' if active_page == 'ielts' else ''}">IELTS Coaching</a>
              <a href="TOEFL.html" class="dropdown-item {'active' if active_page == 'toefl' else ''}">TOEFL iBT</a>
              <a href="spokenenglish.html" class="dropdown-item {'active' if active_page == 'spoken_english' else ''}">Spoken English</a>
              <a href="englishexams.html" class="dropdown-item {'active' if active_page == 'english_exams' else ''}">English Exams &amp; BEC</a>
              <a href="french.html" class="dropdown-item {'active' if active_page == 'french' else ''}">French Language Classes</a>
              <a href="german.html" class="dropdown-item {'active' if active_page == 'german' else ''}">German Language Classes</a>
            </div>
          </div>

          <div class="nav-item">
            <a href="immigrationvisa.html" class="nav-link {'active' if active_page in ['immigration_visa', 'student_visa', 'visitor_visa'] else ''}">
              Visa Services {ICONS['chevron-down']}
            </a>
            <div class="dropdown-menu">
              <a href="immigrationvisa.html" class="dropdown-item {'active' if active_page == 'immigration_visa' else ''}">Immigration &amp; PR Visa</a>
              <a href="studentvisa.html" class="dropdown-item {'active' if active_page == 'student_visa' else ''}">Student Visa</a>
              <a href="visitorvisa.html" class="dropdown-item {'active' if active_page == 'visitor_visa' else ''}">Visitor / Tourist Visa</a>
            </div>
          </div>

          <div class="nav-item">
            <a href="internationaltours.html" class="nav-link {'active' if active_page == 'tours' else ''}">International Tours</a>
          </div>

          <div class="nav-item">
            <a href="center.html" class="nav-link {'active' if active_page == 'centers' else ''}">Centers</a>
          </div>

          <div class="nav-item">
            <a href="inquiry.html" class="nav-link {'active' if active_page == 'inquiry' else ''}">Contact</a>
          </div>
        </nav>

        <!-- Header Actions -->
        <div class="header-actions">
          <a href="inquiry.html" class="btn btn-primary">Apply Now</a>
          <a href="center.html" class="btn btn-secondary">Contact</a>
          <button class="mobile-toggle" aria-label="Toggle navigation menu">
            {ICONS['menu']}
          </button>
        </div>
      </div>
    </header>

    <!-- Mobile Drawer Navigation -->
    <div class="mobile-drawer" role="dialog" aria-modal="true" aria-label="Mobile Navigation">
      <div class="mobile-drawer__panel">
        <div class="mobile-drawer__header">
          <div class="brand-logo">
            <div class="brand-logo__wordmark">
              <span class="brand-logo__primary">Cambridge</span>
              <span class="brand-logo__secondary">Institute</span>
            </div>
          </div>
          <button class="mobile-drawer__close" aria-label="Close navigation">
            {ICONS['x']}
          </button>
        </div>

        <div class="mobile-drawer__nav">
          <a href="index.html" class="mobile-nav-link" style="font-weight: 600; color: var(--color-navy-900);">Home</a>

          <div class="mobile-nav-group">
            <button class="mobile-nav-group__title">About Us {ICONS['chevron-down']}</button>
            <div class="mobile-nav-group__items">
              <a href="aboutcambridge.html" class="mobile-nav-link">About Cambridge</a>
              <a href="testimonials.html" class="mobile-nav-link">Testimonials</a>
              <a href="franchisee.html" class="mobile-nav-link">Franchisee / Associate</a>
              <a href="cambridgeinmedia.html" class="mobile-nav-link">Cambridge In Media</a>
              <a href="certificatesofauthorizations.html" class="mobile-nav-link">Certificates Of Authorizations</a>
            </div>
          </div>

          <div class="mobile-nav-group">
            <button class="mobile-nav-group__title">Study Abroad {ICONS['chevron-down']}</button>
            <div class="mobile-nav-group__items">
              <a href="usastudent.html" class="mobile-nav-link">USA Student Visa</a>
              <a href="ukstudy.html" class="mobile-nav-link">UK Study</a>
              <a href="australiastudy.html" class="mobile-nav-link">Australia Study</a>
              <a href="newzealandstudy.html" class="mobile-nav-link">New Zealand Study</a>
              <a href="canadastudy.html" class="mobile-nav-link">Canada Study</a>
              <a href="europestudy.html" class="mobile-nav-link">Europe Study</a>
              <a href="singaporestudy.html" class="mobile-nav-link">Singapore Study</a>
            </div>
          </div>

          <div class="mobile-nav-group">
            <button class="mobile-nav-group__title">Coaching {ICONS['chevron-down']}</button>
            <div class="mobile-nav-group__items">
              <a href="IELTS.html" class="mobile-nav-link">IELTS Coaching</a>
              <a href="TOEFL.html" class="mobile-nav-link">TOEFL iBT</a>
              <a href="spokenenglish.html" class="mobile-nav-link">Spoken English</a>
              <a href="englishexams.html" class="mobile-nav-link">English Exams &amp; BEC</a>
              <a href="french.html" class="mobile-nav-link">French Language Classes</a>
              <a href="german.html" class="mobile-nav-link">German Language Classes</a>
            </div>
          </div>

          <div class="mobile-nav-group">
            <button class="mobile-nav-group__title">Visa Services {ICONS['chevron-down']}</button>
            <div class="mobile-nav-group__items">
              <a href="immigrationvisa.html" class="mobile-nav-link">Immigration Visa</a>
              <a href="studentvisa.html" class="mobile-nav-link">Student Visa</a>
              <a href="visitorvisa.html" class="mobile-nav-link">Visitor Visa</a>
            </div>
          </div>

          <a href="internationaltours.html" class="mobile-nav-link">International Tours</a>
          <a href="center.html" class="mobile-nav-link">Centers</a>
          <a href="inquiry.html" class="mobile-nav-link">Contact &amp; Inquiry</a>
        </div>

        <div class="mobile-drawer__footer">
          <a href="inquiry.html" class="btn btn-primary btn-full">Apply Now</a>
          <a href="https://api.whatsapp.com/send?phone=919998806666" target="_blank" class="btn btn-teal btn-full">
            {ICONS['whatsapp']} WhatsApp Us
          </a>
        </div>
      </div>
    </div>
    '''

def render_footer():
    return f'''
    <!-- Site Footer -->
    <footer class="site-footer">
      <div class="container">
        <div class="site-footer__grid">
          <!-- Col 1: About & Info -->
          <div>
            <div class="brand-logo" style="margin-bottom: var(--space-4);">
              <div class="brand-logo__emblem" style="background-color: var(--color-gold-600); color: #0C1A45;">CI</div>
              <div class="brand-logo__text">
                <span class="brand-logo__title" style="color: #ffffff;">Cambridge Institute</span>
                <span class="brand-logo__subtitle" style="color: var(--color-gold-500);">Excellence in Global Education</span>
              </div>
            </div>
            <p class="site-footer__brand-desc">
              Institutional Excellence in Global Education. A premier centre of excellence for Spoken English, French, German, IELTS, TOEFL, BEC &amp; Study Abroad Visas since 1999.
            </p>
            <div class="site-footer__contact-item">
              {ICONS['map-pin']}
              <span>307-308, 3rd Floor, Shree Ratnamaya Palace, Beside Rohtawala Flats, Opp. Deepak Petrol Pump, Satellite, Ahmedabad-380060, Gujarat, India</span>
            </div>
          </div>

          <!-- Col 2: Direct Contact Details -->
          <div>
            <h3 class="site-footer__heading">Contact &amp; Support</h3>
            <div class="site-footer__contact-item">
              {ICONS['phone']}
              <div>
                <div><strong>Call:</strong> +91 99988 06666</div>
                <div><strong>Mobile:</strong> +91 8866232322</div>
              </div>
            </div>
            <div class="site-footer__contact-item">
              {ICONS['mail']}
              <div><strong>Email:</strong> info@cambriz.com</div>
            </div>
            <div class="site-footer__contact-item">
              {ICONS['clock']}
              <div>
                <div>Mon to Sat: 8:00 AM to 8:00 PM</div>
                <div>Sunday: 10:30 AM to 1:30 PM</div>
              </div>
            </div>
          </div>

          <!-- Col 3: Key Services -->
          <div>
            <h3 class="site-footer__heading">Key Services</h3>
            <ul class="site-footer__list">
              <li><a href="IELTS.html" class="site-footer__link">IELTS Coaching (Academic/General)</a></li>
              <li><a href="TOEFL.html" class="site-footer__link">TOEFL iBT Classes</a></li>
              <li><a href="spokenenglish.html" class="site-footer__link">Spoken English Mastery</a></li>
              <li><a href="french.html" class="site-footer__link">French Language Classes</a></li>
              <li><a href="german.html" class="site-footer__link">German Language Classes</a></li>
              <li><a href="usastudent.html" class="site-footer__link">USA Student Visas</a></li>
              <li><a href="canadastudy.html" class="site-footer__link">Canada Study &amp; SDS</a></li>
              <li><a href="immigrationvisa.html" class="site-footer__link">Immigration Visa Services</a></li>
            </ul>
          </div>

          <!-- Col 4: Institution Links & Legal -->
          <div>
            <h3 class="site-footer__heading">Institution</h3>
            <ul class="site-footer__list">
              <li><a href="aboutcambridge.html" class="site-footer__link">About Cambridge</a></li>
              <li><a href="testimonials.html" class="site-footer__link">Student Testimonials</a></li>
              <li><a href="certificatesofauthorizations.html" class="site-footer__link">Official Authorizations</a></li>
              <li><a href="franchisee.html" class="site-footer__link">Franchisee Opportunities</a></li>
              <li><a href="cambridgeinmedia.html" class="site-footer__link">Press &amp; Media</a></li>
              <li><a href="center.html" class="site-footer__link">Branch Centers</a></li>
              <li><a href="privacypolicy.html" class="site-footer__link">Privacy Policy &amp; Terms</a></li>
            </ul>
          </div>
        </div>

        <!-- Bottom Bar -->
        <div class="site-footer__bottom">
          <div>
            &copy; 2026 Cambridge Institute. All Rights Reserved. Institutional Excellence in Global Education.
          </div>
          <div class="social-links">
            <a href="https://facebook.com" target="_blank" rel="noopener noreferrer" class="social-link" aria-label="Facebook">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
            </a>
            <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" class="social-link" aria-label="Instagram">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="20" height="20" x="2" y="2" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"/></svg>
            </a>
            <a href="https://api.whatsapp.com/send?phone=919998806666" target="_blank" rel="noopener noreferrer" class="social-link" aria-label="WhatsApp">
              {ICONS['whatsapp']}
            </a>
          </div>
        </div>
      </div>
    </footer>

    <!-- Floating Action Bar for Mobile Viewports -->
    <div class="floating-mobile-bar" aria-label="Quick Actions">
      <a href="tel:+919998806666" class="btn btn-secondary btn-sm" style="font-size: 12px; padding: 0 8px;">
        {ICONS['phone']} Call
      </a>
      <a href="https://api.whatsapp.com/send?phone=919998806666" target="_blank" rel="noopener noreferrer" class="btn btn-teal btn-sm" style="font-size: 12px; padding: 0 8px;">
        {ICONS['whatsapp']} WhatsApp
      </a>
      <a href="inquiry.html" class="btn btn-primary btn-sm" style="font-size: 12px; padding: 0 8px;">
        Apply Now
      </a>
    </div>
    '''

def render_page_hero(title, subtitle, breadcrumb_parent, breadcrumb_current, badge_text='', badge_class='badge--navy'):
    badge_html = f'<div style="margin-bottom: var(--space-3);"><span class="badge {badge_class}">{badge_text}</span></div>' if badge_text else ''
    return f'''
    <section class="hero-banner hero-banner--inner">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span class="breadcrumb__sep">/</span>
          <span>{breadcrumb_parent}</span>
          <span class="breadcrumb__sep">/</span>
          <span style="color: #ffffff; font-weight: 500;">{breadcrumb_current}</span>
        </nav>
        {badge_html}
        <h1 class="h1-title" style="color: #ffffff; margin-bottom: var(--space-3);">{title}</h1>
        <p class="body-large" style="color: #E2E8F0; max-width: 780px;">{subtitle}</p>
      </div>
    </section>
    '''

def render_quick_inquiry_card(title="Book Free Profile Assessment", desc="Get personalized counsel on admission, visa eligibility, and preparation batches."):
    return f'''
    <div class="inquiry-card">
      <div style="margin-bottom: var(--space-6);">
        <span class="caption-eyebrow caption-eyebrow--gold">Quick Counseling</span>
        <h3 class="h3-title" style="margin-top: 4px; margin-bottom: 8px;">{title}</h3>
        <p class="body-small">{desc}</p>
      </div>
      
      <form class="js-inquiry-form" novalidate>
        <div class="form-grid">
          <div class="form-group">
            <label class="form-label" for="inq_name">Full Name *</label>
            <input type="text" id="inq_name" name="name" class="form-control" placeholder="Enter your full name" required />
            <span class="form-error">Please enter your full name.</span>
          </div>

          <div class="form-group">
            <label class="form-label" for="inq_phone">Mobile Number *</label>
            <input type="tel" id="inq_phone" name="phone" class="form-control" placeholder="+91 99988 06666" required />
            <span class="form-error">Please enter a valid phone number.</span>
          </div>

          <div class="form-group">
            <label class="form-label" for="inq_email">Email Address *</label>
            <input type="email" id="inq_email" name="email" class="form-control" placeholder="yourname@gmail.com" required />
            <span class="form-error">Please enter a valid email address.</span>
          </div>

          <div class="form-group">
            <label class="form-label" for="inq_coaching">Coaching *</label>
            <select id="inq_coaching" name="coaching" class="form-control" required>
              <option value="" disabled selected>Select Coaching Program</option>
              <option value="IELTS Coaching">IELTS Coaching (Academic / General)</option>
              <option value="TOEFL iBT">TOEFL iBT Preparation</option>
              <option value="Spoken English">Spoken English &amp; Fluency</option>
              <option value="German Language">German Language (A1–B2)</option>
              <option value="French Language">French Language (A1–B2)</option>
              <option value="Cambridge English / BEC">Cambridge English &amp; BEC</option>
              <option value="PTE Academic">PTE Academic</option>
              <option value="GRE / GMAT">GRE / GMAT Preparation</option>
              <option value="Other Coaching">Other / General Counseling</option>
            </select>
            <span class="form-error">Please select a coaching program.</span>
          </div>

          <div class="form-group form-group--full">
            <label class="form-label" for="inq_msg">Specific Requirements / Message</label>
            <textarea id="inq_msg" name="message" class="form-control" placeholder="Mention your current education, target score, or preferred batch timings..."></textarea>
          </div>

          <div class="form-group form-group--full">
            <button type="submit" class="btn btn-primary btn-full">
              Submit Inquiry &amp; Request Callback {ICONS['arrow-right']}
            </button>
            <div class="form-status" style="display: none; margin-top: 12px; padding: 12px; border-radius: var(--radius-md); font-size: 14px; text-align: center;"></div>
            <p class="body-small" style="text-align: center; margin-top: 8px; font-size: 12px;">
              🔒 We respect your privacy. Your information is 100% confidential.
            </p>
          </div>
        </div>
      </form>
    </div>
    '''

def render_sidebar(active_slug=''):
    study_links = [
        ('usastudent.html', 'USA Student Visa', 'study_usa'),
        ('ukstudy.html', 'UK Study Abroad', 'study_uk'),
        ('australiastudy.html', 'Australia Study', 'study_australia'),
        ('canadastudy.html', 'Canada Study (SDS)', 'study_canada'),
        ('europestudy.html', 'Europe & Germany Study', 'study_europe'),
        ('newzealandstudy.html', 'New Zealand Study', 'study_nz'),
        ('singaporestudy.html', 'Singapore Study', 'study_singapore'),
    ]
    coaching_links = [
        ('IELTS.html', 'IELTS Coaching (Band 7+)', 'ielts'),
        ('TOEFL.html', 'TOEFL iBT Preparation', 'toefl'),
        ('spokenenglish.html', 'Spoken English & Fluency', 'spoken_english'),
        ('french.html', 'French Language Classes', 'french'),
        ('german.html', 'German Language Classes', 'german'),
        ('englishexams.html', 'Cambridge Exams & BEC', 'english_exams'),
    ]
    visa_links = [
        ('immigrationvisa.html', 'Immigration & PR Visa', 'immigration_visa'),
        ('studentvisa.html', 'Student Visa Guidance', 'student_visa'),
        ('visitorvisa.html', 'Visitor / Tourist Visa', 'visitor_visa'),
        ('internationaltours.html', 'International Tours', 'tours'),
    ]

    def make_items(items):
        out = ''
        for href, label, slug in items:
            active = 'active' if slug == active_slug else ''
            out += f'<a href="{href}" class="sidebar-link {active}">{label} {ICONS["chevron-right"]}</a>'
        return out

    return f'''
    <aside>
      <div class="sidebar-widget">
        <h4 class="sidebar-widget__title">Study Abroad</h4>
        <div class="sidebar-links">
          {make_items(study_links)}
        </div>
      </div>

      <div class="sidebar-widget">
        <h4 class="sidebar-widget__title">Language Coaching</h4>
        <div class="sidebar-links">
          {make_items(coaching_links)}
        </div>
      </div>

      <div class="sidebar-widget">
        <h4 class="sidebar-widget__title">Visa &amp; Travel</h4>
        <div class="sidebar-links">
          {make_items(visa_links)}
        </div>
      </div>

      <div class="sidebar-widget" style="background: var(--color-navy-900); color: #ffffff; border: none;">
        <h4 class="sidebar-widget__title" style="color: var(--color-gold-500); border-color: var(--color-gold-600);">Need Immediate Help?</h4>
        <p class="body-small" style="color: #CBD5E1; margin-bottom: var(--space-4);">
          Talk to our Senior Counselors in Ahmedabad for spot evaluation.
        </p>
        <a href="tel:+919998806666" class="btn btn-gold btn-full btn-sm" style="margin-bottom: var(--space-2);">
          {ICONS['phone']} +91 99988 06666
        </a>
        <a href="https://api.whatsapp.com/send?phone=919998806666" target="_blank" rel="noopener noreferrer" class="btn btn-teal btn-full btn-sm">
          {ICONS['whatsapp']} Chat on WhatsApp
        </a>
      </div>
    </aside>
    '''

def write_file(filename, content):
    path = os.path.join(BASE_DIR, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated {filename}")

print("Generator core loaded.")
