import pymysql
 
conn = pymysql.connect(
    host='localhost', 
    user='root', 
    password='python',
    db='python',
    port=3305, 
    charset='utf8')
 
e_id = "3"
e_name = "6"
sex = "6"
addr = "6"

curs = conn.cursor()
sql = f"""
    update emp
    set
        e_name = '{e_name}',
        sex = '{sex}',
        addr = '{addr}'
    where
        e_id = '{e_id}'
"""
print("sql",sql)
curs.execute(sql)

print("cnt", curs.rowcount)
conn.commit() 

curs.close()
conn.close()
