from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

from time import sleep
from songs import SONGS_LIST

import os


class musicDownloader():
    def __init__(self):
        options = Options()
        options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 2
        })

        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )

        URL = 'https://tomp3.cc/enyi47a'
        self.driver.get(URL)

    def download(self, link):
        self.driver.execute_script("document.getElementById('k__input').setAttribute('value', '%s')" % link);

        # click convert button
        convert_btn = self.driver.find_element("id", "btn-start")
        convert_btn.click()

        sleep(2)

        # click download button
        download_btn = self.driver.find_element("id", "btn-convert")

        # if download is slower than it should be
        while not download_btn:
            sleep(2)

        download_btn.click()

        convertButton = self.driver.find_element("id", "asuccess")

        sleep(2)

        convertButton.click()

        sleep(1)

        # go to first tab if it opens a new one
        first_window = self.driver.window_handles[0]
        self.driver.switch_to.window(first_window)

        sleep(4)


music = musicDownloader()

for url in SONGS_LIST:
    try:
        BASE_URL = 'https://www.youtube.com/watch?v='
        music.download(BASE_URL + url)
    except Exception as error:
        MESSAGE = 'i\'m sorry, an error ocurred...'

        # clear console, so it shows only 1 time
        os.system('cls')
        print(MESSAGE, error)