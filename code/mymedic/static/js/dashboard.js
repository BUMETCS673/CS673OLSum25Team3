document.addEventListener('DOMContentLoaded', function() {
  
  const scheduleButtons = document.querySelectorAll('.action-card .btn');
  if (scheduleButtons[0]) {
    scheduleButtons[0].addEventListener('click', function() {
      alert('Schedule appointment feature coming soon!');
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

document.addEventListener("DOMContentLoaded", function () {
  const recordCount = localStorage.getItem("medical_records_count");
  if (recordCount !== null) {
    const countElement = document.getElementById("medical-records-count");
    if (countElement) {
      countElement.textContent = recordCount;
    }
  }
});