import { defineConfig, Plugin } from 'vite';
import { resolve } from 'path';
import fs from 'fs';

function csvInquiryPlugin(): Plugin {
  return {
    name: 'vite-plugin-csv-inquiry',
    configureServer(server) {
      server.middlewares.use((req, res, next) => {
        if (req.url === '/api/inquiry' && req.method === 'POST') {
          let body = '';
          req.on('data', (chunk) => {
            body += chunk;
          });
          req.on('end', () => {
            try {
              const data = JSON.parse(body || '{}');
              const dataDir = resolve(__dirname, 'data');
              if (!fs.existsSync(dataDir)) {
                fs.mkdirSync(dataDir, { recursive: true });
              }
              const csvPath = resolve(dataDir, 'inquiries.csv');
              const fileExists = fs.existsSync(csvPath);

              // CSV Headers
              const headers = ['Timestamp', 'Full Name', 'Phone', 'Email', 'Coaching', 'Message', 'Source Page'];

              // Format date: YYYY-MM-DD HH:mm:ss
              const now = new Date();
              const pad = (n: number) => String(n).padStart(2, '0');
              const timestamp = `${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())} ${pad(now.getHours())}:${pad(now.getMinutes())}:${pad(now.getSeconds())}`;

              const escapeCsv = (val: any = '') => `"${String(val ?? '').replace(/"/g, '""')}"`;

              const row = [
                escapeCsv(timestamp),
                escapeCsv(data.name || ''),
                escapeCsv(data.phone || ''),
                escapeCsv(data.email || ''),
                escapeCsv(data.coaching || ''),
                escapeCsv(data.message || ''),
                escapeCsv(data.page || '')
              ].join(',') + '\n';

              if (!fileExists) {
                fs.writeFileSync(csvPath, headers.map(escapeCsv).join(',') + '\n' + row, 'utf8');
              } else {
                fs.appendFileSync(csvPath, row, 'utf8');
              }

              res.statusCode = 200;
              res.setHeader('Content-Type', 'application/json');
              res.end(JSON.stringify({
                success: true,
                message: 'Inquiry successfully saved to inquiries.csv',
                file: 'data/inquiries.csv'
              }));
            } catch (err: any) {
              res.statusCode = 500;
              res.setHeader('Content-Type', 'application/json');
              res.end(JSON.stringify({ success: false, message: err?.message || 'Server error' }));
            }
          });
          return;
        }
        next();
      });
    }
  };
}

export default defineConfig({
  plugins: [csvInquiryPlugin()],
  root: '.',
  base: './',
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        aboutcambridge: resolve(__dirname, 'aboutcambridge.html'),
        testimonials: resolve(__dirname, 'testimonials.html'),
        franchisee: resolve(__dirname, 'franchisee.html'),
        cambridgeinmedia: resolve(__dirname, 'cambridgeinmedia.html'),
        certificatesofauthorizations: resolve(__dirname, 'certificatesofauthorizations.html'),
        immigrationvisa: resolve(__dirname, 'immigrationvisa.html'),
        studentvisa: resolve(__dirname, 'studentvisa.html'),
        visitorvisa: resolve(__dirname, 'visitorvisa.html'),
        internationaltours: resolve(__dirname, 'internationaltours.html'),
        usastudent: resolve(__dirname, 'usastudent.html'),
        ukstudy: resolve(__dirname, 'ukstudy.html'),
        australiastudy: resolve(__dirname, 'australiastudy.html'),
        newzealandstudy: resolve(__dirname, 'newzealandstudy.html'),
        canadastudy: resolve(__dirname, 'canadastudy.html'),
        europestudy: resolve(__dirname, 'europestudy.html'),
        singaporestudy: resolve(__dirname, 'singaporestudy.html'),
        TOEFL: resolve(__dirname, 'TOEFL.html'),
        IELTS: resolve(__dirname, 'IELTS.html'),
        spokenenglish: resolve(__dirname, 'spokenenglish.html'),
        englishexams: resolve(__dirname, 'englishexams.html'),
        french: resolve(__dirname, 'french.html'),
        german: resolve(__dirname, 'german.html'),
        inquiry: resolve(__dirname, 'inquiry.html'),
        center: resolve(__dirname, 'center.html'),
        privacypolicy: resolve(__dirname, 'privacypolicy.html')
      }
    }
  },
  server: {
    port: 5173,
    open: false
  }
});
