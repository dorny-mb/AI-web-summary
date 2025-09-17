import os
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

def isAPIKeyValid():

    if not api_key:
        print("Error: OPENAI_API_KEY environment variable is not set.")
    elif not api_key.startswith("sk-"):
        print("Error: OPENAI_API_KEY does not appear to be valid.")
    elif api_key.strip() != api_key:
        print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
    else:
        print("API key found and looks good so far!")


__all__ = ["isAPIKeyValid"]