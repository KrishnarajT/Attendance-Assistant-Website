from pydantic import BaseModel
from typing import Optional, List

# {
#   "_id": "Teacher ID Generated by MongoDB",
#   "name": "Teacher Name",
#   "email": "teacher.name@mitwpu.edu.in",
#   "subjects": [
#     "Subject ID 1",
#     "Subject ID 2"
#   ],
#   "panels": [
#     "Panel ID 1",
#     "Panel ID 2"
#   ]
# }


class TeacherModel(BaseModel):
    name: str
    email: str
    subjects: List[str]
    panels: List[str]


class TeacherIDModel(BaseModel):
    teacher_id: str
