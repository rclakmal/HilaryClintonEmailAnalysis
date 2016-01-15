'''
Created on Jan 15, 2016

@author: rclakmal
'''

import pandas as pd
import re
from collections import Counter

word_list = []
email_dataframe = pd.read_csv("../output/Emails.csv")
raw_text_list = email_dataframe['RawText'].tolist()
for raw_text in raw_text_list:
    word_list = word_list + re.findall('\w+',raw_text.lower())
print Counter(word_list).most_common(20)


