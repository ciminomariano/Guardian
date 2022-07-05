from Converter.src.constants.constants import FILES_IN_HYPERFILE_FORMAT
from Converter.src.service.converter_service import ConverterService

if __name__ == '__main__':
    #Instantiate the service
    converter = ConverterService()
    converter.convert_to_csv(FILES_IN_HYPERFILE_FORMAT)


