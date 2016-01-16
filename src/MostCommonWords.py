'''
Created on Jan 15, 2016

@author: rclakmal
'''

import pandas as pd
import enchant
import re
import csv
from collections import Counter

# Reading all the text in raw email body and partitioning to words.
word_list = []
email_dataframe = pd.read_csv("../input/Emails.csv")
raw_text_list = email_dataframe['RawText'].tolist()
for raw_text in raw_text_list:
    word_list = word_list + re.findall('\w+', raw_text.lower())

# Considering non-language specific words checking for top 100 high frequncy words.
english_checker = enchant.Dict("en_US")
high_frequency_words = Counter(x for x in word_list if not english_checker.check(x)).most_common(100)

# Saving to a CSV.
with open("../output/100mostcommonwords.csv", 'w') as csvfile:
    fieldnames = ['Word', 'Count']
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    for word_count_pair in high_frequency_words:
        word = word_count_pair[0]
        count = word_count_pair[1]
        row = [word, count]
        writer.writerow(row)
