# miapp/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date
from account.models import Couple


@login_required
def home(request):
    dias_con_pareja = None
    pareja = None

    try:
        if Couple.objects.filter(novio=request.user).exists():
            couple = Couple.objects.get(novio=request.user)
            pareja = couple.novia 
        else:
            couple = Couple.objects.get(novia=request.user)
            pareja = couple.novio  

        if couple.aniversario:
            dias_con_pareja = (date.today() - couple.aniversario).days

    except Couple.DoesNotExist:
        pass

    context = {
        'username': request.user.username,
        'dias_con_pareja': dias_con_pareja,
        'pareja': pareja
    }
    return render(request, 'babe/home.html', context)
