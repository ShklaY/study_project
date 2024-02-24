from config import BASE_URL

from interaction_with_web_pages.methods_to_interact_with_pages import MethodsToInteractWithPages
from interaction_with_web_pages.page_objects.menu_bar import MenuBar


class ElementsPage(MethodsToInteractWithPages):
    def __init__(self, driver):
        super().__init__(driver)
        self.menu_bar = MenuBar(self.driver)
        self.url = f'{BASE_URL}/elements'
