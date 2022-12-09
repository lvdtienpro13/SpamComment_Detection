import urllib.request
import re

class VietnamesePreprocessing:
    def __init__(self):
        data = urllib.request.urlopen(
            r"https://raw.githubusercontent.com/stopwords/vietnamese-stopwords/master/vietnamese-stopwords-dash.txt")
        self.stop_words = [item.decode("utf-8").strip() for item in list(data)]

    def clean(self, input: str):
        return input.strip().replace("\n", " ")

    def to_lower(self, input):
        return input.lower()

    def delete_punctuation(self, input):
        s1 = re.sub(r'[^\w\s]', '', input)
        return s1

    def __call__(self, x: str):
        x = self.clean(x)
        x = self.to_lower(x)
        x = self.delete_punctuation(x)
        return x