import os

import pantab
from tableauhyperapi import TableName


class ConverterService:

    def __init__(self):
        super(ConverterService, self).__init__()

    def convert_to_csv(self, list_of_files):
        """
        Leverages pantab and pandas to convert a .hyper file to a df, and then convert
        the df to a csv file.
        """
        path = os.getcwd()
        table_name = TableName("Extract", "Extract")

        for file in list_of_files:
            df = pantab.frame_from_hyper(path + file, table=table_name)
            file = file.replace("\\"+file+".hyper", "")
            file = path+file
            df.to_csv(str(file) + ".csv")
