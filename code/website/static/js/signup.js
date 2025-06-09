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

async function signup() {
  const btn = document.getElementById('signup-btn');
  const msg = document.getElementById('signup-msg');
  const originalText = btn.innerText;

  // Gather values
  const firstName      = document.getElementById("signup-firstname").value.trim();
  const lastName       = document.getElementById("signup-lastname").value.trim();
  const email          = document.getElementById("signup-email").value.trim();
  const username       = document.getElementById("signup-user").value.trim();
  const password       = document.getElementById("signup-pass").value;
  const confirmPassword= document.getElementById("signup-confirm-pass").value;
  const phone          = document.getElementById("signup-phone").value.trim();
  const dob            = document.getElementById("signup-dob").value;
  const termsAccepted  = document.getElementById("terms-checkbox").checked;

  // Reset message
  msg.innerText = "";
  msg.className = "";

  // Basic validation
  if (!firstName || !lastName || !email || !username || !password || !confirmPassword) {
    msg.innerText = "Please fill in all required fields.";
    msg.className = "text-danger mt-3 text-center";
    return;
  }
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    msg.innerText = "Please enter a valid email address.";
    msg.className = "text-danger mt-3 text-center";
    return;
  }
  if (password.length < 6) {
    msg.innerText = "Password must be at least 6 characters long.";
    msg.className = "text-danger mt-3 text-center";
    return;
  }
  if (password !== confirmPassword) {
    msg.innerText = "Passwords do not match.";
    msg.className = "text-danger mt-3 text-center";
    return;
  }
  if (!termsAccepted) {
    msg.innerText = "Please accept the Terms of Service and Privacy Policy.";
    msg.className = "text-danger mt-3 text-center";
    return;
  }

  // Disable button
  btn.innerText = "Creating Account...";

  // Prepare payload
  const requestData = {
    username,
    password,
    email,
    first_name: firstName,
    last_name: lastName,
    phone: phone || "",
    date_of_birth: dob || null
  };

  try {
    console.log("Sending registration request:", requestData);
    const res = await fetch("/api/register/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(requestData)
    });

    const data = await res.json();
    console.log("Response:", res.status, data);

    if (res.ok && data.message) {
      msg.innerText = "Account created successfully! Redirecting to login...";
      msg.className = "text-success mt-3 text-center";

      // Clear form
      document.querySelectorAll('#signup-form input').forEach(input => {
        input.value = '';
        input.classList.remove('is-valid', 'is-invalid');
      });
      document.getElementById("terms-checkbox").checked = false;

      setTimeout(() => window.location.href = "/login/", 2000);
    } else {
      msg.innerText = data.error || data.detail || "Signup failed. Please try again.";
      msg.className = "text-danger mt-3 text-center";
      console.error("Signup error:", data);
    }
  } catch (err) {
    console.error("Network error:", err);
    msg.innerText = "Network error. Please check your connection.";
    msg.className = "text-danger mt-3 text-center";
  } finally {
    btn.disabled = false;
    btn.innerText = originalText;
  }
}

document.addEventListener('DOMContentLoaded', function() {
  // 1) Eye toggles
  document.querySelectorAll('.password-toggle').forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.dataset.target;
      togglePassword(target, btn);
    });
  });

  // 2) Real-time password match
  document.getElementById('signup-pass')
          .addEventListener('input', checkPasswordMatch);
  document.getElementById('signup-confirm-pass')
          .addEventListener('input', checkPasswordMatch);

  // 3) Enter key submits
  document.querySelectorAll('#signup-form input')
          .forEach(input => input.addEventListener('keypress', e => {
    if (e.key === 'Enter') {
      e.preventDefault();
      signup();
    }
  }));

  // 4) Button click
  document.getElementById('signup-btn')
          .addEventListener('click', e => {
    e.preventDefault();
    signup();
  });
});
