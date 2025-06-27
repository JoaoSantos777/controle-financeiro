from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Sum
from renda.models import Renda
from despesa.models import Despesa


def relatorio_financeiro(request):
    # Filtra rendas e despesas pelo usuário logado
    rendas = Renda.objects.filter(user=request.user)
    despesas = Despesa.objects.filter(user=request.user)

    # Soma total de rendas e despesas do usuário
    renda_total = rendas.aggregate(total=Sum('valor'))['total'] or 0
    despesa_total = despesas.aggregate(total=Sum('valor'))['total'] or 0
    saldo = renda_total - despesa_total

    # Monta detalhes por renda, com despesas associadas
    rendas_detalhes = []
    for renda in rendas:
        despesas_associadas = renda.despesas.filter(user=request.user)
        total_despesas = despesas_associadas.aggregate(total=Sum('valor'))['total'] or 0
        saldo_renda = renda.valor - total_despesas
        rendas_detalhes.append({
            'renda': renda,
            'despesas': despesas_associadas,
            'total_despesas': total_despesas,
            'saldo_renda': saldo_renda,
        })

    context = {
        'renda_total': renda_total,
        'despesa_total': despesa_total,
        'saldo': saldo,
        'rendas_detalhes': rendas_detalhes,
    }
    return render(request, 'relatorio_financeiro.html', context)

