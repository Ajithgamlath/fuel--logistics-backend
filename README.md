# Fuel Logistics Backend (FastAPI)

This backend powers a multi-party fuel distribution platform with dealer ordering, CPSTL logistics, RM Parks coordination, and invoicing.

## 💻 Run Locally

1. Clone repo
2. Create `.env` from `.env.example`
3. Install dependencies:

    pip install -r requirements.txt

4. Run:

    uvicorn fuel_backend_api:app --reload

## 🌐 Deploy
Supports Render / Railway / Docker / Vercel + Supabase