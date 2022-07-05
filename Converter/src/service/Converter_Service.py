import os

import pantab
from tableauhyperapi import TableName


class ConverterService:

    def __init__(self):
        super(ConverterService, self).__init__()

    def convert_to_csv(self):
        """
        Leverages pantab and pandas to convert a .hyper file to a df, and then convert
        the df to a csv file.
        """
        path = os.getcwd()
        users_path = path+"\\users.hyper"
        date_path = path + "\\date.hyper"
        event_category_path = path + "\\event-category.hyper"
        sales_listing_path = path + "\\sales-listing.hyper"
        table_name = TableName("Extract", "Extract")
        users = "users.csv"
        date = "date.csv"
        event_category = "event-category.csv"
        sales_listing = "sales-listing.csv"
        # Uses pantab to convert the hyper file to a df.
        df = pantab.frame_from_hyper(users_path, table=table_name)
        print("Converting to CSV...")
        # Simple pandas->csv operation.
        df.to_csv(users)

        df = pantab.frame_from_hyper(date_path, table=table_name)
        df.to_csv(date)

        df = pantab.frame_from_hyper(event_category_path, table=table_name)
        df.to_csv(event_category)

        df = pantab.frame_from_hyper(sales_listing_path, table=table_name)
        df.to_csv(sales_listing)
