from sqlalchemy import Column, Integer, String, Text
from database import Base

class PromptTemplate(Base):
    __tablename__ = 'prompt_templates'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    template = Column(Text)

class PromptHistory(Base):
    __tablename__ = 'prompt_history'
    id = Column(Integer, primary_key=True, index=True)
    template_id = Column(Integer)
    generated_text = Column(Text)
    token_count = Column(Integer)
    response_time = Column(Integer)
    clarity_score = Column(Integer)
