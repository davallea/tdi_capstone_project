import re
import emoji

def clean(review):
        review = str(review)
        review = str(review.lower())  
        review = emoji.demojize(review)
        review = re.compile(r'https?://\S+|www\.\S+').sub(r'', review)
        review = re.compile('[^a-záéíóúüñ@_-]+').sub(' ', str(review)).strip()
        return ''.join(review)