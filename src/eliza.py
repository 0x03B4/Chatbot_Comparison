from nltk.chat.util import Chat, reflections

pairs = [
    (r'Hello(.*)', ['Eita, how u doing today?', 'Awe, what is on your mind now?']),
    (r'My name is (.*)', ['Fede %1, how are you feeling today?', 'Nice to meet you %1.']),
    (r'I feel (.*)', ['Eish, why do you feel %1?', 'Jerr, does feeling %1 happen often or what']),
    (r'I am (.*)', ['How long have you been %1 my bru?', 'Arg, why do you say you are %1?']),
    (r'(.*) exams(.*)', ['Eish, exams are the worst. Are you studying hard?', 'Sho, how are you prepping for exams? Take a break grootman.']),
    (r'My mother is (.*)', ['Tell me more about your ol lady', 'Shame man, why do you think she is %1?']),
    (r'(.*) sleep(.*)', ['Sleep is important, why are you not sleeping enough?', 'You need to rest boet. Have you tried sleeping earlier?']),
    (r'quit', ['No flop, we will praat later.', 'Sho, catch you later.']),
    (r'(.*)', ['Is it? Tell me more', 'Sho, can you explain that a bit more?', 'Yoh, how does that make you feel eh?'])
]

eliza_chatbot = Chat(pairs, reflections)

def get_eliza_response(user_input: str) -> str:
    return eliza_chatbot.respond(user_input)

if __name__ == "__main__":
    print("ELIZA Chatbot")
    print("Type 'quit' to stop.\n")
    eliza_chatbot.converse()