from google_trans_new import google_translator
from googletrans import Translator


def translation_func(input_language, output_language, text):
    translator = google_translator(url_suffix="com", timeout=10)
    translate = translator.translate(text, "fr")  # You can give any country code eg:"fr","en","th",etc...
    return translate
