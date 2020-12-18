class Product:
    def __int__(self, date, price, desc, link):
        self.date = date
        self.price = price
        self.desc = desc
        self.link = link

    def print(self):
        print("Date Posted: %s // Description: %s // Price: %s" % (self.date, self.desc, self.price))
