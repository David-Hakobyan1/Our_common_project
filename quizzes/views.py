from django.shortcuts import render
import random
from .models import CountriesQuestion, DifferentQuestion, SportQuestion
# from django.core.exceptions import ObjectDoesNotExist


def quizzes(request):
    return render(request, 'quizzes/quizzes.html')


number = 0
id = 1
def play(request, index):
    global id
    global number
    country = CountriesQuestion
    different = DifferentQuestion
    sport = SportQuestion
    topics = [sport, country, different]
    topic = topics[int(index)]
    info = ''
    try:
        quiz = topic.objects.get(id=id)
        if request.method == 'POST':
            id += 1
            answer = request.POST.get('answer')
            if answer == quiz.right_answer:
                info = 'Right'
                number += 1
            else:
                info = 'Wrong'
            quiz = topic.objects.get(id=id)
    except topic.DoesNotExist:
        info = f'"Game over!Your score is {number}/10!"'
        quiz = None
        id = 1
    return render(request, 'quizzes/game.html', {'quiz': quiz, 'number': number, 'info': info, 'index': index})


my_list = ["rock", "paper", "scissors"]
number1 = 0
number2 = 0


def chingachung(request):
    if request.method == 'POST':
        global my_list
        global number1
        global number2
        rands = random.randrange(len(my_list))
        player2 = my_list[rands]
        fnum = request.POST.get('fname')
        if player2 == fnum:
            pass
        if player2 == "paper" and fnum == "rock":
            number2 += 1
        if player2 == "paper" and fnum == "scissors":
            number1 += 1
        if player2 == "scissors" and fnum == "paper":
            number2 += 1
        if player2 == "scissors" and fnum == "rock":
            number1 += 1
        if player2 == "rock" and fnum == "scissors":
            number2 += 1
        if player2 == "rock" and fnum == "paper":
            number1 += 1
        return render(request, 'quizzes/chingachung.html',{'my_list':my_list,'number1':number1,'number2':number2,'info':'ok','fnum':fnum,'player2':player2})
    return render(request, 'quizzes/chingachung.html', {'my_list':my_list,'number1':number1,'number2':number2,'info':'start'})


def subjects(request):
    return render(request, 'quizzes/subjects.html')