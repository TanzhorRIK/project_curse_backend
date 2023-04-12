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
