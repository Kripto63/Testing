# В переменной $datetime содержится дата/время в таком формате:
# 2016-04-11 20:59:03
# Напиши регулярное выражение, которое поможет разбить строку и 
# заполнить переменные $date и $time. В переменную $date должно попасть 2016-04-11, в $time - 20:59:03.

import re

datetime = "2016-04-11 20:59:03"
print("Переменная datetime={}\n".format(datetime))

date = re.search(r'\d{4}-\d{2}-\d{2}', datetime).group(0)
time = re.search(r'\d{2}:\d{2}:\d{2}', datetime).group(0)
print("1-вариант:\ndata = {0}\ntime = {1}\n".format(date, time))

date, time = re.findall(r"\d+\W\d+\W\d+", datetime)
print("2-вариант:\ndata = {0}\ntime = {1}\n".format(date, time))