from constants.elements_path import ElementsPath

class Shop:
    def __init__(self, driver):
        self.driver = driver
        self.root = ElementsPath(driver)

    def sleep(self, seconds = 0.1):
        self.root.sleep(seconds)

    def redirect_self(self):
        self.root.click(ElementsPath.NAVIGATION.SHOP)

    def get_text(self, element_path):
        return self.root.text(element_path)

    # == SHOP ==
    def click_item(self, item_no = 1):
        self.root.click_from_elements(ElementsPath.SHOP.ITEMS.ITEMS_PATH, item_no)
        self.root.sleep(0.8)
    
    def click_next_pages(self, pages = 1):
        for i in range(pages):
            self.root.click(ElementsPath.SHOP.BUTTONS.NEXT_BUTTON)
            self.root.sleep(0.2)


    # == Giày ==
    def get_item_name(self):
        name = self.root.text(ElementsPath.SHOP.ITEMS.ITEM.NAME)
        return name

    def get_no_available_sizes(self):
        no_sizes = len(self.root.elements(ElementsPath.SHOP.ITEMS.ITEM.SIZES.SIZES))
        return no_sizes
    
    def get_size_by_option_index(self, index):
        self.root.select_by_index(ElementsPath.SHOP.ITEMS.ITEM.SIZES_SELECTOR, index)

    def add_item(self):
        self.root.click(ElementsPath.SHOP.ITEMS.ITEM.ADD_TO_BASKET)


    # == Mini cart ==
    def get_mini_cart_no_item(self):
        return self.root.text(ElementsPath.MINI_CART.NO_ITEM)