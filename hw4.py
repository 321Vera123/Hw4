temperature = int(input("Введите температуру: "))
humidity = int(input("Введите влажность воздуха: "))
wind_speed = int(input("Введите скорость ветра: "))
is_raining = False
if temperature > 25:
    print("Сегодня жаркая погода ")
if temperature < 10:
    print("Сегодня холодная погода ")
if humidity >= 80:
    print("Сегодня высокая влажность ")
if wind_speed > 10:
    print("Сегодня сильный ветер ")
if temperature >= 20 and is_raining is False:
    print("Прогуляйтесь в парке")
if temperature < 5 and wind_speed > 8:
    print("Сегодня плохая погода")
if humidity < 30 and temperature > 30:
    print("Сегодня сухая и жаркая погода")
