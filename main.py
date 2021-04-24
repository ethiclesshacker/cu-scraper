import pandas as pd
import requests
import pyperclip
import json

LINK = "https://exametc.com/spres2016/prcs/32/special_result_search_step1_view.php?examid=1107"
LINK = "https://exametc.com/spres2016/prcs/32/special_result_search_step1_view.php?examid=1113"

# 18103411295 -- Khushi Sadhwani

users = range(181017110055, 181017110990)

with open("ids.json","r") as f:
    users = json.load(f)


for user in users:

    try:
        data = {"srch1lbl": user}

        r = requests.post(LINK, data=data)
        print(r.status_code, user)

        tables = pd.read_html(r.text)

        df = tables[0].T
        new_header = df.iloc[0]  # grab the first row for the header
        df = df[1:]  # take the data less the header row
        df.columns = new_header

        dd = tables[1].T
        new_header = dd.iloc[0]  # grab the first row for the header
        dd = dd[1:]  # take the data less the header row
        dd.columns = new_header

        person = df.to_dict('records')[0]
        person['marks'] = dd.to_dict()

        print(json.dumps(person))

        with open("data.json", "a") as file:
            file.write(json.dumps(person)+",")
    except:
        print("Error for", user)
