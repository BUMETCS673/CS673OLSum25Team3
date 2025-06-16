document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("register-form");
  const msg  = document.getElementById("register-msg");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    msg.textContent = "";

    const payload = {
      username:      document.getElementById("username").value.trim(),
      password:      document.getElementById("password").value,
      email:         document.getElementById("email").value.trim(),
      first_name:    document.getElementById("first_name").value.trim(),
      last_name:     document.getElementById("last_name").value.trim(),
      phone:         document.getElementById("phone").value.trim(),
      date_of_birth: document.getElementById("dob").value
    };

    try {
      const response = await fetch(API_REGISTER_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrftoken
        },
        body: JSON.stringify(payload)
      });

      const data = await response.json();

      if (response.ok) {
        msg.className = "text-success text-center mt-2";
        msg.textContent = "Registration successful! Redirecting...";
        setTimeout(() => window.location.href = "/login/", 1500);
      } else {
        msg.className = "text-danger text-center mt-2";
        msg.textContent = data.error || "Registration failed.";
      }
    } catch (err) {
      msg.className = "text-danger text-center mt-2";
      msg.textContent = "Server error. Please try again.";
    }
  });
});
