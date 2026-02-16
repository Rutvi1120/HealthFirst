# 🏥 HealthFirst – Smart Emergency Healthcare Management System

HealthFirst is a web-based Smart Emergency Healthcare Management System developed using **Python and Django**.  
The system provides a centralized digital platform to efficiently manage **emergency SOS requests, ambulance dispatch, hospital resource availability, blood bank management, medical report verification, public health alerts, and emergency guidance**.

It connects **citizens, hospitals, and government authorities** to ensure faster emergency response, secure medical data handling, and transparent healthcare coordination.

---

## 🚀 Key Features

### 👤 User Management
- Role-based registration and authentication
- Supported roles:
  - Citizen
  - Hospital Admin
  - Health Officer
  - Super Admin

### 🚨 Emergency SOS Management
- One-click SOS request by citizens
- Real-time SOS processing
- Automatic identification of nearby hospitals
- SOS locking mechanism to prevent duplicate acceptance

### 🚑 Ambulance Management
- Ambulance registration by hospitals
- Real-time ambulance status tracking
- Ambulance assignment to SOS requests

### 🏥 Hospital Resource Management
- Real-time hospital bed availability (ICU, Oxygen, General)
- Resource initialization and live updates
- Citizen-side hospital resource viewing

### 🩸 Blood Bank Management
- Blood stock initialization and updates
- Blood availability search across hospitals

### 📄 Medical Report Management
- Secure medical report upload
- Hash-based report integrity verification
- Controlled access to verified medical reports

### 📢 Public Health Alerts & Guidance
- Publish and view public health alerts
- Emergency and first-aid guidance by emergency type

### 📝 Feedback System
- Citizens can submit feedback after emergency resolution
- Hospitals can view feedback reports

---

## 🛠️ Technology Stack

- **Backend:** Python 3, Django
- **Database:** MySQL / PostgreSQL
- **Frontend:** HTML, CSS, Bootstrap
- **Authentication:** Django Authentication System
- **Security:** Role-Based Access Control (RBAC)
- **Version Control:** Git & GitHub

---


---

## 🔄 System Workflow

### 1️⃣ User Registration & Login
- Users register based on role (Citizen / Hospital / Officer)
- Secure login and role-based dashboard access

---

### 2️⃣ Emergency SOS Workflow
1. Citizen triggers an SOS request
2. System generates SOS ID instantly
3. Nearby hospitals are identified in the background
4. Hospitals receive SOS notification
5. First hospital to accept the SOS locks the request
6. Citizen receives SOS acceptance confirmation

---

### 3️⃣ Ambulance Dispatch Workflow
1. Hospital assigns an available ambulance to the SOS
2. Ambulance status is updated in real time:
   - Dispatched
   - En Route
   - Arrived
3. Citizen tracks ambulance status from dashboard

---

### 4️⃣ Hospital Resource Management Workflow
1. Hospital initializes bed availability (ICU, Oxygen, General)
2. Beds are updated in real time
3. Citizens can view hospital-wise bed availability

---

### 5️⃣ Medical Report Workflow
1. Authorized user uploads medical report
2. System generates a hash value for integrity
3. Hash is verified in the background
4. Only verified reports are accessible to users

---

### 6️⃣ Blood Bank Workflow
1. Hospitals initialize blood stock
2. Blood stock is updated regularly
3. Users search blood availability by blood group

---

### 7️⃣ Public Health Alert & Guidance Workflow
1. Health officers publish alerts and emergency guidance
2. Alerts are instantly visible to all users
3. Users access first-aid instructions by emergency type

---

### 8️⃣ Feedback Workflow
1. Citizen submits feedback after emergency resolution
2. Hospitals view feedback associated with their services

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/Rutvi1120/HealthFirst
cd HealthFirst
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver



