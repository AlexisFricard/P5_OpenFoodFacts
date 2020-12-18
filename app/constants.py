""" CONSTANTS FILE """

# MESSAGES SHORTCUT

menu_opt_0_msg     = "|  0  ||    Fermer le programme                                                     |"
menu_opt_1_msg     = "|  1  ||    Quel aliment souhaitez-vous remplacer ?                                 |"
menu_opt_2_msg     = "|  2  ||    Retrouver mes aliments substitués.                                      |"

select_action_msg  = ">>>         Selectionnez une action                                               <<<"
select_cat_msg     = ">>>         Selectionnez le chiffre d'une catégorie                               <<<"
select_product_msg = ">>>         Selectionnez l'id du produit                                          <<<"
back_to_menu_msg   = ">>>         Appuyer sur ENTRER pour revenir au menu principal                     <<<"
best_product_msg   = ">>>         Voici le meilleur produit que nous avons trouvez :                    <<<"
replace_msg        = ">>>         Remplacerait ce produit :                                             <<<"
value_error_msg    = ">>>         Erreur de saisie, >>>{}<<< n'est pas une donnée correct               <<<"
no_substitute_msg  = ">>>         Il n'y as pas de meilleurs produit, nutriscore = {}                    <<<\n"
duplicate_msg      = ">>>         Le produit sélectionné est déjà dans \"Mes aliments substitués\" !    <<<"
save_msg           = ">>>         Voulez vous sauvegarder ?                                             <<<"
save_opt_1         = "|  1  ||    Sauvegarder ma recherche                                                |"
save_opt_0         = "|  0  ||    Retour au menu                                                          |"
data_saved         = "\n               Les données ont été sauvgardées                "


principal_menu     = "################################## MENU PRINCIPAL ###################################"
category_menu      = "#################################### CATEGORIES #####################################"
opt_0_cat_menu     = "|  0  ||  Retour                                                                    |"
product_msg        = "####################################  PRODUITS  #####################################"
substituted_msg    = "############################# MES ALIMENTS SUBSTITUTES ##############################"
small_barre        = "|-----------------------------------------------------------------------------------|"
barre              = "#####################################################################################"
space              = " "

# Lists SHORTCUT

CATEGORYS          = ["pates-a-tartiner", "cremes", "legumineuses", "fromages-de-vache", "pains", "jambons"]
LIST_OF_NUTRISCORE = ["a", "b", "c", "d", "e"]

# VAR FROM CATEGORYS

nb_of_category = len(CATEGORYS) + 1
