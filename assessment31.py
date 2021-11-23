import random
import requests

def generate_grades():
    '''
    Generates a 2D array of 2000 student numbers 
    (ordered starting at 10000) 
    and a random grade for the student.
    Returns the 2D array of student numbers and grades.
    '''
    grades = []
    for i in range(10000, 12000):
        grades.append([i, random.randint(1,100)])
    return grades

def generate_personal():
    '''
    Generates a 2D array of 2000 student numbers 
    (ordered starting at 10000) 
    and a random name for the student.
    Returns the 2D array of student numbers and name.
    '''
    api_url = "https://api.namefake.com/english-canada/random/"
    personal = []
    for i in range(10000, 10010):
        response = requests.get(api_url)
        j = response.json()
        personal.append([i, j['name']])
    return personal
