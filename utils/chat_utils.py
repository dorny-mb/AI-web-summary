from IPython.display import Markdown, display
from classes.Website import Website

# with Ollama SDK
import ollama
MODEL = "llama3.2"


# with OpenAI SDK
# from openai import OpenAI
# openai = OpenAI()


system_prompt = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
Respond in markdown."




def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]


def summarize(url):
    website = Website(url, use_selenium=True)

    # with openAI SDK
    # response = openai.chat.completions.create(
    #     model = "gpt-4o-mini",
    #     messages = messages_for(website)
    # )
    # return response.choices[0].message.content

    # with Ollama SDK
    response = ollama.chat(model=MODEL, messages=messages_for(website))
    return response['message']['content']




def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "\nThe contents of this website is as follows; \
please provide a short summary of this website in markdown. \
If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt

def display_summary(url):
    summary = summarize(url)
    display(Markdown(summary))
    print(summary)