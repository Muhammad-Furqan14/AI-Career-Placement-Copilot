# ==========================================
# AI CAREER PLACEMENT COPILOT
# ROADMAP GENERATOR
# ==========================================

ROADMAP_RESOURCES = {
    "python": "Practice Python fundamentals and problem solving.",
    "machine learning": "Learn supervised and unsupervised machine learning.",
    "deep learning": "Learn neural networks and deep learning fundamentals.",
    "nlp": "Learn text processing, embeddings, and transformers.",
    "llm": "Learn how Large Language Models work.",
    "generative ai": "Learn LLM APIs and Generative AI applications.",
    "rag": "Build a Retrieval-Augmented Generation application.",
    "langchain": "Learn LangChain for LLM application development.",
    "langgraph": "Learn AI agent workflows using LangGraph.",
    "fastapi": "Build REST APIs using FastAPI.",
    "docker": "Learn containerization and Docker.",
    "postgresql": "Learn relational databases and PostgreSQL.",
    "aws": "Learn basic cloud deployment using AWS."
}


def generate_roadmap(missing_skills):

    roadmap = []

    for index, skill in enumerate(missing_skills, start=1):

        recommendation = ROADMAP_RESOURCES.get(
            skill,
            f"Learn the fundamentals of {skill}."
        )

        roadmap.append({
            "step": index,
            "skill": skill,
            "recommendation": recommendation
        })

    return roadmap