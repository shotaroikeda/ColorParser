#!/usr/bin/python
import sys
import pandas as pd

def json_update_good():
    import json
    import requests

    r = requests.get("https://colordatasubmission.firebaseio.com/good.json")
    py_dict = r.json()
    r.close()

    data = [d for e, d in py_dict.items()]

    df = pd.DataFrame.from_dict(data)
    df.to_csv('bin/good.csv')

    return df

def json_update_bad():
    import json
    import requests

    r = requests.get("https://colordatasubmission.firebaseio.com/bad.json")
    py_dict = r.json()
    r.close()

    data = [d for e, d in py_dict.items()]

    df = pd.DataFrame.from_dict(data)
    df.to_csv('bin/bad.csv')

    return df


if __name__ == '__main__':
    sys.argv.pop(0)
    while len(sys.argv) > 0:
        if sys.argv[0] == '-u':
            json_update_good()
            json_update_bad()
