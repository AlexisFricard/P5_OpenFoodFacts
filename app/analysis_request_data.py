""" analysis_request_data file """


class Analysis_data:

    def __init__(self):
        # LISTS OF ALL NAME AND URL TO DETECT DUPLICATIONS
        self.p_name_list = list()
        self.p_url_list = list()

    # METHOD TO DETECT EMPTY FIELD, DUPLICATE NAME AND URL
    def data_checking(self, p_data):

        datas = p_data
        check_list = list()
        duplicate_list = list()
        # ADD TO LIST TRUE OR FALSE, FALSE WHEN IT'S EMPTY
        for field in datas:
            check_list.append(self.checking_empty_field(field))

        # CHECK EMPTY FIELD ###
        if check_list == [True, True, True, True]:

            # ADD TO LIST TRUE OR FALSE, FALSE WHEN IT'S IN DOUBLE
            duplicate_list.append(self.checking_duplicate_name(datas[0]))
            duplicate_list.append(self.checking_duplicate_url(datas[3][-15:]))

            # CHECK IF DUPLICATE NAME OR URL END (15 LAST CHAR)
            if duplicate_list == [True, True]:
                return True
        else:
            return False

    # METHOD TO RETURN TRUE OR FALSE IF THE FIELD IS EMPTY
    def checking_empty_field(self, field):

        if (field is not None and field != ""):
            return True
        else:
            return False

    # METHOD TO RETURN TRUE OR FALSE IF THE NAME IS IN DOUBLE
    def checking_duplicate_name(self, product_name):

        if product_name not in self.p_name_list:
            self.p_name_list.append(product_name)
            return True
        else:
            return False

    # METHOD TO RETURN TRUE OR FALSE IF THE END OF URL IS IN DOUBLE
    def checking_duplicate_url(self, product_url):

        if product_url not in self.p_url_list:
            self.p_url_list.append(product_url)
            return True
        else:
            return False

    def del_lists(self):
        self.p_name_list = []
        self.p_url_list = []
