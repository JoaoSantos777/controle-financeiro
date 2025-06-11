from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Sum
from renda.models import Renda
from despesa.models import Despesa

def relatorio_financeiro(request):
    # Calculando a soma total de rendas e despesas
    renda_total = Renda.objects.aggregate(total=Sum('valor'))['total'] or 0
    despesa_total = Despesa.objects.aggregate(total=Sum('valor'))['total'] or 0

    # Calculando o saldo geral
    saldo = renda_total - despesa_total

    # Criando uma lista com detalhes das rendas
    rendas_detalhes = []
    rendas = Renda.objects.all()

    for renda in rendas:
        despesas_associadas = renda.despesas.all()
        total_despesas = despesas_associadas.aggregate(total=Sum('valor'))['total'] or 0
        saldo_renda = renda.valor - total_despesas
        rendas_detalhes.append({
            'renda': renda,
            'despesas': despesas_associadas,
            'total_despesas': total_despesas,
            'saldo_renda': saldo_renda,
        })

    # Passando os valores para o template
    context = {
        'renda_total': renda_total,
        'despesa_total': despesa_total,
        'saldo': saldo,
        'rendas_detalhes': rendas_detalhes,
    }
    return render(request, 'relatorio_financeiro.html', context)

