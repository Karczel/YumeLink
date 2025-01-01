import requests

languages = []


def fetch_languages():
    """Turn supported detected languages into list of tuples for Django model type hints."""
    global languages
    if not languages:
        url = "https://ws.detectlanguage.com/0.2/languages"
        response = requests.get(url)
        if response.status_code == 200:
            languages = response.json()
            languages = [(lang['code'], lang['name'].title()) for lang in languages]
    return languages
