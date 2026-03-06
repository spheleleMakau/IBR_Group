from django.shortcuts import render


def home(request):
    context = {
        'page': 'home',
    }
    return render(request, 'home.html', context)


def about(request):
    context = {
        'page': 'about',
    }
    return render(request, 'about.html', context)


def projects(request):
    # placeholder project data
    project_list = [
        {'title': f'Project {i}', 'description': 'Short description placeholder'}
        for i in range(1, 7)
    ]
    context = {
        'page': 'projects',
        'projects': project_list,
    }
    return render(request, 'projects.html', context)


def donate(request):
    context = {
        'page': 'donate',
    }
    return render(request, 'donate.html', context)


def contact(request):
    context = {
        'page': 'contact',
    }
    return render(request, 'contact.html', context)
