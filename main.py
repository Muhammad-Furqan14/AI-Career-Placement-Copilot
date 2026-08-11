from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

import os
import shutil

from services.cv_parser import extract_text_from_pdf
from services.skill_analyzer import analyze_skill_gap
from services.roadmap import generate_roadmap


app = FastAPI(
    title="AI Career Placement Copilot",
    description="Analyze CV skills and compare them with a job description",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


os.makedirs("uploads", exist_ok=True)


app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


@app.get("/")
async def home():
    return FileResponse("static/index.html")


@app.post("/analyze")
async def analyze(
    cv: UploadFile = File(...),
    job_description: str = Form(...)
):

    if not cv.filename.lower().endswith(".pdf"):
        return {
            "success": False,
            "error": "Please upload a PDF file only."
        }

    try:
        file_path = os.path.join("uploads", cv.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(cv.file, buffer)

        # Extract CV text
        cv_text = extract_text_from_pdf(file_path)

        # ==============================
        # DEBUG INFORMATION
        # ==============================
        print("\n========== DEBUG START ==========")

        print("\nUPLOADED FILE:")
        print(cv.filename)

        print("\nJOB DESCRIPTION:")
        print(job_description)

        print("\nCV TEXT LENGTH:")
        print(len(cv_text) if cv_text else 0)

        print("\nCV TEXT PREVIEW:")
        print(cv_text[:1000] if cv_text else "NO TEXT EXTRACTED")

        print("\n========== DEBUG END ==========\n")

        if not cv_text or len(cv_text.strip()) == 0:
            return {
                "success": False,
                "error": "Could not extract text from this CV."
            }

        # Analyze skills
        analysis = analyze_skill_gap(
            cv_text,
            job_description
        )

        print("\n========== FINAL ANALYSIS ==========")
        print(analysis)
        print("====================================\n")

        missing_skills = analysis.get("missing_skills", [])

        roadmap = generate_roadmap(missing_skills)

        return {
            "success": True,
            "filename": cv.filename,
            "match_score": analysis.get("match_score", 0),
            "matched_skills": analysis.get("matched_skills", []),
            "missing_skills": missing_skills,
            "extra_skills": analysis.get("extra_skills", []),
            "roadmap": roadmap
        }

    except Exception as e:
        print("\nERROR:")
        print(str(e))

        return {
            "success": False,
            "error": str(e)
        }


@app.get("/api/status")
async def status():
    return {
        "success": True,
        "message": "AI Career Placement Copilot API is running"
    }