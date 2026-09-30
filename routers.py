from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, init_db
from models import PromptTemplate, PromptHistory
from schemas import PromptTemplateCreate, PromptTemplateResponse, PromptHistoryCreate, PromptHistoryResponse

router = APIRouter()

@router.on_event("startup")
async def startup_event():
    init_db()

@router.post("/prompts/", response_model=PromptTemplateResponse)
def create_prompt(prompt: PromptTemplateCreate, db: Session = Depends(SessionLocal)):
    db_prompt = PromptTemplate(**prompt.dict())
    db.add(db_prompt)
    db.commit()
    db.refresh(db_prompt)
    return db_prompt

@router.get("/prompts/{prompt_id}", response_model=PromptTemplateResponse)
def read_prompt(prompt_id: int, db: Session = Depends(SessionLocal)):
    return db.query(PromptTemplate).filter(PromptTemplate.id == prompt_id).first()

@router.post("/prompts/{prompt_id}/test", response_model=PromptHistoryResponse)
def test_prompt(prompt_id: int, data: PromptHistoryCreate, db: Session = Depends(SessionLocal)):
    # Simulate LLM response
    generated_text = f"Simulated response for prompt {prompt_id}"
    response_time = 100  # Simulated response time
    token_count = len(generated_text.split())  # Simulated token count
    clarity_score = 5  # Simulated clarity score
    db_history = PromptHistory(template_id=prompt_id, generated_text=generated_text, token_count=token_count, response_time=response_time, clarity_score=clarity_score)
    db.add(db_history)
    db.commit()
    db.refresh(db_history)
    return db_history
