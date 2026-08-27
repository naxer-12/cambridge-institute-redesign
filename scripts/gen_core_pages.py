import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from generate_all_pages import render_document, render_page_hero, render_quick_inquiry_card, render_sidebar, write_file, ICONS

def generate_index():
    content = f'''
    <!-- 1. Hero Banner Pattern -->
    <section class="hero-banner">
      <div class="container hero-banner__inner">
        <div class="hero-banner__content">
          <span class="hero-banner__eyebrow">The Best Language &amp; Study Abroad Institute</span>
          <h1 class="display-title hero-banner__title">Welcome to Cambridge Institute</h1>
          <p class="hero-banner__description">
            Empowering global careers since 1999. Ahmedabad's premier institute for IELTS, TOEFL, Spoken English, French, German, and end-to-end Study Abroad &amp; Immigration Visas.
          </p>
          <div class="hero-banner__actions">
            <a href="inquiry.html" class="btn btn-gold">Explore Programs {ICONS['arrow-right']}</a>
            <a href="center.html" class="btn btn-secondary">Visit Our Centers</a>
          </div>

          <div class="hero-banner__stats">
            <div>
              <div class="hero-stat__number">25+</div>
              <div class="hero-stat__label">Years of Excellence</div>
            </div>
            <div>
              <div class="hero-stat__number">15,000+</div>
              <div class="hero-stat__label">Students Trained</div>
            </div>
            <div>
              <div class="hero-stat__number">98.4%</div>
              <div class="hero-stat__label">Visa Success Rate</div>
            </div>
          </div>
        </div>

        <div class="hero-banner__form-col">
          {render_quick_inquiry_card("Get Free Career &amp; Visa Counseling", "Fill details for spot profile evaluation &amp; course batches.")}
        </div>
      </div>
    </section>

    <!-- 2. Who We Are (Feature / Value Cards) -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="caption-eyebrow">Institutional Values</span>
          <h2 class="h2-title">Who We Are &amp; What We Stand For</h2>
          <p class="body-regular">
            Founded by eminent educationalist Mr. Devang Solanki (Author of <em>Enrich Your English Series</em>), Cambridge Institute has set benchmarks in foreign language training, IELTS/TOEFL coaching, and ethical visa consultancy across Gujarat.
          </p>
        </div>

        <div class="value-grid">
          <!-- Commitment -->
          <div class="value-card">
            <div class="value-card__icon" style="color: var(--color-navy-900);">
              {ICONS['award']}
            </div>
            <h3 class="value-card__title">Commitment</h3>
            <p class="value-card__text">
              We provide a complete, responsive, and resourceful obligation toward student goals, ensuring maximum score achievement and visa success.
            </p>
          </div>

          <!-- Customer Oriented -->
          <div class="value-card">
            <div class="value-card__icon" style="color: var(--color-teal-700);">
              {ICONS['users']}
            </div>
            <h3 class="value-card__title">Customer Oriented</h3>
            <p class="value-card__text">
              We believe that satisfying the student and parent is the secret to growing clientele and building trusted educational pathways worldwide.
            </p>
          </div>

          <!-- Integrity -->
          <div class="value-card">
            <div class="value-card__icon" style="color: var(--color-gold-600);">
              {ICONS['shield']}
            </div>
            <h3 class="value-card__title">Integrity</h3>
            <p class="value-card__text">
              We realize the immense importance of confidential financial data and academic aspirations entrusted to us, upholding absolute transparency.
            </p>
          </div>

          <!-- Responsibility -->
          <div class="value-card">
            <div class="value-card__icon" style="color: var(--color-navy-900);">
              {ICONS['book-open']}
            </div>
            <h3 class="value-card__title">Responsibility</h3>
            <p class="value-card__text">
              We conduct our business with the highest standards of ethics, regulatory compliance, and strict adherence to international immigration laws.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. What We Offer (Category Cards Grid) -->
    <section class="section" style="background-color: var(--color-surface); border-top: 1px solid var(--color-border); border-bottom: 1px solid var(--color-border);">
      <div class="container">
        <div class="section-header">
          <span class="caption-eyebrow caption-eyebrow--teal">Comprehensive Services</span>
          <h2 class="h2-title">What We Offer</h2>
          <p class="body-regular">
            Explore our specialized categories designed to take you from language mastery to world-class university admission and permanent residency.
          </p>
        </div>

        <div class="service-grid">
          <!-- Visa Services (Navy) -->
          <div class="service-card service-card--navy">
            <div class="service-card__header">
              {ICONS['shield']}
              <h3 class="service-card__title">Visa Services</h3>
            </div>
            <div class="service-card__body">
              <ul class="service-card__list">
                <li class="service-card__item">
                  <a href="immigrationvisa.html">Immigration &amp; PR Visa <span class="arrow">&rarr;</span></a>
                </li>
                <li class="service-card__item">
                  <a href="studentvisa.html">Student Visa Guidance <span class="arrow">&rarr;</span></a>
                </li>
                <li class="service-card__item">
                  <a href="visitorvisa.html">Visitor / Tourist Visa <span class="arrow">&rarr;</span></a>
                </li>
                <li class="service-card__item">
                  <a href="internationaltours.html">International Tours <span class="arrow">&rarr;</span></a>
                </li>
              </ul>
              <a href="immigrationvisa.html" class="btn btn-primary btn-full">
                View all Visa Services &rarr;
              </a>
            </div>
          </div>

          <!-- Study Abroad (Teal) -->
          <div class="service-card service-card--teal">
            <div class="service-card__header">
              {ICONS['globe']}
              <h3 class="service-card__title">Study Abroad</h3>
            </div>
            <div class="service-card__body">
              <ul class="service-card__list">
                <li class="service-card__item">
                  <a href="usastudent.html">USA Student Visa <span class="arrow">&rarr;</span></a>
                </li>
                <li class="service-card__item">
                  <a href="ukstudy.html">UK Higher Education <span class="arrow">&rarr;</span></a>
                </li>
                <li class="service-card__item">
                  <a href="canadastudy.html">Canada Study (SDS Stream) <span class="arrow">&rarr;</span></a>
                </li>
                <li class="service-card__item">
                  <a href="australiastudy.html">Australia Study (Subclass 500) <span class="arrow">&rarr;</span></a>
                </li>
                <li class="service-card__item">
                  <a href="europestudy.html">Europe &amp; Germany Study <span class="arrow">&rarr;</span></a>
                </li>
                <li class="service-card__item">
                  <a href="newzealandstudy.html">New Zealand Study <span class="arrow">&rarr;</span></a>
                </li>
                <li class="service-card__item">
                  <a href="singaporestudy.html">Singapore Study <span class="arrow">&rarr;</span></a>
                </li>
              </ul>
              <a href="usastudent.html" class="btn btn-teal btn-full">
                View all Study Abroad Programs &rarr;
              </a>
            </div>
          </div>

          <!-- Coaching (Gold) -->
          <div class="service-card service-card--gold">
            <div class="service-card__header">
              {ICONS['book-open']}
              <h3 class="service-card__title">Coaching &amp; Languages</h3>
            </div>
            <div class="service-card__body">
              <ul class="service-card__list">
                <li class="service-card__item">
                  <a href="IELTS.html">IELTS Coaching (Band 7+) <span class="arrow">&rarr;</span></a>
                </li>
                <li class="service-card__item">
                  <a href="TOEFL.html">TOEFL iBT Test Prep <span class="arrow">&rarr;</span></a>
                </li>
                <li class="service-card__item">
                  <a href="spokenenglish.html">Spoken English Fluency <span class="arrow">&rarr;</span></a>
                </li>
                <li class="service-card__item">
                  <a href="french.html">French Language (A1-B2) <span class="arrow">&rarr;</span></a>
                </li>
                <li class="service-card__item">
                  <a href="german.html">German Language (Goethe) <span class="arrow">&rarr;</span></a>
                </li>
                <li class="service-card__item">
                  <a href="englishexams.html">Cambridge English &amp; BEC <span class="arrow">&rarr;</span></a>
                </li>
              </ul>
              <a href="IELTS.html" class="btn btn-gold btn-full">
                View all Coaching Programs &rarr;
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. Associate / Franchise CTA -->
    <section class="section">
      <div class="container">
        <div class="associate-cta">
          <div class="associate-cta__inner">
            <div class="associate-cta__content">
              <span class="caption-eyebrow caption-eyebrow--teal">Partnership Opportunity</span>
              <h2 class="h2-title" style="margin-top: 4px; margin-bottom: var(--space-4);">Want to be our Associate?</h2>
              <p class="body-regular" style="margin-bottom: var(--space-6);">
                Transform your city with Cambridge Institute's proven educational franchise model. Benefit from 25+ years of brand authority, standardized curriculum for IELTS, TOEFL, PTE, BEC, Spoken English, French &amp; German, and comprehensive marketing and lead generation support.
              </p>
              <div style="display: flex; gap: var(--space-4); flex-wrap: wrap;">
                <a href="franchisee.html" class="btn btn-teal">Know More &rarr;</a>
                <a href="franchisee.html#apply" class="btn btn-secondary">Join Us as Partner</a>
              </div>
            </div>
            <div class="associate-cta__image-wrap"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- 5. Testimonials -->
    <section class="section" style="background-color: var(--color-surface); border-top: 1px solid var(--color-border);">
      <div class="container">
        <div class="section-header">
          <span class="caption-eyebrow caption-eyebrow--gold">Student Success</span>
          <h2 class="h2-title">What Our Achievers Say</h2>
          <p class="body-regular">Read real reviews from students who achieved high test scores and international university admissions with Cambridge Institute.</p>
        </div>

        <div class="testimonials-grid">
          <!-- Card 1 -->
          <div class="testimonial-card">
            <div>
              <div class="testimonial-card__quote-mark">&ldquo;</div>
              <p class="testimonial-card__text">
                The interactive group coaching for IELTS and the state-of-the-art audio-visual language laboratory completely transformed my learning experience. The approach to test strategy here truly guarantees success!
              </p>
            </div>
            <div class="testimonial-card__author">
              <div class="testimonial-card__avatar">SN</div>
              <div>
                <div class="testimonial-card__name">Sukoon Nima</div>
                <div class="testimonial-card__role">IELTS 8.0 Achiever &bull; University of Melbourne</div>
              </div>
            </div>
          </div>

          <!-- Card 2 -->
          <div class="testimonial-card">
            <div>
              <div class="testimonial-card__quote-mark">&ldquo;</div>
              <p class="testimonial-card__text">
                Their international standard curriculum for German A1 and A2 helped me secure my student visa for Germany seamlessly. The faculty's dedication and embassy interview prep is unmatched in Ahmedabad.
              </p>
            </div>
            <div class="testimonial-card__author">
              <div class="testimonial-card__avatar">SM</div>
              <div>
                <div class="testimonial-card__name">Sukoon Manas</div>
                <div class="testimonial-card__role">Europe Study Visa &bull; TU Munich</div>
              </div>
            </div>
          </div>

          <!-- Card 3 -->
          <div class="testimonial-card">
            <div>
              <div class="testimonial-card__quote-mark">&ldquo;</div>
              <p class="testimonial-card__text">
                The mock visa interviews conducted by Mr. Devang Solanki and the senior team gave me tremendous confidence before my US Consulate interview in Mumbai. I received my F-1 visa on the first attempt!
              </p>
            </div>
            <div class="testimonial-card__author">
              <div class="testimonial-card__avatar">PP</div>
              <div>
                <div class="testimonial-card__name">Priyank Patel</div>
                <div class="testimonial-card__role">USA Student Visa &bull; Northeastern University</div>
              </div>
            </div>
          </div>

          <!-- Card 4 -->
          <div class="testimonial-card">
            <div>
              <div class="testimonial-card__quote-mark">&ldquo;</div>
              <p class="testimonial-card__text">
                Cambridge Institute's French DELF coaching is exceptionally thorough. The phonetics training and daily speaking circles enabled me to score B2 and claim full language points for my Canada PR!
              </p>
            </div>
            <div class="testimonial-card__author">
              <div class="testimonial-card__avatar">AS</div>
              <div>
                <div class="testimonial-card__name">Ananya Shah</div>
                <div class="testimonial-card__role">DELF B2 Qualified &bull; Canada Express Entry PR</div>
              </div>
            </div>
          </div>
        </div>

        <div style="text-align: center; margin-top: var(--space-8);">
          <a href="testimonials.html" class="btn btn-secondary">Read All Verified Testimonials &rarr;</a>
        </div>
      </div>
    </section>

    <!-- 6. Authorizations & Accreditations Strip -->
    <section class="section--sm" style="background-color: var(--color-canvas); border-top: 1px solid var(--color-border);">
      <div class="container" style="text-align: center;">
        <p class="caption-eyebrow" style="margin-bottom: var(--space-4); color: var(--color-muted-600);">
          Recognized Partner &amp; Certified Testing Center Node
        </p>
        <div style="display: flex; justify-content: center; align-items: center; gap: var(--space-8); flex-wrap: wrap; opacity: 0.85;">
          <span style="font-weight: 700; color: var(--color-navy-900); font-size: 16px;">British Council Partner</span>
          <span style="color: var(--color-border-strong);">&bull;</span>
          <span style="font-weight: 700; color: var(--color-navy-900); font-size: 16px;">IDP IELTS Certified</span>
          <span style="color: var(--color-border-strong);">&bull;</span>
          <span style="font-weight: 700; color: var(--color-navy-900); font-size: 16px;">ETS TOEFL iBT Center</span>
          <span style="color: var(--color-border-strong);">&bull;</span>
          <span style="font-weight: 700; color: var(--color-navy-900); font-size: 16px;">Pearson PTE Academic</span>
          <span style="color: var(--color-border-strong);">&bull;</span>
          <span style="font-weight: 700; color: var(--color-navy-900); font-size: 16px;">Cambridge English Assessment</span>
        </div>
      </div>
    </section>
    '''
    html = render_document("English & Foreign Languages Experts | Cambridge Institute Ahmedabad", 
                           "Cambridge Institute in Ahmedabad offers expert coaching in Spoken English, IELTS, TOEFL, French, German, and Study Abroad Visas since 1999.", 
                           content, active_page='home', canonical='index.html')
    write_file('index.html', html)

def generate_about():
    content = f'''
    {render_page_hero("About Cambridge Institute", "Learn about our heritage, pedagogical methodology, leadership, and our 25-year commitment to academic excellence in Ahmedabad.", "About Us", "About Cambridge", "Established 1999", "badge--navy")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--gold">Our Heritage &amp; Vision</span>
            <h2 class="h2-title" style="margin-top: 4px;">Pioneering Global Education in Gujarat</h2>
            <p>
              Cambridge Institute of English and Foreign Languages is a premier training institute headquartered in Ahmedabad, Gujarat. Headed by <strong>Mr. Devang Solanki</strong>, an eminent educationalist and acclaimed author of the <em>Enrich Your English Series</em>, the institute has grown from modest beginnings in 1999 into Gujarat's foremost centre of excellence.
            </p>
            <p>
              Over the last two and a half decades, Cambridge Institute has empowered more than 15,000 students to master English fluency, score Band 7+ and 8+ in IELTS, achieve high percentiles in TOEFL iBT, and attain certified proficiency in French (DELF) and German (Goethe-Zertifikat A1-B2).
            </p>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">Academic Philosophy</span>
            <h3 class="h3-title" style="margin-top: 4px;">The Cambridge Institute Advantage</h3>
            <div class="feature-list" style="margin-top: var(--space-4);">
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>State-of-the-Art Audio-Visual Language Laboratory:</strong> Computerized listening and speaking booths equipped with authentic international testing software for IELTS and TOEFL.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Proprietary Curriculum &amp; Publications:</strong> Four specialized books published under the <em>Enrich Your English Series</em> addressing specific vocabulary and phonetics challenges faced by regional learners.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Certified &amp; Experienced Trainers:</strong> All faculty members hold British Council, IDP, ETS, Alliance Française, or Goethe-Institut accreditations.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Holistic Personality &amp; Interview Grooming:</strong> Beyond test scores, we develop real-world public speaking, debate, accent clarity, and visa interview confidence.
                </div>
              </div>
            </div>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow">Leadership Message</span>
            <h3 class="h3-title" style="margin-top: 4px;">A Message from Mr. Devang Solanki</h3>
            <p style="font-style: italic; color: var(--color-ink-800); border-left: 3px solid var(--color-navy-900); padding-left: var(--space-4); margin: var(--space-4) 0;">
              "Language is not merely a subject; it is the master key to global opportunity. At Cambridge Institute, our approach guarantees success because we treat each learner as an individual with unique ambitions. Whether you are stepping into a foreign university classroom or presenting in an international boardroom, our mission is to ensure you speak with absolute clarity, authority, and confidence."
            </p>
            <p><strong>Mr. Devang Solanki</strong><br/><span class="body-small">Director &amp; Founder, Author of Enrich Your English</span></p>
          </div>
        </div>

        {render_sidebar('about')}
      </div>
    </section>
    '''
    html = render_document("About Cambridge Institute | 25+ Years of Excellence in Ahmedabad", 
                           "Discover Cambridge Institute's history, mission, leadership under Mr. Devang Solanki, and state-of-the-art language training facilities in Ahmedabad.", 
                           content, active_page='about', canonical='aboutcambridge.html')
    write_file('aboutcambridge.html', html)

def generate_testimonials():
    content = f'''
    {render_page_hero("Student Testimonials &amp; Success Stories", "Read authentic reviews from high-scoring students and successful visa applicants across Gujarat.", "About Us", "Testimonials", "Verified Achievers", "badge--gold")}

    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="caption-eyebrow caption-eyebrow--gold">Hall of Fame</span>
          <h2 class="h2-title">Real Words from Real Achievers</h2>
          <p class="body-regular">Over 15,000 alumni are studying and working across the USA, UK, Canada, Australia, Germany, France, and Singapore.</p>
        </div>

        <div class="testimonials-grid">
          <div class="testimonial-card">
            <div>
              <div class="testimonial-card__quote-mark">&ldquo;</div>
              <p class="testimonial-card__text">
                "The interactive group coaching for IELTS and the audio-visual language laboratory completely transformed my learning experience. The approach to learning here truly guarantees success. Scored Band 8.0 on first attempt!"
              </p>
            </div>
            <div class="testimonial-card__author">
              <div class="testimonial-card__avatar">SN</div>
              <div>
                <div class="testimonial-card__name">Sukoon Nima</div>
                <div class="testimonial-card__role">IELTS 8.0 &bull; University of Melbourne, Australia</div>
              </div>
            </div>
          </div>

          <div class="testimonial-card">
            <div>
              <div class="testimonial-card__quote-mark">&ldquo;</div>
              <p class="testimonial-card__text">
                "Their international standard curriculum for German A1 and A2 helped me secure my student visa for Europe seamlessly. The faculty's dedication to grammar precision and speaking practice is unmatched."
              </p>
            </div>
            <div class="testimonial-card__author">
              <div class="testimonial-card__avatar">SM</div>
              <div>
                <div class="testimonial-card__name">Sukoon Manas</div>
                <div class="testimonial-card__role">German A2 &bull; TU Munich Master's Program</div>
              </div>
            </div>
          </div>

          <div class="testimonial-card">
            <div>
              <div class="testimonial-card__quote-mark">&ldquo;</div>
              <p class="testimonial-card__text">
                "I had severe hesitation speaking English in front of people. After joining Cambridge Institute's 2-month Spoken English course, my confidence soared. The vocabulary drills and group discussions changed my professional life."
              </p>
            </div>
            <div class="testimonial-card__author">
              <div class="testimonial-card__avatar">RD</div>
              <div>
                <div class="testimonial-card__name">Rohan Desai</div>
                <div class="testimonial-card__role">Spoken English Graduate &bull; Software Engineer, Ahmedabad</div>
              </div>
            </div>
          </div>

          <div class="testimonial-card">
            <div>
              <div class="testimonial-card__quote-mark">&ldquo;</div>
              <p class="testimonial-card__text">
                "The visa team at Cambridge International is exceptional. They helped me with financial documentation, university SOP reviews, and conducted 5 mock visa interviews. Received my USA F-1 visa without any hassle."
              </p>
            </div>
            <div class="testimonial-card__author">
              <div class="testimonial-card__avatar">PP</div>
              <div>
                <div class="testimonial-card__name">Priyank Patel</div>
                <div class="testimonial-card__role">USA Student Visa &bull; Northeastern University (Boston)</div>
              </div>
            </div>
          </div>

          <div class="testimonial-card">
            <div>
              <div class="testimonial-card__quote-mark">&ldquo;</div>
              <p class="testimonial-card__text">
                "I needed DELF B2 in French for my Canadian Express Entry immigration points. Cambridge Institute provided intensive weekend coaching with past DELF test papers. Cleared with flying colors!"
              </p>
            </div>
            <div class="testimonial-card__author">
              <div class="testimonial-card__avatar">AS</div>
              <div>
                <div class="testimonial-card__name">Ananya Shah</div>
                <div class="testimonial-card__role">French DELF B2 &bull; Canada Express Entry PR</div>
              </div>
            </div>
          </div>

          <div class="testimonial-card">
            <div>
              <div class="testimonial-card__quote-mark">&ldquo;</div>
              <p class="testimonial-card__text">
                "TOEFL iBT preparation at Cambridge Institute's computer lab gave me real-time test simulations. Scored 112/120 and got admitted to Imperial College London with a scholarship!"
              </p>
            </div>
            <div class="testimonial-card__author">
              <div class="testimonial-card__avatar">HV</div>
              <div>
                <div class="testimonial-card__name">Harshil Vora</div>
                <div class="testimonial-card__role">TOEFL 112 &bull; Imperial College London</div>
              </div>
            </div>
          </div>
        </div>

        <div style="margin-top: var(--space-12);">
          {render_quick_inquiry_card("Ready to Write Your Own Success Story?", "Join thousands of successful alumni. Book a free diagnostic test &amp; counseling session today.")}
        </div>
      </div>
    </section>
    '''
    html = render_document("Student Testimonials & Success Stories | Cambridge Institute", 
                           "Read verified student reviews and success stories for IELTS, TOEFL, Spoken English, French, German, and Study Abroad Visas at Cambridge Institute.", 
                           content, active_page='testimonials', canonical='testimonials.html')
    write_file('testimonials.html', html)

def generate_franchisee():
    content = f'''
    {render_page_hero("Franchisee &amp; Associate Opportunities", "Partner with Gujarat's premier language training and visa consultancy brand. Established 1999.", "About Us", "Franchisee", "Business Opportunity", "badge--teal")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">Institutional Partnership</span>
            <h2 class="h2-title" style="margin-top: 4px;">Join the Cambridge Institute Network</h2>
            <p>
              Cambridge Institute of English and Foreign Languages is inviting visionary entrepreneurs, educators, and academy owners to join hands as our official Franchisees and Regional Associates across Gujarat and India.
            </p>
            <p>
              Under the leadership of <strong>Mr. Devang Solanki</strong>, we offer a comprehensive turnkey educational ecosystem covering Spoken English, IELTS, TOEFL, PTE, BEC, French, German A1-B2, and Global Study Abroad &amp; Immigration Visas.
            </p>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow">Support Ecosystem</span>
            <h3 class="h3-title" style="margin-top: 4px;">What We Provide to Our Franchise Partners</h3>
            <div class="feature-list" style="margin-top: var(--space-4);">
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Brand Authority &amp; Goodwill:</strong> Immediate leverage of 25+ years of trusted excellence and thousands of successful alumni.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Standardized Curriculum &amp; Books:</strong> Complete supply of student courseware, including the acclaimed <em>Enrich Your English Series</em> books and digital lab software.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Faculty Recruitment &amp; Master Training:</strong> Regular training of your teaching faculty by master trainers certified by IDP, British Council, and ETS.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Central Visa Processing Support:</strong> Full backend visa documentation, SOP drafting, and embassy mock interview support handled by our head office team in Ahmedabad.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Digital Marketing &amp; Student Inquiries:</strong> Targeted local advertising, social media campaigns, and inquiry leads shared with your branch.
                </div>
              </div>
            </div>
          </div>

          <div id="apply" class="content-block">
            <span class="caption-eyebrow caption-eyebrow--gold">Associate Application</span>
            <h3 class="h3-title" style="margin-top: 4px; margin-bottom: var(--space-4);">Apply for a Franchise Center</h3>
            <form class="js-inquiry-form" novalidate>
              <div class="form-grid">
                <div class="form-group">
                  <label class="form-label" for="fr_name">Applicant Name *</label>
                  <input type="text" id="fr_name" class="form-control" placeholder="Enter your full name" required />
                </div>
                <div class="form-group">
                  <label class="form-label" for="fr_phone">Contact Number *</label>
                  <input type="tel" id="fr_phone" class="form-control" placeholder="+91 99988 06666" required />
                </div>
                <div class="form-group">
                  <label class="form-label" for="fr_email">Email Address *</label>
                  <input type="email" id="fr_email" class="form-control" placeholder="yourname@domain.com" required />
                </div>
                <div class="form-group">
                  <label class="form-label" for="fr_city">Proposed City / Territory *</label>
                  <input type="text" id="fr_city" class="form-control" placeholder="e.g. Rajkot, Surat, Bhavnagar, Gandhinagar" required />
                </div>
                <div class="form-group form-group--full">
                  <label class="form-label" for="fr_bg">Current Educational / Business Background</label>
                  <textarea id="fr_bg" class="form-control" placeholder="Describe your existing premises, coaching institute, or business background..."></textarea>
                </div>
                <div class="form-group form-group--full">
                  <button type="submit" class="btn btn-teal btn-full">
                    Submit Franchise Application &rarr;
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>

        {render_sidebar('franchisee')}
      </div>
    </section>
    '''
    html = render_document("Franchisee & Associate Opportunities | Cambridge Institute", 
                           "Join Cambridge Institute as a franchise partner or associate. Benefit from 25+ years of brand goodwill, IELTS/language curriculum, and centralized visa processing.", 
                           content, active_page='franchisee', canonical='franchisee.html')
    write_file('franchisee.html', html)

def generate_media():
    content = f'''
    {render_page_hero("Cambridge In Media &amp; Press", "Media features, academic seminars, newspaper coverage, and institutional milestones.", "About Us", "Media &amp; Press", "News &amp; Events", "badge--navy")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--gold">Press Coverage</span>
            <h2 class="h2-title" style="margin-top: 4px;">Cambridge Institute in the Headlines</h2>
            <p>
              Over the years, Cambridge Institute and founder Mr. Devang Solanki have been featured in leading national and regional publications including <em>The Times of India</em>, <em>Divya Bhaskar</em>, <em>Gujarat Samachar</em>, and <em>Ahmedabad Mirror</em> for groundbreaking contributions to language pedagogy and ethical study-abroad guidance.
            </p>
          </div>

          <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: var(--space-6); margin-bottom: var(--space-8);">
            <div class="value-card">
              <span class="badge badge--navy" style="margin-bottom: var(--space-2);">The Times of India</span>
              <h4 class="h4-title" style="margin-bottom: var(--space-2);">"Transforming English Fluency in Gujarat"</h4>
              <p class="body-small">Feature article on Mr. Devang Solanki's <em>Enrich Your English</em> books and their impact on Gujarati-medium learners aiming for global universities.</p>
            </div>

            <div class="value-card">
              <span class="badge badge--teal" style="margin-bottom: var(--space-2);">Divya Bhaskar</span>
              <h4 class="h4-title" style="margin-bottom: var(--space-2);">"Foreign Language Demand Surges"</h4>
              <p class="body-small">Coverage on Cambridge Institute's German &amp; French training batches tailored for engineering students and healthcare workers migrating to Europe.</p>
            </div>

            <div class="value-card">
              <span class="badge badge--gold" style="margin-bottom: var(--space-2);">Gujarat Samachar</span>
              <h4 class="h4-title" style="margin-bottom: var(--space-2);">"Mastering IELTS &amp; Visa Interviews"</h4>
              <p class="body-small">Educational column sharing Cambridge Institute's proven tips for clearing student visa interviews for USA and UK universities.</p>
            </div>

            <div class="value-card">
              <span class="badge badge--navy" style="margin-bottom: var(--space-2);">Education Excellence Award</span>
              <h4 class="h4-title" style="margin-bottom: var(--space-2);">Best Language Institute in Ahmedabad</h4>
              <p class="body-small">Felicitation honoring Cambridge Institute's 25 years of educational commitment and student welfare in Gujarat.</p>
            </div>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow">Academic Seminars</span>
            <h3 class="h3-title" style="margin-top: 4px;">Seminars &amp; University Delegations</h3>
            <p>
              Cambridge Institute regularly hosts international university delegates, British Council masterclass sessions, and IDP workshops across Ahmedabad, Vadodara, and Surat to provide direct face-to-face interaction for students and parents.
            </p>
          </div>
        </div>

        {render_sidebar('media')}
      </div>
    </section>
    '''
    html = render_document("Cambridge In Media & Press Coverage | Cambridge Institute Ahmedabad", 
                           "Explore media mentions, newspaper articles, awards, and seminar events featuring Cambridge Institute and Mr. Devang Solanki.", 
                           content, active_page='media', canonical='cambridgeinmedia.html')
    write_file('cambridgeinmedia.html', html)

def generate_authorizations():
    content = f'''
    {render_page_hero("Certificates of Authorizations &amp; Accreditations", "Official partnerships and certified testing center credentials with international examining bodies.", "About Us", "Authorizations", "Verified Credentials", "badge--teal")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">Authorized Test Partners</span>
            <h2 class="h2-title" style="margin-top: 4px;">Globally Recognized Accreditations</h2>
            <p>
              Cambridge Institute operates in strict alignment with international examination bodies and educational authorities. Our credentials guarantee authentic test preparation, genuine study materials, and direct exam registration facilities for students in Ahmedabad.
            </p>
          </div>

          <div style="display: flex; flex-direction: column; gap: var(--space-6); margin-bottom: var(--space-8);">
            <!-- IDP IELTS -->
            <div class="value-card" style="display: grid; grid-template-columns: 80px 1fr; gap: var(--space-4); align-items: center;">
              <div style="width: 70px; height: 70px; border-radius: var(--radius-md); background: var(--color-navy-50); display: flex; align-items: center; justify-content: center; color: var(--color-navy-900); font-weight: 800; font-size: 18px;">
                IDP
              </div>
              <div>
                <span class="badge badge--navy">Official Partner</span>
                <h3 class="h4-title" style="margin: 4px 0;">IDP Education IELTS Certified Referral &amp; Training Partner</h3>
                <p class="body-small">Authorized to prepare students and register official IELTS on Paper &amp; Computer-delivered tests.</p>
              </div>
            </div>

            <!-- British Council -->
            <div class="value-card" style="display: grid; grid-template-columns: 80px 1fr; gap: var(--space-4); align-items: center;">
              <div style="width: 70px; height: 70px; border-radius: var(--radius-md); background: var(--color-teal-50); display: flex; align-items: center; justify-content: center; color: var(--color-teal-700); font-weight: 800; font-size: 18px;">
                BC
              </div>
              <div>
                <span class="badge badge--teal">Registered Node</span>
                <h3 class="h4-title" style="margin: 4px 0;">British Council IELTS Partnership Programme</h3>
                <p class="body-small">Accredited member supporting international candidate registration and preparation standards.</p>
              </div>
            </div>

            <!-- ETS TOEFL -->
            <div class="value-card" style="display: grid; grid-template-columns: 80px 1fr; gap: var(--space-4); align-items: center;">
              <div style="width: 70px; height: 70px; border-radius: var(--radius-md); background: var(--color-gold-50); display: flex; align-items: center; justify-content: center; color: var(--color-gold-700); font-weight: 800; font-size: 18px;">
                ETS
              </div>
              <div>
                <span class="badge badge--gold">Authorized Center</span>
                <h3 class="h4-title" style="margin: 4px 0;">ETS TOEFL iBT Official Preparation Center</h3>
                <p class="body-small">Equipped with ETS authorized prep material, official practice software, and certified trainers.</p>
              </div>
            </div>

            <!-- Pearson PTE -->
            <div class="value-card" style="display: grid; grid-template-columns: 80px 1fr; gap: var(--space-4); align-items: center;">
              <div style="width: 70px; height: 70px; border-radius: var(--radius-md); background: var(--color-navy-50); display: flex; align-items: center; justify-content: center; color: var(--color-navy-900); font-weight: 800; font-size: 18px;">
                PTE
              </div>
              <div>
                <span class="badge badge--navy">Pearson Partner</span>
                <h3 class="h4-title" style="margin: 4px 0;">Pearson Test of English (PTE Academic) Recognized Trainer</h3>
                <p class="body-small">Specialized AI-scored computerized lab testing matching the exact PTE testing algorithm.</p>
              </div>
            </div>
          </div>
        </div>

        {render_sidebar('authorizations')}
      </div>
    </section>
    '''
    html = render_document("Certificates Of Authorizations & Accreditations | Cambridge Institute", 
                           "Official certification of authorizations from IDP, British Council, ETS TOEFL, Pearson PTE, and Cambridge Assessment for Cambridge Institute Ahmedabad.", 
                           content, active_page='authorizations', canonical='certificatesofauthorizations.html')
    write_file('certificatesofauthorizations.html', html)

if __name__ == '__main__':
    generate_index()
    generate_about()
    generate_testimonials()
    generate_franchisee()
    generate_media()
    generate_authorizations()
    print("Core slice generation completed.")
