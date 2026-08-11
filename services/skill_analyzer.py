import re


# ============================================================
# SKILL DATABASE
# ============================================================

SKILLS = {
    "python": ["python"],
    "java": ["java"],
    "c++": ["c++", "cpp", "c plus plus"],
    "c": ["c language", "programming in c"],

    "javascript": ["javascript", "js"],
    "typescript": ["typescript", "ts"],
    "html": ["html", "html5"],
    "css": ["css", "css3"],

    "sql": ["sql"],
    "mysql": ["mysql"],
    "postgresql": ["postgresql", "postgres"],
    "mongodb": ["mongodb", "mongo db"],

    "machine learning": [
        "machine learning",
        "ml"
    ],

    "deep learning": [
        "deep learning",
        "dl"
    ],

    "artificial intelligence": [
        "artificial intelligence",
        "ai"
    ],

    "data analysis": [
        "data analysis",
        "data analytics"
    ],

    "data science": [
        "data science",
        "data scientist"
    ],

    "nlp": [
        "nlp",
        "natural language processing"
    ],

    "computer vision": [
        "computer vision"
    ],

    "tensorflow": ["tensorflow"],
    "pytorch": ["pytorch", "py torch"],
    "scikit-learn": [
        "scikit-learn",
        "scikit learn",
        "sklearn"
    ],

    "pandas": ["pandas"],
    "numpy": ["numpy"],

    "llm": [
        "llm",
        "llms",
        "large language model",
        "large language models"
    ],

    "generative ai": [
        "generative ai",
        "gen ai",
        "genai"
    ],

    "prompt engineering": [
        "prompt engineering",
        "prompt engineer"
    ],

    "langchain": ["langchain"],

    "rag": [
        "rag",
        "retrieval augmented generation",
        "retrieval-augmented generation"
    ],

    "vector database": [
        "vector database",
        "vector databases"
    ],

    "faiss": ["faiss"],
    "pinecone": ["pinecone"],
    "chroma": ["chroma", "chromadb"],

    "fastapi": ["fastapi"],
    "flask": ["flask"],

    "api": [
        "api",
        "apis",
        "rest api",
        "restful api"
    ],

    "git": ["git"],
    "github": ["github"],
    "docker": ["docker"],
    "linux": ["linux"],

    "aws": [
        "aws",
        "amazon web services"
    ],

    "azure": [
        "azure",
        "microsoft azure"
    ],

    "gcp": [
        "gcp",
        "google cloud",
        "google cloud platform"
    ],

    "streamlit": ["streamlit"],
    "gradio": ["gradio"],

    "ai agents": [
        "ai agents",
        "ai agent"
    ],

    "agentic ai": [
        "agentic ai"
    ],

    "excel": [
        "excel",
        "microsoft excel"
    ],

    "power bi": [
        "power bi",
        "powerbi"
    ]
}


# ============================================================
# ROLE SKILLS
# ============================================================

ROLE_SKILLS = {

    "ai engineer": [
        "python",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "nlp",
        "llm",
        "generative ai",
        "langchain",
        "rag",
        "vector database",
        "fastapi",
        "api",
        "git",
        "github",
        "docker"
    ],

    "machine learning engineer": [
        "python",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "scikit-learn",
        "pandas",
        "numpy",
        "docker",
        "git"
    ],

    "data scientist": [
        "python",
        "sql",
        "machine learning",
        "data analysis",
        "data science",
        "pandas",
        "numpy",
        "scikit-learn"
    ],

    "data analyst": [
        "python",
        "sql",
        "data analysis",
        "pandas",
        "numpy",
        "excel",
        "power bi"
    ]
}


# ============================================================
# NORMALIZE TEXT
# ============================================================

def normalize_text(text):

    if not text:
        return ""

    text = text.lower()

    # Replace multiple spaces/newlines with one space
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ============================================================
# EXTRACT SKILLS
# ============================================================

def extract_skills(text):
    """
    Extract known skills from CV or job description.
    """

    text = normalize_text(text)

    if not text:
        return []

    found_skills = set()

    for skill, aliases in SKILLS.items():

        for alias in aliases:

            # Escape special characters such as + in C++
            pattern = r"(?<!\w)" + re.escape(alias) + r"(?!\w)"

            if re.search(pattern, text):
                found_skills.add(skill)
                break

    return sorted(found_skills)


# ============================================================
# DETECT ROLE
# ============================================================

def get_role_skills(text):
    """
    Detect career role and return expected skills.
    """

    text = normalize_text(text)

    if not text:
        return []

    detected_skills = set()

    # Exact role detection
    for role, skills in ROLE_SKILLS.items():

        if role in text:
            detected_skills.update(skills)

    # --------------------------------------------------------
    # AI Engineer aliases
    # This fixes inputs such as:
    # "for ai"
    # "AI career"
    # "AI developer"
    # "artificial intelligence engineer"
    # --------------------------------------------------------

    ai_keywords = [
        "ai engineer",
        "artificial intelligence engineer",
        "ai developer",
        "ai career",
        "for ai",
        "generative ai engineer",
        "llm engineer"
    ]

    if any(keyword in text for keyword in ai_keywords):
        detected_skills.update(ROLE_SKILLS["ai engineer"])

    # Machine Learning aliases
    ml_keywords = [
        "machine learning engineer",
        "ml engineer",
        "machine learning"
    ]

    if any(keyword in text for keyword in ml_keywords):
        detected_skills.update(
            ROLE_SKILLS["machine learning engineer"]
        )

    # Data Scientist aliases
    data_scientist_keywords = [
        "data scientist",
        "data science role",
        "data science job"
    ]

    if any(keyword in text for keyword in data_scientist_keywords):
        detected_skills.update(
            ROLE_SKILLS["data scientist"]
        )

    # Data Analyst aliases
    data_analyst_keywords = [
        "data analyst",
        "data analytics",
        "data analysis job"
    ]

    if any(keyword in text for keyword in data_analyst_keywords):
        detected_skills.update(
            ROLE_SKILLS["data analyst"]
        )

    return sorted(detected_skills)


# ============================================================
# ANALYZE SKILL GAP
# ============================================================

def analyze_skill_gap(cv_text, job_description):
    """
    Compare CV skills with job description skills.
    """

    # Extract skills from CV
    cv_skills = set(extract_skills(cv_text))

    # Extract skills directly mentioned in job description
    direct_job_skills = set(
        extract_skills(job_description)
    )

    # Detect role and get expected skills
    role_skills = set(
        get_role_skills(job_description)
    )

    # Combine both
    job_skills = direct_job_skills.union(role_skills)

    # --------------------------------------------------------
    # FALLBACK FOR SHORT AI INPUTS
    # --------------------------------------------------------

    job_text = normalize_text(job_description)

    if not job_skills and "ai" in job_text:
        job_skills = set(ROLE_SKILLS["ai engineer"])

    # Matched skills
    matched_skills = cv_skills.intersection(job_skills)

    # Missing skills
    missing_skills = job_skills.difference(cv_skills)

    # Extra skills
    extra_skills = cv_skills.difference(job_skills)

    # Match score
    if job_skills:
        match_score = round(
            (len(matched_skills) / len(job_skills)) * 100,
            2
        )
    else:
        match_score = 0

    # ========================================================
    # DEBUG OUTPUT
    # ========================================================

    print("\n========== AI CAREER ANALYSIS ==========")

    print("CV Text Preview:")
    print(cv_text[:300])

    print("\nJob Description:")
    print(job_description)

    print("\nCV Skills:")
    print(sorted(cv_skills))

    print("\nDirect Job Skills:")
    print(sorted(direct_job_skills))

    print("\nRole Skills:")
    print(sorted(role_skills))

    print("\nFinal Job Skills:")
    print(sorted(job_skills))

    print("\nMatched Skills:")
    print(sorted(matched_skills))

    print("\nMissing Skills:")
    print(sorted(missing_skills))

    print("\nExtra Skills:")
    print(sorted(extra_skills))

    print("\nMatch Score:")
    print(match_score)

    print("========================================\n")

    # ========================================================
    # RETURN RESULT
    # ========================================================

    return {
        "match_score": match_score,
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills),
        "extra_skills": sorted(extra_skills)
    }