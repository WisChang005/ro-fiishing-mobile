import logging

import pyautogui


def get_fishing_button_position():
    position = pyautogui.locateOnScreen("fishing_btn.png")
    if position:
        return get_picture_location(*list(position))
    return None


def wait_fishing_btn_available():
    position = None
    for t in range(2):
        position = pyautogui.locateOnScreen("fishing_available.png")
        if position:
            position = get_picture_location(*list(position))
            break
        logging.info("Wait for fishing available...[%s]", t)
    return position


def position_checker(p):
    if not p:
        raise ValueError("Position not found")
    logging.info("Position: %s found", p)


def get_picture_location(x, y, w, h):
    c_x, c_y = (x + (w/2.0)), (y + h/2.0)
    return c_x, c_y


def main():
    while True:
        fish_btn = get_fishing_button_position()
        if fish_btn:
            pyautogui.moveTo(*fish_btn)
            pyautogui.click(*fish_btn)
        else:
            logging.info("Fishing button not found")
            continue

        fish_ava_p = wait_fishing_btn_available()
        if fish_ava_p:
            logging.info("Real deceted Fishing!!!!!")
            pyautogui.moveTo(*fish_ava_p)
            pyautogui.click(*fish_ava_p)
        else:
            logging.info("Trying to fishing...")
            pyautogui.click(*fish_btn)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Stop Fishing")
