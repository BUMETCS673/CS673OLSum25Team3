async function signup() {
  const signupButton = document.querySelector('button');
  const messageElement = document.getElementById("signup-msg");
  const username = document.getElementById("signup-user").value.trim();
  const password = document.getElementById("signup-pass").value;
  const firstname = document.getElementById("signup-firstname").value.trim();
  const lastname = document.getElementById("signup-lastname").value.trim();
  const email = document.getElementById("signup-email").value.trim();

  if (!username || !password || !firstname || !lastname) {
    messageElement.innerText = "Please fill in all fields.";
    messageElement.className = "text-danger mt-3 text-center";
    return;
  }

  if (password.length < 6) {
    messageElement.innerText = "Password must be at least 6 characters long.";
    messageElement.className = "text-danger mt-3 text-center";
    return;
  }

  const originalText = signupButton.innerText;
  signupButton.disabled = true;
  signupButton.innerText = "Creating Account...";
  messageElement.innerText = "";

  try {
    const res = await fetch("/api/register/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: username,
        password: password,
        firstname: firstname,
        lastname: lastname,
        email: email
      })
    });

    const data = await res.json();
    
    if (res.ok && data.message) {
      messageElement.innerText = data.message + " Redirecting to login...";
      messageElement.className = "text-success mt-3 text-center";
      setTimeout(() => {
        window.location.href = "/login/";
      }, 1500);
    } else {
      messageElement.innerText = data.error || "Signup failed. Please try again.";
      messageElement.className = "text-danger mt-3 text-center";
    }
  } catch (error) {
    messageElement.innerText = "Network error. Please check your connection.";
    messageElement.className = "text-danger mt-3 text-center";
  } finally {
    signupButton.disabled = false;
    signupButton.innerText = originalText;
  }
}

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById("signup-pass").addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      signup();
    }
  });
});