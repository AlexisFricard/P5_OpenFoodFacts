""" Analaysis_data file """

from app.constants import (value_error_msg, duplicate_msg, space, barre,
                           data_saved, nb_of_category, letter_or_symb_msg,
                           sub_tab_erased)

from app.mysql_shortcut import (cnx, cursor,
                                del_sub_tab, fill_sub_table,
                                query_all_sub_id_from_sub,
                                query_prod_id_where_cat_id)


# FONCTION TO CHECK IF USER HAS SELECT A RIGHT VALUE
def checking_right_selection():

    user_choice = ""

    while user_choice not in [0, 1, 2, 3]:

        try:

            user_choice = int(input(space * 87))

            if user_choice not in [0, 1, 2, 3]:
                print(value_error_msg.format(user_choice))

        except ValueError:
            print(value_error_msg.format(letter_or_symb_msg))

    else:
        return user_choice


# FONCTION TO CHECK IF USER HAS SELECT A RIGHT CATEGORY
def checking_right_category():

    category_id = ""

    while category_id not in range(0, nb_of_category):

        try:

            category_id = int(input(space * 87))

            if category_id not in range(0, nb_of_category):
                print(value_error_msg.format(category_id))

        except ValueError:
            print(value_error_msg.format(letter_or_symb_msg))

    else:
        return category_id


# FONCTION TO CHECK IF USER HAS SELECT A "VALID" PRODUCT
def checking_right_value(category_id):

    cursor.execute(query_prod_id_where_cat_id.format(category_id))
    list_of_id_product = cursor.fetchall()

    cursor.execute(query_all_sub_id_from_sub)
    list_of_all_id_substitute = cursor.fetchall()

    checking = False
    while checking is not True:

        try:

            product_id = int(input(space * 87))
            if product_id != 0:
                sub_allready_exist = checking_duplicate_substitute(
                    product_id, list_of_all_id_substitute)

                if sub_allready_exist is False:

                    for prod_id in list_of_id_product:

                        prod_id = prod_id[0]

                        if product_id != prod_id:
                            pass
                        elif product_id == prod_id:
                            return product_id

                elif sub_allready_exist is True:
                    product_id = 0
                    print(barre)
                    print(duplicate_msg)
            if product_id == 0:
                return None

            print(value_error_msg.format(product_id))

        except ValueError:
            print(value_error_msg.format(letter_or_symb_msg))


# FONCTION TO CHECK IF USER'S PRODUCT IS NOT ALLREADY IN SUBSITUTE TABLE
def checking_duplicate_substitute(product_id, list_of_all_id_sub):

    for substituted_id in list_of_all_id_sub:

        sub_id = substituted_id[0]

        if int(product_id) == int(sub_id):
            return True

    else:
        return False


# FONCTION TO SAVE SUBSTITUTION
def checking_save_option(substitute_id, product_id):

    save_choice = ""
    while save_choice not in [0, 1]:

        try:

            save_choice = int(input(space * 87))

            if save_choice == 1:

                substitute_data = [substitute_id, product_id]

                cursor.execute(fill_sub_table, substitute_data)

                cnx.commit()
                print(barre, data_saved)

            elif save_choice == 0:
                return

            else:
                print(value_error_msg.format(save_choice))

        except ValueError:
            print(value_error_msg.format(letter_or_symb_msg))


# FUNCTION TO CHECK WHICH DELETION OPTION THE USER HAS SELECTED
def checking_delete_option():

    del_option = ""
    while del_option not in [0, 1]:

        try:

            del_option = int(input(space * 87))

            if del_option == 0:
                return

            elif del_option == 1:
                cursor.execute(del_sub_tab)
                cnx.commit()
                print(barre)
                print(sub_tab_erased)

        except ValueError:
            print(value_error_msg.format(letter_or_symb_msg))
