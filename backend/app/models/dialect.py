from pydantic import BaseModel

class Dialect(BaseModel):
    name: str
    description: str
    example_phrases: dict

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "example_phrases": self.example_phrases
        }
