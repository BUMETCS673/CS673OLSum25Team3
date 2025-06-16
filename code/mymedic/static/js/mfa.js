document.addEventListener("DOMContentLoaded", () => {
  const form     = document.getElementById("mfa-form");
  const mfaMsg = document.getElementById("mfa-msg");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    mfaMsg.textContent = "";

    const payload = {
      code: document.getElementById("code").value.trim(),
    };

    try {
      const res = await fetch(API_MFA_URL, {
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
        mfaMsg.textContent = data.error || "MFA Failed.";
      }
    } catch (err) {
      mfaMsg.textContent = "Server error. Please try again.";
    }
  });
});
