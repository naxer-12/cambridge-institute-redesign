/**
 * Inquiry Form & Consultation Validation Engine
 */

export function setupInquiryForms(): void {
  const forms = document.querySelectorAll<HTMLFormElement>('.js-inquiry-form');

  forms.forEach((form) => {
    form.addEventListener('submit', async (e) => {
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

      // Collect field data
      const nameInput = form.querySelector<HTMLInputElement>('#inq_name, [name="name"]');
      const phoneInput = form.querySelector<HTMLInputElement>('#inq_phone, [name="phone"]');
      const emailInput = form.querySelector<HTMLInputElement>('#inq_email, [name="email"]');
      const coachingInput = form.querySelector<HTMLSelectElement>('#inq_coaching, [name="coaching"]');
      const msgInput = form.querySelector<HTMLTextAreaElement>('#inq_msg, [name="message"]');

      // Also support franchise form if applicable
      const frName = form.querySelector<HTMLInputElement>('#fr_name');
      const frPhone = form.querySelector<HTMLInputElement>('#fr_phone');
      const frEmail = form.querySelector<HTMLInputElement>('#fr_email');
      const frCity = form.querySelector<HTMLInputElement>('#fr_city');
      const frBg = form.querySelector<HTMLTextAreaElement>('#fr_bg');

      const isFranchise = !!frName;

      const payload = isFranchise ? {
        formType: 'franchise',
        name: frName?.value.trim() || '',
        phone: frPhone?.value.trim() || '',
        email: frEmail?.value.trim() || '',
        coaching: `Franchise: ${frCity?.value.trim() || ''}`,
        message: frBg?.value.trim() || '',
        page: window.location.pathname
      } : {
        formType: 'counseling',
        name: nameInput?.value.trim() || '',
        phone: phoneInput?.value.trim() || '',
        email: emailInput?.value.trim() || '',
        coaching: coachingInput?.value || '',
        message: msgInput?.value.trim() || '',
        page: window.location.pathname
      };

      // Show loading state
      const submitBtn = form.querySelector<HTMLButtonElement>('button[type="submit"]');
      const originalHtml = submitBtn ? submitBtn.innerHTML : 'Submit Inquiry';
      let statusDiv = form.querySelector<HTMLDivElement>('.form-status');
      
      if (!statusDiv) {
        statusDiv = document.createElement('div');
        statusDiv.className = 'form-status';
        statusDiv.style.marginTop = '12px';
        statusDiv.style.padding = '12px';
        statusDiv.style.borderRadius = '8px';
        statusDiv.style.fontSize = '14px';
        statusDiv.style.textAlign = 'center';
        submitBtn?.parentElement?.appendChild(statusDiv);
      }

      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerText = 'Submitting...';
      }
      statusDiv.style.display = 'none';

      try {
        const response = await fetch('/api/inquiry', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(payload)
        });

        const result = await response.json();

        if (response.ok && result.success) {
          form.reset();
          statusDiv.style.display = 'block';
          statusDiv.style.background = 'rgba(16, 185, 129, 0.12)';
          statusDiv.style.color = '#065f46';
          statusDiv.style.border = '1px solid #10b981';
          statusDiv.innerHTML = '<strong>Inquiry Recorded!</strong> Your details have been saved to the database. A senior counselor will connect with you within 24 hours.';
        } else {
          throw new Error(result.message || 'Submission failed');
        }
      } catch (err: any) {
        console.error('Form submission error:', err);
        statusDiv.style.display = 'block';
        statusDiv.style.background = 'rgba(239, 68, 68, 0.12)';
        statusDiv.style.color = '#991b1b';
        statusDiv.style.border = '1px solid #ef4444';
        statusDiv.innerHTML = 'Could not save inquiry. Please ensure the backend is active or try again.';
      } finally {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = originalHtml;
        }
      }
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
