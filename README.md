# README.md Translator

Easily translate your readme into other languages using Azure Translator API

- Fork or Clone this repo
- Set up cognitive services in [Azure](https://portal.azure.com/) to obtain your own keys
- Look into `yoo.py` for available language specification
- Enter your choice into `langs` array in `__init__.py`
- Enter text you need to translate in [txt1, txt2... txt*n*]
  - Note that there is a max `10k` character limit per request made to the API hence why you need to split your text
- Make changes as your see fit in the transDoc function
- Enjoy