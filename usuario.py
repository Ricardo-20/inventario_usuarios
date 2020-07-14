class Usuario:
    __contador_usuario=0
    def __init__(self,username,password):
        Usuario.__contador_usuario+=1
        self.__id_usuario=Usuario.__contador_usuario
        self.__username=username
        self.__password=password
    def get_id_usuario(self):
        return self.__id_usuario
    def get_username(self):
        return self.__username
    def set_username(self, username):
        self.__username=username
    def get_password(self):
        return self.__password
    def set_password(self, password):
        self.__password=password
    def __str__(self):
        return "ID_usuario: {0}| user: {1}| password: {2}".format(self.__id_usuario, self.__username,self.__password)
if __name__=='__main__':
    user1=Usuario('richi','12345')
    print(user1)
    user2=Usuario('ringo','54321')
    print(user2)