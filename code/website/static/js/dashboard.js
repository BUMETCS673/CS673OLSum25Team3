// Check authentication on page load
document.addEventListener('DOMContentLoaded', async function() {
  // Validate token first
  const isValid = await validateToken();
  if (!isValid) {
    window.location.href = "/login/";
    return;
  }
  
  // Set up event listeners
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
      method: "POST",
      headers: { 
        "Authorization": `Bearer ${token}`,
        "Content-Type": "application/json"
      }
    });
    
    if (!res.ok) {
      localStorage.removeItem("access");
      return false;
    }
    
    const data = await res.json();
    // Update username in the UI if available
    if (data.username) {
      const usernameElement = document.querySelector('.username');
      if (usernameElement) {
        usernameElement.textContent = data.username;
      }
    }
    
    return true;
  } catch (error) {
    console.log("Token validation failed:", error);
    return false;
  }
}

async function logout() {
  const logoutButton = document.querySelector('button[onclick="logout()"]');
  
  if (logoutButton) {
    logoutButton.disabled = true;
    logoutButton.innerText = "Logging out...";
  }
  
  // Call logout endpoint to clear server session
  const token = localStorage.getItem("access");
  if (token) {
    try {
      await fetch("/api/logout/", {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${token}`,
          "Content-Type": "application/json"
        }
      });
    } catch (error) {
      console.log("Logout error:", error);
    }
  }
  
  // Clear local storage
  localStorage.removeItem("access");
  localStorage.removeItem("refresh");
  
  // Clear session storage
  sessionStorage.clear();
  
  // Redirect to login
  window.location.replace("/login/");
}

// Prevent back button after logout
window.addEventListener('pageshow', function(event) {
  if (event.persisted || (window.performance && window.performance.navigation.type === 2)) {
    // Page was loaded from cache
    validateToken().then(isValid => {
      if (!isValid) {
        window.location.href = "/login/";
      }
    });
  }
});