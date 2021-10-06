from flask import Flask, request
from utils import reed_file, random_user, get_spaceman_count, csv_reader_pandas, mean_transform, work_with_db, read_sql

app = Flask(__name__)


@app.route("/requirements/")
def file_print():
    result = reed_file("requirements.txt")
    return result


@app.route("/generate-users/")
def random_users():
    # breakpoint()
    length = request.args.get('length', '100')
    if length.isdigit():
        length = int(length)
    else:
        length = 100
    result = random_user(length)
    return result


@app.route("/mean/")
def csv_file_mean():
    file_path = 'hw (2) (1).csv'
    sm_in_inch = 2.54
    kg_in_pound = 0.453592
    my_desk = csv_reader_pandas(file_path)
    hi_mean = mean_transform(my_desk['Height(Inches)']['mean'], sm_in_inch)
    wp_mean = mean_transform(my_desk['Weight(Pounds)']['mean'], kg_in_pound)
    return f'Средний рост(см): {hi_mean} Средний вес(кг): {wp_mean}'


@app.route("/space/")
def spaceman_count():
    href = 'http://api.open-notify.org/astros.json'
    item = 'number'
    result = get_spaceman_count(href, item)
    return f'Количество космонавтов в настоящий момент: {result}'


@app.route("/phones/create/")
def phones_create():
    file_path = 'users.db'
    contact_name = request.args['name']
    phone_value = request.args['phone']
    sql = f'''
        INSERT INTO Phones (contactName, phoneValue)
        VALUES ('{contact_name}', '{phone_value}')
        '''
    work_with_db(file_path, sql)
    return f'Пользователь {contact_name} долбавлен'


@app.route("/phones/read/")
def phones_read():
    file_path = 'users.db'
    sql = f'''
        SELECT * FROM Phones
        '''
    result = read_sql(file_path, sql)
    return f'Записи в таблице: {result}'


@app.route("/phones/update/")
def phones_update():
    file_path = 'users.db'
    phone_value = request.args['phone']
    phone_id = request.args['id']

    sql = f'''
        UPDATE Phones
        SET phoneValue = '{phone_value}'
        WHERE phoneID = {phone_id};
        '''
    work_with_db(file_path, sql)
    return f'Phone_update'


@app.route("/phones/delete/")
def phones_delete():
    file_path = 'users.db'
    phone_id = request.args['id']

    sql = f'''
        DELETE FROM Phones
        WHERE phoneID = {phone_id};
        '''
    work_with_db(file_path, sql)
    return 'Phone_delete'


if __name__ == '__main__':
    app.run(host='0.0.0.0')

print(1)