class Flaskdb:
    def __init__(self,db):
        self.__db = db
        self.__cur = db.cursor()

    def get_user_by_name(self,name):
        self.__cur.execute("SELECT * FROM users WHERE name=? ",(name,))
        res=self.__cur.fetchone()
        if res:
            return res
        else:
            return []
        
    def add_user(self,name,password):
        self.__cur.execute("INSERT INTO users (name,password) VALUES (?,?)",(name,password))
        self.__db.commit()

    def check_user(self,name):
        self.__cur.execute("SELECT name FROM users WHERE name=?",(name,))
        res=self.__cur.fetchone()
        if res:
            return False
        return True
    
    def getUserFromDb(self,id):
        self.__cur.execute("SELECT * FROM users WHERE id=? ",(id,))
        res=self.__cur.fetchone()
        if not res:
            return False
        else:
            return res
    
    