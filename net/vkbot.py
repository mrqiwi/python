#!/usr/bin/env python3
import os
import vk_api

from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType

def send_msg(event, text, keys=None):
    lsvk.messages.send(
            user_id = event.user_id,
            message = text,
            random_id = get_random_id(),
            keyboard = keys.get_keyboard() if keys else None)

def handle_msg(event):
    if event.text.lower() in ['reset', 'reboot', 'перезагрузка']:
        text = 'rebooting...' if os.system('shutdown -r now') == 0 else 'cannot run the command'
        send_msg(event, text)

    elif event.text.lower() in ['poweroff', 'off', 'выкл', 'выключение']:
        text = 'shutdowing...' if os.system('shutdown -h now') == 0 else 'cannot run the command'
        send_msg(event, text)

    elif event.text.lower() in ['commands', 'cmds', 'команды']:
        send_msg(event, 'your commands', keyboard)

    else:
        send_msg(event, 'unknown command')

def main_loop():
    for event in lslongpoll.listen():
        if event.type != VkEventType.MESSAGE_NEW:
            continue

        if not event.to_me or not event.text or not event.from_user:
            continue

        if event.user_id not in [414623232]:
            continue

        handle_msg(event)

if __name__ == '__main__':
    vk_session = vk_api.VkApi(token=os.getenv('VKTOKEN'))
    lslongpoll = VkLongPoll(vk_session)
    lsvk = vk_session.get_api()

    # keyboard = VkKeyboard(one_time=True)
    keyboard = VkKeyboard()
    keyboard.add_button('reset', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('poweroff', color=VkKeyboardColor.NEGATIVE)

    main_loop()
