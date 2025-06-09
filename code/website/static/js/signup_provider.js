// Toggle password visibility
function togglePassword(fieldId, button) {
  const field = document.getElementById(fieldId);
  const icon  = button.querySelector('i');
  if (field.type === 'password') {
    field.type = 'text';
    icon.classList.replace('bi-eye', 'bi-eye-slash');
  } else {
    field.type = 'password';
    icon.classList.replace('bi-eye-slash', 'bi-eye');
  }
}

// Check password match in real-time
function checkPasswordMatch() {
  const pw   = document.getElementById('signup-pass').value;
  const cpw  = document.getElementById('signup-confirm-pass').value;
  const fld  = document.getElementById('signup-confirm-pass');
  const ind  = document.getElementById('match-indicator');

  if (!cpw) {
    fld.classList.remove('is-valid', 'is-invalid');
    ind.textContent = '';
    return;
  }
  if (pw === cpw) {
    fld.classList.remove('is-invalid');
    fld.classList.add('is-valid');
    ind.innerHTML = '<i class="bi bi-check-circle-fill text-success"></i>';
  } else {
    fld.classList.remove('is-valid');
    fld.classList.add('is-invalid');
    ind.innerHTML = '<i class="bi bi-x-circle-fill text-danger"></i>';
  }
}

async function signupProvider() {
  const btn = document.getElementById('provider-signup-btn');
  const msg = document.getElementById('provider-signup-msg');
  const origText = btn.innerText;

  // Gather inputs
  const firstName      = document.getElementById('signup-firstname').value.trim();
  const lastName       = document.getElementById('signup-lastname').value.trim();
  const email          = document.getElementById('signup-email').value.trim();
  const username       = document.getElementById('signup-user').value.trim();
  const password       = document.getElementById('signup-pass').value;
  const confirmPassword= document.getElementById('signup-confirm-pass').value;
  const license        = document.getElementById('signup-license').value.trim();
  const specialization = document.getElementById('signup-specialization').value.trim();
  const clinicName     = document.getElementById('signup-clinic-name').value.trim();
  const clinicAddress  = document.getElementById('signup-clinic-address').value.trim();
  const phone          = document.getElementById('signup-phone').value.trim();

  // Reset message
  msg.innerText = '';
  msg.className = '';

  // Validation
  if (![firstName, lastName, email, username, password, confirmPassword, license, specialization, clinicName, clinicAddress].every(Boolean)) {
    msg.innerText = 'Please fill in all required fields.';
    msg.className = 'text-danger mt-3';
    return;
  }
  if (password.length < 6) {
    msg.innerText = 'Password must be at least 6 characters long.';
    msg.className = 'text-danger mt-3';
    return;
  }
  if (password !== confirmPassword) {
    msg.innerText = 'Passwords do not match.';
    msg.className = 'text-danger mt-3';
    return;
  }

  // Disable button
  btn.disabled = true;
  btn.innerText = 'Creating Account...';

  const payload = {
    username,
    password,
    email,
    first_name: firstName,
    last_name: lastName,
    license_number: license,
    specialization,
    clinic_name: clinicName,
    clinic_address: clinicAddress,
    phone
  };

  try {
    const res  = await fetch('/api/register/provider/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();

    if (res.ok) {
      msg.innerText = data.message;
      msg.className = 'text-success mt-3';
      setTimeout(() => window.location.href = '/login/', 2000);
    } else {
      msg.innerText = data.error || 'Signup failed. Please try again.';
      msg.className = 'text-danger mt-3';
    }
  } catch (err) {
    console.error(err);
    msg.innerText = 'Network error. Please try again later.';
    msg.className = 'text-danger mt-3';
  } finally {
    btn.disabled = false;
    btn.innerText = origText;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.password-toggle').forEach(btn => {
    btn.addEventListener('click', () => togglePassword(btn.dataset.target, btn));
  });

  document.getElementById('signup-pass')
    .addEventListener('input', checkPasswordMatch);
  document.getElementById('signup-confirm-pass')
    .addEventListener('input', checkPasswordMatch);

  document.getElementById('provider-signup-btn')
    .addEventListener('click', e => {
      e.preventDefault();
      signupProvider();
    });

  document.querySelectorAll('#provider-signup-form input')
    .forEach(input => {
      input.addEventListener('keypress', e => {
        if (e.key === 'Enter') {
          e.preventDefault();
          signupProvider();
        }
      });
    });
});
