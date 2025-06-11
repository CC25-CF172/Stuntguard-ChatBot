import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

# Inisialisasi lemmatizer
lemmatizer = WordNetLemmatizer()

# Load model dan data yang disimpan
model = load_model("chatbot_model.h5")
intents = json.load(open("stunting_intents.json"))
words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open("classes.pkl", "rb"))

print("Model dan data berhasil dimuat!")
print(f"Ukuran kosakata: {len(words)} kata")
print(f"Jumlah kelas/intents: {len(classes)}")

# Fungsi preprocessing dan prediksi
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=False):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print(f"Found in bag: {w}")
    return np.array(bag)

def predict_class(sentence, model):
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return [{"intent": classes[r[0]], "probability": str(r[1])} for r in results]

def get_response(ints, intents_json):
    if not ints:
        return "Maaf, saya tidak mengerti maksud Anda."
    tag = ints[0]['intent']
    for i in intents_json['intents']:
        if tag == i['tag']:
            return random.choice(i['responses'])
    return "Maaf, saya tidak mengerti maksud Anda."

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = get_response(ints, intents)
    return res

# Mode interaktif
if __name__ == "__main__":
    print("\n Halo! Saya adalah Chatbot Stunting Asisten. Ketik 'keluar' untuk mengakhiri.\n")
    while True:
        user_input = input("Anda : ")
        if user_input.lower() in ["keluar", "exit", "quit"]:
            print("Bot  : Terima kasih telah berbicara. Sampai jumpa!")
            break
        response = chatbot_response(user_input)
        print("Bot  :", response)
