from flask import Flask, render_template, request
import openai

# Creamos una instancia de la clase Flask
app = Flask(__name__)

# Configuramos la clave de la API de OpenAI
openai.api_key = ''


# Inicializamos una lista vacía para almacenar las conversaciones
conversaciones = []

# Definimos una ruta para la página principal de nuestra aplicación
@app.route('/', methods=['GET', 'POST'])
def inicio():
    # Si el método de la solicitud es GET, mostramos la página principal
    if request.method == 'GET':
        return render_template('index.html', chat=conversaciones)
    
    # Si el formulario contiene una pregunta
    if request.form['question']:
        # Formateamos la pregunta del usuario
        pregunta = 'Yo: ' + request.form['question']

        # Hacemos una solicitud a la API de OpenAI para obtener una respuesta
        respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": request.form['question']}
        ],
        temperature=0.9,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6
    )

        # Formateamos la respuesta de la IA
        respuesta_ia = 'AI: ' + respuesta['choices'][0]['message']['content']

        # Añadimos la pregunta y la respuesta a la lista de conversaciones
        conversaciones.append(pregunta)
        conversaciones.append(respuesta_ia)

        # Mostramos la página principal con la conversación actualizada
        return render_template('index.html', chat = conversaciones)
    else:
        # Si el formulario no contiene una pregunta, mostramos la página principal
        return render_template('index.html', chat=conversaciones)
    
# Si este script se ejecuta como el principal, iniciamos la aplicación
if __name__ == '__main__':
    app.run(debug=True, port=4000)

# Para ejecutar el programa primero se debe instalar Flask y OpenAI con los siguientes comandos:
# pip install Flask openai
# Luego se ejecuta el programa con la flecha verde de la esquina superior derecha de VSC.s