salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0
for months in range(1, months + 1):
    if months > 1:
        spend += spend * increase
    deficit = spend - salary # Нехватка денег в этом месяце
    money_capital += deficit # Добавляем дефицит к общей сумме
money_capital = round(money_capital) # Округляем до целого числа

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
