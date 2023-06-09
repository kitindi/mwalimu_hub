from django.shortcuts import render, redirect
from .forms import NewsletterForm
from .models import Job, Blog, Event
from django.db.models import Q

# Create your views here.


def home(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("home-page")
    form = NewsletterForm()
    context = {"form": form}
    return render(request, "schools/home_page.html", context)


def jobboard(request):
    search_query = ""

    if request.GET.get("industry"):
        search_query = request.GET.get("industry")

    jobs = Job.objects.filter(industry__icontains=search_query)
    context = {"jobs": jobs}
    return render(request, "schools/jobboard.html", context)


def jobdetails(request, id):
    job = Job.objects.get(id=id)
    job_industry = job.industry
    job_id = job.id

    related_jobs = Job.objects.filter(
        Q(industry__icontains=job_industry) & ~Q(id=job.id)
    )

    context = {"job": job, "related_jobs": related_jobs}
    return render(request, "schools/jobdetails.html", context)


def schools(request):
    return render(request, "schools/schools.html")


def posts(request):
    blog_posts = Blog.objects.all()

    context = {"blog_posts": blog_posts}
    return render(request, "schools/posts.html", context)


def post(request, id):
    blog_post = Blog.objects.get(id=id)

    context = {"blog_post": blog_post}
    return render(request, "schools/post.html", context)


def events(request):
    event_list = Event.objects.all()
    print(event_list)
    context = {"event_list": event_list}
    return render(request, "schools/events.html", context)


def event(request, id):
    event = Event.objects.get(id=id)

    context = {"event": event}
    return render(request, "schools/event.html", context)
