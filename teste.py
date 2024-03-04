import re
def transformacao_data(date_str):
    data = re.compile(r'(\d{4})-(\d{2})-(\d{2})')
    data_brasileira = data.sub(r'\3/\2/\1', date_str)
    return data_brasileira
date = "2021-11-30"
mudanca_data = transformacao_data(date)
print(mudanca_data)  
