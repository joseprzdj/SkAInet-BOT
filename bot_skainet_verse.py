#!/usr/bin/env python3

import tweepy
import random
from datetime import datetime

# Claves y tokens de acceso
API_KEY = '<sensitive>' 
API_KEY_SECRET = '<sensitive>' 
ACCESS_TOKEN = '<sensitive>'
ACCESS_TOKEN_SECRET = '<sensitive>'
BEARER_TOKEN = "<sensitive>"
CLIENT_ID = '<sensitive>'
CLIENT_SECRET = '<sensitive>'
# Paths to files
PATH = '<your-path>'
OUTPUT_PATH = '<your-output-path>'

hashtags_ia = [
    "#AI",
    "#ArtificialIntelligence",
    "#MachineLearning",
    "#DeepLearning",
    "#NeuralNetworks",
    "#DataScience",
    "#Robotics",
    "#Automation",
    "#BigData",
    "#NLP",
    "#ComputerVision",
    "#IoT",
    "#SmartTech",
    "#ML",
    "#DL",
    "#AIethics",
    "#AIforGood",
    "#IntelligentSystems",
    "#AIApplications",
    "#AIResearch"
]

# Leer y eliminar una frase aleatoria del archivo
def read_random_sentence():
    full_path = PATH
    with open(full_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    if lines:
        random_sentence = random.choice(lines)
        random_sentence_to_tweet = random_sentence.replace('"', '')  # Eliminar las comillas dobles si las hay
        lines.remove(random_sentence)  # Eliminar la frase del archivo

        with open(full_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)  # Actualizar el archivo sin la frase eliminada
        
        return random_sentence_to_tweet

# Registrar la frase publicada en un archivo de log
def log_published_message(message):
    full_path = OUTPUT_PATH
    with open(full_path, 'a', encoding='utf-8') as f:
        f.write(message + '\n')

# Verificar la autenticación y publicar un tweet
def publish_tweet(message):
    # Auth
    client = tweepy.Client(bearer_token=BEARER_TOKEN,
        consumer_key=API_KEY,
        consumer_secret=API_KEY_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )

    hashtag = random.choice(hashtags_ia)
    message_hashtag = message + " " + hashtag

    # Verificar la autenticación
    try:
        if client:
            print("Autenticación exitosa")
            try:
                response = client.create_tweet(text=message_hashtag)
                if response:
                    print("Tweet publicado correctamente")
                    print(f"Mensaje: {message_hashtag}")
                    log_published_message(message_hashtag)
            except tweepy.errors.TweepyException as e:
                print(f"Error al publicar el tweet: {e}")
                print(f"Tipo de error: {type(e).__name__}")                     
        else:
            print("Fallo en la autenticación")
    except tweepy.errors.TweepyException as e:
        print(f"Error de autenticación: {e}")

# Main
if __name__ == "__main__":
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_datetime}")
    message = read_random_sentence()
    #print(message)
    publish_tweet(message)
