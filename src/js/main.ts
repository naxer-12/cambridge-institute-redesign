import '../css/main.css';
import '../css/components.css';
import { setupInquiryForms } from './inquiry-form';

document.addEventListener('DOMContentLoaded', () => {
  // 1. Sticky Header Observer
  const header = document.querySelector<HTMLElement>('.site-header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 20) {
        header.classList.add('site-header--scrolled');
      } else {
        header.classList.remove('site-header--scrolled');
      }
    });
  }

  // 2. Mobile Drawer Navigation
  const mobileToggle = document.querySelector<HTMLButtonElement>('.mobile-toggle');
  const mobileDrawer = document.querySelector<HTMLElement>('.mobile-drawer');
  const drawerClose = document.querySelector<HTMLButtonElement>('.mobile-drawer__close');

  function openDrawer() {
    if (mobileDrawer) {
      mobileDrawer.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeDrawer() {
    if (mobileDrawer) {
      mobileDrawer.classList.remove('open');
      document.body.style.overflow = '';
    }
  }

  if (mobileToggle && mobileDrawer) {
    mobileToggle.addEventListener('click', openDrawer);
  }

  if (drawerClose && mobileDrawer) {
    drawerClose.addEventListener('click', closeDrawer);
  }

  if (mobileDrawer) {
    mobileDrawer.addEventListener('click', (e) => {
      if (e.target === mobileDrawer) {
        closeDrawer();
      }
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && mobileDrawer?.classList.contains('open')) {
      closeDrawer();
    }
  });

  // 3. Mobile Nav Accordion Groups
  const groupTitles = document.querySelectorAll<HTMLButtonElement>('.mobile-nav-group__title');
  groupTitles.forEach((btn) => {
    btn.addEventListener('click', () => {
      const parent = btn.parentElement;
      if (parent) {
        parent.classList.toggle('expanded');
      }
    });
  });

  // 4. Accordions (FAQs, syllabus modules, etc.)
  const accordionTriggers = document.querySelectorAll<HTMLButtonElement>('.accordion-trigger');
  accordionTriggers.forEach((trigger) => {
    trigger.addEventListener('click', () => {
      const item = trigger.closest('.accordion-item');
      if (item) {
        item.classList.toggle('active');
      }
    });
  });

  // 5. Tab Panels
  const tabButtons = document.querySelectorAll<HTMLButtonElement>('.tab-btn');
  tabButtons.forEach((btn) => {
    btn.addEventListener('click', () => {
      const tabTarget = btn.getAttribute('data-tab');
      if (!tabTarget) return;

      const container = btn.closest('.tab-container');
      if (!container) return;

      container.querySelectorAll('.tab-btn').forEach((b) => b.classList.remove('active'));
      container.querySelectorAll('.tab-pane').forEach((p) => p.classList.remove('active'));

      btn.classList.add('active');
      const targetPane = container.querySelector(`#${tabTarget}`);
      if (targetPane) targetPane.classList.add('active');
    });
  });

  // 6. Initialize Forms
  setupInquiryForms();
});
