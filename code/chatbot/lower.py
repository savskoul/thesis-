import json

with open("intents_fully_greek_natural.json", "r", encoding="utf-8") as f:
    intents = json.load(f)
    
def lowercase_intents(intents):
    for intent in intents["intents"]:
        intent["patterns"] = [p.lower() for p in intent["patterns"]]
        intent["responses"] = [r.lower() for r in intent["responses"]]
    return intents

intents_lower = lowercase_intents(intents)


with open("intents_fully_greek_lower.json", "w", encoding="utf-8") as f:
    json.dump(intents_lower, f, ensure_ascii=False, indent=2)