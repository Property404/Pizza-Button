from splinter import Browser
import time
import sys



# User Detail Class
class UserDetail:
    first_name=None
    last_name=None
    address=None
    zipCode=None
    phone_number=None
    email=None
    tiwtter=None
    cc_number=None
    cc_type=None
    cc_expM=None
    cc_expY=None
    cc_sec=None
    instructions=""

    def __init__(self,filename):
        file=open(filename,"r").read()
        self.first_name=file[file.index("<first_name>")+12:file.index("</first_name>")]
        self.last_name=file[file.index("<last_name>")+11:file.index("</last_name>")]
        self.address=file[file.index("<address>")+9:file.index("</address>")]
        self.zipCode=file[file.index("<zip>")+5:file.index("</zip>")]
        self.phone_number=file[file.index("<phone_number>")+14:file.index("</phone_number>")]
        self.email=file[file.index("<email>")+7:file.index("</email>")]
        self.cc_number=file[file.index("<cc_number>")+11:file.index("</cc_number>")]
        self.cc_type=file[file.index("<cc_type>")+9:file.index("</cc_type>")]
        self.cc_expM=file[file.index("<cc_expM>")+9:file.index("</cc_expM>")]
        self.cc_expY=file[file.index("<cc_expY>")+9:file.index("</cc_expY>")]
        self.cc_sec=file[file.index("<cc_sec>")+8:file.index("</cc_sec>")]
        self.twitter=file[file.index("<twitter>")+9:file.index("</twitter>")]
        self.billing_address=file[file.index("<billing_address>")+17:file.index("</billing_address>")]
        self.billing_zip=file[file.index("<billing_zip>")+13:file.index("</billing_zip>")]
        self.billing_city=file[file.index("<billing_city>")+14:file.index("</billing_city>")]
	self.instructions=file[file.index("<instructions>")+14:file.index("</instructions>")]
    def export(self):
        text=""
        text+="<first_name>"+self.first_name+"</first_name>\n"
        text+="<last_name>"+self.last_name+"</last_name>\n"
        text+="<address>"+self.address+"</address>\n"
        text+="<zip>"+self.zipCode+"</zip>\n"
        text+="<phone_number>"+self.phone_number+"</phone_number>\n"
        text+="<email>"+self.email+"</email>\n"
        text+="<twitter>"+self.twitter+"</twitter>\n"
        text+="<billing_address>"+self.billing_address+"</billing_address>\n"
        text+="<billing_zip>"+self.billing_zip+"</billing_zip>\n"
        text+="<billing_city>"+self.billing_city+"</billing_city>\n"
	text+="<instructions>"+self.instructions+"</instructions>\n"
        #NSA
        text+="<cc_number>"+self.cc_number+"</cc_number>\n"
        text+="<cc_type>"+self.cc_type+"</cc_type>\n"
        text+="<cc_expM>"+self.cc_expM+"</cc_expM>\n"
        text+="<cc_expY>"+self.cc_expY+"</cc_expY>\n"
        text+="<cc_sec>"+self.cc_sec+"</cc_sec>\n"
        return text
def output(text):
    sys.stdout.write(text+" "*10+"\r")
    sys.stdout.flush()
def order(detail,use_card= True):
    output("papajohns.order called")
    # Get phone info
    area_code=detail.phone_number[0:3]
    phone_prefix=detail.phone_number[3:6]
    phone_suffix=detail.phone_number[6:len(detail.phone_number)]

    output("Constructing splinter object")
    # Order Pizza
    with Browser() as browser:
	output("Succesfully constructed splinter object")
        # Find pizza and check out
        url="http://order.papajohns.com/index.html?site=WEB"
        browser.visit(url)
	output("Initiating order")
        browser.fill('geoAddress.address1',detail.address)
        browser.fill('geoAddress.zipCode',detail.zipCode)
        browser.find_by_id('setLocationSubmit').click()
        browser.find_by_name('addBtn')[1].click()
        browser.find_by_id('readyToCheckoutBtn').click()
        browser.visit("http://order.papajohns.com/build/edit/1/0.html")
	for i in range(5):
        	if browser.is_element_present_by_id("topping_35-img",5):
			browser.find_by_id("topping_35-img").click()
			time.sleep(1)
			break
		else:
			print "TOPPING ERROR"
			if i==4:
				print "FATAL TOPPING ERROR"	
				return
        output("Part 1 of order succesfull")
        browser.find_by_id("orderBuilderContinueBtn").click()
        
        browser.visit("https://order.papajohns.com/secure/checkout.html")

        #Make Cheese
        browser.fill('geoAddress.driverInstructions',detail.instructions)

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
        output("Part 2 of order successfull")
      




        
        #Select Payment Type
        if use_card:
	    output("use_card==true")
            #Fill in CC
            #Select credit card as payment methon
            browser.find_by_id("paymentCreditCard-img").click()
            browser.find_by_id("creditCardType-Button").click()

            
            #Select credit card type
            cardTypes = {'Visa': 2, 'MasterCard': 3, 'AmericanExpress': 4, 'Discover': 5}
            cardtype = browser.find_by_xpath('//*[@id="creditCardType-List"]/li['+str(cardTypes[detail.cc_type])+']/div')
            cardtype.click()
            
            #fill in CC number
            browser.fill("paymentSummary.creditCardPayment.cardNumber", detail.cc_number)
            #fill in CC expiration month
            month = str(int(detail.cc_expM) + 1)
            browser.find_by_id("ccExpDateMonth-Button").click()
            expMon = browser.find_by_xpath('//*[@id="ccExpDateMonth-List"]/li['+month+']/div')
            expMon.click()
            #fill in CC expiration year
            year = str(int(detail.cc_expY) - 2013)
            if(year <= 1):
                exit();
            browser.find_by_id("ccExpDateYear-Button").click()
            expYear = browser.find_by_xpath('//*[@id="ccExpDateYear-List"]/li['+year+']/div')
            expYear.click()
            #fill in CC name
            browser.fill("paymentSummary.creditCardPayment.nameOnCard", detail.first_name + " " + detail.last_name)
            #fill in CVV
            browser.fill("paymentSummary.creditCardPayment.cvv", detail.cc_sec)
            browser.find_by_id("differentAddress-img").click()
            browser.fill("paymentSummary.creditCardPayment.billingAddress.address1", detail.billing_address)
            browser.fill("paymentSummary.creditCardPayment.billingAddress.city", detail.billing_city)
            browser.fill("paymentSummary.creditCardPayment.billingAddress.postalCode", detail.billing_zip)
            browser.fill("paymentSummary.creditCardPayment.billingAddress.phoneNumber.phone1", area_code)
            browser.fill("paymentSummary.creditCardPayment.billingAddress.phoneNumber.phone2", phone_prefix)
            browser.fill("paymentSummary.creditCardPayment.billingAddress.phoneNumber.phone3", phone_suffix)
        else:
            browser.find_by_id('paymentCash-img').click()
        output("Finished payment")
        #Confirm Age over 13
        browser.find_by_id('minAgeConfirmation-img').click()
	output("Placing order")
        #Place Order
        #browser.find_by_id('placeOrderBtn').click()
        time.sleep(10)
	output("Order placed")
