#######################
### Category Object ###
#######################

from mysql_shortcut import (cnx, cursor, add_category,
                            query_cat_id, update_category_id)


class Category:

    def __init__(self):

        self.id = 0
        self.name = ""

    def add(self, category_name):

        c_data = (self.id, category_name)

        cursor.execute(add_category, c_data)
        cnx.commit()

    def update(self, category_name):

        request = (query_cat_id.format(category_name))
        cursor.execute(request)

        cat_id = cursor.fetchone()

        cursor.execute(update_category_id, cat_id)
        cnx.commit()
