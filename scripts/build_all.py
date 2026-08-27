import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, 'scripts')

scripts = [
    'gen_core_pages.py',
    'gen_study_abroad_pages.py',
    'gen_coaching_pages.py',
    'gen_visa_contact_pages.py'
]

print("=== Starting Full Cambridge Institute Website Generation ===")
for s in scripts:
    path = os.path.join(SCRIPTS_DIR, s)
    print(f"Running {s}...")
    res = subprocess.run([sys.executable, path], cwd=BASE_DIR, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error running {s}:")
        print(res.stderr)
        sys.exit(1)
    else:
        print(res.stdout.strip())

# Verify all 26 files exist
REQUIRED_FILES = [
    'index.html', 'aboutcambridge.html', 'testimonials.html', 'franchisee.html', 
    'cambridgeinmedia.html', 'certificatesofauthorizations.html', 'immigrationvisa.html', 
    'studentvisa.html', 'visitorvisa.html', 'internationaltours.html', 'usastudent.html', 
    'ukstudy.html', 'australiastudy.html', 'newzealandstudy.html', 'canadastudy.html', 
    'europestudy.html', 'singaporestudy.html', 'TOEFL.html', 'IELTS.html', 
    'spokenenglish.html', 'englishexams.html', 'french.html', 'german.html', 
    'inquiry.html', 'center.html', 'privacypolicy.html'
]

missing = []
for f in REQUIRED_FILES:
    fpath = os.path.join(BASE_DIR, f)
    if not os.path.exists(fpath):
        missing.append(f)

if missing:
    print(f"❌ Error: Missing files: {missing}")
    sys.exit(1)
else:
    print(f"✅ Success: All {len(REQUIRED_FILES)} pages successfully generated!")
