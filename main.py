from indicators import analyze_text

print("🔍 AI-Based Deception Indicator (Text)")
print("⚠️ This is NOT a lie detector. It analyzes linguistic patterns.\n")

text = input("Enter a statement:\n> ")

result = analyze_text(text)
score = result["score"]

if score <= 30:
    verdict = "🟢 Likely Truth"
elif score <= 55:
    verdict = "🟡 Uncertain"
else:
    verdict = "🔴 Likely Deceptive"

print("\n📊 Analysis Result")
print("--------------------")
print("Verdict:", verdict)
print("Deception Confidence:", f"{score}%")
print("Sentiment Polarity:", result["sentiment"])
print("Avg Sentence Length:", result["avg_sentence_length"])

if result["hesitation_words"]:
    print("Hesitation Words Detected:", ", ".join(result["hesitation_words"]))

if result["certainty_words"]:
    print("Certainty Words Detected:", ", ".join(result["certainty_words"]))
