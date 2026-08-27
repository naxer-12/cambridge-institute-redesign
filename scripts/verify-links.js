import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const projectRoot = path.dirname(__dirname);

const PAGES = [
  'index.html', 'aboutcambridge.html', 'testimonials.html', 'franchisee.html', 
  'cambridgeinmedia.html', 'certificatesofauthorizations.html', 'immigrationvisa.html', 
  'studentvisa.html', 'visitorvisa.html', 'internationaltours.html', 'usastudent.html', 
  'ukstudy.html', 'australiastudy.html', 'newzealandstudy.html', 'canadastudy.html', 
  'europestudy.html', 'singaporestudy.html', 'TOEFL.html', 'IELTS.html', 
  'spokenenglish.html', 'englishexams.html', 'french.html', 'german.html', 
  'inquiry.html', 'center.html', 'privacypolicy.html'
];

console.log(`Verifying links across ${PAGES.length} HTML pages...`);

let totalLinksChecked = 0;
let errors = [];

PAGES.forEach((page) => {
  const filePath = path.join(projectRoot, page);
  if (!fs.existsSync(filePath)) {
    errors.push(`Missing page file: ${page}`);
    return;
  }

  const content = fs.readFileSync(filePath, 'utf-8');
  const hrefRegex = /href=["']([^"']+)["']/g;
  let match;

  while ((match = hrefRegex.exec(content)) !== null) {
    const href = match[1];
    totalLinksChecked++;

    // Ignore external URLs, tel, mailto, and in-page anchor hashes
    if (
      href.startsWith('http://') ||
      href.startsWith('https://') ||
      href.startsWith('tel:') ||
      href.startsWith('mailto:') ||
      href.startsWith('#') ||
      href.startsWith('javascript:')
    ) {
      continue;
    }

    const cleanHref = href.split('#')[0].split('?')[0];
    if (!cleanHref) continue;

    const targetPath = path.join(projectRoot, cleanHref);
    if (!fs.existsSync(targetPath)) {
      errors.push(`[${page}] Broken internal link: "${href}" -> target "${targetPath}" does not exist.`);
    }
  }
});

console.log(`Checked ${totalLinksChecked} links.`);

if (errors.length > 0) {
  console.error(`\n❌ Found ${errors.length} link errors:`);
  errors.forEach((err) => console.error(`  - ${err}`));
  process.exit(1);
} else {
  console.log(`✅ All internal links across all 26 pages are 100% valid!`);
}
