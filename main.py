from converter_service import ConverterService
from constants import FILES_IN_HYPERFILE_FORMAT


if __name__ == '__main__':
    #Instantiate the service
    converter = ConverterService()
    converter.convert_to_csv(FILES_IN_HYPERFILE_FORMAT)


