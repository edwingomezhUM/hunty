from connection.mongoConnection import MongoConnection
from datetime import datetime
from heyoo import WhatsApp


class update_chat():

    def __init__(self) -> None:
        pass

    def update_data(self, data=None):

        # INSTACIA DE LA BASE DE DATOS
        BD = MongoConnection()
        current = datetime.now()

        # MENSAJE A ENVIAR
        textoMensaje = "Hola huntry saludos"

        if data != None:

            # TELEFONO QUE RECIBE (EL DE NOSOTROS QUE DIMOS DE ALTA)
            telefonoEnvia = data['entry'][0]['changes'][0]['value']['messages'][0]['from']

            "json para insertar en bd"
            jsonInsert = {
                "user_id": telefonoEnvia,
                "mensaje_recibido": data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body'],
                "mensaje_enviado": textoMensaje,
                "fecha": current
            }
        else:
            # TELEFONO QUE RECIBE (EL DE NOSOTROS QUE DIMOS DE ALTA)
            telefonoEnvia = "573122327042"

            "json para insertar en bd"
            jsonInsert = {
                "user_id": telefonoEnvia,
                "mensaje_recibido": "NA",
                "mensaje_enviado": textoMensaje,
                "fecha": current
            }

        # TOKEN DE ACCESO DE FACEBOOK
        token = 'EAAIXVaWBa24BAGIKE7foMoCI0Qna9Wy4jp3m6aC9FVFaoh3MvZCjVGfcXPrahju7TgNgfzm6jvwktxaSRwl7rsDZAXFXXrmOqICZBSMgiDqZAxsnXQkjSd44D7ZCLHEC9vSZCIhzFyl4qoQn36HgWkQi0IWUPeCClBaVowm9VeF5ba5jo5Iak7MuYgqO4dZBh2fLaqaf9Ib9YbecdfddZAZCu'
        # IDENTIFICADOR DE NÚMERO DE TELÉFONO
        idNumeroTeléfono = '107003559098299'

        # URL DE LA IMAGEN A ENVIAR
        urlImagen = 'https://i.imgur.com/uxaTHdo.png'
        # INICIALIZAMOS ENVIO DE MENSAJES
        mensajeWa = WhatsApp(token, idNumeroTeléfono)
        # ENVIAMOS UN MENSAJE DE TEXTO
        mensajeWa.send_message(textoMensaje, telefonoEnvia)
        # ENVIAMOS UNA IMAGEN
        mensajeWa.send_image(image=urlImagen, recipient_id=telefonoEnvia,)

        try:
            insertMongo = BD.db.interacciones_whatsapp.insert_one(jsonInsert)

        except Exception as e:
            print(f"Error updating data: {e}")

        return "registro exitoso"
