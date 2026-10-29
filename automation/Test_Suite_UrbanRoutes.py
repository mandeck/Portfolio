from selenium import webdriver
import Input_data_UrbanRoutes
import helpers_SMS
from POM_UrbanRoutes import UrbanRoutesPage
import time


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        # opening
        cls.driver = webdriver.Chrome()
        # setting routes_page = UrbanRoutesPage class for whole test suite
        cls.routes_page = UrbanRoutesPage(cls.driver)
        if helpers_SMS.is_url_reachable(Input_data_UrbanRoutes.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server.")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running.")

    # Test setting "from" and "to" addresses:
    def test_set_route(self):
        # open / reload webpage
        self.driver.get(Input_data_UrbanRoutes.URBAN_ROUTES_URL)
        # enter from and to address
        self.routes_page.enter_locations(Input_data_UrbanRoutes.ADDRESS_FROM, Input_data_UrbanRoutes.ADDRESS_TO)
        time.sleep(3) # visual confirmation for presentation purposes
        # test / assert from address
        actual_value = self.routes_page.get_from_text()
        expected_value = Input_data_UrbanRoutes.ADDRESS_FROM
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
        # test / assert to address
        actual_value = self.routes_page.get_to_text()
        expected_value = Input_data_UrbanRoutes.ADDRESS_TO
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
        print('function created for set route')

    # Test selecting "Supportive" card
    def test_select_plan(self):
        # open / reload webpage
        self.driver.get(Input_data_UrbanRoutes.URBAN_ROUTES_URL)
        # enter from and to address
        self.routes_page.enter_locations(Input_data_UrbanRoutes.ADDRESS_FROM, Input_data_UrbanRoutes.ADDRESS_TO)
        # click call a taxi
        self.routes_page.click_call_taxi()
        # click the Supportive plan
        self.routes_page.click_supportive_plan()
        time.sleep(3) # visual confirmation
        # test / assert Supportive plan is now active
        actual_value = self.routes_page.get_supportive_card_class()  # actual class attribute s/b "tcard active"
        expected_value = 'active'  # expects the value 'active' somewhere in the class attribute
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
        print('function created for selected plan')

    # Test completing steps to fill out phone number
    def test_fill_phone_number(self):
        # open / reload webpage
        self.driver.get(Input_data_UrbanRoutes.URBAN_ROUTES_URL)
        # enter from and to address
        self.routes_page.enter_locations(Input_data_UrbanRoutes.ADDRESS_FROM, Input_data_UrbanRoutes.ADDRESS_TO)
        # click call a taxi
        self.routes_page.click_call_taxi()
        # click the Supportive plan
        self.routes_page.click_supportive_plan()
        # select phone number field, write in and confirm phone number, write in and confirm SMS
        self.routes_page.click_phone_button()
        time.sleep(1) # visual confirmation for presentation purposes
        self.routes_page.enter_phone_number(Input_data_UrbanRoutes.PHONE_NUMBER)
        time.sleep(1) # visual confirmation for presentation purposes
        self.routes_page.click_next_button()   # Triggers SMS activity in app
        time.sleep(1) # visual confirmation for presentation purposes
        code = helpers_SMS.retrieve_phone_code(self.driver)  # Retrieve SMS code from 'helpers.py'
        time.sleep(1) # visual confirmation for presentation purposes
        self.routes_page.enter_SMS_field(code)
        time.sleep(1) # visual confirmation for presentation purposes
        self.routes_page.click_SMS_confirm()
        time.sleep(3) # visual confirmation for presentation purposes
        # Verify phone number added
        actual_value = self.routes_page.get_confirmed_phone_number() # retrieves added value
        expected_value = Input_data_UrbanRoutes.PHONE_NUMBER  # +1 123 123 12 12
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
        print('function created for filled phone number')

    # Testing completion of credit card details
    def test_fill_credit_card(self):
        # open / reload webpage
        self.driver.get(Input_data_UrbanRoutes.URBAN_ROUTES_URL)
        # enter from and to address
        self.routes_page.enter_locations(Input_data_UrbanRoutes.ADDRESS_FROM, Input_data_UrbanRoutes.ADDRESS_TO)
        # click call a taxi
        self.routes_page.click_call_taxi()
        # click the Supportive plan
        self.routes_page.click_supportive_plan()
        # select payment options
        self.routes_page.click_payment()
        time.sleep(1) # visual confirmation for presentation purposes
        self.routes_page.click_add_card()
        time.sleep(1) # visual confirmation for presentation purposes
        # enter credit card number, CVV
        self.routes_page.enter_card_number(Input_data_UrbanRoutes.CARD_NUMBER)
        time.sleep(1) # visual confirmation for presentation purposes
        self.routes_page.enter_cv_field(Input_data_UrbanRoutes.CARD_CODE)
        time.sleep(1) # visual confirmation for presentation purposes
        # click off, then click link card and close options
        self.routes_page.click_off()
        self.routes_page.link_card()
        self.routes_page.click_close()
        time.sleep(3) # visual confirmation for presentation purposes
        # verify card is added
        actual_value = self.routes_page.get_card_confirmation()
        expected_value = 'Card'
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
        print('function created for filled card')

    # Testing comment field for driver
    def test_comment_for_driver(self):
        # open / reload webpage
        self.driver.get(Input_data_UrbanRoutes.URBAN_ROUTES_URL)
        # enter from and to address
        self.routes_page.enter_locations(Input_data_UrbanRoutes.ADDRESS_FROM, Input_data_UrbanRoutes.ADDRESS_TO)
        # click call a taxi
        self.routes_page.click_call_taxi()
        # click the Supportive plan
        self.routes_page.click_supportive_plan()
        # write in comment for driver
        self.routes_page.enter_driver_comment(Input_data_UrbanRoutes.MESSAGE_FOR_DRIVER)
        time.sleep(3) # visual confirmation for presentation purposes
        # verify comment is written
        actual_value = self.routes_page.get_driver_comment()
        expected_value = Input_data_UrbanRoutes.MESSAGE_FOR_DRIVER
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
        print('function created for comment for driver')

    # Testing slider for ordering blanket and handkerchiefs
    def test_order_blanket_and_handkerchiefs(self):
        # open / reload webpage
        self.driver.get(Input_data_UrbanRoutes.URBAN_ROUTES_URL)
        # enter from and to address
        self.routes_page.enter_locations(Input_data_UrbanRoutes.ADDRESS_FROM, Input_data_UrbanRoutes.ADDRESS_TO)
        # click call a taxi
        self.routes_page.click_call_taxi()
        # click the Supportive plan
        self.routes_page.click_supportive_plan()
        # click slider
        self.routes_page.add_blankets_and_handkerchiefs()
        time.sleep(3) # visual confirmation
        # verify slider is active
        actual_value = self.routes_page.is_switch_checked()
        assert actual_value, f"Expected switch to be checked, but got '{actual_value}'"
        print('function created for ordering a blanket and handkerchiefs')

    # Testing addition of 2 ice creams to the order
    def test_order_2_ice_creams(self):
        # open / reload webpage
        self.driver.get(Input_data_UrbanRoutes.URBAN_ROUTES_URL)
        # enter from and to address
        self.routes_page.enter_locations(Input_data_UrbanRoutes.ADDRESS_FROM, Input_data_UrbanRoutes.ADDRESS_TO)
        # click call a taxi
        self.routes_page.click_call_taxi()
        # click the Supportive plan
        self.routes_page.click_supportive_plan()
        # click '+' twice
        self.routes_page.click_ice_cream_plus_twice()
        time.sleep(3) # visual confirmation
        # verify count
        actual_value = self.routes_page.get_ice_cream_count()
        expected_value = '2'
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
        print('function created for ordering 2 ice creams')

    # Testing the final step of ordering the service.
    def test_car_search_model_appears(self):
        # open / reload webpage
        self.driver.get(Input_data_UrbanRoutes.URBAN_ROUTES_URL)
        # enter from and to address
        self.routes_page.enter_locations(Input_data_UrbanRoutes.ADDRESS_FROM, Input_data_UrbanRoutes.ADDRESS_TO)
        # click call a taxi
        self.routes_page.click_call_taxi()
        # click the Supportive plan
        self.routes_page.click_supportive_plan()
        # enter phone number details
        self.routes_page.click_phone_button()
        time.sleep(1) # visual confirmation
        self.routes_page.enter_phone_number(Input_data_UrbanRoutes.PHONE_NUMBER)
        time.sleep(1) # visual confirmation
        self.routes_page.click_next_button()   # Triggers SMS activity in app
        code = helpers_SMS.retrieve_phone_code(self.driver)  # Retrieve SMS code from 'helpers.py'
        self.routes_page.enter_SMS_field(code)
        time.sleep(1) # visual confirmation
        self.routes_page.click_SMS_confirm()
        time.sleep(1) # visual confirmation
        # write comment for driver
        self.routes_page.enter_driver_comment(Input_data_UrbanRoutes.MESSAGE_FOR_DRIVER)
        time.sleep(1) # visual confirmation
        # click order taxi
        self.routes_page.click_order_taxi()
        time.sleep(3) # visual confirmation
        # verify popup appears
        actual_value = self.routes_page.get_car_search_popup_text()
        expected_value = 'Car search'
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
        print('function created for car search model appearing')

    # Close the browser after all tests are done
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()