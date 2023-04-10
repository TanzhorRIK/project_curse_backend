import json, datetime, math


def get_data() -> list:
    """This function return data from json-file"""
    with open("operations.json", mode="r", encoding="utf-8") as in_f:
        f = in_f.read()
        data = json.loads(f)
        return data


def filtr(data: list) -> list:
    """This function return data:list with operations,
     if these operations are performed"""
    result = []
    for operation in data:
        for item in operation.items():
            if item[0] == "state" and item[1] == "EXECUTED":
                result.append(operation)
                break
    return result


def srted(data: list) -> list:
    """This function sorts list by date and time in descending order
     and return new list"""
    data = sorted(data, key=lambda x: in_date_time(x["date"]), reverse=True)
    return data


def in_date_time(string: str) -> datetime.datetime:
    """This function reformated string with date-time in object datetime"""
    d, t = string.split("T")
    y, mn, d = map(int, d.split("-"))
    h, m, s = int(t.split(":")[0]), int(t.split(":")[1]), math.ceil(
        float(t.split(":")[2]))
    dt = datetime.datetime(y, mn, d, h, m, s)
    return (dt)


def format_data(operation: list) -> str:
    """This function gets a list of arguments for formatting according
     to the pattern and returns a f-string"""
    dte = in_date_time(operation["date"])
    dscrtin = operation["description"]
    if "from" in operation:
        frm = operation["from"].rsplit(maxsplit=1)[0]
        frm_id_card_hidden = operation["from"].rsplit(maxsplit=1)[1]
        frm_id_card_hidden = f"{frm_id_card_hidden[:4]} {frm_id_card_hidden[4:6]}** **** {frm_id_card_hidden[-4:]}"
    else:
        frm = ""
        frm_id_card_hidden = ""
    oprtnamnt = operation["operationAmount"]
    to_the = operation["to"]
    return f"{dte.strftime('%d.%m.%Y')} {dscrtin}\n {frm} {frm_id_card_hidden} -> {to_the.split()[0]} **{to_the.split()[1][-4:]}\n{oprtnamnt['amount']} {oprtnamnt['currency']['name']}"
