from django.shortcuts import render


def prizm(request):

    return render(request, "prizm/prizm.html")

def vanilla(request):

    return render(request, "vanilla.html")

def fullPageScrolling(request):

    return render(request, "fullPageScrolling.html")

