# Sample customer feedback comments
feedback_comments = [
    "I am extremely satisfied with the service.",
    "The product quality is average, nothing special.",
    "Very disappointed with the delivery time.",
    "The customer support team was very helpful.",
    "Product did not meet my expectations.",
    "I'm neutral about my purchase experience.",
    "Fantastic quality at a great price!"
]

# Lists of keywords associated with positive, neutral, and negative sentiments
positive_keywords = ["satisfied", "helpful", "fantastic", "great"]
neutral_keywords = ["average", "neutral"]
negative_keywords = ["disappointed", "did not meet"]

# Function to classify feedback
def classify_feedback(comment):
    for keyword in positive_keywords:
        if keyword in comment.lower():
            return "Positive"
    for keyword in neutral_keywords:
        if keyword in comment.lower():
            return "Neutral"
    for keyword in negative_keywords:
        if keyword in comment.lower():
            return "Negative"
    return "Unclassified"

# Classifying and printing the results
for comment in feedback_comments:
    sentiment = classify_feedback(comment)
    print(f"Comment: \"{comment}\" - Sentiment: {sentiment}")
