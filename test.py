import getpass

import oracledb

un = 'hr'
cs = 'localhost:1521/ORCL'
pw = getpass.getpass(f'Enter password for {un}@{cs}: ')

with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
    with connection.cursor() as cursor:
        sql = """select sysdate from dual"""
        for r in cursor.execute(sql):
            print(r)

