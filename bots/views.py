from django.shortcuts import render


def prizm(request):

    return render(request, "prizm/prizm.html")

def vanila(request):

    return render(request, "vanila.html")

def fullPageScrolling(request):

    return render(request, "fullPageScrolling.html")

