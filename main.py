print("--- Калькулятор бюджета на Испанию ---")

# Запрашиваем данные у пользователя
rubles = float(input("Сколько рублей ты откладываешь в месяц? "))
exchange_rate = float(input("Какой сейчас курс евро? (например, 100) "))

# Считаем
euros_per_month = rubles / exchange_rate
goal = 5000  # Наша цель - 5000 евро на переезд
months_needed = goal / euros_per_month

# Выводим результат
print("--------------------------------------")
print(f"Ты откладываешь примерно {round(euros_per_month, 2)} евро в месяц.")
print(f"Чтобы накопить {goal} евро, тебе понадобится {round(months_needed, 1)} месяцев.")
