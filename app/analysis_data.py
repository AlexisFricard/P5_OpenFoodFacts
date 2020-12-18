""" Analaysis_data file """

from app.constants import value_error_msg, duplicate_msg, space, nb_of_category
from app.mysql_shortcut import (cursor, query_all_id_product_cat,
                                query_all_sub_id_from_sub)


class Analysis_data:

    # TO RETURN IF THE SELECTED PRODUCT IS ALLREADY IN Substitute TABLE
    def checking_duplicate_substitute(self, product_id, list_of_all_id_sub):

        for substituted_id in list_of_all_id_sub:

            sub_id = substituted_id[0]

            if int(product_id) == int(sub_id):
                return True

        else:
            return False

    # METHOD TO CHECK IF USER HAS SELECT RIGHT VALUE
    def checking_right_selection(self):

        user_choice = ""

        while user_choice not in [0, 1, 2]:

            try:

                user_choice = int(input(space * 87))

                if user_choice not in [0, 1, 2]:
                    print(value_error_msg.format(user_choice))

            except ValueError:
                user_choice = ""
                print(value_error_msg.format(user_choice))

        else:
            return user_choice

    # METHOD TO CHECK IF USER HAS SELECT RIGHT CATEGORY
    def checking_right_category(self):

        category_id = ""

        while category_id not in range(0, nb_of_category):

            try:

                category_id = int(input(space * 87))

                if category_id not in range(0, nb_of_category):
                    print(value_error_msg.format(category_id))

            except ValueError:
                category_id = ""
                print(value_error_msg.format(category_id))

        else:
            return category_id

    # METHOD TO CHECK IF USER HAS SELECT RIGHT PRODUCT
    def checking_right_value(self, category_id):

        cursor.execute(query_all_id_product_cat.format(category_id))
        list_of_id_product = cursor.fetchall()

        cursor.execute(query_all_sub_id_from_sub)
        list_of_all_id_substitute = cursor.fetchall()

        checking = False
        while checking is not True:

            try:

                product_id = int(input(space * 87))
                sub_allready_exist = self.checking_duplicate_substitute(
                    product_id, list_of_all_id_substitute)

                if sub_allready_exist is False:

                    for prod_id in list_of_id_product:

                        prod_id = prod_id[0]

                        if product_id != prod_id:
                            pass
                        elif product_id == prod_id:
                            return product_id

                elif sub_allready_exist is True:

                    print(duplicate_msg)
                    return None

                print(value_error_msg.format(product_id))

            except ValueError:
                product_id = ""
                print(value_error_msg.format(product_id))
