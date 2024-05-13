class UserAuthentication:
    def login(self, username, password):
        print("User logged in")

    def logout(self):
        print("User logged out")


class PaymentProcessing:
    def process_payment(self, payment_method):
        print("Payment processed")


class InventoryManagement:
    def update_inventory(self, product_id, quantity):
        print("Inventory updated")


class OrderFulfillment:
    def fulfill_order(self, order_id):
        print("Order fulfilled")


class ECommerceFacade():
    def __init__(self,userAuthentication,paymentProcessing,inventoryManagment,orderFulfillment):
        self.userAuthentication=userAuthentication
        self.paymentProcessing=paymentProcessing
        self.inventoryManagment=inventoryManagment
        self.orderFulfillment=orderFulfillment

    def purchase_product(self,username,password,payment_method,product_id,quantity):
        self.userAuthentication.login(username,password)
        self.paymentProcessing.process_payment(payment_method)
        self.inventoryManagment.update_inventory(product_id,quantity)
        self.orderFulfillment.fulfil_order(product_id)
        self.userAuthentication.logout()



# https://medium.com/hprog99/mastering-the-facade-design-pattern-in-java-a-comprehensive-guide-with-practical-examples-f3a19f58440e