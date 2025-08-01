from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.models.translation import TranslationRequest, TranslationResponse
from app.services.nlp_processor import process_translation
from app.utils.logger import configure_logger

app = FastAPI()
logger = configure_logger()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/translate", response_model=TranslationResponse)
async def translate_comment(request: TranslationRequest):
    try:
        result = process_translation(
            request.comment, 
            request.dialect,
            request.context
        )
        return {"translated_comment": result}
    except ValueError as e:
        logger.error(f"Translation error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.critical(f"Server error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/health")
async def health_check():
    return {"status": "ok"}
