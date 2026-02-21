## SDG 4 Project Management System

ระบบจัดการโครงการ SDG 4 (REO Planning Helper) สำหรับสรุป/บริหารโครงการของหน่วยงาน
ปัจจุบันมีทั้ง **prototype** และ **backend (Flask API)**

- **Frontend (SPA Prototype)**: อยู่ในโฟลเดอร์ `prototype/` และ `frontend/`  
- **Backend (Flask API)**: อยู่ในโฟลเดอร์ `backend/` ใช้ Flask + SQLAlchemy

เอกสารนี้อธิบาย **tech stack**, วิธีติดตั้ง, โครงสร้างไฟล์ และการแบ่งผู้ดูแล route ของทีม

---

## Tech Stack / Framework

- **Backend**
  - ภาษา: Python 3.x
  - Framework: Flask
  - ORM: Flask‑SQLAlchemy (ใช้ SQLite เป็นฐานข้อมูลเริ่มต้น)

- **Frontend**
  - HTML / CSS / JavaScript (Single Page Application)
  - UI: Tailwind CSS + DaisyUI
  - กราฟ: Chart.js
  - Dialog / Toast: SweetAlert2

---

## วิธีติดตั้งและรัน Backend (Flask API)

1. ติดตั้ง Python 3.x ให้เรียบร้อย (เพิ่ม `python` / `py` ลงใน PATH)
2. เปิดเทอร์มินัลมาที่โฟลเดอร์โปรเจกต์หลัก:

   ```bash
   cd SDG/main/backend
   ```

3. (แนะนำ) สร้าง virtual environment

   ```bash
   python -m venv .venv
   .venv\Scripts\activate    # บน Windows PowerShell
   ```

4. ติดตั้ง package ที่ใช้ใน backend

   ```bash
   pip install -r requirements.txt
   ```

5. รัน backend (development)

   ```bash
   python run.py
   ```

   จากนั้น backend จะเปิดที่ `http://127.0.0.1:5000`  
   สามารถทดสอบได้ด้วยการเรียก `GET /api/health`

> **หมายเหตุ:** ตอนนี้ backend ยังเป็นโครงสร้างเบื้องต้น ยังไม่เชื่อมต่อกับฐานข้อมูลจริงและ frontend

---

## โครงสร้างไฟล์หลัก

### Backend (`backend/`)

```text
backend/
  app/
    __init__.py           # create_app + register_blueprints
    config.py             # การตั้งค่า Flask/DB
    extensions.py         # db = SQLAlchemy()
    models.py             # โครง model หลัก (Org, User, Project, AuditLog, ...)
    routes/
      auth_routes.py      # Login / Logout / Current user
      dashboard_routes.py # Dashboard summary
      project_routes.py   # Project CRUD
      report_routes.py    # รายงาน / Export โครงการ
      org_routes.py       # Organization management
      pin_routes.py       # ตั้งค่า PIN หน่วยงาน
      user_routes.py      # User & role management
      audit_routes.py     # Audit log
  run.py                  # จุดรันหลักของ backend
  requirements.txt        # รายการ Python packages
```

### Frontend / Prototype

- `frontend/`
  - `index.html` – หน้าเว็บหลัก (เวอร์ชันสำหรับต่อ backend)
  - `app.js`, `styles.css` – logic และสไตล์ฝั่ง client
- `prototype/`
  - `index.html`, `app.js`, `styles.css` – prototype ดั้งเดิมที่ทำงานบน browser + localStorage

---

## Route & Maintainer Table

เงื่อนไข: **สมาชิกทุกคนต้องดูแลอย่างน้อย 2 routes**  
ด้านล่างนี้เป็นการ mapping route → file → ผู้ดูแล

### 1) นายอัครพนธ์ โอมาโฮนี่ (Login System / Authenticate & Validate)

- File: `app/routes/auth_routes.py`

| HTTP | URL                    | Description                      | Maintainer                 |
|------|------------------------|----------------------------------|----------------------------|
| POST | `/api/auth/login`      | เข้าสู่ระบบ                     | นายอัครพนธ์ โอมาโฮนี่    |
| POST | `/api/auth/logout`     | ออกจากระบบ                      | นายอัครพนธ์ โอมาโฮนี่    |
| GET  | `/api/auth/me`         | ข้อมูลผู้ใช้ปัจจุบัน            | นายอัครพนธ์ โอมาโฮนี่    |

### 2) นายไชยวัฒน์ ทำดี (Dashboard System / Read & Export)

- File: `app/routes/dashboard_routes.py`
- File: `app/routes/report_routes.py` (export/report)

| HTTP | URL                          | Description                           | Maintainer           |
|------|------------------------------|---------------------------------------|----------------------|
| GET  | `/api/dashboard/summary`     | สรุปตัวเลขบน Dashboard               | นายไชยวัฒน์ ทำดี    |
| GET  | `/api/dashboard/by-org`      | สรุปตามหน่วยงาน                      | นายไชยวัฒน์ ทำดี    |
| GET  | `/api/dashboard/by-sdg`      | สรุปตาม SDG Target                    | นายไชยวัฒน์ ทำดี    |
| GET  | `/api/projects/export`       | ส่งออกข้อมูลโครงการ (CSV ฯลฯ)        | นายไชยวัฒน์ ทำดี    |

### 3) นายกฤษฎาพงษ์ ทิณพัฒน์ (Project Management / Create & Delete)

- File: `app/routes/project_routes.py`

| HTTP | URL                                           | Description                      | Maintainer                    |
|------|-----------------------------------------------|----------------------------------|-------------------------------|
| GET  | `/api/projects/`                              | ดึงรายการโครงการ (list + filter)| นายกฤษฎาพงษ์ ทิณพัฒน์       |
| GET  | `/api/projects/<project_id>`                  | รายละเอียดโครงการ               | นายกฤษฎาพงษ์ ทิณพัฒน์       |
| POST | `/api/projects/`                              | สร้างโครงการใหม่                | นายกฤษฎาพงษ์ ทิณพัฒน์       |
| PUT  | `/api/projects/<project_id>`                  | แก้ไขโครงการ                    | นายกฤษฎาพงษ์ ทิณพัฒน์       |
| DELETE | `/api/projects/<project_id>`                | ลบโครงการ                       | นายกฤษฎาพงษ์ ทิณพัฒน์       |
| POST | `/api/projects/<project_id>/images`           | อัปโหลดรูปโครงการ               | นายกฤษฎาพงษ์ ทิณพัฒน์       |
| DELETE | `/api/projects/<project_id>/images/<image_id>` | ลบรูปโครงการ                 | นายกฤษฎาพงษ์ ทิณพัฒน์       |

### 4) นายศิขรินทร์ ภูติโส (Organization Management / Admin & View)

- File: `app/routes/org_routes.py`

| HTTP | URL                                   | Description                                 | Maintainer              |
|------|---------------------------------------|---------------------------------------------|-------------------------|
| GET  | `/api/orgs/`                          | รายการหน่วยงาน (มุมมอง Admin)             | นายศิขรินทร์ ภูติโส    |
| GET  | `/api/orgs/public`                    | รายการหน่วยงานแบบ read-only (User)        | นายศิขรินทร์ ภูติโส    |
| POST | `/api/orgs/`                          | สร้างหน่วยงานใหม่                          | นายศิขรินทร์ ภูติโส    |
| PUT  | `/api/orgs/<org_id>`                  | แก้ไขข้อมูลหน่วยงาน                        | นายศิขรินทร์ ภูติโส    |
| DELETE | `/api/orgs/<org_id>`                | ลบหน่วยงาน (ต้องไม่มีข้อมูลที่เกี่ยวข้อง)  | นายศิขรินทร์ ภูติโส    |
| DELETE | `/api/orgs/<org_id>/cascade`        | ลบหน่วยงานพร้อมข้อมูลที่เกี่ยวข้องทั้งหมด  | นายศิขรินทร์ ภูติโส    |

### 5) นายพิชชากร คำพรม (User & Role Management / Create & Update)

- File: `app/routes/user_routes.py`
- File: `app/routes/pin_routes.py` (ตั้งค่า PIN หน่วยงาน)

| HTTP | URL                                    | Description                                 | Maintainer             |
|------|----------------------------------------|---------------------------------------------|------------------------|
| GET  | `/api/users/`                          | รายการผู้ใช้ทั้งหมด                        | นายพิชชากร คำพรม     |
| POST | `/api/users/`                          | สร้างผู้ใช้ใหม่                            | นายพิชชากร คำพรม     |
| PUT  | `/api/users/<user_id>`                 | แก้ไขข้อมูลผู้ใช้/บทบาท                    | นายพิชชากร คำพรม     |
| PUT  | `/api/users/<user_id>/password`        | เปลี่ยนรหัสผ่านผู้ใช้                     | นายพิชชากร คำพรม     |
| PUT  | `/api/orgs/<org_id>/pin`               | ตั้งค่าหรือรีเซ็ต PIN ของหน่วยงาน         | นายพิชชากร คำพรม     |
| POST | `/api/orgs/pins/reset-all`             | ตั้ง PIN ของทุกหน่วยงานเป็นค่าเริ่มต้น   | นายพิชชากร คำพรม     |

### 6) นายนัธทวัฒน์ เขาแก้ว (Audit Log / Read, Filter)

- File: `app/routes/audit_routes.py`

| HTTP | URL                          | Description                           | Maintainer              |
|------|------------------------------|---------------------------------------|-------------------------|
| GET  | `/api/audit-logs/`          | ดึงรายการ audit log + filter         | นายนัธทวัฒน์ เขาแก้ว  |
| GET  | `/api/audit-logs/filters`   | คืนตัวเลือก filter (actions / users) | นายนัธทวัฒน์ เขาแก้ว  |

