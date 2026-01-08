# AI-Based Deception Indicator (Text)

An explainable NLP-based system that analyzes linguistic patterns in text to estimate the likelihood of deception.

⚠️ **Disclaimer:**  
This is NOT a lie detector.  
It is a rule-based linguistic indicator designed for learning and demonstration purposes.

---

## 🔍 What This Project Does
The system takes a text statement as input and evaluates it using multiple linguistic indicators to classify it as:

- 🟢 Likely Truth  
- 🟡 Uncertain  
- 🔴 Likely Deceptive  

Along with a **deception confidence score** and explanation.

---

## 🧠 Indicators Used
- Hesitation words (e.g., *honestly, trust me, maybe, I swear*)
- Over-justification and sentence length
- Emotional polarity (sentiment analysis)
- Certainty words (e.g., *because, since*)

---

## 🛠️ Tech Stack
- Python  
- TextBlob (NLP)  
- Rule-based scoring (Explainable AI)

---

## ▶️ How to Run
```bash
py -3.14 .\main.py
