from difflib import get_close_matches


# get_close_matches function is used to compare a list and a string and it's going to find the best match in that list


def get_best_match(user_question: str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]  # list comprehension to take the questions out of the dictionary
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    # provide a word or a string that will be the question and compare it to the list of questions
    # it will only return the first best one because it can return multiple
    # the cutoff parameter which is 60% of a match

    if matches:
        return matches[0]


def chat_bot(knowledge: dict):
    while True:
        user_input: str = input('You: ')
        best_match: str | None = get_best_match(user_input, knowledge)

        if answer := knowledge.get(best_match):
            print(f'Bot: {answer}')
        else:
            print('Bot: I do not understand..please try again')


if __name__ == '__main__':
    brain: dict = {'hello': 'Hello!',
                   'How are you?': "I am good, thanks!",
                   'What time is it?': 'I don\'t know',
                   'Goodbye': 'See you later!'}

    chat_bot(knowledge=brain)
