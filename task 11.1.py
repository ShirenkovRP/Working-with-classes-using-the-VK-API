# Вам предстоит решить задачу поиска общих друзей у пользователей VK.
# Ссылка на документацию VK/dev. Токен для запросов:
# 10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c
import requests


class VkUsers:
    url = "https://api.vk.com/method/"

    def __init__(self, token, version, user_ids=None):
        self.user_ids = user_ids
        self.token = token
        self.version = version
        self.params = {
            "user_ids": self.user_ids,
            "access_token": self.token,
            "v": self.version,
            "fields": "domain"
            }
        self.basic_fields = requests.get(self.url + "users.get", self.params).json()["response"][0]
        
    # Список друзей
    def friends_get(self):
        if "deactivated" not in self.basic_fields:
            url_friends_get = self.url + "friends.get"
            friends_params = {"user_id": self.user_ids, "access_token": self.token, "v": self.version}
            friends_get = requests.get(url_friends_get, friends_params).json()["response"]["items"]
            return set(friends_get)
        else:
            return set()

    def __str__(self):
        return "https://vk.com/" + self.basic_fields["domain"]
    
        
# Задача №1
# Пользователя нужно описать с помощью класса и реализовать метод поиска общих друзей, используя API VK.

token = "10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c"

user = VkUsers(token, "5.126")
print(user.basic_fields)
print()

# Задача №2 
# Поиск общих друзей должен происходить с помощью оператора &, т.е. user1 & user2 должен выдать список общих друзей
# пользователей user1 и user2, в этом списке должны быть экземпляры классов.

user1 = user.friends_get()
user2 = VkUsers(token, "5.126", "551843217").friends_get()

# список общих друзей пользователей user1 и user2
list_frends = []
for i in (user1 & user2):
    specimen = VkUsers(token, "5.126", i)
    list_frends.append(specimen)
    
print(list_frends)
print()

# Задача №3
# Вывод print(user) должен выводить ссылку на профиль пользователя в сети VK
print(user)
