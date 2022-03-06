from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep
import os


class WhatsAppSender:
    def __init__(self):
        os.environ["WDM_LOG_LEVEL"] = "0"

        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("--profile-directory=Default")
        options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def send_message(self, number, message):
        url = f'https://web.whatsapp.com/send?phone={number}&text={message}'
        self.driver.get(url)
        try:
            button = WebDriverWait(self.driver, 15).until(condition.element_to_be_clickable((
                By.XPATH, "//button[@class='_4sWnG']"
            )))
            sleep(1)
            button.click()
            print(f'{number} - Message has sent')

        except Exception as err:
            print(f'{number} - Sending error. '
                  f'No connection to the Internet or the number is not valid')

            input("Make sure that the device and computer are"
                  "connected to the Internet and press Enter...")

    def worker(self, number_list, message, timeout=3):
        self.driver.get('https://web.whatsapp.com')
        input("After authorizing on WhatsApp press Enter...")
        for number in number_list:
            if len(number) > 8:
                print(f"{number} - Start sending")
                self.send_message(number, message)
                sleep(timeout)

        self.driver.close()


if __name__ == "__main__":

    nums = ['+380670000000', ]
    msg = 'test'

    whatsapp = WhatsAppSender()
    whatsapp.worker(nums, msg)




