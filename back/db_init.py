import psycopg2
import csv
import json

with open('database.json', 'r', encoding='utf-8') as f:
    read_data = f.read()

data = json.loads(read_data)

user = data.get('user')
password = data.get('password')
host = data.get('host')
dbname = data.get('dbname')
port = data.get('port')

psql = None
pc = None


def conn():
    global psql, pc
    try:
        psql = psycopg2.connect(f"""
                dbname={dbname}
                user={user}
                host={host}
                password={password}
                port={port}
            """)
    except:
        print("Error")
    pc = psql.cursor()


def close():
    global psql, pc
    psql.commit()
    pc.close()
    psql.close()
    pc = None
    psql = None


def create_table():
    global psql, pc
    conn()
    pc.execute('''CREATE TABLE  IF NOT EXISTS chat(
                id SERIAL PRIMARY KEY,
                question TEXT,
                answer TEXT
            );''')

    pc.execute('''CREATE TABLE  IF NOT EXISTS report(
                id SERIAL PRIMARY KEY,
                question TEXT,
                answer TEXT,
                change_answer TEXT
            );''')
    close()


def data_in():
    global psql, pc
    conn()
    with open('./data_in/ChatBotData.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            row[0] = row[0].replace("'", "`")
            row[1] = row[1].replace("'", "`")
            pc.execute(f"""
                INSERT INTO chat (question, answer)
                VALUES ('{row[0]}', '{row[1]}')
            """)
    close()


def get_reports():
    global psql, pc
    conn()
    pc.execute('''
        SELECT *
        FROM report;
    ''')
    value = pc.fetchall()
    data = []
    for idx, q, a, c in value:
        data.append({"id": idx, "question": q,
                     "answer": a, 'change_answer': c})
    close()
    return data


def get_report(id):
    global psql, pc
    conn()
    pc.execute(f'''
        SELECT *
        FROM report
        WHERE id={id};
    ''')
    value = pc.fetchone()
    data = {"id": value[0], "question": value[1],
            "answer": value[2], "change_answer": value[3]}
    close()
    return data


def post_report(kwargs):
    global psql, pc
    conn()
    question = kwargs['question'].replace("'", "`")
    answer = kwargs['answer'].replace("'", "`")
    change_answer = kwargs['change_answer'].replace("'", "`")
    pc.execute(f"""
        INSERT INTO report (question, answer, change_answer)
        VALUES ('{question}', '{answer}', '{change_answer}');
    """)
    close()


def delete_report(id):
    global psql, pc
    conn()
    res = pc.execute(f"""
        DELETE FROM report
        WHERE id = {id};
    """)
    close()