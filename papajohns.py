from splinter import Browser
import time



# User Detail Class
class UserDetail:
    first_name=None
    last_name=None
    address=None
    zip=None
    phone_number=None
    email=None
    cc_number=None
    cc_type=None
    cc_exp=None
    cc_sec=None
    twitter=None

    def __init__(self,filename):
        file=open(filename,"r").read()
        self.first_name=file[file.index("<first_name>")+12:file.index("</first_name>")]
        self.last_name=file[file.index("<last_name>")+11:file.index("</last_name>")]
        self.address=file[file.index("<address>")+9:file.index("</address>")]
        self.zip=file[file.index("<zip>")+5:file.index("</zip>")]
        self.phone_number=file[file.index("<phone_number>")+14:file.index("</phone_number>")]
        self.email=file[file.index("<email>")+7:file.index("</email>")]
        self.twitter=file[file.index("<twitter>")+9:file.index("</twitter>")]
    def export(self):
        text=""
        text+="<twitter>"+self.twitter+"</twitter>\n"
        text+="<first_name>"+self.first_name+"</first_name>\n"
        text+="<last_name>"+self.last_name+"</last_name>\n"
        text+="<address>"+self.address+"</address>\n"
        text+="<zip>"+self.zip+"</zip>\n"
        text+="<phone_number>"+self.phone_number+"</phone_number>\n"
        text+="<email>"+self.email+"</email>\n"
        return text
def order(detail,use_card=False):
    # Get phone info
    area_code=detail.phone_number[0:3]
    phone_prefix=detail.phone_number[3:6]
    phone_suffix=detail.phone_number[6:len(detail.phone_number)]

    # Order Pizza
    with Browser() as browser:
        # Find pizza and check out
        url="http://order.papajohns.com/index.html?site=WEB"
        browser.visit(url)
        browser.fill('geoAddress.address1',detail.address)
        browser.fill('geoAddress.zipCode',detail.zip)
        browser.find_by_id('setLocationSubmit').click()
        browser.find_by_name('addBtn')[1].click()
        browser.find_by_id('readyToCheckoutBtn').click()
        browser.visit("https://order.papajohns.com/secure/checkout.html")

        #Make Cheese
        browser.fill('geoAddress.driverInstructions',"PLEASE DO NOT SEND PEPPORONI. CHEESE DID NOT WORK. I AM MUSLIM.")

        #Fill in first and last name
        browser.fill('customer.firstName',detail.first_name)
        browser.fill('customer.lastName',detail.last_name)

        #Fill in Phone number
        browser.fill('customer.phone.phone1',area_code)
        browser.fill('customer.phone.phone2',phone_prefix)
        browser.fill('customer.phone.phone3',phone_suffix)

        #Fill in Email
        browser.fill('customer.email',detail.email)
        browser.fill('customer.confirmationEmail',detail.email)

        #Select Payment Type
        if use_card:
            browser.find_by_id('').click()
        else:
            browser.find_by_id('paymentCash-img').click()

        #Confirm Age over 13
        browser.find_by_id('minAgeConfirmation-img').click()

        #Place Order
        #browser.find_by_id('placeOrderBtn').click()
