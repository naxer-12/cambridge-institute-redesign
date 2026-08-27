import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
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
