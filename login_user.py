class LoginUser:
    def create(self, user):
        self.__user = user
        return self
    def getUserFromDb(self, id, db):
        self.__user = db.getUserFromDb(id)
        return self if self.__user else None
    def is_authenticated(self):
        return True
    def is_anonymous(self):
        return False
    def is_active(self):
        return True
    def get_id(self):
        return str(self.__user["id"])