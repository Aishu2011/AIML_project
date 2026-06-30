import os
import json
import pickle
import pandas as pd

from src.logger import LoggerManager
from src.exceptions import InvalidFileException
from src.base_handler import BaseHandler

class DataWriter(BaseHandler):
    """
    A class to write data into different file formats
    """

    def __init__(self):
        super().__init__()

    def write_data(self,data,file_path : str):
        try:
            directory = os.path.dirname(file_path)

            if directory:
                os.makedirs(directory,exist_ok=True)

            if file_path.endswith(".csv"):
                data.to_csv(file_path, index=False)
                self.logger.info(f"CSV file '{file_path}' saved successfully.")

            elif file_path.endswith(".json"):
                 with open(file_path, "w") as file:
                    json.dump(data, file, indent=4)

                 self.logger.info(f"JSON file '{file_path}' saved successfully.")
            
            elif file_path.endswith(".txt"):
                with open(file_path, "w") as file:
                    file.write(str(data))

                self.logger.info(f"TXT file '{file_path}' saved successfully.")

            elif file_path.endswith(".pkl"):
                with open(file_path, "wb") as file:
                    pickle.dump(data, file)

                self.logger.info(f"Pickle file '{file_path}' saved successfully.")

            else:
                raise InvalidFileException("Unsupported file format.")
            
        except Exception as e:
            self.logger.error(str(e))
            raise

        finally:
            self.logger.info("File writing operation completed.")