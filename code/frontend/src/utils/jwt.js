export const jwtUtils = {
  
  setToken: (key, token) => {
    localStorage.setItem(key, token);
  },

  getToken: (key) => {
    return localStorage.getItem(key);
  },

  removeToken: (key) => {
    localStorage.removeItem(key);
  },

  parseJwt: (token) => {
    try {
      const tokenPayload = token.split('.')[1];
      const base64Payload = tokenPayload.replace(/-/g, '+').replace(/_/g, '/');
      const jsonPayload = decodeURIComponent(atob(base64Payload).split('').map(c => {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
      }).join(''));
      return JSON.parse(jsonPayload);
    } catch (e) {
      return null;
    }
  },

  isTokenExpired: (token) => {
    if (!token) return true;
    const decoded = jwtUtils.parseJwt(token);
    if (!decoded) return true;
    return decoded.exp * 1000 < Date.now();
  }
};