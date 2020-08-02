from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep
from songs import SONGS_LIST


class musicDownloader():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://ytmp3.cc/')

    def download(self, link):
        BASE_URL = 'https://www.youtube.com/watch?v='
        self.link = link

        url_input = self.driver.find_element_by_xpath('//*[@id="input"]')
        url_input.send_keys(BASE_URL + link)

        convert_btn = self.driver.find_element_by_xpath('//*[@id="submit"]')
        convert_btn.click()

        sleep(4)

        download_btn = self.driver.find_element_by_xpath(
            '//*[@id="buttons"]/a[1]')

        while not download_btn:
            sleep(2)

        download_btn.click()

        sleep(3)

        next_btn = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[1]/div[3]/a[3]')
        next_btn.click()

    def close(self):
        self.driver.close()


music = musicDownloader()

for url in SONGS_LIST:
    music.download(url)
