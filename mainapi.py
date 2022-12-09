from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


students = {
    1: {
        "name":"nishu",
        "location":"gurgoan",
        "age": "30"
    }
}

class Student(BaseModel):
    name: str
    age: int
    location: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    location: Optional[str] = None  

@app.get("/")
def index():
    return {"Hello":"Welcome"}

#Path Parameter
@app.get("/get-student/{student_id}")
def get_student(student_id: int= Path(None,description="The ID of the student that you wanna view",
                          gt=0, lt=50)):
    return students[student_id]


#Query Parameter
#google.com/result?search=Python

@app.get("/get-by-name")
def get_name(*, name: Optional[str] = None, test :int): #make sure default(required parameter must be placed before Optional or can use *)
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
        return {"Data":"Not Matched"}


#Query PArameter with path
@app.get("/get-by-name/{student_id}")
def get_name_byId(*,student_id: int, name: Optional[str] = None, test :int):
        if students[student_id]["name"]==name:
            return students[student_id]
        return {"Data":"Not Matched"}


#Request Body Parameter
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student:Student):
    if student_id in students:
        return {"Errro": "Already Exists"}

    students[student_id] =student
    return students[student_id]


@app.put("/update-student/{student_id}")
def update_student(student_id: int , student:UpdateStudent):
    if student_id not in students:
        return {"message":"Not in the student list"}
    
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age
    
    if student.location != None:
        students[student_id].location = student.location

    print(students[student_id], "1")
    return students[student_id]


@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return {"message":"No records found"}

    del students[student_id]
    return {"message": "deleted record successfully"}



