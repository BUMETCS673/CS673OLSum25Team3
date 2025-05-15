# MyMedic

**A secure, patient-centered health record platform.**

## Project Overview

MyMedic is a personal medical system designed to help patients by giving them secure and convenient access to their complete medical history. It centralizes patient health records, promotes efficient care coordination, and improves overall patient convenience.

## Team Members & Roles

- John Gutierrez – Team Lead, Requirements Lead, QA Lead, Design/Implementation Lead, Security Lead, Configuration Lead  
- Indra Sigicharla – Team Lead, Configuration Lead  
- Adriel Domingo – Requirements Lead  
- Tyler Gonsalves – Design/Implementation Lead, Configuration Lead  
- Mengliang Tan – QA Lead  
- Uzay Isin Alici – Security Lead  
- Hongcheng Ding – Design/Implementation Lead  

## Key Features

### Essential
- User Registration & Login
- View and Edit Personal Information

### Desirable
- Family Accounts
- Notification System

### Optional
- Voice Assistant

## Target Users
- Patients managing personal or family health records  
- Healthcare Providers such as clinics and hospitals  
- Pharmacies for prescription and medication tracking  

## Technology Stack

- Frontend: JavaScript (React)
- Backend: Python (Django)
- Database: SQLite
- Authentication: OAuth 2.0
- Containerization: Docker

## Development Strategy

Using TrunkFlow:
- All production-ready code lives in the `main` branch.
- Features, bug fixes, and hotfixes are developed in individual branches.
- Changes are merged into `main` through pull requests with CI checks and code review.

## Security Highlights

- HIPAA Compliance: Protection of Personal Health Information (PHI)
- Access Control: Role-based (patients, doctors, admins)
- Authentication: Multi-factor authentication (MFA)
- Encryption: HTTPS via SSL/TLS, encryption at rest and in transit
- Vulnerability Scanning: Regular automated scans
- Incident Response: Breach notification and containment procedures
- Backup & Recovery: Daily secure backups and recovery plans

## Tools & Infrastructure

- GitHub (Version Control)
- Jira (Issue Tracking)
- Google Drive (Collaboration)
- Discord (Team Communication)
- Docker (Containerization)

## Risks & Challenges

Risks Identified:
- Personnel & Communication
- Incomplete Requirements
- Lack of Tech Stack Proficiency
- Security Concerns
- Integration & Deployment Delays (High Priority)

## Project Status

- Tech stack selected
- Risks identified and mitigation planned
- Drafted user stories and requirements
- Team onboarding new member

### Next Steps
- Refine requirements and user stories
- Draft SDD (Software Design Document)
- Draft STD (Software Test Document)
- Create UI mockups
- Begin container and environment setup
