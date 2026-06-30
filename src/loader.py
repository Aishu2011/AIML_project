import os
import json
import pandas as pd

from src.exceptions import InvalidFileException, InvalidPathException
from src.base_handler import BaseHandler

class DataLoader(BaseHandler):
    """
    A class to load data from csv,json and txt files.
    """
    def __init__(self):
        
        super().__init__()

    def load_data(self,file_path: str):
        try:
            if not os.path.exists(file_path):
                raise InvalidPathException(f"File '{file_path}' does not exist.")
                
            if self.is_supported_extension(file_path, (".csv",)):
                data=pd.read_csv(file_path)
                self.logger.info(f"CSV file '{file_path}' loaded successfully.")
                return data
                
            elif self.is_supported_extension(file_path, (".json",)):
                with open(file_path,"r") as file:
                    data=json.load(file)

                self.logger.info(f"JSON file '{file_path}' loaded successfully.")
                return data
                
            elif self.is_supported_extension(file_path, (".txt",)):
                with open(file_path,"r") as file:
                    data=file.read()

                self.logger.info(f"TXT file '{file_path}' loaded successfully.")
                return data
                
            else:
                raise InvalidFileException("Unsupported file format.")
                
        except Exception as e:
            self.logger.error(str(e))
            raise

        finally:
            self.logger.info("File loading operation completed.")
                    
