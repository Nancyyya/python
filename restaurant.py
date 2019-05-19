
#9-4
class Restaurant():
    """餐馆类"""
    def __init__(self,restaurant_name,cuisine_type):
        """初始化"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """描述餐馆"""
        print('describe restaurant______')
        print('name: ' + self.restaurant_name.title())
        print('type: ' + self.cuisine_type)

    def open_restaurant(self):
        """餐馆开张"""
        print('Open now!!!')

    def set_number_served(self,people):
        """设置用餐人数"""
        self.number_served = people
        print('number_served '+ str(self.number_served))

    def increment_number_served(self,people):
        """设置增加人数"""
        self.number_served += people
        print('number_served '+ str(self.number_served))
