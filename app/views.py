from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile, Pig, Schedule
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/registration/login')
def home(request):
    pigs = Pig.objects.all()
    return render(request, "home.html",{'pigs': pigs})

def signup(request):
    if request.method == "POST":
        profile = Profile()
        username = request.POST["username"]
        password = request.POST["password"]
        profile.nickname = request.POST["nickname"]
        found_user = User.objects.filter(username=username)
        if len(found_user):
            error = "이미 존재하는 아이디입니다."
            return render(request, "registration/signup.html", {"error": error})
        new_user = User.objects.create_user(username=username, password=password)
        profile.user = new_user        

        profile.save()

        auth.login(request, new_user)

        return redirect("home")
    return render(request, "registration/signup.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(
                request, user)
            return redirect("home")
            
        error = "아이디 또는 비밀번호가 틀립니다."
        return render(request, "registration/login.html", {"error":error})
    return render(request, "registration/login.html")

def logout(request):
    auth.logout(request)

    return redirect("home")

@login_required(login_url="/registration/login")
def pig_new(request):
    if request.method == "POST":
        new_Pig = Pig.objects.create(
            pig_name = request.POST["pig_name"],
            pig_description = request.POST["pig_description"],
            exchange_rate = request.POST["exchange_rate"],
        )
        return redirect('home')
    profiles = Profile.objects.all()
    return render(request, 'pig_new.html', {'profiles' : profiles})


def pig_detail(request, pig_pk):
    pig = Pig.objects.get(pk=pig_pk)
    schedules = Schedule.objects.filter(pig_info = pig_pk)

    return render(request, 'pig_detail.html', {'pig': pig, 'schedules': schedules})


def schedule_new(request, pig_pk):
    if request.method =='POST':
      pig = Pig.objects.get(pk=pig_pk)
      new_schedule = Schedule.objects.create(
        pig_info = pig,
        schedule_name = request.POST['schedule_name'],
        schedule_description = request.POST['schedule_description'],
        where_to_meet = request.POST['where_to_meet'],
        when_to_meet =request.POST['when_to_meet'],
      )

      return redirect('pig_detail', pig_pk) 
    return render(request, 'schedule_new.html', {"pig_pk": pig_pk})

def pig_bye(request):
    return render(request, 'pig_bye.html')


def landing(request):
    return render(request, 'landing.html')

def bye_winner(request):
    return render(request, 'bye_winner.html')

def bye_donate(request):
    return render(request, 'bye_donate.html')

def bye_winner_complete(request):
    return render(request, 'bye_winner_complete.html')
