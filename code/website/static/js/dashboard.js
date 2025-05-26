// Check authentication on page load
const token = localStorage.getItem("access");
if (!token) {
  window.location.href = "/login/";
}

function logout() {
  const logoutButton = document.querySelector('button');
  
  // Show loading state
  logoutButton.disabled = true;
  logoutButton.innerText = "Logging out...";
  
  // Clear token and redirect
  localStorage.removeItem("access");
  
  setTimeout(() => {
    window.location.href = "/login/";
  }, 500);
}

// Optional: Add token validation
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
    return true; // Don't redirect on network errors
  }
}

// Uncomment if you implement token validation endpoint
// validateToken();