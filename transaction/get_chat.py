from connection.mongoConnection import MongoConnection
from bson import json_util, ObjectId
import json


class get_chat():

    def __init__(self) -> None:
        pass

    def get(self):

        # INSTACIA DE LA BASE DE DATOS
        BD = MongoConnection()

        try:
            getMessages = BD.db.interacciones_whatsapp.find()
            return self.formatter(getMessages)

        except Exception as e:
            print(f"Error updating data: {e}")

    def get_CHAT_ID(self, id):

        # INSTACIA DE LA BASE DE DATOS
        BD = MongoConnection()

        try:
            getMessages = BD.db.interacciones_whatsapp.find(
                {"_id": ObjectId(id)})

            return self.formatter(getMessages)

        except Exception as e:
            print(f"Error updating data: {e}")

    def get_CHAT_USER_ID(self, user_id):

        # INSTACIA DE LA BASE DE DATOS
        BD = MongoConnection()

        try:
            getMessages = BD.db.interacciones_whatsapp.find(
                {"user_id": user_id})
            return self.formatter(getMessages)

        except Exception as e:
            print(f"Error updating data: {e}")

    #convertir salida en json
    def formatter(self, getMessages):
        json_resultados = []
        for documento in getMessages:
            json_resultados.append(json.loads(json_util.dumps(documento)))

        return json_resultados
