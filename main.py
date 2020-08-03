from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

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
            chrome_options=options,
            executable_path=ChromeDriverManager().install()
        )

        URL = 'https://ytmp3.cc/'
        self.driver.get(URL)

    def download(self, link):
        BASE_URL = 'https://www.youtube.com/watch?v='
        self.link = link

        # send URL to the input
        url_input = self.driver.find_element_by_xpath('//*[@id="input"]')
        url_input.send_keys(BASE_URL + link)

        # click convert button
        convert_btn = self.driver.find_element_by_xpath('//*[@id="submit"]')
        convert_btn.click()

        sleep(4)

        # click download button
        download_btn = self.driver.find_element_by_xpath(
            '//*[@id="buttons"]/a[1]'
        )

        # if download is slower than it should be
        while not download_btn:
            sleep(2)

        download_btn.click()

        sleep(3)

        # go to first tab if it opens a new one
        first_window = self.driver.window_handles[0]
        self.driver.switch_to.window(first_window)

        # click convert next, then restart it all
        next_btn = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[1]/div[3]/a[3]'
        )
        next_btn.click()


music = musicDownloader()

for url in SONGS_LIST:
    try:
        music.download(url)
    except:
        MESSAGE = 'i\'m sorry, an error ocurred...'

        # clear console, so it shows only 1 time
        os.system('cls')
        print(MESSAGE)
#
#
#
