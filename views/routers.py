import fastapi
from models.courses import Course

router = fastapi.APIRouter()
fakedb = []


@router.get('/')
def read_root():
    return {"greetings": "Welcome"}


@router.get('/courses')
def get_courses():
    return fakedb


@router.get('/courses/{course_id}')
def get_a_course(course_id: int):
    course = course_id - 1
    return fakedb[course]


@router.post('/courses')
def add_course(course: Course):
    fakedb.append((course.dict()))
    return fakedb[-1]


@router.delete('/courses/{course_id}')
def delete_course(course_id: int):
    fakedb.pop(course_id - 1)
    return {'message': 'deletion successful'}
