async function searchRecords() {
  const input = document.getElementById("search-input").value.trim();
  const resultsDiv = document.getElementById("search-results");

  resultsDiv.innerHTML = "";

  if (!input) {
    resultsDiv.innerHTML = `<p class="text-danger">⚠️ Please enter a search term.</p>`;
    return;
  }

  try {
    const response = await fetch(`/api/search/?q=${encodeURIComponent(input)}`);
    const data = await response.json();

    if (data.length === 0) {
      resultsDiv.innerHTML = `<p>No results found for "<strong>${input}</strong>".</p>`;
      return;
    }

/**
@ai-generated
Tool: ChatGPT (OpenAI)
Prompt: "Render search results as an HTML list from filtered JSON data"
Generated on: 2025-06-08
Modified by: Mengliang Tan
Modifications: Display doctor, prescription, date, dosage, and notes in formatted HTML

Verified: ✅ Tested via frontend display
*/
    let html = `<ul class="list-group mt-3">`;
    data.forEach(record => {
      html += `<li class="list-group-item">
     <strong>Doctor:</strong> ${record.doctor} <br>
     <strong>Prescription:</strong> ${record.prescription} <br>
     <strong>Date:</strong> ${record.date} <br>
     <strong>Dosage:</strong> ${record.dosage} <br>
     <strong>Notes:</strong> ${record.notes}  
  </li>`;
    });
    html += `</ul>`;
    resultsDiv.innerHTML = html;

  } catch (err) {
    resultsDiv.innerHTML = `<p class="text-danger">❌ Error searching records. Please try again later.</p>`;
  }
}

