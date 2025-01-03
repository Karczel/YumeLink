from deep_translator import GoogleTranslator


def translate_text(text, target_language='en'):
    """
    Translate the given text into the target language using Google Translate.
    """
    try:
        # Automatically detects the source language
        translated_text = GoogleTranslator(source='auto', target=target_language).translate(text)
        return translated_text
    except Exception as e:
        return f"Error: {str(e)}"
