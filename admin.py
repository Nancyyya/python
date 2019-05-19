from user2 import User
class Privileges():
    """特权类"""
    def __init__(self):
        self.privileges=['can add people','can delete people']

    def show_privileges(self):
        """展示特权"""
        print(self.privileges)

class Admin(User):
    """管理员类"""
    def __init__(self,first_name,last_name,**usr_info):
        """初始化"""
        super().__init__(first_name,last_name,**usr_info) ### **user_info???
        self.privileges=Privileges()
