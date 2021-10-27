import random
import requests

def generate_grades():
    grades = []
    for i in range(10001, 12000):
        grades.append([i, random.randint(1,100)])
    return grades

def generate_personal():
    api_url = "https://api.namefake.com/english-canada/random/"
    personal = []
    for i in range(10001, 10003):
        response = requests.get(api_url)
        j = response.json()
        personal.append([i, j['name']])
    return personal
