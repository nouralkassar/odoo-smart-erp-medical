# Smart Medical ERP System (Odoo + Docker)

## Overview

This project is a custom ERP system built using **Odoo** with Docker deployment.  
It simulates a **smart emergency medical hospital system** capable of handling real-time triage, logistics, security, and disaster-response operations.

The system is modular and designed to demonstrate advanced ERP engineering concepts including:

- Python & XML custom Odoo modules
- Real-time decision simulation (IoT-inspired)
- Role-Based Access Control (RBAC)
- Separation of Duties (SoD)
- Disaster-resilient operations

---

## Key Features

### 1. Emergency Triage System (Pulse Simulation)

- Custom Odoo module built with Python & XML
- Simulated IoT-like real-time vital signs processing
- Automatic patient classification:
  - Critical
  - Medium
  - Stable
- Fast decision support for emergency cases

---

### 2. Security & Access Control (RBAC + SoD)

- Multi-level role-based access system
- Roles include:
  - Doctor
  - Nurse
  - Receptionist
  - Inventory Manager
  - Admin
- Separation of Duties (SoD) applied across workflows
- Secure data access and restricted operations

---

### 3. Medical Inventory & Logistics System

- Centralized inventory management
- Batch tracking and expiration date monitoring
- Medical supply lifecycle control
- Fleet management for mobile medical units
- Triple verification mechanism for stock accuracy

---

### 4. Disaster Response Mode

- CRM and POS systems adapted for emergency scenarios
- Offline-ready workflow design
- Remote triage and medicine distribution support
- Designed for deployment in disaster or disconnected environments

---

## Deployment (Docker)

### Run the system:

```bash
docker-compose up -d
```
