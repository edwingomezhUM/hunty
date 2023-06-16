import os
from pymongo import MongoClient
# from dotenv import load_dotenv

# load_dotenv()

class MongoConnection:

    # Este metodo permite instanciar un objeto de esta clas
    def __init__(self):

        try:
            # self.client = MongoClient(os.environ.get("MONGO_CONNECTION"), retryWrites=False)
            self.client = MongoClient("mongodb://datalab:Datalab2022*@40.87.47.53:27017/", retryWrites=False)
            self.db = self.client['prueba_whatsapp']
        
        except Exception as e:
            
            print(f"No se pudo conectar a la base de datos. Error: {e}")