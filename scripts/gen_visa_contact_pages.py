import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from generate_all_pages import render_document, render_page_hero, render_quick_inquiry_card, render_sidebar, write_file, ICONS

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

def generate_immigration_visa():
    faqs = [
        ('What is the minimum CRS score required for Canada Express Entry?', 'CRS cutoff scores vary across draws. Candidates with Master’s degrees, strong IELTS scores (CLB 9 / Band 8.0 in Listening and 7.0 in Reading, Writing, Speaking), and 3+ years of skilled experience have high competitive chances. Additional points can be gained through Provincial Nominations (+600 points) or French language skills (+50 points).'),
        ('How does Australia SkillSelect work?', 'Australia requires a minimum of 65 points on the points test covering Age, English proficiency, Educational Qualifications, and Skilled Employment. Invitations are issued for Subclass 189 (Skilled Independent), Subclass 190 (State Nominated), and Subclass 491 (Regional).')
    ]

    content = f'''
    {render_page_hero("Immigration &amp; Permanent Residency (PR) Visas", "Expert immigration consultancy for Canada Express Entry &amp; PNP, Australia SkillSelect, and UK Skilled Worker visas.", "Visa Services", "Immigration Visa", "PR Specialists", "badge--navy")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          <div class="content-block">
            <span class="caption-eyebrow">Permanent Residency Pathways</span>
            <h2 class="h2-title" style="margin-top: 4px;">Migrate to Canada, Australia &amp; UK</h2>
            <p>
              Cambridge International is Ahmedabad's trusted immigration consultancy with over two decades of experience in legal migration pathways. Our certified immigration legal team handles profile evaluation, Educational Credential Assessment (ECA via WES), Expression of Interest (EOI) filings, and state nomination applications.
            </p>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow">Key Immigration Streams</span>
            <h3 class="h3-title" style="margin-top: 4px;">Countries &amp; Visa Categories We Specialize In</h3>
            <div class="feature-list" style="margin-top: var(--space-4);">
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Canada Express Entry (FSWP &amp; CEC):</strong> Federal Skilled Worker Program and Canadian Experience Class points maximization with IELTS/French CLB optimization.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Canada Provincial Nominee Programs (PNP):</strong> Ontario (OINP), British Columbia (BC PNP), Alberta (AAIP), and Saskatchewan (SINP) state nominations granting 600 bonus CRS points.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Australia General Skilled Migration (GSM):</strong> Subclass 189 (Independent PR), Subclass 190 (State Nominated PR), and Subclass 491 (Skilled Work Regional).
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>UK Skilled Worker &amp; Global Talent:</strong> Employer-sponsored skilled worker visas and high-potential individual visas.
                </div>
              </div>
            </div>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow">Document Checklist</span>
            <h3 class="h3-title" style="margin-top: 4px;">End-to-End Documentation Support</h3>
            <p>
              Our Ahmedabad headquarters provides complete support for Educational Credential Assessments (ECA with WES/IQAS), Police Clearance Certificates (PCC), Medical examinations, Reference Letters in exact NOC format, and proof of settlement funds.
            </p>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow">Frequently Asked Questions</span>
            <h3 class="h3-title" style="margin-top: 4px;">Immigration Visa FAQs</h3>
            {render_faq_accordion(faqs)}
          </div>
        </div>

        {render_sidebar('immigration_visa')}
      </div>
    </section>
    '''
    html = render_document("Immigration & Permanent Residency (PR) Visa | Cambridge Institute", 
                           "Trusted immigration consultancy in Ahmedabad for Canada Express Entry, PNP, and Australia SkillSelect 189/190/491 PR visas. Book free evaluation.", 
                           content, active_page='immigration_visa', canonical='immigrationvisa.html')
    write_file('immigrationvisa.html', html)

def generate_student_visa():
    content = f'''
    {render_page_hero("Student Visa Guidance &amp; Roadmap", "Comprehensive end-to-end support for international student visas across USA, UK, Canada, Australia, Europe &amp; NZ.", "Visa Services", "Student Visa", "98.4% Success Rate", "badge--navy")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          <div class="content-block">
            <span class="caption-eyebrow">Proven Methodology</span>
            <h2 class="h2-title" style="margin-top: 4px;">Our 6-Stage Student Visa Success Process</h2>
            <p>
              Applying for a student visa requires rigorous documentation, financial transparency, and convincing presentation of genuine student intent. Over 25 years, Cambridge International has perfected a 6-stage roadmap ensuring visa approvals with minimal stress.
            </p>
            
            <div class="feature-list" style="margin-top: var(--space-6);">
              <div class="feature-item">
                <div style="width: 32px; height: 32px; border-radius: var(--radius-pill); background: var(--color-navy-900); color: #ffffff; display: flex; align-items: center; justify-content: center; font-weight: 700; flex-shrink: 0;">1</div>
                <div>
                  <strong>Profile Assessment &amp; Career Mapping:</strong> Evaluating academic percentages, backlog limits, gaps, test scores (IELTS/TOEFL/GRE), and career goals.
                </div>
              </div>
              <div class="feature-item">
                <div style="width: 32px; height: 32px; border-radius: var(--radius-pill); background: var(--color-navy-900); color: #ffffff; display: flex; align-items: center; justify-content: center; font-weight: 700; flex-shrink: 0;">2</div>
                <div>
                  <strong>University Shortlisting &amp; Applications:</strong> Selecting ambitious, target, and safe accredited universities with high visa approval records.
                </div>
              </div>
              <div class="feature-item">
                <div style="width: 32px; height: 32px; border-radius: var(--radius-pill); background: var(--color-navy-900); color: #ffffff; display: flex; align-items: center; justify-content: center; font-weight: 700; flex-shrink: 0;">3</div>
                <div>
                  <strong>SOP &amp; LOR Drafting:</strong> Professional editing of customized Statement of Purpose (SOP) addressing Genuine Student (GS) criteria.
                </div>
              </div>
              <div class="feature-item">
                <div style="width: 32px; height: 32px; border-radius: var(--radius-pill); background: var(--color-navy-900); color: #ffffff; display: flex; align-items: center; justify-content: center; font-weight: 700; flex-shrink: 0;">4</div>
                <div>
                  <strong>Financial Documentation &amp; CA Verification:</strong> Structuring education loans, bank deposits, affidavit of sponsorship, and asset valuation reports.
                </div>
              </div>
              <div class="feature-item">
                <div style="width: 32px; height: 32px; border-radius: var(--radius-pill); background: var(--color-navy-900); color: #ffffff; display: flex; align-items: center; justify-content: center; font-weight: 700; flex-shrink: 0;">5</div>
                <div>
                  <strong>Visa Lodging &amp; Mock Embassy Interviews:</strong> Rigorous 1-on-1 mock interviews simulating real visa consulate questions (for US F-1, German embassy, etc.).
                </div>
              </div>
              <div class="feature-item">
                <div style="width: 32px; height: 32px; border-radius: var(--radius-pill); background: var(--color-navy-900); color: #ffffff; display: flex; align-items: center; justify-content: center; font-weight: 700; flex-shrink: 0;">6</div>
                <div>
                  <strong>Pre-Departure Briefing &amp; Forex:</strong> Forex currency cards, student SIM cards, accommodation assistance, and airport pickup arrangements.
                </div>
              </div>
            </div>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow">Country Comparison</span>
            <h3 class="h3-title" style="margin-top: 4px;">Student Visa Requirements at a Glance</h3>
            <p>We handle student visas for all top global destinations:</p>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: var(--space-4); margin-top: var(--space-4);">
              <div style="background: var(--color-canvas); padding: var(--space-4); border-radius: var(--radius-md);">
                <strong>USA (F-1 Visa):</strong> Form I-20, SEVIS I-901 fee, DS-160, and Mumbai/Delhi consulate interview.
              </div>
              <div style="background: var(--color-canvas); padding: var(--space-4); border-radius: var(--radius-md);">
                <strong>UK (Student Route):</strong> CAS from licensed sponsor, 28-day funds rule, TB test, and biometric appointment.
              </div>
              <div style="background: var(--color-canvas); padding: var(--space-4); border-radius: var(--radius-md);">
                <strong>Canada (Study Permit):</strong> DLI Letter of Acceptance, GIC of CAD $20,635, and SDS online processing.
              </div>
              <div style="background: var(--color-canvas); padding: var(--space-4); border-radius: var(--radius-md);">
                <strong>Germany (National Student Visa):</strong> University admission letter, APS Certificate, and Blocked Account setup.
              </div>
            </div>
          </div>
        </div>

        {render_sidebar('student_visa')}
      </div>
    </section>
    '''
    html = render_document("Student Visa Guidance & Application Roadmap | Cambridge Institute", 
                           "Complete student visa processing for USA, UK, Canada, Australia, and Germany. SOP drafting, financial guidance, and mock embassy interviews in Ahmedabad.", 
                           content, active_page='student_visa', canonical='studentvisa.html')
    write_file('studentvisa.html', html)

def generate_visitor_visa():
    content = f'''
    {render_page_hero("Visitor &amp; Tourist Visa Services", "Hassle-free tourist, family visit, and business visas for USA (B1/B2), UK, Schengen Europe, Canada &amp; Australia.", "Visa Services", "Visitor Visa", "Hassle-Free Processing", "badge--navy")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          <div class="content-block">
            <span class="caption-eyebrow">Travel with Peace of Mind</span>
            <h2 class="h2-title" style="margin-top: 4px;">Professional Visitor Visa Consultancy</h2>
            <p>
              We all know obtaining a visitor visa can be a complex and stressful process. At Cambridge International, with over 20 years of experience, we make the entire application hassle-free. Customer satisfaction and prompt execution are our primary benchmarks.
            </p>
            <p>
              Our dedicated visa team manages your documentation, invitation letter formatting, flight itineraries, embassy appointment scheduling, and mock interview preparations.
            </p>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow">Destinations</span>
            <h3 class="h3-title" style="margin-top: 4px;">Visitor Visa Categories We Process</h3>
            <div class="feature-list" style="margin-top: var(--space-4);">
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>USA B1/B2 Tourist &amp; Business Visa:</strong> 10-year multiple entry visa application, DS-160 filling, emergency appointment expediting, and consulate interview grooming.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>UK Standard Visitor Visa:</strong> 6-month, 2-year, 5-year, and 10-year multiple-entry visas for tourism, family visits, or business meetings.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Schengen Visa (Europe 27 Countries):</strong> Single and multiple entry tourist visas covering France, Germany, Switzerland, Italy, Spain, Austria, and the Netherlands.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Canada &amp; Australia Visitor Visas:</strong> 10-year Canada visitor visa (V-1) and Subclass 600 Australia Tourist Stream.
                </div>
              </div>
            </div>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow">Overseas Travel Insurance</span>
            <h3 class="h3-title" style="margin-top: 4px;">Comprehensive Overseas Medical Insurance</h3>
            <p>
              Travel care-free with our international travel insurance packages (Platinum, Gold, Silver, Bronze) covering emergency medical expenses, baggage loss, passport theft, and flight delays meeting all Schengen &amp; international embassy requirements.
            </p>
          </div>
        </div>

        {render_sidebar('visitor_visa')}
      </div>
    </section>
    '''
    html = render_document("Visitor & Tourist Visa Services | USA, UK, Schengen | Cambridge Institute", 
                           "Visitor and tourist visa assistance in Ahmedabad for USA B1/B2, UK, Europe Schengen, Canada, and Australia. Overseas travel insurance and embassy appointments.", 
                           content, active_page='visitor_visa', canonical='visitorvisa.html')
    write_file('visitorvisa.html', html)

def generate_international_tours():
    content = f'''
    {render_page_hero("International Educational &amp; University Exposure Tours", "Faculty-led study trips, university campus immersion, and cultural exchange tours across UK, USA, Europe &amp; Asia.", "Tours", "International Tours", "Global Exposure", "badge--navy")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          <div class="content-block">
            <span class="caption-eyebrow">Educational Travel</span>
            <h2 class="h2-title" style="margin-top: 4px;">Bridging Classrooms with Global Landmarks</h2>
            <p>
              Cambridge International organizes bespoke international educational delegations, school and college exposure trips, and university campus tours across Singapore, Thailand, Malaysia, Hong Kong, Mauritius, Australia, Switzerland, UK, USA, and China.
            </p>
            <p>
              Our academic tours combine hands-on workshops at world-leading universities (Oxford, Cambridge, NUS, MIT) with enriching cultural exploration, STEM science centers, and corporate site visits.
            </p>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow">Featured Tour Circuits</span>
            <h3 class="h3-title" style="margin-top: 4px;">Popular Educational Destinations</h3>
            <div class="feature-list" style="margin-top: var(--space-4);">
              <div class="feature-item">
                {ICONS['plane']}
                <div>
                  <strong>Singapore &amp; Malaysia Innovation Tour:</strong> NUS campus visit, Science Centre Singapore, NEWater Plant, Marina Bay sustainability tour, and Petronas Towers.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['plane']}
                <div>
                  <strong>UK Academic Heritage Tour:</strong> Oxford &amp; Cambridge University lectures, British Museum, Greenwich Royal Observatory, and Shakespeare's Stratford-upon-Avon.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['plane']}
                <div>
                  <strong>USA STEM &amp; NASA Tour:</strong> Kennedy Space Center astronaut training experience, MIT &amp; Harvard campus walks, and New York UN Headquarters.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['plane']}
                <div>
                  <strong>Europe Science &amp; Culture Tour:</strong> CERN particle physics laboratory (Geneva), Swiss Alps glacier engineering, and Paris Louvre museum.
                </div>
              </div>
            </div>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow">Institutional Inquiries</span>
            <h3 class="h3-title" style="margin-top: 4px;">Customized Group Tours for Schools &amp; Colleges</h3>
            <p>
              We provide complete turnkey logistics including group visa processing, certified tour leaders, 4-star student-safe accommodations, Indian meals abroad, and comprehensive travel insurance.
            </p>
          </div>
        </div>

        {render_sidebar('tours')}
      </div>
    </section>
    '''
    html = render_document("International Educational Tours & University Delegations | Cambridge Institute", 
                           "International study tours and university immersion trips for schools and colleges across UK, USA, Europe, Singapore, and Australia organized from Ahmedabad.", 
                           content, active_page='tours', canonical='internationaltours.html')
    write_file('internationaltours.html', html)

def generate_inquiry():
    content = f'''
    {render_page_hero("Inquiry &amp; Free Profile Assessment", "Schedule a personalized 1-on-1 counseling session with our Senior Study Abroad &amp; Language Experts.", "Contact Us", "Inquiry", "Free Counseling", "badge--gold")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          {render_quick_inquiry_card("Personalized Consultation &amp; Profile Evaluation", "Fill in your details below and our senior counselors will get in touch within 24 business hours.")}

          <div class="content-block" style="margin-top: var(--space-8);">
            <span class="caption-eyebrow">What Happens Next?</span>
            <h3 class="h3-title" style="margin-top: 4px;">Our Consultation Guarantee</h3>
            <div class="feature-list" style="margin-top: var(--space-4);">
              <div class="feature-item">
                {ICONS['check']}
                <div><strong>Same-Day Response:</strong> A dedicated senior counselor will reach out via phone or WhatsApp to understand your background.</div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div><strong>Free English Diagnostic Test:</strong> Take our 30-minute diagnostic test to evaluate your current IELTS or Spoken English band level.</div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div><strong>Zero Obligation Roadmap:</strong> Receive a tailored country, university, and visa roadmap with detailed budget estimates.</div>
              </div>
            </div>
          </div>
        </div>

        {render_sidebar('inquiry')}
      </div>
    </section>
    '''
    html = render_document("Inquiry & Free Profile Assessment | Cambridge Institute Ahmedabad", 
                           "Book a free study abroad and language coaching consultation at Cambridge Institute Ahmedabad. Instant profile evaluation and demo class registration.", 
                           content, active_page='inquiry', canonical='inquiry.html')
    write_file('inquiry.html', html)

def generate_center():
    centers = [
        {
            'name': 'Satellite Head Office (Ahmedabad)',
            'address': '307-308, 3rd Floor, Shree Ratnamaya Palace, Beside Rohtawala Flats, Opp. Deepak Petrol Pump, Pithampura, Satellite, Ahmedabad-380060, Gujarat, India',
            'phone': '+91 99988 06666, 8866232322',
            'email': 'info@cambriz.com',
            'hours': 'Mon to Sat: 8:00 AM - 8:00 PM | Sun: 10:30 AM - 1:30 PM',
            'map_link': 'https://maps.google.com/?q=Cambridge+Institute+Satellite+Ahmedabad'
        },
        {
            'name': 'Navrangpura Center (Ahmedabad)',
            'address': 'Near Gujarat University &amp; CG Road, Navrangpura, Ahmedabad-380009, Gujarat, India',
            'phone': '+91 99988 06666, +91 98243 93391',
            'email': 'navrangpura@cambriz.com',
            'hours': 'Mon to Sat: 8:00 AM - 8:00 PM',
            'map_link': 'https://maps.google.com/?q=Navrangpura+Ahmedabad'
        },
        {
            'name': 'Maninagar Center (Ahmedabad East)',
            'address': 'Near Kankaria &amp; Maninagar Railway Station, Ahmedabad-380008, Gujarat, India',
            'phone': '+91 8866232322',
            'email': 'maninagar@cambriz.com',
            'hours': 'Mon to Sat: 8:30 AM - 7:30 PM',
            'map_link': 'https://maps.google.com/?q=Maninagar+Ahmedabad'
        },
        {
            'name': 'Nikol / Bapunagar Center (Ahmedabad East)',
            'address': 'Raspan Arcade, Nikol Ring Road, Ahmedabad-382350, Gujarat, India',
            'phone': '+91 99988 06666',
            'email': 'nikol@cambriz.com',
            'hours': 'Mon to Sat: 8:30 AM - 7:30 PM',
            'map_link': 'https://maps.google.com/?q=Nikol+Ahmedabad'
        },
        {
            'name': 'Vadodara Regional Center',
            'address': 'Alkapuri Main Road, Opposite Railway Station, Vadodara-390007, Gujarat, India',
            'phone': '+91 99988 06666',
            'email': 'vadodara@cambriz.com',
            'hours': 'Mon to Sat: 9:00 AM - 7:00 PM',
            'map_link': 'https://maps.google.com/?q=Alkapuri+Vadodara'
        },
        {
            'name': 'Surat Regional Center',
            'address': 'Ghod Dod Road, Athwa, Surat-395007, Gujarat, India',
            'phone': '+91 8866232322',
            'email': 'surat@cambriz.com',
            'hours': 'Mon to Sat: 9:00 AM - 7:00 PM',
            'map_link': 'https://maps.google.com/?q=Ghod+Dod+Road+Surat'
        }
    ]

    cards_html = ''
    for c in centers:
        cards_html += f'''
        <div class="content-block" style="margin-bottom: var(--space-6);">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: var(--space-4); flex-wrap: wrap;">
            <div>
              <span class="badge badge--navy">Official Center</span>
              <h3 class="h3-title" style="margin-top: 6px; margin-bottom: var(--space-2);">{c['name']}</h3>
            </div>
            <a href="{c['map_link']}" target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-sm">
              {ICONS['map-pin']} View on Google Maps
            </a>
          </div>

          <div style="margin-top: var(--space-4); display: flex; flex-direction: column; gap: var(--space-3);">
            <div style="display: flex; gap: var(--space-2); font-size: 15px; color: var(--color-ink-800);">
              <span style="color: var(--color-navy-900); font-weight: 600; min-width: 80px;">Address:</span>
              <span>{c['address']}</span>
            </div>
            <div style="display: flex; gap: var(--space-2); font-size: 15px; color: var(--color-ink-800);">
              <span style="color: var(--color-navy-900); font-weight: 600; min-width: 80px;">Phone:</span>
              <span><a href="tel:+919998806666" style="color: var(--color-navy-900); font-weight: 600;">{c['phone']}</a></span>
            </div>
            <div style="display: flex; gap: var(--space-2); font-size: 15px; color: var(--color-ink-800);">
              <span style="color: var(--color-navy-900); font-weight: 600; min-width: 80px;">Email:</span>
              <span><a href="mailto:{c['email']}">{c['email']}</a></span>
            </div>
            <div style="display: flex; gap: var(--space-2); font-size: 15px; color: var(--color-muted-600);">
              <span style="color: var(--color-navy-900); font-weight: 600; min-width: 80px;">Timings:</span>
              <span>{c['hours']}</span>
            </div>
          </div>
        </div>
        '''

    content = f'''
    {render_page_hero("Centers &amp; Branch Directory", "Visit our headquarters in Satellite, Ahmedabad, or our regional branches across Gujarat.", "Contact Us", "Centers", "Branch Network", "badge--navy")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          {cards_html}
        </div>

        {render_sidebar('centers')}
      </div>
    </section>
    '''
    html = render_document("Centers & Branch Directory | Cambridge Institute Ahmedabad", 
                           "Find Cambridge Institute branches in Ahmedabad (Satellite, Navrangpura, Maninagar, Nikol), Vadodara, and Surat with addresses, phone numbers, and maps.", 
                           content, active_page='centers', canonical='center.html')
    write_file('center.html', html)

def generate_privacy_policy():
    content = f'''
    {render_page_hero("Privacy Policy &amp; Terms of Service", "Transparent policies governing student data protection, cookies, and regulatory compliance.", "Legal", "Privacy Policy", "Legal Disclosures", "badge--navy")}

    <section class="section">
      <div class="container" style="max-width: 960px;">
        <div class="content-block">
          <h2 class="h2-title">Privacy Policy</h2>
          <p class="body-small" style="margin-bottom: var(--space-6);">Last updated: January 2026</p>
          
          <h3 class="h4-title">1. Introduction</h3>
          <p>
            Cambridge Institute and Cambridge International ("we", "our", or "us") are committed to protecting the privacy and personal information of our students, prospective applicants, franchisees, and website visitors. This Privacy Policy details how we collect, process, store, and safeguard your data.
          </p>

          <h3 class="h4-title" style="margin-top: var(--space-6);">2. Information We Collect</h3>
          <p>
            We collect personal details provided voluntarily when you fill out our counseling forms, enroll in coaching courses (IELTS, TOEFL, Spoken English, French, German), or request visa evaluation services. This may include your name, contact numbers, email address, academic credentials, test scores, passport copies, financial proofs, and destination preferences.
          </p>

          <h3 class="h4-title" style="margin-top: var(--space-6);">3. How We Use Your Data</h3>
          <p>
            Your information is strictly utilized to:
          </p>
          <ul style="padding-left: 20px; line-height: 26px; color: var(--color-ink-700); margin-bottom: var(--space-4);">
            <li>Process course admissions, class schedules, and mock exam results.</li>
            <li>Submit university applications and facilitate student/immigration visa processing.</li>
            <li>Communicate updates regarding batch timings, visa deadlines, and embassy appointments.</li>
            <li>Ensure compliance with statutory educational and immigration laws.</li>
          </ul>

          <h3 class="h4-title" style="margin-top: var(--space-6);">4. Data Confidentiality &amp; Security</h3>
          <p>
            We adhere to strict data protection standards under the Information Technology Act (India) and international privacy frameworks. We never sell, rent, or trade your personal information to third-party marketing entities.
          </p>

          <h3 class="h4-title" style="margin-top: var(--space-6);">5. Contact Our Data Protection Officer</h3>
          <p>
            If you have questions regarding this Privacy Policy or wish to review or update your records, contact us at:
          </p>
          <p>
            <strong>Cambridge Institute</strong><br/>
            307-308, 3rd Floor, Shree Ratnamaya Palace, Satellite, Ahmedabad-380060, Gujarat, India<br/>
            Email: <a href="mailto:info@cambriz.com" style="color: var(--color-navy-900); font-weight: 600;">info@cambriz.com</a> | Phone: +91 99988 06666
          </p>
        </div>
      </div>
    </section>
    '''
    html = render_document("Privacy Policy & Terms of Service | Cambridge Institute", 
                           "Privacy policy and data protection terms for students and visitors of Cambridge Institute Ahmedabad.", 
                           content, active_page='privacy', canonical='privacypolicy.html')
    write_file('privacypolicy.html', html)

if __name__ == '__main__':
    generate_immigration_visa()
    generate_student_visa()
    generate_visitor_visa()
    generate_international_tours()
    generate_inquiry()
    generate_center()
    generate_privacy_policy()
    print("Visa, Tours & Contact slice generation completed.")
