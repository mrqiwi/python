#!/usr/bin/python3

import vk_api
import getpass
import time
from vk_api.longpoll import VkLongPoll, VkEventType

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':

    login = '+79006015544'
    password = getpass.getpass()

    cmd_off = ['off', 'poweroff', 'выкл', 'выключить', 'выключение']
    cmd_rb = ['reboot', 'restart', 'перезагрузка', 'перезагрузить', 'перезапустить', 'перезапуск', 'рестарт']

    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()
    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            if event.user_id == 414623232:

                if event.text.lower() in cmd_off:
                    print('выключить')
                elif event.text.lower() in cmd_rb:
                    print('перезагрузить')
                elif is_number(event.text):
                    print('это число')
                else:
                    print('что то другое')

            # random+=1
            # if event.from_user: #Если написали в ЛС
            #     time.sleep(5)
            #     vk.messages.send(user_id=event.user_id, message='hello Mutant', random_id=random)


