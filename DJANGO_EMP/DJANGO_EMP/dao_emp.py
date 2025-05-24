import pymysql

class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost', 
            user='root', 
            password='python',
            db='python',
            port=3305, 
            charset='utf8')
 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def selectList(self):
        sql = "select * from emp"
        self.curs.execute(sql)
 
        list = self.curs.fetchall()
        return list
    
    def selectOne(self,e_id):
        sql = f"""
            select 
                e_id,e_name,sex,addr
            from 
                emp 
            where 
            e_id = '{e_id}'
        """
        self.curs.execute(sql)
        
        obj = self.curs.fetchall()
        return obj[0]
    
    def insert(self,e_id,e_name,sex,addr):
        sql = f"""
            insert into emp
                (e_id,e_name,sex,addr)
            value 
                ('{e_id}','{e_name}','{sex}','{addr}')
        """
        self.curs.execute(sql)
        cnt = self.curs.rowcount
        self.conn.commit()
        
        return cnt
    
    def update(self,e_id,e_name,sex,addr):
        sql = f"""
            update emp
            set 
                e_name = '{e_name}',
                sex = '{sex}',
                addr = '{addr}'
            where
                e_id = '{e_id}'
        """
        self.curs.execute(sql)
        cnt = self.curs.rowcount
        self.conn.commit()
        
        return cnt
    
    def delete(self,e_id):
        sql = f"""
            delete from emp
            where
                e_id = '{e_id}'
        """
        self.curs.execute(sql)
        cnt = self.curs.rowcount
        self.conn.commit()
        
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoEmp()
    list = de.selectList()
    print("list",list)
    
    # obj = de.selectOne("1")
    # print("obj", obj)
    
    # cnt = de.insert("6", "6", "6", "6")
    # print("cnt", cnt)
    
    # cnt = de.update("6", "7", "7", "7")
    # print("cnt", cnt)
    
    # cnt = de.delete("6")
    # print("cnt", cnt)
    
