from flask import Flask, jsonify, request

from transaction.update_chat import update_chat
from transaction.get_chat import get_chat

app = Flask(__name__)


@app.route("/messages/", methods=["POST", "GET"])
def webhook_whatsapp():
    # SI HAY DATOS RECIBIDOS VIA GET
    if request.method == "GET":

        id = request.args.get('id')
        user_id = request.args.get('user_id')

        # INSTACIA DE CLASE
        get = get_chat()

        if id is not None:
            # LLAMADO A METODO
            getMessages = get.get_CHAT_ID(id)

            # RETORNAMOS EL STATUS EN UN JSON
            return jsonify(getMessages, 200)
        
        elif user_id is not None:

            # LLAMADO A METODO
            getMessages = get.get_CHAT_USER_ID(user_id)

            # RETORNAMOS EL STATUS EN UN JSON
            return jsonify(getMessages, 200)
        
        else:

            # LLAMADO A METODO
            getMessages = get.get()

            # RETORNAMOS EL STATUS EN UN JSON
            return jsonify(getMessages, 200)

        # AUTENTICACION DEL SERVICIO fase inical de conexión con FACEBOOK
        # SI EL TOKEN ES IGUAL AL QUE RECIBIMOS
        # if request.args.get('hub.verify_token') == "pruebahunty":
        #     # ESCRIBIMOS EN EL NAVEGADOR EL VALOR DEL RETO RECIBIDO DESDE FACEBOOK
        #     return request.args.get('hub.challenge')
        # else:
        #     # SI NO SON IGUALES RETORNAMOS UN MENSAJE DE ERROR
        #     return "Error de autentificacion."

    elif request.method == "POST":

        if request.data:
            # RECIBIMOS TODOS LOS DATOS ENVIADO VIA JSON

            data = request.get_json()

            # INSTACIA DE CLASE
            insert = update_chat()

            # LLAMADO A METODO
            insertChat = insert.update_data(data)

            # RETORNAMOS EL STATUS EN UN JSON
            return jsonify({"status": "success"}, 200)
        else:

            # INSTACIA DE CLASE
            insert = update_chat()

            # LLAMADO A METODO
            insertChat = insert.update_data()

            # RETORNAMOS EL STATUS EN UN JSON
            return jsonify({"status": "success"}, 200)


if __name__ == "__main__":
    app.run(debug=True)
