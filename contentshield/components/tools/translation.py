try:
    import googletrans

except ValueError as ve:
    raise ValueError(
        "`googletrans` is not installed. Please try `pip install googletrans`"
    ) from ve


class GoogleTranslator:
    def __init__(self, from_lang="vi", to_lang="en"):
        self.from_lang = from_lang
        self.to_lang = to_lang
        self.translator = googletrans.Translator()

    def run(self, text: str) -> str:

        result = self.translator.translate(
            text, src=self.from_lang, dest=self.to_lang
        ).text
        return result

    def _detect(self):
        "Detect source language"
        ...
