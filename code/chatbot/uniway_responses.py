from transformers import pipeline
import random
import json

with open("intents_expanded_en.json", "r") as f:
    intents_en = json.load(f)

# Παραφραστική επέκταση 
def paraphrase_response(response):
    paraphrases = [
        f"{response}",
        f"To put it another way: {response}",
        f"Let me explain: {response}",
        f"Here’s how I’d phrase it: {response}",
        f"{response} Please let me know if that helps!"
    ]
    return random.choice(paraphrases)

# Επέκταση responses στα Αγγλικά
for intent in intents_en["intents"]:
    base = intent["responses"]
    expanded = []
    while len(expanded) < 60:
        expanded.append(paraphrase_response(random.choice(base)))
    intent["responses"] = list(set(expanded))[:60]

# Μετάφραση στα Ελληνικά με OPUS-MT
translation_pipeline = pipeline("translation", model="Helsinki-NLP/opus-mt-en-el")

# Μεταφραση καθε intent
intents_gr = []
for intent in intents_en["intents"]:
    responses_en = intent["responses"]
    responses_gr = []
    for i in range(0, len(responses_en), 10):
        batch = responses_en[i:i+10]
        translations = translation_pipeline(batch)
        responses_gr.extend([t['translation_text'] for t in translations])
    intents_gr.append({
        "tag": intent["tag"],
        "patterns": [],  # patterns από τα Ελληνικά
        "responses": responses_gr,
        "context_set": ""
    })

with open("intents_expanded_en_updated.json", "w") as f:
    json.dump(intents_en, f, indent=2)

with open("intents_expanded_gr_updated.json", "w", encoding="utf-8") as f:
    json.dump({"intents": intents_gr}, f, ensure_ascii=False, indent=2)