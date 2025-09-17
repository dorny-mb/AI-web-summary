from utils.creds_utils import isAPIKeyValid
from utils.chat_utils import display_summary

# Load environment variables in a file called .env
isAPIKeyValid()

display_summary("https://media.nsoko.io")


