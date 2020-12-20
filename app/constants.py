""" CONSTANTS FILE """

# MESSAGES SHORTCUT

principal_menu     = "################################## MENU PRINCIPAL ###################################"
select_action_msg  = ">>>                            Sélectionnez une action                            <<<"
menu_opt_0_msg     = "|  0  ||    Fermer le programme                                                     |"
menu_opt_1_msg     = "|  1  ||    Quel aliment souhaitez-vous remplacer ?                                 |"
menu_opt_2_msg     = "|  2  ||    Retrouver mes aliments substitués.                                      |"
menu_opt_3_msg     = "|  3  ||    Supprimer mes aliments substitués.                                      |"

category_menu      = "#################################### CATEGORIES #####################################"
select_cat_msg     = ">>>                          Sélectionnez une catégorie                           <<<"
opt_0_cat_menu     = "|  0  ||  Retour                                                                    |"

product_menu       = "##################################### PRODUITS ######################################"
select_product_msg = ">>>                 Sélectionnez l'id du produit ou 0 pour quitter                <<<"

save_menu          = "#################################### SAUVEGARDER ####################################"
save_msg           = ">>>                           Voulez-vous sauvegarder ?                           <<<"
save_opt_0         = "|  0  ||    Non, retour au menu                                                     |"
save_opt_1         = "|  1  ||    SAUVEGARDER                                                             |"
data_saved         = ">>>                         Les données ont été sauvegardé                          <<<"

substituted_menu   = "############################# MES ALIMENTS SUBSTITUTES ##############################"
back_to_menu_msg   = ">>>              Appuyez sur [Entrée] pour revenir au menu principal              <<<"

delete_menu        = "##################################### SUPPRIMER #####################################"
confirmation_msg   = ">>>     Voulez-vous vraiment supprimer définitement mes aliments substitués ?     <<<"
opt_0_del_menu     = "|  0  ||  Non, ne pas suprimmer \"Mes aliments substitutés\"                        |"
opt_1_del_menu     = "|  1  ||  SUPPRIMER                                                                 |"
sub_tab_erased     = ">>>                   Toutes les substitutions ont été supprimé                   <<<"

substitution_menu  = "################################### SUBSTITUTION ####################################"
best_product_msg   = ">>>              Voici le meilleur produit que nous avons trouvez                 <<<"
replace_msg        = ">>>                        Il remplacerait ce produit                             <<<"

# "ERROR MESSAGES"

no_substitute_msg  = ">>>              Il n'y as pas de meilleurs produit, nutriscore = {}                <<<"
no_sub_in_table    = ">>>      Il n'y as aucun produit sauvegardé dans \"Mes aliments substitués\" !      <<<"
duplicate_msg      = ">>>         Le produit sélectionné est déjà dans \"Mes aliments substitués\" !      <<<"
value_error_msg    = ">>> Erreur de saisie, >>> {} <<< n'est pas correct <<<"
letter_or_symb_msg = "[Entrée], une lettre ou un symbole"

barre              = "#####################################################################################"
small_barre        = "|-----------------------------------------------------------------------------------|"
space              = " "

# Lists SHORTCUT

CATEGORYS          = ["pates-a-tartiner", "cremes", "legumineuses", "fromages-de-vache", "pains", "jambons"]
LIST_OF_NUTRISCORE = ["a", "b", "c", "d", "e"]

# VAR FROM CATEGORYS

nb_of_category = len(CATEGORYS) + 1
