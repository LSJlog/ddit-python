import pymysql
 
conn = pymysql.connect(
    host='localhost', 
    user='root', 
    password='python',
    db='python',
    port=3305, 
    charset='utf8')
 
curs = conn.cursor()
sql = """
    insert into emp
        (e_id, e_name, sex, addr) 
    values
        (%s, %s, %s, %s)"
"""
curs.execute(sql, ('3', '3', '3', '3'))
conn.commit() 

curs.close()
conn.close()
