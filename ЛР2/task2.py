salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
required_capital = 0
current_money = 0
current_spend = spend
for month in range(months):
    total = current_money + salary
    if total < current_spend:
        deficit = current_spend - total
        required_capital += deficit
        current_money += deficit
    current_money = current_money + salary - current_spend
    current_spend *= (1 + increase)
required_capital = round(required_capital)
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", required_capital)
