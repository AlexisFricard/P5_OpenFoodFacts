from MySql_ShortCut import cnx, cursor, add_product


class Product:
    """ Describes MacGyver"""

    def __init__(self):

        self.id = 0
        self.name = ""
        self.nutriscore = ""
        self.stores = ""
        self.url = ""

    def add(self, product_name, nutriscore, stores, product_url):

        self.name = product_name
        self.nutriscore = nutriscore
        self.stores = stores
        self.url = product_url

        p_data = (self.name, self.nutriscore, self.stores, self.url)

        cursor.execute(add_product, p_data)
        cnx.commit()
