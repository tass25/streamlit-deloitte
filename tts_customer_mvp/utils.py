import os
import json
from collections import Counter
from time import strftime

HISTORY_FILE = "data/history.json"

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_history(data):
    os.makedirs("data", exist_ok=True)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_to_history(role, text, lang):
    history = load_history()
    history.append({
        "role": role,
        "text": text,
        "lang": lang,
        "time": strftime("%H:%M:%S")
    })
    save_history(history)

def get_language_stats():
    history = load_history()
    langs = [item["lang"] for item in history]
    return Counter(langs)

def get_most_common_phrases(top_n=5):
    history = load_history()
    texts = [item["text"] for item in history]
    return Counter(texts).most_common(top_n)
