document.addEventListener("DOMContentLoaded", function () {
    const container = document.getElementById("records-container");
    const previewBody = document.getElementById("preview-body");
    const downloadBtn = document.getElementById("download-btn");
    const confirmDownloadBtn = document.getElementById("confirm-download");
    const retryBtn = document.getElementById("retry-btn");
    const errorContainer = document.getElementById("error-container");
    const recordMessage = document.getElementById("record-message");

    const records = [
        { title: "Annual Physical Exam", date: "2024-01-15", summary: "Routine check-up. Vitals normal. No follow-up needed." },
        { title: "Blood Test Report", date: "2024-02-20", summary: "Slightly elevated cholesterol. Recommended dietary changes." },
        { title: "Flu Vaccination", date: "2024-03-05", summary: "Administered seasonal influenza vaccine. No side effects." },
        { title: "Dermatology Consultation", date: "2024-04-12", summary: "Treated for mild eczema. Prescribed topical corticosteroid." },
        { title: "Eye Examination", date: "2024-05-18", summary: "20/20 vision confirmed. No corrective lenses required." },
        { title: "MRI Scan (Knee)", date: "2024-06-22", summary: "Minor inflammation observed. Recommended physiotherapy." },
        { title: "Cardiology Checkup", date: "2024-07-15", summary: "Heart function normal. No abnormalities detected." },
        { title: "Dental Cleaning", date: "2024-08-05", summary: "Teeth cleaned. No cavities or issues noted." },
        { title: "Allergy Testing", date: "2024-09-10", summary: "Positive for dust mites and pollen. Prescribed antihistamines." },
        { title: "COVID-19 Booster Shot", date: "2024-10-02", summary: "Booster administered. Mild soreness at injection site." },
        { title: "Nutrition Counseling", date: "2024-11-08", summary: "Advised on low-sodium diet for better blood pressure management." },
        { title: "Physical Therapy Follow-Up", date: "2024-12-15", summary: "Improved mobility after 6 sessions. Continued exercises recommended." },
        { title: "Annual Physical Exam", date: "2025-01-10", summary: "Routine check-up. Vitals normal. Follow-up appointment scheduled." },
        { title: "Blood Test Report", date: "2025-02-11", summary: "Cholesterol levels improved. Continue current diet plan." },
        { title: "Flu Vaccination", date: "2025-03-12", summary: "Administered seasonal influenza vaccine. No adverse reactions." },
        { title: "Dermatology Consultation", date: "2025-04-13", summary: "Eczema well-controlled. Continue current treatment regimen." },
        { title: "Eye Examination", date: "2025-05-14", summary: "Vision remains stable at 20/20. Annual follow-up recommended." },
        { title: "MRI Scan (Knee)", date: "2025-06-15", summary: "Significant improvement in inflammation. Continue physiotherapy." }
    ];

    // Update dashboard stats
    localStorage.setItem("medical_records_count", records.length);

    function loadRecords() {
        container.innerHTML = "";

        if (records.length === 0) {
            if (recordMessage) {
                recordMessage.style.display = "block";
            }
            downloadBtn.disabled = true;
            return;
        }

        records.forEach((r) => {
            const col = document.createElement("div");
            col.className = "col-md-4";
            col.innerHTML = `
                <div class='record-card'>
                    <div class='record-title'>${r.title}</div>
                    <div class='record-date'>${r.date}</div>
                    <div class='record-summary'>${r.summary}</div>
                </div>`;
            container.appendChild(col);
        });

        container.style.display = "flex";
        errorContainer.style.display = "none";
        downloadBtn.disabled = false;

        if (recordMessage) {
            recordMessage.style.display = "none";
        }
    }

    retryBtn?.addEventListener("click", loadRecords);

    downloadBtn.addEventListener("click", () => {
        let html = "<h4>Preview</h4>";
        records.forEach((r) => {
            html += `<div><b>${r.title}</b><br>Date: ${r.date}<br>${r.summary}</div><hr>`;
        });
        previewBody.innerHTML = html;
        new bootstrap.Modal(document.getElementById("previewModal")).show();
    });

    confirmDownloadBtn.addEventListener("click", () => {
        const { jsPDF } = window.jspdf;
        const doc = new jsPDF();
        let y = 20;
        records.forEach((r) => {
            doc.text(`• ${r.title}`, 10, y += 10);
            doc.text(`Date: ${r.date}`, 15, y += 8);
            doc.text(`Summary: ${r.summary}`, 15, y += 8);
            y += 10;
        });
        doc.save("Medical_Records.pdf");
    });

    loadRecords();
});
