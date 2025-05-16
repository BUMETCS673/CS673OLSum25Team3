import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import axios from 'axios';

describe('API 测试', () => {
    it('应该从后端获取数据', async () => {
      const response = await axios.get('http://localhost:3232/v1/health')
      expect(response.status).toBe(200);
    });
});