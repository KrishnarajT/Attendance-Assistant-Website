from pydantic import BaseModel
from typing import Optional, List

# {
#     "_id": "Subject ID Generated by MongoDB",
#     "name": "Subject Name",
#     "subject_code": "Subject Code"
# }
class Subject(BaseModel):
    name: str
    subject_code: str