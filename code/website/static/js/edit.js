async function submit_edit() {
  const editButton = document.querySelector('button');
  const messageElement = document.getElementById("edit-msg");
  const firstname = document.getElementById("edit-firstname").value.trim();
  const lastname = document.getElementById("edit-lastname").value.trim();
  const email = document.getElementById("edit-email").value.trim();
  const phone = document.getElementById("edit-phone").value.trim();
  const birthdate = document.getElementById("edit-birthdate").value.trim();

  try {
    const res = await fetch("/api/edit_profile/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        token: localStorage.getItem("access"),
        firstname: firstname,
        lastname: lastname,
        email: email,
        phone: phone,
        birthdate: birthdate
      })
    });

    const data = await res.json();
    console.log(data);
    
    messageElement.innerText = "Profile updated successfully!";
    messageElement.className = "text-success mt-3 text-center";
    
  } catch (error) {
    messageElement.innerText = "Network error. Please check your connection.";
    messageElement.className = "text-danger mt-3 text-center";
  } finally {
    editButton.disabled = false;
    editButton.innerText = originalText;
  }
}