##################################
###    Substitute_food file    ###
### Main methods:              ###
### 1 - main_loop (selections) ###
### 2 - find_substitute        ###
### 3 - save_change (options)  ###
##################################
import random

import app.analysis_data as ad


from app.constants import (back_to_menu_msg, space, LIST_OF_NUTRISCORE,
                           barre, data_saved, no_substitute_msg)


from app.mysql_shortcut import (cursor, cnx, query_nutr_from_product_id,
                                query_better_nutr_from_prod, fill_sub_table)


from app.display import (display_menu, display_category,
                         display_product_from_category,
                         display_substitute_proposition,
                         display_substitute_tab, display_save_msg)


def main_loop():

    ### MAIN LOOP ###
    analysis = ad.Analysis_data()
    category_id = int()
    menu_loop = True

    while menu_loop is True:

        display_menu()
        user_choice = analysis.checking_right_selection()
        ### CHECKING ACTION ###
        ### IF 0, CLOSE APP ###
        if user_choice == 0:
            return
        ### IF 1, OFFER TO USER CATEGORYS SELECTION ###
        if user_choice == 1:

            selections_loop = False
            ### WHILE SELECTION IS NOT GOOD ###
            while selections_loop is not True:

                display_category()
                category_id = analysis.checking_right_category()
                ### CATEGORY CHECKING ###
                if category_id == 0:
                    selections_loop = True

                else:
                    display_product_from_category(category_id)
                    product_id = analysis.checking_right_value(category_id)
                    ### IF PRODUCT ID IS GOOD ###
                    if product_id != False:
                        ### FIND SUBSTITUTE ###
                        substitute_id = find_substitute(
                            product_id, category_id)
                        ### IF SUBSTITUTE IS GOOD ###
                        if substitute_id != False:
                            display_substitute_proposition(product_id,
                                                           substitute_id)
                        ### OFFER TO USER TO SAVE CHANGEMENT ###
                            save_change(substitute_id, product_id)
                    ### TO LEAVE THE LOOP ###
                    selections_loop = True
        ### IF 2, DISPLAY SUBSTITUTE PRODUCTS ###
        if user_choice == 2:

            display_substitute_tab()
            ### WAIT USER ACTION BEFORE DISPLAY PRINCIPAL MENU ###
            input(back_to_menu_msg)
            ### TO COME BACK IN MENU LOOP ###
            user_choice == None


def find_substitute(selected_id_product, selected_id_cat):

    ### TO STORE NUTRISCORE OF SELECTED PRODUCT ###
    cursor.execute(query_nutr_from_product_id.format(selected_id_product))

    for nutr_selected_prod in cursor:
        ### NUTRISCORE OF SELECTED PRODUCT STORED IN ###
        nutr_selected_prod = nutr_selected_prod[0]
    ### FOR EACH LETTRE OF NUTRISCORE (A TO E) ###
    for nutr in LIST_OF_NUTRISCORE:
        ### INITIALIZE LIST OF BEST PRODUCT ID ###
        best_product_id = []
        ### TO FIND ALL PRODUCTS IN SAME CATEGORY WITH NUTRISCORE = nutr ###
        cursor.execute(query_better_nutr_from_prod.format(
            nutr, selected_id_cat))
        ### FOR EACH ID AND NUTRISCORE (= nutr) ###
        for id, nutriscore in cursor:
            ### IF THE SAME ###
            if nutriscore == nutr_selected_prod:
                ### PRINT THERE IS NO BETTER PRODUCT ###
                print(no_substitute_msg.format(nutriscore))
                ### RETURN FALSE, I CAN'T FIND SUBSTITUTE ###
                return False
            ### IF NOT, ADD IT TO MY LIST OF BEST PRODUCT ID ###
            elif nutriscore != nutr_selected_prod:
                best_product_id.append(id)
                pass
        ### IF NOT EMPTY ###
        if best_product_id:
            ### RETURN RANDOM ID TO MY LIST ###
            return random.choice(best_product_id)


def save_change(substitute_id, product_id):

    display_save_msg()
    ### OFFER TO USER 2 OPTIONS ###
    save_statement = int(input(space*87))
    ### IF USER ADD 1 ###
    if save_statement == 1:

        substitute_data = [substitute_id, product_id]
        ### ADD TO SUBSTITUTE TAB THE SUBSTITUTE_ID AND PRODUCT_ID ###
        cursor.execute(fill_sub_table, substitute_data)
        ### UPDATE DB ###
        cnx.commit()

        print(barre, data_saved)
    # OR IF USER ADD 2, LEAVE
    elif save_statement == 0:
        return
