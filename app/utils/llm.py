import google.generativeai as genai
import os
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv()

def query_llm(question: str) -> str:
    """
    Queries the Gemini LLM with a travel-related question and returns a structured response.
    Args:
        question: The user's question (e.g., "What documents for Uganda to Germany?").
    Returns:
        Formatted response with visa, passport, documents, and advisories.
    Raises:
        ValueError: If API key is missing.
        Exception: If the API call fails.
    """
    logger.debug(f"Querying Gemini LLM with question: {question}")
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not set in environment variables")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash-8b")

    prompt = (
        f"For a traveler asking '{question}', provide a structured response with:\n"
        "- Required visa documents\n"
        "- Passport requirements\n"
        "- Additional necessary documents\n"
        "- Any relevant travel advisories\n"
        "Format the response in clear, concise bullet points."
    )

    try:
        response = model.generate_content(prompt)
        result = response.text.strip()
        logger.debug(f"Gemini LLM returned: {result}")
        return result
    except Exception as e:
        logger.error(f"Gemini API error: {str(e)}")
        raise Exception(f"Gemini API error: {str(e)}")
