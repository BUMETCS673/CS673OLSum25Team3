document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("mfa-form");
  const msg = document.getElementById("mfa-msg");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    msg.textContent = "";

    const code = document.getElementById("code").value.trim();

    try {
      const res = await fetch(API_MFA_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({ code })
      });

      const data = await res.json();

      if (res.ok) {
        window.location.href = "/dashboard/";
      } else {
        msg.textContent = data.error || "Verification failed.";
      }
    } catch (err) {
      msg.textContent = "Server error. Please try again.";
    }
  });
});
