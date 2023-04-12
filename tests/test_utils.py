from src import utils
import datetime


def test_data_sorted(test_data_filter):
    for d in test_data_filter[:5]:
        print(d["date"])

    print("\n" + "-------------------" + "\n")

    print(*[x["date"] for x in utils.data_sorted(test_data_filter)][:5],
          sep="\n")

    assert test_data_filter[:5] != utils.data_sorted(test_data_filter)[:5]


def test_data_filter(test_data):
    print("\n\nВо всех данных статус \"EXECUTED\":")
    print(all(x["state"] == "EXECUTED" for x in test_data))

    assert all(x["state"] == "EXECUTED" for x in test_data) == False

    print("\n" + "-------------------" + "\n")

    print("Во всех отфильтрованных данных статус \"EXECUTED\":")
    print(all(x["state"] == "EXECUTED" for x in utils.data_filter(test_data)))

    assert all(
        x["state"] == "EXECUTED" for x in utils.data_filter(test_data)) == True


def test_in_date_time(test_data_strings_date):
    print("\n\nВо всех данных статус тип str:")
    print(all(type(x) == str for x in test_data_strings_date))

    assert all(type(x) == str for x in test_data_strings_date) == True

    print("\n" + "-------------------" + "\n")

    print("Во всех данных статус тип datetime.datetime:")
    print(all(type(utils.in_date_time(x)) == datetime.datetime for x in
              test_data_strings_date))

    assert all(type(utils.in_date_time(x)) == datetime.datetime for x in
               test_data_strings_date) == True


def test_format_data(test_data_filter):
    for operation in test_data_filter:
        dt = operation["date"]
        dscrptn = operation["description"]
        frm = operation["from"] if "Перевод" in dscrptn else ""
        # Шаблон 1, если frm не пуст
        if len(frm) != 0:
            lst_to_check = [utils.in_date_time(dt).strftime('%d.%m.%Y'),
                            "** ****", "->"]
        # Шаблон 2, если frm пуст
        else:
            lst_to_check = [utils.in_date_time(dt).strftime('%d.%m.%Y'), "->",
                            " **"]

        # есть ли все шаблоны в форматированной строке
        for test in lst_to_check:
            assert test in utils.format_data(operation)
