# Our POM file

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Defining the page class, locators and method in the class
class UrbanRoutesPage:
    # Locators as class attributes

    # Address locators:
    FROM_LOCATOR = (By.ID, 'from')  # from field is located by element ID = 'from' -> <input id="from" class="input" type="text" placeholder="East 2nd Street, 601" value="">
    TO_LOCATOR = (By.ID, 'to')   # to field is located by element ID = 'to' -> <input id="to" class="input" type="text" placeholder="1300 1st St" value="">
    CALL_TAXI_LOCATOR = (By.XPATH, "//button[text()='Call a taxi']") # <button type="button" class="button round">Call a taxi</button>
    SUPPORTIVE_CARD_LOCATOR = (By.XPATH, "//div[contains(@class,'tcard')][.//div[text()='Supportive']]")  # <div class="tcard active"><div class="tcard-title">Supportive</div>
    # Phone number locators:
    PHONE_BUTTON = (By.CSS_SELECTOR, "div.np-text")  # phone button -> <div class="np-text">Phone number</div>
    PHONE_FIELD = (By.ID, "phone")  # Phone number field -> <input id="phone" class="input" type="text" name="phone" placeholder="+1 ххх ххх хх хх" value="">
    NEXT_BUTTON = (By.XPATH, "//button[text()='Next']") # Next button -> <button type="submit" class="button full">Next</button>
    SMS_FIELD = (By.CSS_SELECTOR, "input.input#code") # SMS code field -> <input id="code" class="input" type="text" placeholder="xxxx" value="">
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Confirm']") # Confirm button -> <button type="submit" class="button full">Confirm</button>
    # Test credit card add locators:
    CLICK_PAYMENT_METHOD = (By.CSS_SELECTOR, "div.pp-value-text") # Payment method button with 'Cash' text -> <div class="pp-value-text">Cash</div>
    ADD_CARD = (By.XPATH, "//div[text()='Add card']") # Add a Card button -> <div class="pp-title">Add card</div>
    CARD_FIELD = (By.ID, "number") # Card number field -> <input type="text" id="number" name="number" placeholder="1234 0000 4321" class="card-input" value="">
    CV_FIELD = (By.CSS_SELECTOR, "input.card-input#code")  # CV code field -> <input type="text" id="code" name="code" placeholder="12" class="card-input" value="">
    REMOVE_FOCUS = (By.XPATH, "//div[text()='Adding a card']")  # Remove focus by clicking unreactive element -> <div class="head">Adding a card</div>
    CLICK_LINK_CARD = (By.XPATH, "//button[text()='Link']")  # Click 'Link' -> <button type="submit" class="button full">Link</button>
    CLICK_CLOSE_LOCATOR = (By.CSS_SELECTOR, "button.close-button.section-close")  # Click 'x' -> <div class="section active"><button class="close-button section-close"></button>
    #Test driver comment:
    COMMENT_FIELD_LOCATOR = (By.ID, "comment") # Comment field -> <input id="comment" class="input" type="text" name="comment" placeholder="Get some whiskey" value="">
    #Test order blankets + handkerchiefs
    BLANKET_SLIDER = (By.CSS_SELECTOR, "div.switch span.slider") # Slider element -> <div class="switch"><input type="checkbox" class="switch-input"><span class="slider round"></span></div> - avoid using "slider round"
    BLANKET_CHECKBOX_LOCATOR =  (By.CSS_SELECTOR, "div.switch input.switch-input") # Verifying checked or unchecked -> element <input type="checkbox" class="switch-input"> -> something to do with its properties tab and 'checked:true' or 'checked:false'
    #Test order 2 ice creams
    ICE_CREAM_PLUS_LOCATOR = (By.CSS_SELECTOR, "div.counter-plus")   # Clicking + sign -> <div class="counter-plus">+</div>
    ICE_CREAM_COUNT_LOCATOR = (By.CSS_SELECTOR, "div.counter-value")   # Verifying number -> <div class="counter-value">2</div>
    #Test driver search popup
    ORDER_TAXI_BUTTON = (By.XPATH, "//span[text()='Order']")  # Click order taxi button -> <span class="smart-button-main">Order</span>
    CAR_SEARCH_POPUP = (By.XPATH, "//div[text()='Car search']")  # Verifying popup -> <div class="order-header-title">Car search</div>


    def __init__(self, driver):
        self.driver = driver  # Initialize the driver
        self.wait = WebDriverWait(self.driver, 10)

    #Test address fields
    def enter_from_location(self, from_text):
        # Enter From
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)
    def enter_to_location(self, to_text):
        # Enter To
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)
    def enter_locations(self, from_text, to_text):
        # combine from and to locations
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
    def get_from_text(self):
        # retrieve text in from address field
        return self.driver.find_element(*self.FROM_LOCATOR).get_attribute('value')

    #Select supportive card
    def click_call_taxi(self):
        # wait until element is clickable, then click call taxi
        button = self.wait.until(EC.element_to_be_clickable(self.CALL_TAXI_LOCATOR))
        button.click()
    def get_to_text(self):
        # retrieve text in to address field
        return self.driver.find_element(*self.TO_LOCATOR).get_attribute('value')
    def click_supportive_plan(self):
        # click supportive option
        self.driver.find_element(*self.SUPPORTIVE_CARD_LOCATOR).click()
    def get_supportive_card_class(self):
        # same locator, used AFTER the click, but reading state back
        return self.driver.find_element(*self.SUPPORTIVE_CARD_LOCATOR).get_attribute('class')

    #Add Phone Number methods
    def click_phone_button(self):
        # click button to begin phone number add process
        self.driver.find_element(*self.PHONE_BUTTON).click()
    def enter_phone_number(self, phone_number):
        # enter phone number in field
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone_number)
    def click_next_button(self):
        # submit phone number
        self.driver.find_element(*self.NEXT_BUTTON).click()
    def enter_SMS_field(self, sms_text):
        # enter SMS confirmation code into field
        self.driver.find_element(*self.SMS_FIELD).send_keys(sms_text)
    def click_SMS_confirm(self):
        # submit confirmation code
        self.driver.find_element(*self.CONFIRM_BUTTON).click()
    def get_confirmed_phone_number(self):
        # retrieve submitted phone number located on initial button
        return self.driver.find_element(*self.PHONE_BUTTON).text

    #Add Credit Card methods
    def click_payment(self):
        self.driver.find_element(*self.CLICK_PAYMENT_METHOD).click()
    def click_add_card(self):
        self.driver.find_element(*self.ADD_CARD).click()
    def enter_card_number(self, card_number):
        self.driver.find_element(*self.CARD_FIELD).send_keys(card_number)
    def enter_cv_field(self, cv):
        self.driver.find_element(*self.CV_FIELD).send_keys(cv)
    def click_off(self):
        self.driver.find_element(*self.REMOVE_FOCUS).click()
    def link_card(self):
        self.driver.find_element(*self.CLICK_LINK_CARD).click()
    def click_close(self):
        # Method for closing the payment method pop-up:
        # Finds ALL elements matching CLICK_CLOSE_LOCATOR and stores them as a list in 'buttons'
        # (there are 4 matching elements on the page — one per section, most hidden).
        buttons = self.driver.find_elements(*self.CLICK_CLOSE_LOCATOR)
        # Loops through the list of elements to find which ONE is currently visible/displayed.
        for button in buttons:
            if button.is_displayed():  # checks if THIS specific element is visible right now
                button.click()  # clicks that element
                break  # stops the for loop immediately once a visible element is clicked

        # NOTE: this pattern (find_elements + is_displayed loop) was needed because
        # find_element (singular) kept grabbing a hidden/wrong close button, causing
        # ElementNotInteractableException — multiple sections share this same button
        # structure, but only one is visible at a time.
    def get_card_confirmation(self):
        return self.driver.find_element(*self.CLICK_PAYMENT_METHOD).text

    #Comment for Driver Field
    def enter_driver_comment(self, comment):
        self.driver.find_element(*self.COMMENT_FIELD_LOCATOR).send_keys(comment)
    def get_driver_comment(self):
        # retrieve comment in from comment field
        return self.driver.find_element(*self.COMMENT_FIELD_LOCATOR).get_attribute('value')

    #Add blankets and handkerchiefs
    def add_blankets_and_handkerchiefs(self):
        if not self.is_switch_checked():   # Verifies slider is not already active before clicking
            checkbox_container = self.driver.find_element(*self.BLANKET_SLIDER)
            checkbox_container.click()
    def is_switch_checked(self):
        checkbox = self.driver.find_element(*self.BLANKET_CHECKBOX_LOCATOR)
        return checkbox.is_selected()  #returns current Boolean indicator

    #Add 2 ice creams
    def click_ice_cream_plus_twice(self):
        button = self.wait.until(EC.element_to_be_clickable(self.ICE_CREAM_PLUS_LOCATOR)) # Allows the for loop in test program to run properly
        for i in range(2):  # iterate twice
            button.click()
    def get_ice_cream_count(self):
        return self.driver.find_element(*self.ICE_CREAM_COUNT_LOCATOR).text

    #Complete taxi order and confirm search box
    def click_order_taxi(self):
        button = self.wait.until(EC.element_to_be_clickable(self.ORDER_TAXI_BUTTON))
        button.click()
    def get_car_search_popup_text(self):
        element = self.wait.until(EC.visibility_of_element_located(self.CAR_SEARCH_POPUP))
        return element.text

