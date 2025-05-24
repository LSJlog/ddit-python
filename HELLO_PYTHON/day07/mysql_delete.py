import pymysql
 
conn = pymysql.connect(
    host='localhost', 
    user='root', 
    password='python',
    db='python',
    port=3305, 
    charset='utf8')
 
e_id = "3"

curs = conn.cursor()
sql = f"""
    delete from emp
    where
        e_id = '{e_id}'
"""
print("sql",sql)
curs.execute(sql)

print("cnt", curs.rowcount)
conn.commit() 

curs.close()
conn.close()
