from textblob import TextBlob

HESITATION_WORDS = [
    "maybe", "probably", "honestly", "to be frank", "trust me",
    "i swear", "i think", "kind of", "sort of"
]

CERTAINTY_WORDS = [
    "because", "therefore", "since", "as a result"
]


def analyze_text(text):
    text_lower = text.lower()
    blob = TextBlob(text_lower)
    sentiment = blob.sentiment.polarity

    sentences = [s for s in text.split('.') if s.strip()]
    avg_sentence_length = (
        sum(len(s.split()) for s in sentences) / max(len(sentences), 1)
    )

    hesitation_found = [w for w in HESITATION_WORDS if w in text_lower]
    certainty_found = [w for w in CERTAINTY_WORDS if w in text_lower]

    score = 0

    # Hesitation words
    if hesitation_found:
        score += 40

    # Multiple hesitation words
    if len(hesitation_found) >= 2:
        score += 20

    # Emotional extremes
    if sentiment > 0.7 or sentiment < -0.7:
        score += 15

    # Flat emotion (suspicious)
    if -0.2 < sentiment < 0.2:
        score += 10

    # Long defensive sentence
    if avg_sentence_length > 18:
        score += 20

    # Certainty words reduce suspicion
    if certainty_found:
        score -= 10

    score = max(0, min(100, score))

    # ✅ RETURN IS CRITICAL
    return {
        "score": score,
        "sentiment": round(sentiment, 2),
        "hesitation_words": hesitation_found,
        "certainty_words": certainty_found,
        "avg_sentence_length": round(avg_sentence_length, 2)
    }
