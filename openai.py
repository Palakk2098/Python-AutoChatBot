from openai import OpenAI

# pip install openai


client = OpenAI(
    api_key="#####"
)

chatHistory='''
chat that is copied
'''

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a person named Haryy who speaks Hindi as well as English. He is from India and is a coder. You analyze the chat history and respond like Harry."},
        {
            "role": "user",
            "content": chatHistory
        }
    ]
)

print(completion.choices[0].message.content)