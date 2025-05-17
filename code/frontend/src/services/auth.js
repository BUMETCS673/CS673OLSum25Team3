import api from './api';
import { jwtUtils } from '../utils/jwt';

export const authService = {
  login: async (username, password) => {
    try {
      const response = await api.post('/auth/login', { username, password });
      const { token, refreshToken, user } = response.data;
      
      jwtUtils.setToken('auth_token', token);
      jwtUtils.setToken('refresh_token', refreshToken);
      
      return { success: true, user };
    } catch (error) {
      return { 
        success: false, 
        error: error.response?.data?.message || '登录失败' 
      };
    }
  },

  logout: async () => {
    try {
      await api.post('/auth/logout');
    } finally {
      jwtUtils.removeToken('auth_token');
      jwtUtils.removeToken('refresh_token');
    }
  },

  getCurrentUser: async () => {
    try {
      const response = await api.get('/auth/verify');
      return response.data;
    } catch (error) {
      return null;
    }
  },

  isAuthenticated: () => {
    const token = jwtUtils.getToken();
    return token && !jwtUtils.isTokenExpired(token);
  }
};