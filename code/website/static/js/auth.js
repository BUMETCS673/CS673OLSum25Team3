/**
 * Fetches the current user’s role from the API.
 * @returns {Promise<'patient'|'provider'|null>} 
 */
export async function getUserRole() {
  const token = localStorage.getItem('access');
  if (!token) return null;

  const res = await fetch('/api/validate-token/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    }
  });

  if (!res.ok) {
    console.error('Failed to validate token', await res.text());
    return null;
  }

  const { role } = await res.json();
  return role;  // "patient" or "provider"
}

/**
 * Returns true if the current user is a patient.
 */
export async function isPatient() {
  const role = await getUserRole();
  return role === 'patient';
}

/**
 * Returns true if the current user is a provider.
 */
export async function isProvider() {
  const role = await getUserRole();
  return role === 'provider';
}


// import { isPatient, isProvider } from './auth.js';

// document.addEventListener('DOMContentLoaded', async () => {
//   if (await isPatient()) {
//      e.g. show patient dashboard link
//   }

//   if (await isProvider()) {
//      e.g. show provider dashboard link
//   }
// });
