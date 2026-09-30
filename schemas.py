from pydantic import BaseModel

class PromptTemplateCreate(BaseModel):
    title: str
    template: str

class PromptTemplateResponse(BaseModel):
    id: int
    title: str
    template: str

    class Config:
        orm_mode = True

class PromptHistoryCreate(BaseModel):
    template_id: int
    generated_text: str
    token_count: int
    response_time: int
    clarity_score: int

class PromptHistoryResponse(BaseModel):
    id: int
    template_id: int
    generated_text: str
    token_count: int
    response_time: int
    clarity_score: int

    class Config:
        orm_mode = True
