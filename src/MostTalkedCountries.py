import pandas as pd
import re
import csv
from collections import Counter

#Writing
word_list = []
email_dataframe = pd.read_csv("../input/Emails.csv")
raw_text_list = email_dataframe['RawText'].tolist()
for raw_text in raw_text_list:
    word_list = word_list + re.findall('\w+', raw_text.lower())

#Using pyCountry module to list down all the countries. Used only the first 3 letters of the country since most
high_frequency_words = Counter(x for x in word_list if not english_checker.check(x)).most_common(100)

with open("../output/mostcommoncountries.csv", 'w') as csvfile:
    fieldnames = ['Word', 'Count']
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    for key, value in high_frequency_words.iteritems():
        writer.writerow(key + value)