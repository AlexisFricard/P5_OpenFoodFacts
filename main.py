""" main file """

import random

from app.display import (display_menu, display_category,
                         display_products_from_category,
                         display_substitution, display_substitutes,
                         display_save_msg, display_del_msg)

from app.analysis_data import (checking_right_selection,
                               checking_right_category,
                               checking_right_value,
                               checking_save_option,
                               checking_delete_option)

from app.constants import LIST_OF_NUTRISCORE, no_substitute_msg


from app.mysql_shortcut import (query_best_nutr_from_prod,
                                query_nutr_where_prod_id,
                                cursor)


def main_loop():

    # MAIN LOOP
    category_id = int()
    menu_loop = True

    while menu_loop is True:

        display_menu()
        user_choice = checking_right_selection()
        # CHECKING ACTION
        if user_choice == 0:
            return

        if user_choice == 1:

            selections_loop = False

            while selections_loop is not True:

                display_category()
                category_id = checking_right_category()
                # CHECKING CATEGORY
                if category_id == 0:
                    selections_loop = True

                else:
                    display_products_from_category(category_id)
                    product_id = checking_right_value(category_id)
                    # CHECKING PRODUCT SELECTION
                    if product_id is not None:

                        substitute_id = find_substitute(
                            product_id, category_id)

                        if substitute_id is not False:
                            display_substitution(product_id,
                                                 substitute_id)
                            display_save_msg()
                            checking_save_option(substitute_id, product_id)

                    selections_loop = True

        if user_choice == 2:

            display_substitutes()
            user_choice = None

        if user_choice == 3:

            display_del_msg()
            checking_delete_option()


def find_substitute(selected_id_product, selected_id_cat):

    cursor.execute(query_nutr_where_prod_id.format(selected_id_product))

    for nutr_selected_prod in cursor:
        nutr_selected_prod = nutr_selected_prod[0]

    for nutr in LIST_OF_NUTRISCORE:

        best_product_id = []

        cursor.execute(query_best_nutr_from_prod.format(
            nutr, selected_id_cat))

        for id, nutriscore in cursor:

            if nutriscore == nutr_selected_prod:
                print(no_substitute_msg.format(nutriscore))
                return False

            elif nutriscore != nutr_selected_prod:
                best_product_id.append(id)
                pass

        if best_product_id:
            return random.choice(best_product_id)


if __name__ == "__main__":

    main_loop()
