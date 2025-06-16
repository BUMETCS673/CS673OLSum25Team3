document.addEventListener("DOMContentLoaded", () => {
  const form     = document.getElementById("login-form");
  const loginMsg = document.getElementById("login-msg");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    loginMsg.textContent = "";

    const payload = {
      username: document.getElementById("username").value.trim(),
      password: document.getElementById("password").value
    };

    try {
      const res = await fetch(API_LOGIN_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken":   csrfToken
        },
        body: JSON.stringify(payload)
      });
      const data = await res.json();

      if (res.ok) {
        window.location.href = "/dashboard/";
      } else {
        loginMsg.textContent = data.error || "Login failed.";
      }
    } catch (err) {
      loginMsg.textContent = "Server error. Please try again.";
    }
  });
});
