
import telegram
import requests
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

# Define el token de acceso que te proporcionó BotFather
TOKEN = "5993087367:AAGCA_pOaSkqGo27_RRQj527Inzv1-W7C_M"

# Define la URL base de la API
API_BASE_URL = "https://api-football-v1.p.rapidapi.com/v3"

# Define la clave de la API
API_KEY = "82cae17872ec48b48e49882647c47fed"

# Crea el objeto updater y dispatcher
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

# Define la función para el comando /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="¡Bienvenido al bot VictoryVision! Proporcionaremos predicciones basadas en datos anteriores de partidos de fútbol.")

# Define la función para manejar los mensajes de texto
def predict(update, context):
    # Obtener el mensaje del usuario
    message = update.message.text

    # Hacer una solicitud a la API de fútbol para obtener los datos de partidos anteriores
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "api-football-v1.p.rapidapi.com"
    }
    url = f"{API_BASE_URL}/fixtures?league=39&season=2022&team=X&last=5"
    response = requests.get(url, headers=headers)

    # Procesar los datos de la respuesta de la API y generar una predicción
    # En este ejemplo, simplemente generamos una predicción aleatoria
    import random
    prediction = random.choice(["El equipo X ganará", "El equipo Y ganará", "El partido terminará en empate"])

    # Enviar la predicción al usuario
    context.bot.send_message(chat_id=update.effective_chat.id, text=prediction)

# Registra los handlers
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

predict_handler = MessageHandler(Filters.text & (~Filters.command), predict)
dispatcher.add_handler(predict_handler)

# Inicia el bot
updater.start_polling()

# Mantén el bot activo
updater.idle()
