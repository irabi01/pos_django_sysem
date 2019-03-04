from django.shortcuts import render

# Create your views here.
def _loginView(request):
    template = "pos/login.html"
    return render(request, template, {})


def _dashboard(request):
    template = "dashboard/dashboard.html"
    return render(request, template, {})