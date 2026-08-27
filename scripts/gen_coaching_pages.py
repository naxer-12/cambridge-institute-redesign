import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from generate_all_pages import render_document, render_page_hero, render_quick_inquiry_card, render_sidebar, write_file, ICONS

def render_course_overview(features):
    items = ''
    for label, val in features:
        items += f'''
        <div style="background: var(--color-surface); border: 1px solid var(--color-border); border-radius: var(--radius-md); padding: var(--space-4);">
          <div class="body-small" style="color: var(--color-muted-600); text-transform: uppercase; letter-spacing: 0.05em; font-weight: 600;">{label}</div>
          <div style="font-size: 16px; font-weight: 700; color: var(--color-navy-900); margin-top: 4px;">{val}</div>
        </div>
        '''
    return f'''
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--space-4); margin-bottom: var(--space-8);">
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

def generate_ielts():
    features = [
        ('Target Score', 'Band 7.5 to 8.5+'),
        ('Course Duration', '2 Months / Intensive 1 Month'),
        ('Batch Timings', 'Morning, Evening &amp; Weekends'),
        ('Exam Types', 'Academic &amp; General Training'),
        ('Mock Tests', 'Weekly Full-Length Lab Mocks'),
        ('Faculty', 'British Council &amp; IDP Certified')
    ]
    faqs = [
        ('What is the difference between IELTS Academic and General Training?', 'IELTS Academic is required for university admissions at undergraduate and postgraduate levels. IELTS General Training is intended for immigration (such as Canada Express Entry, Australia PR) and work visas.'),
        ('How does Cambridge Institute ensure a Band 7+ or 8+ score?', 'We combine daily interactive group lectures, one-on-one speaking interview drills, detailed task-by-task writing corrections with band criteria, and weekly computer/paper simulated mock exams under strict timed conditions.'),
        ('Do you provide study material and practice audio tests?', 'Yes! Every enrolled student receives our comprehensive IELTS Cambridge toolkit, including Cambridge official past papers (Volumes 1-19), audio listening files, vocabulary booster sets, and essay template guides.')
    ]

    content = f'''
    {render_page_hero("IELTS Coaching Classes in Ahmedabad", "Master IELTS Academic &amp; General Training with certified master trainers and achieve Band 7.5 to 8.5+.", "Coaching", "IELTS Coaching", "Target Band 7.5+", "badge--gold")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          {render_course_overview(features)}

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--gold">Elite Exam Preparation</span>
            <h2 class="h2-title" style="margin-top: 4px;">Why Cambridge Institute for IELTS?</h2>
            <p>
              Cambridge Institute is Ahmedabad's premier authorized IELTS training partner. Under the guidance of Mr. Devang Solanki and British Council / IDP certified master trainers, thousands of our students have achieved Band 7.5, 8.0, and 8.5+ on their very first attempt.
            </p>
            <p>
              Our dedicated audio-visual language laboratory, individual speaking interview evaluations, and personalized writing task reviews address the exact weaknesses of Indian students.
            </p>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--gold">Comprehensive 4-Module Breakdown</span>
            <h3 class="h3-title" style="margin-top: 4px;">What You Will Master</h3>
            <div class="feature-list" style="margin-top: var(--space-4);">
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Listening Module (40 Questions, 30 Mins):</strong> Mastering diverse accents (British, American, Australian), prediction strategies, map labeling, and multiple-choice questions.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Reading Module (40 Questions, 60 Mins):</strong> Skimming, scanning, True/False/Not Given mastery, headings matching, and speed enhancement techniques for complex academic texts.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Writing Module (Task 1 &amp; Task 2, 60 Mins):</strong> Report writing / letter composition and 250+ word academic essay structuring, lexical resource expansion, and grammatical accuracy.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Speaking Module (3-Part Interview, 11-14 Mins):</strong> Daily 1-on-1 mock interviews, cue card fluency training, pronunciation clarity, and elimination of mother-tongue influence (MTI).
                </div>
              </div>
            </div>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--gold">Weekly Mock Tests</span>
            <h3 class="h3-title" style="margin-top: 4px;">Simulated Exam Environment</h3>
            <p>
              Every Saturday, students undertake a full-length, real-time mock exam simulating the actual IDP / British Council test environment. Detailed band score feedback cards are provided on Monday with individualized corrective plans.
            </p>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--gold">Frequently Asked Questions</span>
            <h3 class="h3-title" style="margin-top: 4px;">IELTS Coaching FAQs</h3>
            {render_faq_accordion(faqs)}
          </div>
        </div>

        {render_sidebar('ielts')}
      </div>
    </section>
    '''
    html = render_document("IELTS Coaching in Ahmedabad | Band 7+ Strategy | Cambridge Institute", 
                           "Best IELTS coaching classes in Ahmedabad for Academic and General Training. Audio-visual lab, 1-on-1 speaking drills, and weekly mock exams at Cambridge Institute.", 
                           content, active_page='ielts', canonical='IELTS.html')
    write_file('IELTS.html', html)

def generate_toefl():
    features = [
        ('Target Score', '100 to 115+ / 120'),
        ('Duration', '2 Months Comprehensive'),
        ('Testing Mode', 'Computer-Delivered (iBT)'),
        ('Lab Facilities', 'Dedicated High-Tech Terminals'),
        ('Mock Tests', '15+ Full Computerized Mocks'),
        ('Faculty', 'ETS Authorized Trainers')
    ]
    faqs = [
        ('What is the TOEFL iBT score scale?', 'TOEFL iBT is scored on a scale of 0–120 points, with 30 points allocated to each of the 4 sections: Reading, Listening, Speaking, and Writing. Top US universities typically require a score of 95–105+.'),
        ('How is the Speaking section conducted in TOEFL?', 'Unlike IELTS where you speak to a human examiner, in TOEFL iBT you record your responses into a microphone connected to a computer. Our lab is specifically calibrated to simulate this exact testing format.')
    ]

    content = f'''
    {render_page_hero("TOEFL iBT Coaching Classes in Ahmedabad", "Computerized test preparation with official ETS software, audio-visual laboratory practice, and certified faculty.", "Coaching", "TOEFL iBT", "Score 100+ / 120", "badge--gold")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          {render_course_overview(features)}

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--gold">Computer-Based Mastery</span>
            <h2 class="h2-title" style="margin-top: 4px;">Why Prepare for TOEFL at Cambridge Institute?</h2>
            <p>
              The Test of English as a Foreign Language (TOEFL iBT) is the gold standard for admission to universities in the United States, Canada, and premier global technical institutes.
            </p>
            <p>
              Cambridge Institute features an exclusive ETS-certified computer laboratory where students train on computerized workstations using authentic ETS practice interfaces, noise-canceling headsets, and speech recognition tools.
            </p>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--gold">4 Core Modules</span>
            <h3 class="h3-title" style="margin-top: 4px;">TOEFL iBT Syllabus &amp; Strategy</h3>
            <div class="feature-list" style="margin-top: var(--space-4);">
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Reading Section (35 Mins):</strong> Academic passages, vocabulary-in-context questions, sentence insertion, and summary tables.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Listening Section (36 Mins):</strong> University classroom lectures and campus conversations with note-taking strategies.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Speaking Section (16 Mins):</strong> 4 tasks (1 independent + 3 integrated) focusing on topic development, vocal delivery, and time management.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Writing Section (29 Mins):</strong> Integrated writing task (reading + lecture synthesis) and Academic Discussion task with real-time typing practice.
                </div>
              </div>
            </div>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--gold">FAQs</span>
            <h3 class="h3-title" style="margin-top: 4px;">TOEFL iBT FAQs</h3>
            {render_faq_accordion(faqs)}
          </div>
        </div>

        {render_sidebar('toefl')}
      </div>
    </section>
    '''
    html = render_document("TOEFL iBT Coaching in Ahmedabad | Score 100+ | Cambridge Institute", 
                           "Authorized TOEFL iBT coaching classes in Ahmedabad. Computer-based lab practice, official ETS software, and speech delivery training at Cambridge Institute.", 
                           content, active_page='toefl', canonical='TOEFL.html')
    write_file('TOEFL.html', html)

def generate_spoken_english():
    features = [
        ('Skill Levels', 'Beginner, Intermediate, Advanced'),
        ('Duration', '2 to 3 Months Flexible'),
        ('Key Books', 'Enrich Your English Series (4 Vols)'),
        ('Methodology', '100% Practical Speaking Drills'),
        ('Batch Options', 'Morning, Evening, Corporate'),
        ('Target', 'Fluency, Accent, Confidence')
    ]
    faqs = [
        ('I have studied in Gujarati medium. Can I become fluent in English?', 'Absolutely! Over the last 25 years, thousands of students from vernacular and Gujarati medium backgrounds have gained flawless English fluency at Cambridge Institute. Our books under the "Enrich Your English Series" were authored specifically to bridge vernacular thought patterns into English sentence construction.'),
        ('What activities are included in daily classes?', 'Classes include daily conversation circles, extempore speeches, group discussions (GDs), audio-visual listening drills, role plays, pronunciation drills, and grammar error correction.')
    ]

    content = f'''
    {render_page_hero("Spoken English &amp; Personality Development", "Transform your fluency, grammar, pronunciation, and corporate communication with Gujarat's #1 language institute.", "Coaching", "Spoken English", "25+ Years Legacy", "badge--gold")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          {render_course_overview(features)}

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--gold">Master English Fluency</span>
            <h2 class="h2-title" style="margin-top: 4px;">Speak English Naturally with Confidence</h2>
            <p>
              Cambridge Institute of English and Foreign Languages was founded in 1999 with the vision of eradicating language barriers for students, professionals, homemakers, and business leaders across Gujarat.
            </p>
            <p>
              Our founder, <strong>Mr. Devang Solanki</strong>, has authored four authoritative books under the <em>Enrich Your English Series</em> that systematically build active vocabulary, correct common grammatical pitfalls, and eliminate mother-tongue hesitation.
            </p>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--gold">3-Tier Progressive Curriculum</span>
            <h3 class="h3-title" style="margin-top: 4px;">Course Structure</h3>
            <div class="feature-list" style="margin-top: var(--space-4);">
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Level 1 - Fundamental Grammar &amp; Sentence Construction:</strong> Tenses, prepositions, modal verbs, active/passive voice, and basic daily conversation.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Level 2 - Conversational Fluency &amp; Vocabulary Expansion:</strong> 5,000+ practical words from <em>Enrich Your English</em>, idiomatic expressions, debates, and picture descriptions.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Level 3 - Professional &amp; Executive Communication:</strong> Public speaking, boardroom presentations, job interview cracking, email writing, and accent neutralization.
                </div>
              </div>
            </div>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--gold">FAQs</span>
            <h3 class="h3-title" style="margin-top: 4px;">Spoken English FAQs</h3>
            {render_faq_accordion(faqs)}
          </div>
        </div>

        {render_sidebar('spoken_english')}
      </div>
    </section>
    '''
    html = render_document("Spoken English Classes in Ahmedabad | Cambridge Institute", 
                           "Learn fluent Spoken English in Ahmedabad. Practical conversation, Enrich Your English curriculum, public speaking, and personality development since 1999.", 
                           content, active_page='spoken_english', canonical='spokenenglish.html')
    write_file('spokenenglish.html', html)

def generate_english_exams():
    features = [
        ('Certifications', 'Cambridge KET, PET, FCE, BEC'),
        ('PTE Academic', 'AI-Scored Computer Prep'),
        ('Duration', '2 Months Specialized'),
        ('Recognition', 'Accepted Worldwide by Employers'),
        ('Lab Access', 'Interactive Mock Test Terminals'),
        ('Eligibility', 'Students, Professionals, Teachers')
    ]
    faqs = [
        ('What is the Cambridge BEC Certificate?', 'The Business English Certificate (BEC) is an internationally recognized qualification awarded by Cambridge Assessment English, certifying workplace English proficiency for multinational employers and business schools.'),
        ('What is PTE Academic coaching at Cambridge Institute?', 'PTE Academic is a 2-hour computer-based English test accepted for study abroad and Australian/New Zealand/Canadian immigration. We provide 2-month intensive coaching with AI-based simulated mock tests.')
    ]

    content = f'''
    {render_page_hero("Cambridge English Qualifications, BEC &amp; PTE", "Globally recognized Cambridge Assessment English certificates, Business English (BEC), and Pearson PTE Academic.", "Coaching", "English Exams &amp; BEC", "Cambridge Credentials", "badge--gold")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          {render_course_overview(features)}

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--gold">Global Qualifications</span>
            <h2 class="h2-title" style="margin-top: 4px;">Cambridge University English Examinations</h2>
            <p>
              Cambridge English Qualifications are in-depth exams that make learning English enjoyable, effective, and rewarding. Our qualifications are based on research into effective teaching and learning, accepted by over 25,000 organizations worldwide.
            </p>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--gold">Exam Programs</span>
            <h3 class="h3-title" style="margin-top: 4px;">Courses Offered</h3>
            <div class="feature-list" style="margin-top: var(--space-4);">
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>Business English Certificates (BEC):</strong> BEC Preliminary (B1), BEC Vantage (B2), and BEC Higher (C1) for corporate careers.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>General English Suite:</strong> B1 Preliminary (PET), B2 First (FCE), and C1 Advanced (CAE).
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>PTE Academic Preparation:</strong> 2-month course, 2 hours daily, computerized practice for Australia, UK, and Canada study/visa requirements.
                </div>
              </div>
            </div>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--gold">FAQs</span>
            <h3 class="h3-title" style="margin-top: 4px;">Cambridge Exams FAQs</h3>
            {render_faq_accordion(faqs)}
          </div>
        </div>

        {render_sidebar('english_exams')}
      </div>
    </section>
    '''
    html = render_document("Cambridge English Exams, BEC & PTE Academic | Cambridge Institute", 
                           "Cambridge English Qualifications (BEC, FCE, CAE) and PTE Academic preparation classes in Ahmedabad. Official practice materials and test booking.", 
                           content, active_page='english_exams', canonical='englishexams.html')
    write_file('englishexams.html', html)

def generate_french():
    features = [
        ('Levels Offered', 'CEFR A1, A2, B1, B2, C1'),
        ('Exam Preparation', 'DELF, DALF, TEF Canada, TCF'),
        ('Duration', '2.5 Months per CEFR Level'),
        ('Batch Timings', 'Weekday &amp; Weekend Batches'),
        ('Teaching Mode', 'Authentic French Pedagogical Method'),
        ('Faculty', 'Alliance Française Certified Experts')
    ]
    faqs = [
        ('How many points does French grant for Canada PR (Express Entry)?', 'Under Canada Express Entry, scoring NCLC 7 (DELF B2 equivalent) in French can earn you up to 50 additional CRS points for French language skills, even if English is your primary language!'),
        ('What is the DELF Exam?', 'DELF (Diplôme d’Études en Langue Française) is the official French proficiency diploma awarded by the French Ministry of Education, valid for life and recognized worldwide for university admissions and employment.')
    ]

    content = f'''
    {render_page_hero("French Language Classes in Ahmedabad", "Learn French from A1 to B2/C1 for study abroad in France, Canada Express Entry (TEF/TCF), and career growth.", "Coaching", "French Classes", "DELF &amp; TEF Canada", "badge--gold")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          {render_course_overview(features)}

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--gold">Language of Global Diplomacy</span>
            <h2 class="h2-title" style="margin-top: 4px;">French Language Training at Cambridge Institute</h2>
            <p>
              Cambridge Institute is Ahmedabad's premier French language coaching destination where students learn French in an authentic immersion environment.
            </p>
            <p>
              Whether you are preparing for higher education in France, seeking substantial CRS points for <strong>Canada Permanent Residency (TEF / TCF Canada)</strong>, or wanting to learn a beautiful world language, our structured CEFR modules guarantee fluency and exam success.
            </p>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--gold">CEFR Level Progression</span>
            <h3 class="h3-title" style="margin-top: 4px;">French Course Levels</h3>
            <div class="feature-list" style="margin-top: var(--space-4);">
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>A1 (Discovery / Beginner):</strong> Basic vocabulary, everyday greetings, numbers, family, present tense, phonetics rules, and self-introduction.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>A2 (Survival / Elementary):</strong> Past tenses (passé composé, imparfait), shopping, ordering at restaurants, travel expressions, and routine tasks.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>B1 (Independent User):</strong> Expressing opinions, debates, future &amp; conditional tenses, formal letter writing, and professional discussions.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>B2 (Advanced / TEF Canada Benchmark):</strong> Complex academic texts, fluent spontaneous conversation, subjonctif mastery, and complete DELF B2 exam preparation.
                </div>
              </div>
            </div>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--gold">FAQs</span>
            <h3 class="h3-title" style="margin-top: 4px;">French Language FAQs</h3>
            {render_faq_accordion(faqs)}
          </div>
        </div>

        {render_sidebar('french')}
      </div>
    </section>
    '''
    html = render_document("French Language Classes in Ahmedabad | DELF & TEF Canada | Cambridge Institute", 
                           "Learn French in Ahmedabad with certified trainers. Intensive preparation for DELF A1-B2 exams and TEF/TCF Canada immigration at Cambridge Institute.", 
                           content, active_page='french', canonical='french.html')
    write_file('french.html', html)

def generate_german():
    features = [
        ('Levels Offered', 'CEFR A1, A2, B1, B2, C1'),
        ('Exam Preparation', 'Goethe-Zertifikat, TestDaF, OSD'),
        ('Duration', '2.5 Months per CEFR Level'),
        ('Special Track', 'Medical Professionals (Doctors/Nurses)'),
        ('Lab Practice', 'Goethe Listening &amp; Speaking Simulations'),
        ('Faculty', 'Goethe-Institut Certified Linguists')
    ]
    faqs = [
        ('Why is German language required for studying in Germany?', 'While many Master’s programs are taught in English, public universities and German visa consulates often require at least A1 or A2 certificate for visa issuance. For daily life, student jobs, and internships in German tech hubs, B1/B2 German is indispensable.'),
        ('Do you prepare healthcare professionals (Doctors & Nurses) for Germany?', 'Yes! We run dedicated medical German batches preparing doctors and nurses for the Approbation licensing exams and Fachsprachenprüfung (FSP) with hospital clinical terminologies.')
    ]

    content = f'''
    {render_page_hero("German Language Classes in Ahmedabad", "Master German A1, A2, B1, B2 for tuition-free university education in Germany, job seeker visas, and healthcare careers.", "Coaching", "German Classes", "Goethe-Zertifikat Prep", "badge--gold")}

    <section class="section">
      <div class="container page-layout-grid">
        <div>
          {render_course_overview(features)}

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--gold">Gateway to European Careers</span>
            <h2 class="h2-title" style="margin-top: 4px;">German Language Coaching at Cambridge Institute</h2>
            <p>
              Germany is Europe’s largest economy and the top global destination for tuition-free higher education and high-paying engineering and medical careers.
            </p>
            <p>
              At Cambridge Institute in Ahmedabad, we provide intensive, highly interactive German language training strictly mapped to the Common European Framework of Reference for Languages (CEFR) and official <strong>Goethe-Institut exam patterns</strong>.
            </p>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--gold">CEFR Syllabus Overview</span>
            <h3 class="h3-title" style="margin-top: 4px;">German Course Levels</h3>
            <div class="feature-list" style="margin-top: var(--space-4);">
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>German A1 (Beginner):</strong> German alphabet, articles (der, die, das), cases (Nominativ, Akkusativ), verb conjugations, basic conversations, and Goethe A1 exam pattern.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>German A2 (Elementary):</strong> Dativ case, modal verbs, past tense (Perfekt, Präteritum), reflexive verbs, giving directions, and conversational fluency.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>German B1 (Intermediate):</strong> Complex clauses, Genitiv, Passiv, Konjunktiv II, university discussions, and Goethe B1 module clearing.
                </div>
              </div>
              <div class="feature-item">
                {ICONS['check']}
                <div>
                  <strong>German B2 (Upper Intermediate / Professional):</strong> Advanced grammar, technical vocabulary, academic debate, and preparation for TestDaF / Goethe B2 certification.
                </div>
              </div>
            </div>
          </div>

          <div class="content-block">
            <span class="caption-eyebrow caption-eyebrow--gold">FAQs</span>
            <h3 class="h3-title" style="margin-top: 4px;">German Language FAQs</h3>
            {render_faq_accordion(faqs)}
          </div>
        </div>

        {render_sidebar('german')}
      </div>
    </section>
    '''
    html = render_document("German Language Classes in Ahmedabad | Goethe A1-B2 | Cambridge Institute", 
                           "Learn German in Ahmedabad with Goethe-certified instructors. Preparation for Goethe-Zertifikat A1, A2, B1, B2 and German university admissions at Cambridge Institute.", 
                           content, active_page='german', canonical='german.html')
    write_file('german.html', html)

if __name__ == '__main__':
    generate_ielts()
    generate_toefl()
    generate_spoken_english()
    generate_english_exams()
    generate_french()
    generate_german()
    print("Coaching slice generation completed.")
