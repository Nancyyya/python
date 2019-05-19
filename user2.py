#9-5
class User():
    """用户定义"""
    def __init__(self,first_name,last_name,**usr_info):
        """初始化"""
        self.first_name = first_name
        self.last_name = last_name
        self.usr_info = usr_info
        self.login_attempts = 0

    def describe_user(self):
        """描述用户"""
        print('describe user-------')
        print('first_name: ' + self.first_name.title())
        print('last_name: ' + self.last_name.title())
        for key,val in self.usr_info.items():
            print(key+': '+ val)

    def greet_user(self):
        """问候"""
        print('Hello, ' + self.first_name.title() + ' ' + self.last_name.title())

    def increment_login_attempts(self):
        """自增"""
        self.login_attempts+=1

    def reset_login_attempts(self):
        """reset"""
        self.login_attempts=0
