money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0

current_budjet = money_capital + salary #всего денег
while current_budjet >= spend:
    months += 1
    money_capital = current_budjet - spend
    spend *= (1 + increase)
    current_budjet = money_capital + salary

print("Количество месяцев, которое можно протянуть без долгов:", months)
