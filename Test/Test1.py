from Pages1.HomePage import Home
from Utility.BrowserDebugger import debug_request
from Pages1.RegistrationPage import Register
from Utility.ReadExcel import readExcel
import json
import allure
@allure.story('Python Test Automation Framework')
@allure.feature('Registration')
@allure.testcase('Registration Test Case')
def test_example(selenium):


    with open('../Data/data.json') as json_file:

        data = json.load(json_file)
        selenium.get('http://demo.guru99.com/test/newtours/')
        #debug_request(selenium)
        selenium.set_page_load_timeout(20)
        m = Home(selenium)
        m.getRegister().click()
        r = Register(selenium)
        r.setFirstName(data['firstname'])
        r.setLastName(data['lastname'])
        r.setPhone(data['mobileno'])
        r.setCountry(data['country'])
        r.setEmail(data['emailid'])
        r.setUserName(data['lastname'])
        r.setPassword(data['password'])
        r.setConfirmPassword(data['password'])
        r.submitRegistration()