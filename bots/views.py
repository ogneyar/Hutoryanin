from django.shortcuts import render


def prizm(request):

    return render(request, "prizm/prizm.html")

def semyanika(request):

    return render(request, "7yanika/7yanika.html")

def vanilla(request):

    return render(request, "vanilla.html")

def fullPageScrolling(request):

    return render(request, "fullPageScrolling.html")

