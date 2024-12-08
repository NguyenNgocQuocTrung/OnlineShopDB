from constants.elements_path import ElementsPath

class Cart:
    def __init__(self, driver):
        self.driver = driver
        self.root = ElementsPath(driver)

    def sleep(self, seconds = 0.1):
        self.root.sleep(seconds)

    def redirect_self(self):
        self.root.click(ElementsPath.NAVIGATION.CART)

    def get_item_name_by_index(self, index=1):
        #default sẽ lấy item đầu tiên
        name = self.root.text(f"{ElementsPath.CART.CART_ITEMS.ITEM.NAME}[{index}]")
        return name
    
    def get_list_of_item_names(self):
        elements = self.root.elements(ElementsPath.CART.CART_ITEMS.ITEM.NAME)
        return [str(element.text).lower() for element in elements]
    
    def int_price(self, text):
        str_price = str(text).lower().split(',')[0].replace('.', '')
        return int(str_price)
    
    def get_discount_after_apply(self, discount="10OFF"):
        self.root.input(ElementsPath.CART.DISCOUNT.DISCOUNT_INPUT, f"{discount}")
        self.root.click(ElementsPath.CART.DISCOUNT.APPLY_BUTTON)
        self.root.sleep(0.5)

        return int(str(self.root.text(ElementsPath.CART.SUMMARY.DISCOUNT)).replace('-', '').replace('%', ''))
