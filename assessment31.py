import random
import requests

def generate_grades():
    '''
    Generates an array of 2000 student numbers (ordered starting at 10001) and a random grade for the student
    '''
    grades = []
    for i in range(10001, 12000):
        grades.append([i, random.randint(1,100)])
    return grades

def generate_personal():
    '''
    Generates an array of 2000 student numbers (ordered starting at 10001) and a random name for the student
    '''
    api_url = "https://api.namefake.com/english-canada/random/"
    personal = []
    for i in range(10001, 10003):
        response = requests.get(api_url)
        j = response.json()
        personal.append([i, j['name']])
    return personal
