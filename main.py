from datetime import datetime

birthdate_date = input('Write the birthdate: ')
birthdate_date = datetime.strptime(birthdate_date, '%Y-%m-%d')
date_now = datetime.strptime(str(datetime.now().date()), '%Y-%m-%d')
hours_lived = (date_now.day-birthdate_date.day)*24 +\
              (date_now.month - birthdate_date.day)*730 +\
              (date_now.year - birthdate_date.day)*8760
print(hours_lived, "Hours lived.")
