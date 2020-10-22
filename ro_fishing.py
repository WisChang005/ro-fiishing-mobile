import time
import logging

import pyautogui


class RoFishing:

    def __init__(self):
        self.color_r_th = None
        self.color_g_th = None
        self.color_b_th = None
        self.fishing_btn = None
        self.avaliable_threshold = 3

    def first_time_manual_fishing(self):
        input("Please move the mouse to the fishing button and press enter...")
        self.fishing_btn = pyautogui.position()
        logging.debug("Get Mouse Position: %s", self.fishing_btn)
        self.click_fishing_button()
        input("Wait and Press enter to fishing...")
        self.color_r_th, self.color_g_th, self.color_b_th = self.get_fishing_button_color()
        logging.info("Remember the color [R=%s, G=%s, B=%s]", self.color_r_th, self.color_g_th, self.color_b_th)
        self.click_fishing_button()

    def click_fishing_button(self):
        pyautogui.moveTo(*self.fishing_btn)
        pyautogui.click(*self.fishing_btn)

    def wait_for_fishing_button_avaliable(self):
        for _ in range(60):
            _r, _g, _b = self.get_fishing_button_color()
            if self._is_the_color_available(_r, _g, _b):
                break
            time.sleep(0.2)

    def get_fishing_button_color(self):
        im = pyautogui.screenshot()
        x, y = self.fishing_btn
        r, g, b = im.getpixel((x, y))
        return r, g, b

    def _is_the_color_available(self, r, g, b):
        if (self.color_r_th - r) <= self.avaliable_threshold \
                and (self.color_g_th - g) <= self.avaliable_threshold \
                and (self.color_b_th - b) <= self.avaliable_threshold:
            return True
        return False


def main():
    rf = RoFishing()
    rf.first_time_manual_fishing()
    time.sleep(4)
    logging.info("Auto Fishing Start...")
    while True:
        rf.click_fishing_button()
        rf.wait_for_fishing_button_avaliable()

        logging.info("Pull fishing rod...")
        rf.click_fishing_button()
        time.sleep(4)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="ro_fishing.log")
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Stop Fishing")
