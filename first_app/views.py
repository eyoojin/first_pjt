import random
from faker import Faker
from django.shortcuts import render
# render(render, template_name): 미완성 제품을 모아서 완성본의 html을 만듦

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request):
    my_name = 'yoojin'
    # my_name_b

    context = {
        'my_name': my_name,
        # my_name_a: my_name_b
    }

    return render(request, 'hello.html', context)
    
def lunch(request):
    menu = ['김밥', '국밥', '김치찌개']
    
    pick = random.choice(menu)

    context = {
        'pick': pick,
    }

    return render(request, 'lunch.html', context)

def lotto(request):
    numbers = range(1, 46)

    lucky = random.sample(numbers, 6)
    lucky.sort()

    context = {
        'lucky': lucky,
    }

    return render(request, 'lotto.html', context)

def profile(request, username):
    context = {
        'username': username,
    }

    return render(request, 'profile.html', context)

def cube(request, number):
    result = number ** 3
    # python식 해결법 int() -> 비추천

    context = {
        'number': number,
        'result': result,
    }

    return render(request, 'cube.html', context)

# pip install faker
def articles(request):
    fake = Faker()
    fake_articles = []

    for i in range(100):
        fake_articles.append(fake.text())


    context = {
        'fake_articles': fake_articles,
    }

    return render(request, 'articles.html', context)

