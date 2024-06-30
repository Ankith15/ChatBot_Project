import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# nltk.download('stopwords')
# nltk.download('wordnet')
def cleaning(text, remove_stopwords=False, lemmatize=False):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    
    cleantxt = re.sub(r'http\S+', '', text)
    cleantxt = re.sub(r'@\S+', '', cleantxt)
    cleantxt = re.sub(r'#(\S+)', r'\1', cleantxt)
    cleantxt = re.sub(r'\bRT\b|\bcc\b', '', cleantxt)
    cleantxt = re.sub(r'[^A-Za-z0-9.,]', ' ', cleantxt)
    cleantxt = re.sub(r'\s+', ' ', cleantxt)
    cleantxt = cleantxt.strip()
    cleantxt = cleantxt.lower()

    words = cleantxt.split()

    if remove_stopwords:
        words = [word for word in words if word not in stop_words]

    if lemmatize:
        words = [lemmatizer.lemmatize(word) for word in words]

    cleantxt = ' '.join(words)
    
    return cleantxt