"""
Grocery Help v2
"""
import toga
from toga.style import Pack
from toga.style.pack import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class GroceryHelp(toga.App):
    def startup(self):
        filler1 = toga.Label('')
        filler2 = toga.Label('')
        filler3 = toga.Label('')
        filler4 = toga.Label('')
        
        main_box = toga.Box(style=Pack(direction=COLUMN))
        user_box = toga.Box(style=Pack(direction=ROW))
        pass_box = toga.Box(style=Pack(direction=ROW))

        #names
        name_title = toga.Label(
            'Grocery Help',
            style=Pack(padding=(0, 5), text_align=CENTER, font_size=20, color='blue')        )
        name_label = toga.Label(
            'Type in your login credentials for Walmart or Safeway, and then select the store in the dropdown.',
            style=Pack(padding=(0, 5), text_align=CENTER)
        )
        name_label2 = toga.Label(
            'Click the search for slot button if you want to look for a slot, or click the go shopping button to navigate to the store website.',
            style=Pack(padding=(0, 5), text_align=CENTER)
        )
        name_label3 = toga.Label(
            'The app will notify you when there is an available delivery slot.',
            style=Pack(padding=(0, 5), text_align=CENTER)
        )

        name_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        name_box.add(name_label)
        name_box.add(filler2)
        name_box.add(name_label2)
        name_box.add(filler3)
        name_box.add(name_label3)
        name_box.add(filler4)

        user_label = toga.Label(
            'Email:',
            style=Pack(padding_bottom=5, padding_left=5)
        )
        self.user_input = toga.TextInput(style=Pack(padding_left=10,
                                                    padding_right=5,
                                                    padding_bottom=5,
                                                    flex = 1))
        pass_label = toga.Label(
            'Password:',
            style=Pack(padding_top=5, padding_left=5)
        )
        self.pass_input = toga.PasswordInput(style=Pack(padding_left=5,
                                                        padding_right=5,
                                                        padding_top=5,
                                                        flex = 1))
        user_box.add(user_label)
        user_box.add(self.user_input)
        pass_box.add(pass_label)
        pass_box.add(self.pass_input)
        
        button1 = toga.Button(
            'Walmart',
            on_press=self.searchwalmart,
            style=Pack(padding_left=75, padding_right=75,
                       padding_top=10, padding_bottom=10)
        )
        button2 = toga.Button(
            'Safeway',
            on_press=self.searchsafeway,
            style=Pack(padding_left=75, padding_right=75,
                       padding_top=10, padding_bottom=10)
        )

        searchbutton = toga.Button(
            'Search for slot',
            on_press=self.search,
            style=Pack(padding_left=75, padding_right=75,
                       padding_top=10, padding_bottom=10)
        )

        shopbutton = toga.Button(
            'Go shopping!',
            on_press=self.shop,
            style=Pack(padding_left=75, padding_right=75,
                       padding_top=10, padding_bottom=10)
        )

        self.selection = toga.Selection(items=['Select a store!', 'Walmart', 'Safeway'],
                                   style=Pack(padding_left=75, padding_right=75,
                                              padding_top=10, padding_bottom=10))
        
        main_box.add(name_title)
        main_box.add(name_box)
        main_box.add(user_box)
        main_box.add(pass_box)
        main_box.add(self.selection)
        main_box.add(searchbutton)
        main_box.add(shopbutton)

        #display
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def shop(self, widget):
        store = self.selection.value
        if store=='Select a store!':
            self.main_window.info_dialog(
                'Error',
                "Please select a store"
            )
        elif store =='Walmart':
            self.shopwalmart()
        else:
            self.shopsafeway()

    def search(self, widget):
        store = self.selection.value
        if store=='Select a store!':
            self.main_window.info_dialog(
                'Error',
                "Please select a store"
            )
        elif store =='Walmart':
            self.searchwalmart()
        else:
            self.searchsafeway()

    def shopwalmart(self):
        if self.user_input.value and self.pass_input.value:
            name = self.user_input.value
            pwd = self.pass_input.value
        else:
            name = None
            pwd = None
            self.main_window.info_dialog(
                'Error',
                "Please type in your login information"
            )
        if name!=None and pwd !=None: 
            driver = webdriver.Safari()
            driver.get("https://www.walmart.com/account/login?tid=0&vid=2&returnUrl=%2Fbook-slot")
            assert "Login" in driver.title
            elem = driver.find_element_by_name("email")
            elem.send_keys(name)
            elem = driver.find_element_by_name("password")
            elem.send_keys(pwd)
            elem.send_keys(Keys.RETURN)
        
    def shopsafeway(self):
        if self.user_input.value and self.pass_input.value:
            name = self.user_input.value
            pwd = self.pass_input.value
        else:
            name = None
            pwd = None
            self.main_window.info_dialog(
                'Error',
                "Please type in your login information"
            )
        if name!=None and pwd !=None: 
            driver = webdriver.Safari()
            driver.get("https://www.safeway.com/erums/store/prebook")
            time.sleep(5)
            assert "Safeway" in driver.title
            time.sleep(5)
            elem = driver.find_element_by_name("userId")
            elem.send_keys(name)
            elem = driver.find_element_by_name("inputPassword")
            elem.send_keys(pwd)
            elem.send_keys(Keys.RETURN)

    def searchwalmart(self):
        if self.user_input.value and self.pass_input.value:
            name = self.user_input.value
            pwd = self.pass_input.value
        else:
            name = None
            pwd = None
            self.main_window.info_dialog(
                'Error',
                "Please type in your login information"
            )
        if name!=None and pwd !=None: 
            driver = webdriver.Safari()
            driver.get("https://www.walmart.com/account/login?tid=0&vid=2&returnUrl=%2Fbook-slot")
            assert "Login" in driver.title
            elem = driver.find_element_by_name("email")
            elem.send_keys(name)
            elem = driver.find_element_by_name("password")
            elem.send_keys(pwd)
            elem.send_keys(Keys.RETURN)
            content=driver.page_source
            flag = content.find("All times are currently booked.")
            while flag==True:
               print("No slots available, check back later")
               time.sleep(5)
               driver.refresh()
               time.sleep(10)
               flag = content.find("All times are currently booked.")
            print("A slot is available!")
            driver.close()
            self.main_window.info_dialog(
                'A slot is available!',
                "Log on now and start shopping."
            )
        
    def searchsafeway(self):
        if self.user_input.value and self.pass_input.value:
            name = self.user_input.value
            pwd = self.pass_input.value
        else:
            name = None
            pwd = None
            self.main_window.info_dialog(
                'Error',
                "Please type in your login information"
            )
        if name!=None and pwd !=None: 
            driver = webdriver.Safari()
            driver.get("https://www.safeway.com/erums/store/prebook")
            time.sleep(5)
            assert "Safeway" in driver.title
            time.sleep(5)
            elem = driver.find_element_by_name("userId")
            elem.send_keys(name)
            elem = driver.find_element_by_name("inputPassword")
            elem.send_keys(pwd)
            elem.send_keys(Keys.RETURN)
            flag = False
            while flag!=True:
               try: 
                  elem = driver.find_element_by_name("selectedSlot")
                  print("A slot is available!")
                  flag = True
                  driver.close()
                  self.main_window.info_dialog(
                      'A slot is available!',
                      "Log on now and start shopping."
                  )
               except:
                  print("No slots available, check back later")
                  time.sleep(5)
                  driver.refresh()
                  time.sleep(10)
    
def main():
    return GroceryHelp()


