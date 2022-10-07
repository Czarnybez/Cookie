from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Engine:

    def __init__(self):
        PATH = "c:\\dev\\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("http://orteil.dashnet.org/experiments/cookie/")
        self.money = 0
        self.upgrades = {}

    def cooki_click(self):
        self.driver.find_element(By.ID,"cookie").click()

    def get_price(self, ids):
        try:
            price = self.driver.find_element(By.XPATH, f'//*[@id="{ids}"]/b').text
            if price == "":
                price = 9000000000000000000
            else:
                price = int(price.split("-")[1].strip().replace(",", ""))
            return price
        except:
            pass


    def get_money(self):
        money = self.driver.find_element(By.ID, 'money').text
        if ',' in money:
            money = int(money.strip().replace(",", ""))
        return int(money)

    def setup(self):

        ids =  self.driver.find_elements(By.CSS_SELECTOR, "#store div")
        for item in ids:
            id = item.get_attribute('id')
            price = int(self.get_price(id))
            self.upgrades[id] = price
        return self.upgrades



    def print(self, ids):
        return self.driver.find_element(By.XPATH, f'//*[@id="{ids}"]/b').text



    def update_price(self, id):

        price = game.get_price(id)
        self.upgrades[id]=price

        return self.upgrades


    def buy_update(self):

        affordable_upgrades = {}
        self.money = self.get_money()

        for id, cost in self.upgrades.items():
            if self.money >= cost:
                affordable_upgrades = id

        try:
            self.driver.find_element(By.XPATH, f'//*[@id="{affordable_upgrades}"]/b' ).click()
            game.update_price(affordable_upgrades)
        except:
            print(self.driver.find_element(By.XPATH, f'//*[@id="{affordable_upgrades}"]/b' ).text)

    def add_time(self):
        pass

timeout = time.time() + 5


game = Engine()
game.setup()


while True:
    game.cooki_click()

    if time.time() > timeout:

        game.buy_update()
        timeout = time.time() + 5


