import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from generate_all_pages import render_document, render_page_hero, render_quick_inquiry_card, render_sidebar, write_file, ICONS

def render_country_stats(stats):
    items = ''
    for num, label in stats:
        items += f'''
        <div style="background: var(--color-surface); border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: var(--space-4); text-align: center;">
          <div style="font-size: 22px; font-weight: 700; color: var(--color-teal-700); line-height: 1.2;">{num}</div>
          <div class="body-small" style="margin-top: 4px; font-weight: 500;">{label}</div>
        </div>
        '''
    return f'''
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: var(--space-4); margin-bottom: var(--space-8);">
      {items}
    </div>
    '''

def render_faq_accordion(faqs):
    items = ''
    for q, a in faqs:
        items += f'''
        <div class="accordion-item">
          <button class="accordion-trigger">
            <span>{q}</span>
            {ICONS['chevron-down']}
          </button>
          <div class="accordion-content">
            <p>{a}</p>
          </div>
        </div>
        '''
    return f'''
    <div class="accordion" style="margin-top: var(--space-4);">
      {items}
    </div>
    '''

def generate_usa():
    stats = [
        ('Up to 3 Years', 'STEM OPT Work Permit'),
        ('4,000+', 'Accredited Universities'),
        ('Fall / Spring', 'Major Intakes'),
        ('20 Hrs/Week', 'On-Campus Work Rights')
    ]
    faqs = [
        ('What is the F-1 Student Visa process for USA?', 'After securing admission and receiving your Form I-20 from a SEVP-certified institution, you pay the SEVIS I-901 fee, complete the DS-160 visa application, and schedule two appointments: OFC (Biometrics) and the Consular Interview at the US Embassy/Consulate.'),
        ('What is the STEM OPT extension?', 'Students graduating in Science, Technology, Engineering, or Math (STEM) fields can extend their 12-month Optional Practical Training (OPT) by an additional 24 months, allowing up to 3 full years of work authorization in the USA.'),
        ('Can I get scholarships for US universities?', 'Yes! US universities offer Merit-based scholarships, Graduate Assistantships (GA/TA/RA) covering full tuition waivers and monthly stipends, and institutional grants based on GRE/GMAT and academic records.')
    ]

    content = f'''
    {render_page_hero("USA Student Visa &amp; Higher Education", "Complete admission, scholarship, and F-1 visa interview guidance for top American universities.", "Study Abroad", "USA Student Visa", "Top Global Destination", "badge--teal")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          {render_country_stats(stats)}

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">American Education System</span>
            <h2 class="h2-title" style="margin-top: 4px;">Why Study in the United States?</h2>
            <p>
              The United States hosts the world's most flexible and research-intensive higher education system. American degrees are globally renowned for their academic rigor, cutting-edge technology exposure, and unmatched career mobility.
            </p>
            <p>
              At <strong>Cambridge International</strong> in Ahmedabad, we provide end-to-end guidance from university shortlisting and SOP/LOR editing to SEVIS registration and mock embassy visa interview drills.
            </p>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">Types of Institutions</span>
            <h3 class="h3-title" style="margin-top: 4px;">Higher Education Categories in USA</h3>
            <div class="feature-list" style="margin-top: var(--space-4);">
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Public &amp; State Universities:</strong> Large government-funded institutions with world-class research facilities (e.g. University of California, Purdue, Texas A&amp;M).
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Private Universities &amp; The Ivy League:</strong> Prestigious endowed universities renowned for faculty excellence and global alumni networks (e.g. Harvard, MIT, Columbia, Northeastern).
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Technical &amp; STEM Institutes:</strong> Specialized institutions focusing on engineering, computer science, and data analytics.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Community Colleges (2+2 Pathway):</strong> Affordable 2-year Associate Degree pathways transferring into top 4-year Bachelor's programs.
                </div>
              </div>
            </div>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">Visa Assistance</span>
            <h3 class="h3-title" style="margin-top: 4px;">How Cambridge International Prepares You for the F-1 Visa</h3>
            <p>
              Securing university admission is only the first step. The US F-1 visa interview is decisive. Our dedicated team provides:
            </p>
            <ul style="padding-left: 20px; line-height: 28px; color: var(--color-ink-700);">
              <li>SEVIS I-901 registration &amp; DS-160 document verification</li>
              <li>Financial statement vetting &amp; CA valuation certificate guidance</li>
              <li>1-on-1 mock interviews simulating real US Consulate questions</li>
              <li>Presentation technique coaching &amp; confidence building</li>
              <li>Do's and Don'ts for direct consulate approval</li>
            </ul>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">Frequently Asked Questions</span>
            <h3 class="h3-title" style="margin-top: 4px;">USA Student Visa FAQs</h3>
            {render_faq_accordion(faqs)}
          </div>
        </div>

        {render_sidebar('study_usa')}
      </div>
    </section>
    '''
    html = render_document("USA Student Visa Guidance & Admissions | Cambridge Institute", 
                           "Complete admission and F-1 visa assistance for US universities. SEVIS, financial documentation, mock interviews, and STEM OPT guidance in Ahmedabad.", 
                           content, active_page='study_usa', canonical='usastudent.html')
    write_file('usastudent.html', html)

def generate_uk():
    stats = [
        ('1 Year', "Master's Degree Duration"),
        ('2 Years', 'Graduate Route Post-Study Visa'),
        ('Sept / Jan', 'Primary Intakes'),
        ('20 Hrs/Week', 'Part-Time Work Allowed')
    ]
    faqs = [
        ('What is the Graduate Route Visa in the UK?', 'The Graduate Route allows international students who complete an undergraduate or master’s degree in the UK to stay and work in any sector for 2 years (3 years for PhD graduates) without needing employer sponsorship.'),
        ('Can I study in the UK without IELTS?', 'Yes! Several prestigious UK universities accept Class 12 English marks (typically 70%+ from CBSE/ICSE/Gujarat Board) or medium-of-instruction letters in place of IELTS.'),
        ('How much does a UK Master’s degree cost?', 'Tuition fees range between £13,000 to £24,000 per year depending on the university and program. Because UK Master’s courses are only 1 year in length, overall living and tuition expenses are significantly lower than other countries.')
    ]

    content = f'''
    {render_page_hero("UK Higher Education &amp; Graduate Route", "Study at world-renowned British universities with 1-year Master's programs and 2-year post-study work permits.", "Study Abroad", "UK Study", "Fast-Track Master's", "badge--teal")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          {render_country_stats(stats)}

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">British Excellence</span>
            <h2 class="h2-title" style="margin-top: 4px;">Why Choose the United Kingdom?</h2>
            <p>
              Home to centuries-old academic traditions, Russell Group research institutions, and dynamic cosmopolitan cities, the UK is one of the premier study destinations worldwide.
            </p>
            <p>
              A major advantage of the UK is its <strong>1-year intensive Master's degree</strong> format, which saves a full year of living expenses and tuition fees, allowing graduates to enter the workforce and utilize the <strong>2-year Graduate Route Post-Study Work Visa</strong> ahead of global peers.
            </p>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">Step-by-Step Roadmap</span>
            <h3 class="h3-title" style="margin-top: 4px;">UK Admission &amp; Student Visa Roadmap</h3>
            <div class="feature-list" style="margin-top: var(--space-4);">
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Course &amp; University Selection:</strong> Selecting the right course across Russell Group and modern UK universities.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>CAS (Confirmation of Acceptance for Studies):</strong> Securing your unconditional offer and CAS letter.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Financial Maintenance Proof:</strong> Maintaining required 28-day funds for tuition balance and UKVI living costs.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Visa Application &amp; TB Test:</strong> Preparing TB clearance, biometric appointments, and interview readiness.
                </div>
              </div>
            </div>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">Common Inquiries</span>
            <h3 class="h3-title" style="margin-top: 4px;">UK Study FAQs</h3>
            {render_faq_accordion(faqs)}
          </div>
        </div>

        {render_sidebar('study_uk')}
      </div>
    </section>
    '''
    html = render_document("Study in UK | 1-Year Masters & Graduate Route Visa | Cambridge Institute", 
                           "Complete admission and visa guidance for UK universities. 1-year master's degrees, 2-year post-study work visa (PSW), scholarships, and CAS processing in Ahmedabad.", 
                           content, active_page='study_uk', canonical='ukstudy.html')
    write_file('ukstudy.html', html)

def generate_australia():
    stats = [
        ('2 to 4 Years', 'Post-Study Work Rights (PSW)'),
        ('Group of 8', 'World Top 100 Universities'),
        ('Feb / July', 'Main Academic Intakes'),
        ('48 Hrs/Fortnight', 'Part-Time Work Permitted')
    ]
    faqs = [
        ('What is the Subclass 500 Student Visa?', 'The Subclass 500 visa allows international students to live, study, and work part-time in Australia for the full duration of their registered CRICOS course.'),
        ('What are the PR pathways after studying in Australia?', 'Graduates can apply for the Subclass 485 Temporary Graduate Visa, gain local work experience, and lodge an Expression of Interest (EOI) under SkillSelect for Subclass 189, 190 (State Nominated), or 491 (Regional) visas.'),
        ('What is the Genuine Student (GS) requirement?', 'The Australian Department of Home Affairs requires students to demonstrate genuine intent to complete quality education, backed by strong academic and financial profiles.')
    ]

    content = f'''
    {render_page_hero("Study in Australia &amp; Subclass 500 Visa", "Study at world top-ranked Group of Eight (Go8) universities with generous post-study work rights and permanent residency pathways.", "Study Abroad", "Australia Study", "High Quality of Life", "badge--teal")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          {render_country_stats(stats)}

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">Australian Higher Education</span>
            <h2 class="h2-title" style="margin-top: 4px;">Why Study in Australia?</h2>
            <p>
              Australia offers world-class academic institutions, stunning landscapes, safe multicultural cities, and high post-graduation employment rates. Seven Australian cities rank among the world’s top student destinations.
            </p>
            <p>
              Cambridge International provides comprehensive guidance on CRICOS registered courses, university scholarships, Genuine Student (GS) compliance, and Subclass 500 student visa lodging.
            </p>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">Institutions &amp; Degrees</span>
            <h3 class="h3-title" style="margin-top: 4px;">Top Australian Universities &amp; TAFE Institutes</h3>
            <p>We represent leading institutions across Australia including:</p>
            <ul style="padding-left: 20px; line-height: 28px; color: var(--color-ink-700);">
              <li><strong>Group of Eight (Go8):</strong> University of Melbourne, University of Sydney, UNSW, Australian National University, Monash University, University of Queensland.</li>
              <li><strong>Technology &amp; Applied Universities:</strong> RMIT, Deakin, UTS, QUT, Curtin University.</li>
              <li><strong>Regional Universities:</strong> Extra points towards Permanent Residency and extended post-study work streams.</li>
            </ul>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">FAQs</span>
            <h3 class="h3-title" style="margin-top: 4px;">Australia Study &amp; Visa FAQs</h3>
            {render_faq_accordion(faqs)}
          </div>
        </div>

        {render_sidebar('study_australia')}
      </div>
    </section>
    '''
    html = render_document("Study in Australia | Subclass 500 Visa & Go8 Universities | Cambridge Institute", 
                           "Complete admission and student visa guidance for Australian universities. CRICOS courses, Subclass 500 visa, GTE/GS support, and PR pathways in Ahmedabad.", 
                           content, active_page='study_australia', canonical='australiastudy.html')
    write_file('australiastudy.html', html)

def generate_canada():
    stats = [
        ('Up to 3 Years', 'Post-Graduation Work Permit (PGWP)'),
        ('SDS Stream', 'Fast-Track 20-Day Processing'),
        ('Sept / Jan / May', 'Three Major Intakes'),
        ('20 Hrs/Week', 'Off-Campus Work Authorization')
    ]
    faqs = [
        ('What is the Student Direct Stream (SDS) for Canada?', 'SDS is an expedited study permit processing category for Indian students with an IELTS score of 6.0 overall, GIC of CAD $20,635, and first-year tuition fee payment at a Designated Learning Institution (DLI).'),
        ('What is the PGWP work permit?', 'Graduates of 2-year or longer programs at eligible Canadian public colleges and universities can receive an open work permit for up to 3 years with no employer restrictions.'),
        ('How does Canadian education help in PR?', 'Canadian credentials and skilled work experience grant significant additional points under Express Entry Canadian Experience Class (CEC) and Provincial Nominee Programs (PNP).')
    ]

    content = f'''
    {render_page_hero("Study in Canada, SDS Stream &amp; PGWP", "Pursue diploma, degree, and postgraduate programs at top Canadian Designated Learning Institutions (DLIs) with direct pathways to PR.", "Study Abroad", "Canada Study", "Direct PR Pathway", "badge--teal")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          {render_country_stats(stats)}

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">Canadian Opportunities</span>
            <h2 class="h2-title" style="margin-top: 4px;">Why Study in Canada?</h2>
            <p>
              Canada is renowned for affordable tuition fees, world-class polytechnics and universities, safe multicultural cities, and the most transparent immigration pathways in the world.
            </p>
            <p>
              At Cambridge International, our senior visa counselors assist students with DLI college/university admissions, Guaranteed Investment Certificate (GIC) account opening, and SDS study permit filing with high success rates.
            </p>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">Key Programs</span>
            <h3 class="h3-title" style="margin-top: 4px;">Types of Qualifications in Canada</h3>
            <div class="feature-list" style="margin-top: var(--space-4);">
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Post-Graduate Certificates / Diplomas (1-2 Years):</strong> Highly practical programs with built-in Co-op industry internships.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Bachelor's Degrees (4 Years):</strong> Comprehensive academic degrees across engineering, computer science, business, and healthcare.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Master's Degrees (1-2 Years):</strong> Advanced thesis and course-based master's programs at top research universities.
                </div>
              </div>
            </div>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">Frequently Asked Questions</span>
            <h3 class="h3-title" style="margin-top: 4px;">Canada Study &amp; SDS FAQs</h3>
            {render_faq_accordion(faqs)}
          </div>
        </div>

        {render_sidebar('study_canada')}
      </div>
    </section>
    '''
    html = render_document("Study in Canada | SDS Visa, DLIs & PGWP Work Permit | Cambridge Institute", 
                           "Complete admission and student visa guidance for Canadian DLIs. SDS fast-track visa processing, GIC assistance, PGWP, and Express Entry PR pathways in Ahmedabad.", 
                           content, active_page='study_canada', canonical='canadastudy.html')
    write_file('canadastudy.html', html)

def generate_europe():
    stats = [
        ('€0 Tuition', 'Public Universities in Germany'),
        ('27 Countries', 'Schengen Visa Free Mobility'),
        ('18 Months', 'Post-Study Job Seeker Visa'),
        ('English Taught', 'Thousands of Master’s Programs')
    ]
    faqs = [
        ('Are public universities in Germany really tuition-free?', 'Yes! Most public universities in Germany charge zero tuition fees for both domestic and international students. You only pay a nominal semester contribution of €150–€350 which includes regional public transport.'),
        ('What is the APS Certificate for Germany?', 'The Academic Evaluation Centre (APS) certificate is mandatory for Indian students applying for German university admissions and student visas to verify educational credentials.'),
        ('Can I study in Europe in English without knowing the local language?', 'Yes! Thousands of Bachelor’s and Master’s degrees across Germany, France, Ireland, and the Netherlands are taught entirely in English. Learning basic German or French (A1/A2) is recommended for daily life and part-time jobs.')
    ]

    content = f'''
    {render_page_hero("Study in Europe &amp; Germany (Tuition-Free)", "High-tech education, zero tuition fees at German public universities, and 27-country Schengen mobility.", "Study Abroad", "Europe Study", "Tuition-Free Public Unis", "badge--teal")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          {render_country_stats(stats)}

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">European Hub of Innovation</span>
            <h2 class="h2-title" style="margin-top: 4px;">Why Study in Germany &amp; Europe?</h2>
            <p>
              Germany is Europe’s economic powerhouse and the premier global destination for engineering, automotive, data science, and business management education. With world-class public universities offering <strong>tuition-free education</strong>, students receive elite training with minimal financial burden.
            </p>
            <p>
              Cambridge Institute provides specialized APS certificate filing support, Blocked Account setup guidance, university admissions (Uni-Assist), and German A1/A2/B1 language training under one roof.
            </p>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">Key European Destinations</span>
            <h3 class="h3-title" style="margin-top: 4px;">Countries We Cover</h3>
            <div class="feature-list" style="margin-top: var(--space-4);">
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Germany:</strong> TU9 technical universities, applied sciences (FH), 18-month post-study work visa, high engineering salaries.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>France:</strong> Renowned business schools (Grandes Écoles), luxury brand management, 2-year post-study work permit.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Ireland:</strong> European tech capital (Google, Meta, Apple European HQs), English-speaking, 2-year post-study work visa.
                </div>
              </div>
            </div>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">FAQs</span>
            <h3 class="h3-title" style="margin-top: 4px;">Europe &amp; Germany Study FAQs</h3>
            {render_faq_accordion(faqs)}
          </div>
        </div>

        {render_sidebar('study_europe')}
      </div>
    </section>
    '''
    html = render_document("Study in Europe & Germany | Tuition-Free Universities | Cambridge Institute", 
                           "Study in Germany with zero tuition fees. Complete guidance for APS certification, Blocked Account, German language coaching, and European student visas in Ahmedabad.", 
                           content, active_page='study_europe', canonical='europestudy.html')
    write_file('europestudy.html', html)

def generate_nz():
    stats = [
        ('Up to 3 Years', 'Post-Study Work Visa'),
        ('8 Public Unis', '100% in Top 3% Globally'),
        ('Feb / July', 'Main Semesters'),
        ('Green List', 'Fast-Track PR Occupations')
    ]
    faqs = [
        ('What is the Green List in New Zealand?', 'The Green List contains highly in-demand roles in engineering, IT, healthcare, and trades that offer fast-tracked or direct pathways to New Zealand Residence.'),
        ('Can my spouse work while I study in New Zealand?', 'Yes! Partners of international students enrolled in eligible Master’s or Green List qualifications are eligible for an Open Partner Work Visa.')
    ]

    content = f'''
    {render_page_hero("Study in New Zealand &amp; Pathway Visas", "World-class education, safe environment, post-study work rights, and Green List fast-track residency.", "Study Abroad", "New Zealand Study", "Green List Occupations", "badge--teal")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          {render_country_stats(stats)}

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">Kiwi Academic Excellence</span>
            <h2 class="h2-title" style="margin-top: 4px;">Why Study in New Zealand?</h2>
            <p>
              All 8 public universities in New Zealand rank in the top 3% worldwide (QS World University Rankings). New Zealand offers an innovative British-style educational system, stunning natural beauty, high safety standards, and progressive post-study work policies.
            </p>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">Institutions</span>
            <h3 class="h3-title" style="margin-top: 4px;">8 State-Funded Universities &amp; Polytechnics</h3>
            <p>Universities include University of Auckland, University of Otago, Victoria University of Wellington, University of Canterbury, Massey University, University of Waikato, Lincoln University, and AUT.</p>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">FAQs</span>
            <h3 class="h3-title" style="margin-top: 4px;">New Zealand Study FAQs</h3>
            {render_faq_accordion(faqs)}
          </div>
        </div>

        {render_sidebar('study_nz')}
      </div>
    </section>
    '''
    html = render_document("Study in New Zealand | Pathway Visa & Post-Study Work | Cambridge Institute", 
                           "Complete admission and student visa guidance for New Zealand universities and polytechnics. Green list PR pathways and post-study work visas in Ahmedabad.", 
                           content, active_page='study_nz', canonical='newzealandstudy.html')
    write_file('newzealandstudy.html', html)

def generate_singapore():
    stats = [
        ('2 Years', 'Fast-Track Bachelor’s Degrees'),
        ('Global Hub', 'Asia’s Financial & Tech Capital'),
        ('Multiple', 'Intakes Throughout Year'),
        ('Top Ranked', 'NUS & NTU in World Top 15')
    ]
    faqs = [
        ('Can I get UK or Australian degrees in Singapore?', 'Yes! Leading private educational institutes in Singapore (PSB Academy, SIM, Kaplan) partner with top UK and Australian universities to award identical degrees in Singapore at a fraction of the cost.'),
        ('How safe is Singapore for international students?', 'Singapore is consistently ranked among the safest cities in the world with zero tolerance for crime, world-class healthcare, and clean modern infrastructure.')
    ]

    content = f'''
    {render_page_hero("Study in Singapore &amp; Fast-Track Degrees", "Asia's premier education and financial hub offering fast-track degrees and global corporate exposure.", "Study Abroad", "Singapore Study", "Asia's Premier Hub", "badge--teal")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          {render_country_stats(stats)}

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">Global Asian Gateway</span>
            <h2 class="h2-title" style="margin-top: 4px;">Why Choose Singapore?</h2>
            <p>
              Singapore is a premier global education and financial center located close to India. Students benefit from accelerated degrees, high standard of living, and proximity to regional headquarters of Fortune 500 corporations.
            </p>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--teal">FAQs</span>
            <h3 class="h3-title" style="margin-top: 4px;">Singapore Study FAQs</h3>
            {render_faq_accordion(faqs)}
          </div>
        </div>

        {render_sidebar('study_singapore')}
      </div>
    </section>
    '''
    html = render_document("Study in Singapore | Fast-Track Degrees & Asian Hub | Cambridge Institute", 
                           "Study in Singapore with accelerated degree options from top UK and Australian universities. Complete student visa and admissions support in Ahmedabad.", 
                           content, active_page='study_singapore', canonical='singaporestudy.html')
    write_file('singaporestudy.html', html)

if __name__ == '__main__':
    generate_usa()
    generate_uk()
    generate_australia()
    generate_canada()
    generate_europe()
    generate_nz()
    generate_singapore()
    print("Study Abroad slice generation completed.")
