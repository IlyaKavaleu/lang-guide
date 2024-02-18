from django.shortcuts import render, redirect, get_object_or_404

from orders.models import Order
from paid_lessons.forms import PaidLessonForm, AddChapterForm, PaidChapterForm
from paid_lessons.models import PaidLesson, PaidСhapter
from programming_guide.settings import AUTH_USER_MODEL
from users.models import User


def add_paid_lesson(request, user_id):
    if request.method != 'POST':
        form = PaidLessonForm()
    else:
        form = PaidLessonForm(data=request.POST)
        if form.is_valid():
            user_form = form.save(commit=False)
            user = User.objects.get(id=user_id)
            user_form.teacher = user
            user_form.save()
            return redirect('paid_lessons:list_paid_lesson', user_id=user_id)
    context = {'form': form}
    return render(request, 'paid_lessons/add_paid_lesson.html', context)


def add_paid_chapter(request, lesson_id):
    lesson = PaidLesson.objects.get(id=lesson_id)
    if request.method != 'POST':
        form = PaidChapterForm()
    else:
        form = PaidChapterForm(data=request.POST)
        if form.is_valid():
            chapter_form = form.save(commit=False)
            chapter_form.lesson = lesson
            chapter_form.save()
            return redirect('paid_lessons:show_lesson', lesson_id=lesson.id)
    context = {'form': form}
    return render(request, 'paid_lessons/add_chapter.html', context)


def list_paid_lesson(request, user_id):
    teacher = get_object_or_404(User, id=user_id)
    lessons = PaidLesson.objects.filter(teacher=teacher)
    context = {'lessons': lessons, 'teacher': teacher}
    return render(request, 'paid_lessons/list_paid_lesson.html', context)


def all_paid_lessons(request):
    paid_lessons = PaidLesson.objects.all()
    context = {'paid_lessons': paid_lessons}
    return render(request, 'paid_lessons/all_paid_lessons.html', context)


def show_lesson(request, lesson_id, user_id=None):
    lesson = PaidLesson.objects.get(id=lesson_id)
    teacher = lesson.teacher.id
    chapters = PaidСhapter.objects.filter(lesson=lesson)
    is_purchased = Order.objects.filter(initiator=request.user, status=Order.PAID).exists()
    context = {'chapters': chapters, 'lesson': lesson, 'teacher': teacher, 'is_purchased': is_purchased}
    return render(request, 'paid_lessons/paid_lesson.html', context)


def add_lesson(request, user_id):
    teacher = User.objects.get(id=user_id)
    if request.method != 'POST':
        form = PaidLessonForm()
    else:
        form = PaidLessonForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.teacher = teacher
            form.save()
            return redirect('paid_lessons:list_paid_lesson', user_id=teacher.id)
    context = {'teacher': teacher, 'form': form}
    return render(request, 'paid_lessons/add_lesson.html', context)


def add_chapter(request, lesson_id):
    lesson = PaidLesson.objects.get(id=lesson_id)
    if request.method != 'POST':
        form = AddChapterForm()
    else:
        form = AddChapterForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.lesson = lesson
            form.save()
            return redirect('paid_lessons:show_lesson', lesson.id)
    context = {'lesson': lesson, 'form': form}
    return render(request, 'paid_lessons/add_chapter.html', context)


def edit_paid_chapter(request, chapter_id):
    chapter = PaidСhapter.objects.get(id=chapter_id)
    if request.method != 'POST':
        form = PaidChapterForm(instance=chapter)
    else:
        form = PaidChapterForm(request.POST, request.FILES, instance=chapter)
        if form.is_valid():
            form.save()
            return redirect('paid_lessons:show_lesson', lesson_id=chapter.lesson.id)
    context = {'form': form, 'chapter': chapter}
    return render(request, 'paid_lessons/edit_paid_chapter.html', context)


def edit_paid_lesson(request, lesson_id):
    lesson = PaidLesson.objects.get(id=lesson_id)
    if request.method != 'POST':
        form = PaidLessonForm(instance=lesson)
    else:
        form = PaidLessonForm(request.POST, request.FILES, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('paid_lessons:list_paid_lesson', user_id=lesson.teacher.id)
    context = {'form': form, 'lesson': lesson}
    return render(request, 'paid_lessons/edit_paid_lesson.html', context)


def delete_lesson(request, lesson_id):
    lesson = PaidLesson.objects.get(id=lesson_id)
    lesson.delete()
    return redirect('paid_lessons:list_paid_lesson', user_id=lesson.teacher.id)


def delete_chapter(request, chapter_id):
    chapter = PaidСhapter.objects.get(id=chapter_id)
    chapter.delete()
    return redirect('paid_lessons:show_lesson', lesson_id=chapter.lesson.id)
