# Packages and Depndcy
from typing import Final
import emoji  # make sure to pip install emoji
import config
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update

BOT_TOKEN: Final = config.TOKEN
BOT_USERNAME: Final = config.USERNAME


# Bot initiation commads here
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello there! and Welcome to English Valley Press on /help to find out how to use me')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
    I am a robot built to help you with your TOEFL exams. 
    please note, TOEFL and IELTS are designed to test the following skills 
    Speaking, Reading, Listening and Vocabs.
    
    you can start the trainings with the following commands

    /help -> opens this message box
    /choose -> opens a chat box of available trainings 
    /about -> find out more about me and the English Valley Community
    """)


async def choose_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
    here is a list of trainings I can help you with:

    /listening -> start taking trainings for a TOEFL or IELTS level listening skills
    /Speaking -> start taking spoken English trainings
    /Writing -> start learning from basic to advance Writing skills
    /Reading -> start learning helpful Reading skills
    /Vocab -> learn TOEFL and IELTS vocabs 
    """)


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
    I'm EngValley AI. 
    I was built and Deployed by English Valley team in order to help students prepare for their TOEFL and IELTS exams. I teach using proven online tutoring methods along videos, audio, pdf doc. and many more. 
    
    If you would like to commence training now kindly /choose here
    
    Channel: @EnglishValleyLanguage
    group: @EnglishValleyLanguagage
    """)

# bot tasks here
# speaking section


async def speaking_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(f"""
    BRIEF EXPLAINATION:    
    
    The TOEFL speaking section consists of six tasks that assess your ability to speak in English in an academic setting. The speaking skills that are assessed in the TOEFL include:

1. Speaking clearly and coherently: You will need to speak clearly and coherently, using appropriate grammar and vocabulary.

2. Organizing your ideas: You will need to organize your ideas in a logical and coherent manner, using appropriate transitions and linking words.

3. Expressing your opinion: You will need to express your opinion on a given topic, providing reasons and examples to support your opinion.

4. Summarizing information: You will need to summarize information from a reading passage or a lecture, using your own words.

5. Synthesizing information: You will need to synthesize information from a reading passage and a lecture, and express your opinion on the topic.

6. Responding to questions: You will need to respond to questions asked by the examiner, providing relevant information and examples.

Overall, the TOEFL speaking section assesses your ability to communicate effectively in English in an academic setting, using appropriate grammar, vocabulary, and organization of ideas.
    """)

    await update.message.reply_text(f"""
    Now we shall proceed to the tasks. 

    kindly note, the tasks are time bounded hence if you feel you're not ready please choose a suitable time to start.
    If you're ready{emoji.emojize(':smiling_face_with_smiling_eyes:')} let's get the ball rolling. 
    """)

    await update.message.reply_text(f"""
   Please follow this link to find the material and be reminded to practice along the video.
   The ball is in your court.

   https://t.me/engvalleyAITOEFLSpeakingsection/2
    """)


# listening section
async def listening_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"""
    BRIEF EXPLANATION:

    The TOEFL listening section consists of several audio recordings, each followed by a set of questions. The recordings are taken from academic lectures, classroom discussions, and conversations between students and professors. 

The listening skills that are assessed in the TOEFL include:

1. Understanding main ideas: You will need to identify the main idea of each recording and understand how the details support it.

2. Identifying details: You will need to identify specific details in the recording, such as facts, examples, and definitions.

3. Making inferences: You will need to make logical inferences based on the information presented in the recording.

4. Understanding vocabulary in context: You will need to understand the meaning of words and phrases as they are used in the recording.

5. Understanding the speaker's attitude and purpose: You will need to understand the speaker's attitude and purpose, such as whether they are expressing an opinion, providing information, or making a suggestion.

Overall, the TOEFL listening section is designed to assess your ability to listen and understand academic English spoken at a natural pace.

    """)

# reading section


async def reading_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(f"""
    BRIEF EXPLANATION:

    The TOEFL reading section consists of several passages, each followed by a set of questions. The passages are taken from academic texts, such as textbooks and journal articles, and cover a range of topics in fields such as science, social science, and the humanities. 

The reading skills that are assessed in the TOEFL include:

1. Understanding main ideas: You will need to identify the main idea of each passage and understand how the details support it.

2. Identifying details: You will need to identify specific details in the passage, such as facts, examples, and definitions.

3. Making inferences: You will need to make logical inferences based on the information presented in the passage.

4. Understanding vocabulary in context: You will need to understand the meaning of words and phrases as they are used in the passage.

5. Understanding rhetorical functions: You will need to understand how the author uses language to achieve a particular purpose, such as to persuade, inform, or entertain.

Overall, the TOEFL reading section is designed to assess your ability to read and understand academic texts in English

    
    """)

# vocabs section


async def vocabs_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(f"""
    BRIEF EXPLANATION:

    The TOEFL vocabulary section does not exist as a separate section. However, vocabulary is an important part of both the reading and listening sections of the TOEFL. 

The vocabulary skills that are assessed in the TOEFL include:

1. Understanding word meanings: You will need to understand the meaning of words and phrases as they are used in the context of the passage or recording.

2. Understanding word relationships: You will need to understand how words are related to each other, such as synonyms, antonyms, and word families.

3. Understanding academic vocabulary: You will need to understand academic vocabulary that is commonly used in academic texts and lectures.

4. Understanding idiomatic expressions: You will need to understand idiomatic expressions that are commonly used in English.

5. Using context clues: You will need to use context clues to determine the meaning of unfamiliar words.

Overall, the TOEFL assesses your ability to understand and use a wide range of vocabulary in an academic context.

    """)

# writing section


async def writing_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"""
    BRIEF EXPLANATION:

    The TOEFL writing section consists of two tasks:

1. Integrated Writing Task: In this task, you will read a passage and listen to a lecture on the same topic. You will then write a response that summarizes the main points of both the reading and the lecture and shows the relationship between them.

2. Independent Writing Task: In this task, you will be given a prompt and asked to write an essay in response. You will need to express your opinion on the topic, support your ideas with reasons and examples, and demonstrate your ability to organize and develop your thoughts in a clear and coherent manner.

Both tasks are designed to assess your ability to write in English at an academic level. You will be evaluated on your ability to organize and develop your ideas, use appropriate grammar and vocabulary, and demonstrate your understanding of the topic.
    
    """)

# bot Responses here


def handle_response(text: str):
    processed: str = text.lower()
    if 'hi' in processed:
        return 'Hey there!'
    elif 'hello' in processed:
        return "hi! how may I help you?"
    elif 'hey' in processed:
        return "Ohayo! how is it going?"

    elif 'how are you?' in processed:
        return "I'm fine, thanks for asking. How are you today?"
    elif 'hru' in processed:
        return "I'm good, How are you today?"

    elif "who r u" in processed:
        return "Engvalley AI is my name"
    elif "what's your name?" in processed:
        return "EngValley AI, call me Eng AI for short"
    elif "ur name" in processed:
        return "It's EngValley babe"

    elif 'fine' in processed:
        return "I'm glad you're okey. kindly let me know how I can help you"
    elif 'good' in processed:
        return "I'm glad press /help if you need me"
    elif "i'M fine" in processed:
        return "great!! press /help if you need me"
    elif "i'M okey" in processed:
        return "That's superb!! press /help if you need me"

    elif 'thanks' in processed:
        return "I'm glad I could help. let me know how I can help you /help"
    elif 'tnx' in processed:
        return "just doing my job, no need to thank me press /help if you need me"
    elif 'thank you' in processed:
        return "any time. press /help if you need me"

    elif "I'm sad" in processed:
        return "I am sorry to hear that"

    elif "fuck u" in processed:
        return "Sorry if I did anything wrong"
    elif "fuck" in processed:
        return "lol that's not a polite thing to say"
    elif "shit" in processed:
        return "mmmm..."
    elif "stupid" in processed:
        return "mmmm...I might try to be emotional even if I'm a robot"

    return "Sorry! but I don't understand what you wrote...err"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    if message_type == "group":
        if BOT_USERNAME in text:
            newtext: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(newtext)
        else:
            return
    else:
        response: str = handle_response(text)

    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


# run bot
if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()

    # commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("choose", choose_command))
    app.add_handler(CommandHandler("about", about_command))

    # tasks commands
    app.add_handler(CommandHandler("speaking", speaking_command))
    app.add_handler(CommandHandler("reading", reading_command))
    app.add_handler(CommandHandler("writing", writing_command))
    app.add_handler(CommandHandler("vocab", vocabs_command))
    app.add_handler(CommandHandler("listening", listening_command))

    # bot msg
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # ERRR
    app.add_error_handler(error)

    # checking if bot is initiated
    print('bot is runing...')
    app.run_polling(poll_interval=5)
