# Security Policy

## Reporting a Vulnerability

We take security seriously and want to ensure that our application remains safe for all users. 
If you discover a security vulnerability in this project, **please do not open a public GitHub issue**.

Instead, report it privately to the development team: mymedic-help@gmail.com

Please include as much of the following information as possible:

- Description of the issue (e.g., XSS, SQL injection, broken authentication)
- Files or features involved
- Steps to reproduce the issue
- Potential impact or how it could be exploited
- Suggestions for a possible fix (if any)

---

## Current Security Features

✅ **CSRF Protection**  
All user forms, including MFA verification, are protected with CSRF tokens to prevent cross-site request forgery attacks.

✅ **Authentication and MFA**  
The app supports Multi-Factor Authentication (MFA) during login for enhanced user security.

✅ **Input Validation**  
User input is validated on both client and server sides to reduce injection risks.

✅ **Session Management**  
Django's built-in session and cookie protection is enabled.

---

## Best Practices

We encourage developers contributing to this project to:

- Avoid hard-coding secrets in the source code
- Sanitize user inputs
- Keep dependencies updated
- Follow Django’s security recommendations

---

## Coordinated Disclosure

We support responsible disclosure. If you report an issue privately, we’ll work with you to investigate and patch the vulnerability as quickly as possible.

