from django.test import TestCase
import datetime as dt

# Create your tests here.
teraz = dt.datetime.now()
jutro = teraz + dt.timedelta(days=1)
wynik = (jutro - teraz).total_seconds() / 3600

print(wynik)