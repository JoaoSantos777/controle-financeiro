# views.py (app relatorios)

from django.shortcuts import render
from django.db.models import Sum
from renda.models import Renda
from despesa.models import Despesa

def relatorio_financeiro(request):
    # Calculando a soma total de rendas e despesas
    renda_total = Renda.objects.aggregate(total=Sum('valor'))['total'] or 0
    despesa_total = Despesa.objects.aggregate(total=Sum('valor'))['total'] or 0

    # Calculando o saldo
    saldo = renda_total - despesa_total

    # Obtendo as rendas e despesas detalhadas
    rendas = Renda.objects.all()
    despesas = Despesa.objects.all()

    # Passando os valores para o template
    context = {
        'renda_total': renda_total,
        'despesa_total': despesa_total,
        'saldo': saldo,
        'rendas': rendas,
        'despesas': despesas,
    }
    return render(request, 'relatorio_financeiro.html', context)
