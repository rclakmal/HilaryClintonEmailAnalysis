import pandas as pd
import re
import csv
import enchant
import pycountry
from collections import Counter

# Reading all the text in raw email body and partitioning to words.
word_list = []
email_dataframe = pd.read_csv("../input/Emails.csv")
raw_text_list = email_dataframe['RawText'].tolist()
for raw_text in raw_text_list:
    word_list = word_list + re.findall('\w+', raw_text.lower())

# Using pyCountry module to list down all the countries. We consider shorten forms of the countries as well.
# Example: We consider all 3 formats of pakistan. (pakistan, pk, pak).
# But if it is a language specific word such as 'us', we ignore those items from our search.
country_list = []
english_checker = enchant.Dict("en_US")
country_list = []
for country in pycountry.countries:
    country_list.append(country.name.strip().lower())
    if not english_checker.check(country.alpha2.lower()):
        country_list.append(country.alpha2.lower())
    if not english_checker.check(country.alpha3.lower()):
        country_list.append(country.alpha3.lower())

high_frequency_countries = Counter(x for x in word_list if x in country_list).most_common(100)

with open("../output/mostcommoncountries.csv", 'w') as csvfile:
    fieldnames = ['Country', 'Count']
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    for country_count_pair in high_frequency_countries:
        country = country_count_pair[0]
        count = country_count_pair[1]
        row = [country, count]
        writer.writerow(row)


