from database import SessionLocal
from models import PromptTemplate

def seed_data():
    db = SessionLocal()
    example_prompts = [
        PromptTemplate(title="Friendly Blog Post", template="Write a {tone} blog post about {topic}"),
        PromptTemplate(title="Formal Email", template="Write a {tone} email to {recipient} about {topic}"),
    ]
    db.add_all(example_prompts)
    db.commit()

if __name__ == '__main__':
    seed_data()
