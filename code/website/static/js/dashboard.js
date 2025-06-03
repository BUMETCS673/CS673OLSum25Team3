function logout() {
  const logoutButton = document.querySelector('button[onclick="logout()"]');
  
  if (logoutButton) {
    logoutButton.disabled = true;
    logoutButton.innerText = "Logging out...";
  }
  
  localStorage.removeItem("access");
  
  setTimeout(() => {
    window.location.href = "/login/";
  }, 500);
}

document.addEventListener('DOMContentLoaded', function() {
  
  const scheduleButtons = document.querySelectorAll('.action-card .btn');
  if (scheduleButtons[0]) {
    scheduleButtons[0].addEventListener('click', function() {
      alert('Schedule appointment feature coming soon!');
    });
  }
  
  if (scheduleButtons[1]) {
    scheduleButtons[1].addEventListener('click', function() {
      alert('View records feature coming soon!');
    });
  }
  
  if (scheduleButtons[2]) {
    scheduleButtons[2].addEventListener('click', function() {
      alert('Manage prescriptions feature coming soon!');
    });
  }
  
  const statCards = document.querySelectorAll('.stat-card');
  statCards.forEach(card => {
    card.addEventListener('click', function() {

      const statLabel = this.querySelector('.stat-label').textContent;
      alert(`${statLabel} details coming soon!`);
    });
    
    card.style.cursor = 'pointer';
  });
  
  const actionCards = document.querySelectorAll('.action-card');
  actionCards.forEach(card => {
    card.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-5px)';
    });
    
    card.addEventListener('mouseleave', function() {
      this.style.transform = 'translateY(0)';
    });
  });
});

async function validateToken() {
  const token = localStorage.getItem("access");
  if (!token) return false;
  
  try {
    const res = await fetch("/api/validate-token/", {
      method: "GET",
      headers: { 
        "Authorization": `Bearer ${token}`,
        "Content-Type": "application/json"
      }
    });
    
    if (!res.ok) {
      localStorage.removeItem("access");
      window.location.href = "/login/";
      return false;
    }
    
    return true;
  } catch (error) {
    console.log("Token validation failed:", error);
    return true; 
  }
}