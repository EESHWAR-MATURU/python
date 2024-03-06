import datetime

# Neeta's 26th birthday
birthday_26 = datetime.datetime(1993, 5, 26)

# Neeta's 25th birthday
birthday_25 = birthday_26.replace(year=birthday_26.year - 1)

# Get the day of the week for Neeta's 25th birthday
day_of_week = birthday_25.strftime('%A')

print(f"Neeta celebrated his 25th birthday on a {day_of_week}.")
