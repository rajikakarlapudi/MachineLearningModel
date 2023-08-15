from elevenlabs import generate, play, set_api_key
set_api_key("15d451acb300eda213ede30cba66049a")

text=input("enter the text ")
audio = generate(
    text,
    voice="Bella"
)

play(audio, notebook=True)
