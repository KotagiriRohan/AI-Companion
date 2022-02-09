import transformers

nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")

for i in range(5):
    text = input("user -->")
    chat = nlp(transformers.Conversation(text), pad_token_id=50256)
    print('bot -->', str(chat))