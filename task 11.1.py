# Вам предстоит решить задачу поиска общих друзей у пользователей VK.
# Ссылка на документацию VK/dev. Токен для запросов:
# 10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c
import requests


class User:
    url = "https://api.vk.com/method/"

    def __init__(self, userid, token_user, version_user):
        self.user_ids = userid
        self.token = token_user
        self.version = version_user
        self.params = {
            "user_ids": self.user_ids,
            "access_token": self.token,
            "v": self.version,
            "fields": "domain"
            }
        self.basic_fields = requests.get(self.url + "users.get", self.params).json()
        self.friends = requests.get(self.url + "friends.get", {
            "user_id": self.user_ids,
            "access_token": self.token,
            "v": self.version
            }).json()

    def __and__(self, otheruser):
        self.mutaluserlist = []
        for i in self.friends["response"]["items"]:
            if i in otheruser.friends["response"]["items"]:
                self.mutaluserlist.append(User(i, self.token, self.token))
        return self.mutaluserlist
        
    def __str__(self):
        return "https://vk.com/" + self.basic_fields["response"][0]["domain"]
    
        
# Задача №1
# Пользователя нужно описать с помощью класса и реализовать метод поиска общих друзей, используя API VK.

token = "10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c"
version = "5.126"

userid_1 = None  # 552934290 # 'count': 16
userid_2 = "551843217"  # 171691064

user_1 = User(userid_1, token, version)
user_2 = User(userid_2, token, version)

# Задача №2 
# Поиск общих друзей должен происходить с помощью оператора &, т.е. user1 & user2 должен выдать список общих друзей
# пользователей user1 и user2, в этом списке должны быть экземпляры классов.

mutaluserlist = user_1 & user_2
print(mutaluserlist)


# Задача №3
# Вывод print(user) должен выводить ссылку на профиль пользователя в сети VK
print(user_1)  
