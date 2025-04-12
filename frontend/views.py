from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import UsedInstrument, Job, CommunityPost, Lesson, Enrollment
from .forms import CustomUserCreationForm
from .models import LectureRoom

def index(request):
    return render(request, "index.html")

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = CustomUserCreationForm()
    return render(request, "sign_up.html", {"form": form})


def lessons(request):
    lessons = Lesson.objects.all()
    return render(request, "lessons.html", {
        "items": lessons,
        "page_type": "lessons"
    })


def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, "lesson_detail.html", {"lesson": lesson})


@login_required
def enroll_lesson(request, lesson_id):
    if request.method == "POST":
        lesson = get_object_or_404(Lesson, id=lesson_id)
        Enrollment.objects.get_or_create(user=request.user, lesson=lesson, is_paid=True)
        return redirect("my_page")
    return redirect("lesson_detail", lesson_id=lesson_id)

@login_required
def my_page(request):
    enrollments = Enrollment.objects.filter(user=request.user, is_paid=True).select_related("lesson")
    return render(request, "my_page.html", {
        "enrollments": enrollments,
        "page_type": "my_page"
    })

@login_required
def enter_classroom(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    room = LectureRoom.objects.filter(enrollment__lesson=lesson, enrollment__user=request.user).first()
    return render(request, "classroom.html", {
        "lesson": lesson,
        "room_url": room.room_url if room else "#"
    })


def human_resources(request):
    jobs = Job.objects.all()
    return render(request, "human_resources.html", {
        "items": jobs,
        "page_type": "human_resources"
    })


def community(request):
    posts = CommunityPost.objects.all()
    return render(request, "community.html", {
        "items": posts,
        "page_type": "community"
    })


def used_instruments(request):
    instruments = UsedInstrument.objects.all()
    return render(request, "used_instruments.html", {
        "items": instruments,
        "page_type": "used_instruments"
    })
