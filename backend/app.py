from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

ner = pipeline("ner", model="d4data/biomedical-ner-all", aggregation_strategy="simple")
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
advice_gen = pipeline("text2text-generation", model="google/flan-t5-small")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    print("User:", user_msg)

    entities = [ent["word"] for ent in ner(user_msg)]
    print("Entities:", entities)

    diseases = ["flu", "cold", "migraine", "dengue", "covid", "gastritis"]
    classification = classifier(user_msg, candidate_labels=diseases)
    predicted = classification["labels"][0]
    print("Predicted disease:", predicted)

    prompt = f"User symptoms: {entities}. Possible disease: {predicted}. Give short advice."
    advice = advice_gen(prompt, max_new_tokens=100, temperature=0.7, repetition_penalty=2.0, top_p=0.9)[0]["generated_text"]

    red_flag_keywords = ["chest pain", "unconscious", "bleeding", "severe"]
    alert = any(k in user_msg.lower() for k in red_flag_keywords)
    final = f"🚨 {advice}" if alert else advice

    print("Bot:", final)
    return jsonify({"bot": final})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
