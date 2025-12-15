# Netflix Clone

A full-stack Netflix Clone built with **Next.js 14**, **FastAPI**, **Tailwind CSS**, and **OMDb API**.

This repository is for educational purposes only; playback and streaming are performed via third-party embed services (e.g., VidSrc, VidFast) and no content is hosted here.

## Features

- **Movies & TV Shows**: Browse trending and popular content fetched from OMDb.
- **Deep Search**: Search for any movie or TV show.
- **Authentication**: JWT-based Signup and Login.
- **My List**: Save your favorite content to your watchlist.
- **Streaming**: Iframe-based playback via VidSrc (supports Movies and TV Seasons/Episodes).
- **Responsive UI**: Fully responsive design with Netflix-inspired dark theme and animations.

## Tech Stack

- **Frontend**: Next.js, TypeScript, Tailwind CSS, Framer Motion, Lucide Icons.
- **Backend**: Python FastAPI, SQLModel (SQLite).
- **External API**: OMDb (Metadata), VidSrc (Playback).

## Prerequisities

- Node.js 18+
- Python 3.10+

## Setup Instructions

### 1. Backend Setup

```bash
cd backend
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file in `backend/` with your OMDb key:
```
OMDB_API_KEY=
```

Note: Do not commit your `backend/.env` file. Add your OMDb key locally before running the backend.

To publish this project to GitHub (example):

```bash
git init
git add .
git commit -m "Initial commit"
# Create a remote repository on GitHub (use the website or `gh repo create`) then:
git remote add origin <your-repo-url>
git branch -M main
git push -u origin main
```

Run the server:
```bash
python -m uvicorn app.main:app --reload

```
The backend runs on `http://127.0.0.1:8000`.

### 2. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```
The frontend runs on `http://localhost:3000`.

## Deployment

### Backend
- Deploy FastAPI to standard Python hosting (e.g., Railway, Render, DigitalOcean).
- Ensure `OMDB_API_KEY` is set in production environment variables.

### Frontend
- Deploy Next.js to **Vercel** or **Netlify**.
- Set build command to `npm run build`.

## Disclaimer
This project is for educational purposes only. It does not host any content. All media is provided via third-party embed scripts.
Do Not Deploy it anywhere
# NetflixCl
