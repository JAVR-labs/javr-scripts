import os

import keyboard

keys = []
while not keyboard.is_pressed("end"):
    new_key = {
        "Name": str(keyboard.read_key()).lower(),
        "isPressed": False
    }
    if new_key['Name'] not in map(lambda x: x['Name'], keys):
        keys.append(new_key)

    for key in keys:
        if keyboard.is_pressed(key['Name']) and not key['isPressed']:
            print("Pressed:", key['Name'])
            key['isPressed'] = True
        elif not keyboard.is_pressed(key['Name']) and key['isPressed']:
            print("Released:", key['Name'])
            key['isPressed'] = False
            if not any(map(lambda x: x['isPressed'], keys)):
                print('-------------------')
