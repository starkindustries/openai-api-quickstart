import os
from dotenv import load_dotenv
from openai import OpenAI


def get_gpt_response(prompt):
    client = OpenAI(
        api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    load_dotenv()
    user_input = input("Enter your message: ")
    response = get_gpt_response(user_input)
    print("GPT-3 response:", response)
