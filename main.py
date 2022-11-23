from transformers import pipeline

translator = pipeline("translation_ru_to_en", "Helsinki-NLP/opus-mt-ru-en")

translator("Да прибудет с тобой сила, студент")
