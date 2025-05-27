async function login() {
  const loginButton = document.querySelector('button');
  const messageElement = document.getElementById("login-msg");
  const username = document.getElementById("login-user").value.trim();
  const password = document.getElementById("login-pass").value;

  if (!username || !password) {
    messageElement.innerText = "Please fill in all fields.";
    return;
  }

  const originalText = loginButton.innerText;
  loginButton.disabled = true;
  loginButton.innerText = "Logging in...";
  messageElement.innerText = "";

  try {
    const res = await fetch("/api/login/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: username,
        password: password
      })
    });

    const data = await res.json();
    
    if (data.access) {
      localStorage.setItem("access", data.access);
      messageElement.innerText = "Login successful! Redirecting...";
      messageElement.className = "text-success mt-3 text-center";
      setTimeout(() => {
        window.location.href = "/dashboard/";
      }, 500);
    } else {
      messageElement.innerText = data.error || "Login failed. Please try again.";
      messageElement.className = "text-danger mt-3 text-center";
    }
  } catch (error) {
    messageElement.innerText = "Network error. Please check your connection.";
    messageElement.className = "text-danger mt-3 text-center";
  } finally {
    loginButton.disabled = false;
    loginButton.innerText = originalText;
  }
}

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById("login-pass").addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      login();
    }
  });
});