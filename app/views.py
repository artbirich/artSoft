from datetime import datetime
from django.shortcuts import render, redirect
from .models import Author, Post
from .formes import AddForm


def home(request):
    return render(request, 'home.html')


def consult_design(request):
    return render(request, 'consult_design.html')


def engineer(request):
    return render(request, 'engineer.html')


def operate(request):
    return render(request, 'operate.html')


def about(request):
    return render(request, 'about.html')


def profile(request):
    return render(request, 'profile.html')


def logout(request):
    return render(request, 'logout.html')

def comment(request):
    form = AddForm()

    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = Author.objects.get()
            new_post.issued = datetime.now()

            new_post.save()
            form.save_m2m()

            return redirect('comment')

    comment = Post.objects.all().order_by('-issued')

    return render(request, 'comment.html', {'form': form, 'comment': comment})