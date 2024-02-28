'''
This file contains the routes for interaction with any face recognition models, or actually carrying out the face recognition process.
'''

# import fastapi stuff
from fastapi import APIRouter

# import face rec stuff
from facial_recognition.FaceRec import FaceRec  # main class

# import models
from models.ClientUploadModels import AttendanceModel
from models.StudentModels import EncodingModel
router = APIRouter(prefix="/face_rec", tags=["Face Recognition"])


@router.get("/test", status_code=200, summary="Test route")
def index():
	test_obj = FaceRec()
	# so ideally objects of this class would receive encodings of all the students, and the class image. We would get
	# this from calling functions of other routes (like getting student urls, encoding urls, etc), and then we would
	# call the methods of this class to get the attendance. we would then return that attendance.
	return "Hello, World!"


@router.get("/get_attendance", status_code=200, summary="Get attendance")
def get_attendance(class_att: AttendanceModel):
	pass
	
