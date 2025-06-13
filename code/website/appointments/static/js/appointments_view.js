async function loadAppointments() {
    const tbody = document.getElementById('appointmentsBody');
    const noAppDiv = document.getElementById('noAppointments');
    const table = document.getElementById('appointmentsTable');

    tbody.innerHTML = '';
    try {
        const response = await fetch('/appointments/api/appointments/');
        if (!response.ok) throw new Error('Failed to fetch appointments');
        const appointments = await response.json();

        if (!appointments.length) {
            noAppDiv.style.display = '';
            table.style.display = 'none';
        } else {
            noAppDiv.style.display = 'none';
            table.style.display = '';
            appointments.forEach(app => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${app.datetime}</td>
                    <td>${app.patient_id}</td>
                    <td>${app.doctor_id}</td>
                    <td>${app.reason}</td>
                    <td>${app.status}</td>
                `;
                tbody.appendChild(tr);
            });
        }
    } catch (error) {
        noAppDiv.textContent = 'Appointments view coming soon';
        noAppDiv.style.display = '';
        table.style.display = 'none';
        console.error('Error fetching appointments:', error);
    }
}

window.addEventListener('DOMContentLoaded', loadAppointments);