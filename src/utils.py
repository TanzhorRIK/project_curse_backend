import json

def get_data()->list:
    """This function return data from json-file"""
    with open("operations.json", mode="r", encoding="utf-8") as in_f:
        f = in_f.read()
        data = json.loads(f)
        return data

def filtr(data):
    """This function return data:list with operations,
     if these operations are performed"""
    data = []
    for operation in get_data():
        for item in operation.items():
            if item[0] == "state" and item[1] == "EXECUTED":
                data.append(operation)
                break
    return data

def srted(data):
    """This function sorts list by date and time in descending order
     and return new list"""
    pass
