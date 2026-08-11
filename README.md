**# AI-Career-Placement-Copilot
AI-powered CV analysis and career placement assistant with skill gap analysis, personalized roadmap, and OCR support.
# 🤖 AI Career Placement Copilot

An AI-powered career assistance web application that analyzes a candidate's CV against a target job description and provides a career match score, matched skills, missing skills, and a personalized learning roadmap.

The system also supports OCR for scanned and image-based CVs, making it capable of analyzing resumes even when normal PDF text extraction is not possible.

---

## 🚀 Features

### 📄 CV Analysis
Upload a PDF CV and automatically extract its content for analysis.

### 📊 Career Match Score
Calculates a percentage-based match between the candidate's skills and the requirements of the target job.

### ✅ Matched Skills Detection
Identifies skills that are present in both the candidate's CV and the target job description.

### ⚠️ Skill Gap Analysis
Identifies important skills that are required for the target role but are missing from the candidate's CV.

### 🗺️ Personalized Learning Roadmap
Generates a learning roadmap based on the missing skills and recommends what the candidate should learn next.

### 🔍 OCR Support
Supports scanned and image-based CVs using Optical Character Recognition (OCR).

This allows the system to extract text from CVs where normal PDF text extraction fails.

### 👁️ Live CV Preview
Displays the uploaded PDF CV directly inside the web interface.

### 🌙 Dark / Light Mode
Modern user interface with both dark and light themes.

### 📱 Responsive Interface
Designed to provide a clean and user-friendly experience across different screen sizes.

---

🧠 How It Works

```text
             ┌─────────────────┐
             │    Upload CV    │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │  PDF Processing │
             └────────┬────────┘
                      │
              ┌───────┴────────┐
              │                │
              ▼                ▼
       Text-based CV      Scanned CV
              │                │
              │                ▼
              │           OCR Processing
              │                │
              └───────┬────────┘
                      ▼
              ┌───────────────┐
              │ Text Extraction│
              └───────┬───────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Skill Extraction│
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Job Description │
             │ Skill Analysis  │
             └────────┬────────┘
                      │
             ┌────────┴────────┐
             ▼                 ▼
      Matched Skills      Missing Skills
             │                 │
             └────────┬────────┘
                      ▼
             ┌─────────────────┐
             │  Match Score    │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Learning Roadmap│
             └─────────────────┘

🛠️ Technologies Used
Backend
Python
FastAPI
Frontend
HTML5
CSS3
JavaScript
PDF Processing
PyMuPDF
PDF text extraction
OCR
Tesseract OCR
PyTesseract
Pillow
Development Tools
VS Code
Git
GitHub
📁 Project Structure
AI-Career-Placement-Copilot/
│
├── README.md
├── main.py
├── requirements.txt
│
├── services/
│   ├── __init__.py
│   ├── cv_parser.py
│   ├── roadmap.py
│   └── skill_analyzer.py
│
├── static/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
└── screenshots/
    ├── 01-homepage.png
    ├── 02-cv-preview.png
    ├── 03-analysis-result.png
    ├── 04-ocr-result.png
    └── 05-roadmap.png
📸 Project Screenshots
🏠 CV Upload & Dashboard

📄 CV Preview

📊 AI Career Analysis

🔍 OCR Support

🗺️ Personalized Learning Roadmap

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/Muhammad-Furqan14/AI-Career-Placement-Copilot.git
2. Open the Project
cd AI-Career-Placement-Copilot
3. Create a Virtual Environment
python -m venv venv
4. Activate Virtual Environment

For Windows:

venv\Scripts\activate
5. Install Dependencies
pip install -r requirements.txt
6. Install OCR Requirements

The OCR feature requires:

Tesseract OCR
PyTesseract
Pillow

Make sure Tesseract OCR is installed on your system and configured correctly.

7. Run the Application
uvicorn main:app --reload
8. Open in Browser
http://127.0.0.1:8000
🎯 Example Use Case

A candidate wants to apply for an AI Engineer position.

The candidate:

Uploads their CV.
Enters the target AI Engineer job description.
The system extracts CV information.
Skills are detected from the CV.
Job requirements are analyzed.
The system calculates the career match score.
Matching skills are displayed.
Missing skills are identified.
A personalized learning roadmap is generated.
🔍 OCR Use Case

Traditional PDF text extraction may fail when a CV is:

Scanned from a printer
Converted from an image
Created using a camera/photo
Stored as an image-only PDF

The OCR feature solves this problem by converting text inside images into machine-readable text.

Image / Scanned CV
        ↓
   OCR Processing
        ↓
Extracted Text
        ↓
Skill Detection
        ↓
Career Analysis
📊 Analysis Output

The application provides:

Result	Description
Career Match Score	Percentage match with target role
Matched Skills	Skills found in both CV and job
Missing Skills	Skills required but not found in CV
Extra Skills	Additional skills found in CV
Learning Roadmap	Recommended learning path
🎓 Career Development

This project demonstrates practical experience in:

Python programming
Backend development
FastAPI
PDF processing
OCR
Text extraction
Skill matching
Natural Language Processing concepts
Frontend development
API integration
AI-powered application development

Building this project provides practical experience for an AI Engineer career path, especially in areas such as:

NLP
LLM applications
Generative AI
RAG systems
AI Agents
Document AI
Intelligent automation
🔮 Future Improvements

Planned improvements include:

🤖 LLM-powered CV analysis
🧠 Advanced NLP-based skill extraction
📚 Course recommendations
🔗 Job platform integration
🎯 Multiple career-role comparison
📈 Advanced career analytics
🤝 AI career assistant chatbot
🧩 RAG-based career recommendations
🗣️ Voice-based career assistant
☁️ Cloud deployment
🔐 Security & Privacy

The application is designed to process uploaded CV files for analysis.

For production deployment, additional security measures should be implemented, including:

File validation
File size limits
Secure file storage
Temporary file deletion
Input sanitization
Authentication and authorization
Protection of sensitive CV information

Do not upload API keys, passwords, .env files, or other secrets to the public repository.

###👨‍💻 Author###

**Muhammad Furqan**

Computer Science Student
AI & Cybersecurity Enthusiast

⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.*
