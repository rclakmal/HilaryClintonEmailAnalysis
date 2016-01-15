'''
Created on Jan 15, 2016

@author: rclakmal
'''

import pandas as pd
import sqlite3
from IPython.lib.editorhooks import emacs

con = sqlite3.connect('../output/database.sqlite')
sample = pd.read_sql_query("""
SELECT p.Name Sender,
       e.MetadataSubject Subject
FROM Emails e
INNER JOIN Persons p ON e.SenderPersonId=p.Id
LIMIT 10""", con)
print(sample)

# You can read a CSV file like this
emailData = pd.read_csv("../output/Emails.csv")
print(emailData)
