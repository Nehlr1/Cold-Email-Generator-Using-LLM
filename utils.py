import re

def Clean_Text(text):
    # Removing HTML tags
    text = re.sub(r'<[^>]*?>', '', text)
    # Removing URLs
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    # Removing special characters
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    # Replacing multiple spaces with a single space
    text = re.sub(r'\s{2,}', ' ', text)
    # Trimming leading and trailing whitespace
    text = text.strip()
    # Removing extra whitespace
    text = ' '.join(text.split())
    return text