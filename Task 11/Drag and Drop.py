from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# ActionChains
from selenium.webdriver.common.action_chains import ActionChains

# Python Selenium Exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

# This class holds the data constants, such as the URL to be visited
class Data:
    URL = "https://jqueryui.com/droppable/"

# This class holds the locators for the elements to be interacted with
class Locators:
    SOURCE = "draggable"
    TARGET = "droppable"

# This class combines Data and Locators, performing the drag and drop action using ActionChains
class DragAndDropUsingActionChains(Data, Locators):
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        #ActionChains
        self.actions = ActionChains(self.driver)

    def drag_drop(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.URL)
            sleep(3)

            # Switch to the iframe containing the draggable and droppable elements
            iframe = self.driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
            self.driver.switch_to.frame(iframe)

            # Locate the source and target elements
            source = self.driver.find_element(by=By.ID,value=self.SOURCE)
            target = self.driver.find_element(by=By.ID, value=self.TARGET)

            # Perform drag and drop action
            self.actions.drag_and_drop(source, target).perform()
            sleep(4)
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print(error)
        finally:
            self.driver.quit()

# Create an instance of the class and execute the drag and drop method
if __name__ == "__main__":
    naveen = DragAndDropUsingActionChains()
    naveen.drag_drop()
