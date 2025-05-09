# Travel Advisor AI

A full-stack application for travel queries using FastAPI, Next.js, TailwindCSS, and Google Gemini LLM.

## Backend Setup
1. Install Python 3.9+ and pip.
2. Navigate to `gen_backend/`.
3. Create Virtual environment with `python -m venv venv`
4. Activate virtual environment with `source venv/bin/activate` on linux/macos or `.\venv\Scripts\activate` on windows
5. Run `pip install -r requirements.txt`.
6. Copy `.env.example` to `.env` and set `GEMINI_API_KEY`.
7. Run `uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload`.
8. Access Swagger at `http://localhost:8000/docs`.

## Testing
1. Install pytest: `pip install pytest pytest-asyncio pytest-mock`.
2. Run `pytest tests/ -v`.
3. Tests mock the Gemini API for reliability.
4. Logs are enabled for debugging (check terminal for DEBUG/ERROR messages).

## LLM Prompts
- Prompt: "For a traveler asking '{question}', provide a structured response with:
  - Required visa documents
  - Passport requirements
  - Additional necessary documents
  - Any relevant travel advisories
  Format the response in clear, concise bullet points."

## Environment Variables
- `GEMINI_API_KEY`: Your Google Gemini API key.
