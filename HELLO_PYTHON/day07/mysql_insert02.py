import pymysql
from astropy.io.ascii.latex import AASTex
 
conn = pymysql.connect(
    host='localhost', 
    user='root', 
    password='python',
    db='python',
    port=3305, 
    charset='utf8')

e_id = "5"
e_name = "5"
sex = "5"
addr ="5"
 
curs = conn.cursor()
sql = f"""
    insert into emp
        (e_id, e_name, sex, addr) 
    values
        ('{e_id}','{e_name}','{sex}','{addr}')
"""
cnt = curs.execute(sql)
print("cnt", curs.rowcount)
conn.commit() 

curs.close()
conn.close()
