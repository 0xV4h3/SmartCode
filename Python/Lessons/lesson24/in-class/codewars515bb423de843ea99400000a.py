# PaginationHelper
# https://www.codewars.com/kata/515bb423de843ea99400000a

from math import ceil

class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items = len(collection)
        self.page_size = items_per_page
        self.pages = ceil(self.items / self.page_size)

    def item_count(self):
        return self.items

    def page_count(self):
        return self.pages

    def page_item_count(self, page_index):
        if page_index < 0 or page_index >= self.page_count():
            return -1
        elif page_index == self.page_count() - 1:
            return self.item_count() % self.page_size or self.page_size
        return self.page_size

    def page_index(self, item_index):
        if item_index < 0 or item_index >= self.item_count():
            return -1
        return item_index // self.page_size