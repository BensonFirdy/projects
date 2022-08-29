import json
import requests
import pyergast
import yukinator

y = yukinator.Yuki()
races_2022 = y.get_race_results(year='current')



# print name of the race
print(races_2022[1])