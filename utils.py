def reed_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        result = f.read()
        return result


def random_user(num: int = 100) -> str:
    from faker import Faker
    fake = Faker()
    result = ''
    for _ in range(num):
        result += f'{fake.first_name()} {fake.ascii_email()}</br>'
    return result


def csv_reader_pandas(file_path: str):
    import pandas as pd
    result = pd.read_csv(file_path, skipinitialspace=True).describe()
    return result


def mean_transform(all_sum: float, quantity: float = 1) -> float:
    result = float(all_sum * quantity)
    return result


def get_spaceman_count(href: str, item: str) -> str:
    import requests
    r = requests.get(href).json()[item]
    result = str(r)
    return result


def work_with_db(file_path: str, sql):
    import sqlite3
    con = sqlite3.connect(file_path)
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()


def read_sql(file_path: str, sql):
    import sqlite3
    con = sqlite3.connect(file_path)
    cur = con.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    con.commit()
    con.close()
    return str(result)


def reed_file_my(file_path: str) -> str:
    with open(file_path, "r") as f:
        result = f.read()
        res_arr = result.split('\n')

        return res_arr


dates = reed_file_my('my.csv')
count = 1
check = 1614605860
for i in dates:
    if i.isdigit():
        i = int(i)
        print(check < i)
        if check < i:
            count += 1

print(count)
