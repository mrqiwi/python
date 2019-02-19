#!/usr/bin/python3

import vk_api
import getpass

login = '+79006015544'
password = getpass.getpass()

vk_session = vk_api.VkApi(login, password)
vk_session.auth()

vk = vk_session.get_api()

vk.messages.send(user_id=414623232, message='hi friend', random_id=1111)
# vk.messages.send(user_id=98236022, message='hi friend')