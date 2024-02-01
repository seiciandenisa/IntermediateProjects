from textblob import TextBlob
from dataclasses import dataclass


@dataclass
class Mood:
    emoji: str
    sentiment: float


def get_mood(input_text: str, *, sensitivity: float) -> Mood:  # will return a mood

    # sensitivity will tell the bot which part is positivity and which is negative
    polarity: float = TextBlob(input_text).sentiment.polarity

    friendly_threshold: float = sensitivity
    hostile_threshold: float = sensitivity

    if polarity >= friendly_threshold:
        return Mood('Good', polarity)
    elif polarity <= hostile_threshold:
        return Mood('Bad', polarity)
    else:
        return Mood('Neutral', polarity)


def run_bot():
    print('Enter some text to get a sentiment analysis back: ')
    while True:
        user_input: str = input('You: ')
        mood: Mood = get_mood(user_input, sensitivity=0.3)
        print(f'Bot: {mood.emoji} ({mood.sentiment})')


if __name__ == '__main__':
    run_bot()
