import sqlite3

def create_db():
    con = sqlite3.connect("C:/Users/Stud1/Documents/Belov/БеловА/Htmlcssproject/obj/Projecthtmlcss/test.db")
    cur = con.cursor()
    query = ''' CREATE TABLE users('id' integer primary key, 'Логин' text(100), 'Почта' text(100), 'Пароль' text(100), 'Телефон' text(100))'''
    cur.execute(query)
    con.commit()
    
    
def insert_to_table(Логин, Почта, Пароль, Телефон):
    con = sqlite3.connect("C:/Users/Stud1/Documents/Belov/БеловА/Htmlcssproject/obj/Projecthtmlcss/test.db")
    cur = con.cursor()
    query = f''' INSERT INTO users('Логин', 'Почта', 'Пароль', 'Телефон') VALUES('{Логин}', '{Почта}', '{Пароль}', '{Телефон}') '''
    cur.execute(query)
    con.commit()