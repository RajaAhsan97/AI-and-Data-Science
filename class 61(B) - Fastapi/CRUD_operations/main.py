#uvicorn main:app

from fastapi import FastAPI

app = FastAPI()

#@app.get("/")    # route
#def read_data():
#    return {'Ahsan': 'Hello'}

students = [
    {'id': 1, 'name': 'Ahsan', 'age': 20},
    {'id': 2, 'name': 'Ubaid', 'age': 19}
]

@app.get('/')
def main_root():
    return {'message': 'API is working...'}

# Retrieve
@app.get('/retrieve_students')
def get_students():
    return students

# Create student
@app.post('/create_student')
def create_student(name:str, age:int):
    new_student = {
        'id': len(students) + 1,
        'name': name,
        'age': age
    }

    students.append(new_student)

    return new_student

# Update student
@app.put('/update_student/{id}')
def update_student(id:int, name:str, age:int):
    for s in students:
        if s['id'] == id:
            s['name'] = name
            s['age'] = age

            return s
        
# Delete
@app.delete('/delete_student/{id}')
def delete_student(id:int):
    for s in students:
        if s['id'] == id:
            students.remove(s)

            return {'message': f"{s['name']} student has been deleted successfully"}