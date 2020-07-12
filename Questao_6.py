# SOMA PG ==> soma = (a*(q**n - 1))/q-1, ISOLANDO a, TEMOS  a = soma*(q-1)/(q**n-1)

def Inverso_somaPG(n,soma, q):

    aporte = soma*(q-1)/(q**n-1)

    return aporte


def MonthlyInvestiment(age, future_age, cumulative_amount, anual_rate):

    # NUMERO DE MESES
    n = 12*(future_age-age)

    # MUDA TAXA ANUAL PARA MENSAL
    monthly_rate = (1 + anual_rate)**(1/12)

    aporte = Inverso_somaPG(n,cumulative_amount, monthly_rate)

    return aporte
    
# IDADE ATUAL
age = 18

# IDADE FUTURA
future_age = 50

# QUANTIA ACUMULADA
cumulative_amount = 3000000

# TAXA DE JUROS
anual_rate = 0.10

aporte =  MonthlyInvestiment(age, future_age, cumulative_amount, anual_rate)

print('Seus aportes serao de', aporte)



