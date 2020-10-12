import time
import logging

import pyautogui


def wait_for_color_changed(x, y):
    for _ in range(20):
        logging.info("Position: x=%s, y=%s", x, y)
        im = pyautogui.screenshot()
        r, g, b = im.getpixel((x, y))
        logging.info("r=%s, g=%s, b=%s", r, g, b)
        if is_the_color_available(r, g, b):
            logging.info("The color is available [%s]", (r, g, b))
            break
        time.sleep(0.3)


def is_the_color_available(r, g, b):
    r_th = 203
    g_th = 235
    b_th = 152
    available_th = 3
    if (r_th - r) <= available_th and (g_th - g) <= available_th and (b_th - b) <= available_th:
        return True
    return False


def main():
    while True:
        fish_btn = (1539, 747)
        pyautogui.moveTo(*fish_btn)
        pyautogui.click(*fish_btn)
        wait_for_color_changed(*fish_btn)

        logging.info("Trying to pull fishing rod...")
        pyautogui.click(*fish_btn)
        time.sleep(4)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Stop Fishing")
