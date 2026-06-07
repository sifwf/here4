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
        
    def add_games(self,name,price,desc,release,photo):
        self.__cur.execute("INSERT INTO games (name,price,desc,release,photo) VALUES (?,?,?,?,?)",
                           (name,price,desc,release,photo))
        self.__db.commit()
    
    def get_gameid_by_name(self,name):
        self.__cur.execute("SELECT id FROM games WHERE name=? ",(name,))
        res=self.__cur.fetchone()
        if res:
            return res[0]
        else:
            return None
    
    def add_connect(self,user_id,games_id):
        self.__cur.execute("INSERT INTO connect (user_id,games_id) VALUES (?,?)",(user_id,games_id))
        self.__db.commit()

    def get_gamesid_by_userid(self,user_id : int):
        self.__cur.execute("SELECT games_id FROM connect WHERE user_id=?",(user_id,))
        gm=self.__cur.fetchall()
        if gm:
            games_id_list=[]
            for i in gm:
                games_id_list.append(i[0])
            return games_id_list
        else:
            return []
        
    def get_game_by_id(self,id):
        self.__cur.execute("SELECT name,price,desc,release,photo FROM games WHERE id=?",(id,))
        game=self.__cur.fetchone()
        if game:
            return game
        else:
            return []
    
    def get_games(self,gamesid):
        games=[]
        for id in gamesid:
            game=self.get_game_by_id(id)
            games.append(list(game))
        return games
    
    def if_name_in_database(self,name):
        self.__cur.execute("SELECT name FROM games WHERE name=?",(name,))
        game_count=len(self.__cur.fetchall())
        if game_count>0:
            return True
        return False


    
    