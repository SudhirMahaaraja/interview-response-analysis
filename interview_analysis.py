import spacy
from textblob import TextBlob

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def analyze_response(response):
    # Sentiment analysis using TextBlob
    blob = TextBlob(response)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        sentiment_label = 'Positive'
    elif sentiment < 0:
        sentiment_label = 'Negative'
    else:
        sentiment_label = 'Neutral'

    # Key phrase extraction using spaCy
    doc = nlp(response)
    key_phrases = [chunk.text.lower().strip() for chunk in doc.noun_chunks]

    return sentiment_label, key_phrases

def overall_quality_assessment(sentiment, key_phrases, expected_key_phrases):
    matched_key_phrases = set(key_phrases) & set(expected_key_phrases)
    key_phrase_relevance = len(matched_key_phrases) / len(expected_key_phrases)

    if key_phrase_relevance >= 0.04:
        quality = 'High'
    elif key_phrase_relevance >= 0.02:
        quality = 'Moderate'
    else:
        quality = 'Low'

    return quality, key_phrase_relevance

# Load expected key phrases from file
with open('expected_key_phrases.txt', 'r') as file:
    expected_key_phrases = [line.strip().lower() for line in file.readlines()]

# Prompt user to choose input method
input_method = input("Enter 'file' to read responses from sample_responses.txt or 'manual' to enter responses manually: ").strip().lower()

responses = []
quality_counts = {'High': 0, 'Moderate': 0, 'Low': 0}

if input_method == 'file':
    # Load responses from file
    with open('sample_responses.txt', 'r') as file:
        responses = file.read().strip().split('\n\n')
elif input_method == 'manual':
    while True:
        print("Enter your response. Type 'done' when you finish.")
        response = input("Response: ").strip()
        if response.lower() == 'done':
            break
        responses.append("Response:\n" + response)
else:
    print("Invalid input method. Please enter 'file' or 'manual'.")

for i, response in enumerate(responses):
    response_text = response.split('\n', 1)[1].strip()  # Extract response text
    sentiment, key_phrases = analyze_response(response_text)
    quality, key_phrase_relevance = overall_quality_assessment(sentiment, key_phrases, expected_key_phrases)

    # Update quality counts
    quality_counts[quality] += 1

    print(f'Response {i + 1}:')
    print(f'Text: {response_text}')
    print(f'Sentiment: {sentiment}')
    print(f'Extracted Key Phrases: {key_phrases}')
    print(f'Matched Key Phrases: {list(set(key_phrases) & set(expected_key_phrases))}')
    print(f'Total Relevance: {key_phrase_relevance:.2f}')
    print(f'Quality: {quality}')
    print('\n')

# Final quality counts after all responses
print(f'Final Quality Counts:')
print(f'High: {quality_counts["High"]}')
print(f'Moderate: {quality_counts["Moderate"]}')
print(f'Low: {quality_counts["Low"]}')
