from fastapi import APIRouter, HTTPException
from app.models.query import QueryRequest, QueryResponse
from app.utils.llm import query_llm
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/query", response_model=QueryResponse, summary="Process a travel-related question")
async def handle_query(query: QueryRequest):
    """
    Handles a user query by calling the Gemini LLM and returning a structured response.
    - **question**: The user's travel question (e.g., "What documents for Uganda to Germany?").
    Returns a JSON response with the LLM's answer.
    """
    logger.debug(f"Received question: {query.question}")
    if len(query.question.strip()) < 5:
        raise HTTPException(status_code=400, detail="Question must be at least 5 characters long")
    try:
        response_text = query_llm(query.question)
        logger.debug(f"LLM response: {response_text}")
        return QueryResponse(response=response_text)
    except Exception as e:
        logger.error(f"Error in handle_query: {str(e)}")
        raise HTTPException(status_code=500, detail=f"LLM API error: {str(e)}")
