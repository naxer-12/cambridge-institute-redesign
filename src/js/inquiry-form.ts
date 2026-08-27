/**
 * Inquiry Form & Consultation Validation Engine
 */

export function setupInquiryForms(): void {
  const forms = document.querySelectorAll<HTMLFormElement>('.js-inquiry-form');

  forms.forEach((form) => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      
      let isValid = true;
      const requiredInputs = form.querySelectorAll<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>('[required]');
      
      requiredInputs.forEach((input) => {
        const val = input.value.trim();
        if (!val) {
          input.classList.add('error');
          isValid = false;
        } else {
          input.classList.remove('error');
        }

        // Email validation
        if (input.type === 'email' && val) {
          const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          if (!emailRegex.test(val)) {
            input.classList.add('error');
            isValid = false;
          }
        }

        // Phone validation
        if (input.type === 'tel' && val) {
          const phoneRegex = /^[0-9+ \-()]{7,16}$/;
          if (!phoneRegex.test(val)) {
            input.classList.add('error');
            isValid = false;
          }
        }
      });

      if (!isValid) {
        const firstErr = form.querySelector('.error') as HTMLElement;
        if (firstErr) firstErr.focus();
        return;
      }

      // Show success state
      const submitBtn = form.querySelector<HTMLButtonElement>('button[type="submit"]');
      const originalText = submitBtn ? submitBtn.innerText : 'Submit Inquiry';
      
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerText = 'Submitting...';
      }

      setTimeout(() => {
        alert('Thank you for reaching out to Cambridge Institute! Our Senior Counselor will contact you within 24 business hours.');
        form.reset();
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerText = originalText;
        }
      }, 700);
    });

    // Clear error class on input
    form.querySelectorAll('input, select, textarea').forEach((field) => {
      field.addEventListener('input', () => {
        field.classList.remove('error');
      });
      field.addEventListener('change', () => {
        field.classList.remove('error');
      });
    });
  });
}
