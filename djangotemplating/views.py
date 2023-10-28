from django.shortcuts import render
def home (request):
    return render(request,"index.html")
def about(request):
    return render(request, "about.html")
def error(request):
    return render(request, "error.html")
def blog(request):
    return render(request, "blog.html")
def contact(request):
    return render(request, "contact.html")
def project(request):
    return render(request, "project.html")
def service(request):
    return render(request, "service.html")
def team(request):
    return render(request, "team.html")
def testimonial(request):
    return render(request, "testimonial.html")