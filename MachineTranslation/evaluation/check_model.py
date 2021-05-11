from transformers import AutoModelWithLMHead, RobertaTokenizerFast
model_path = "../models/en_cycl_2021_03_27_06_25_49"

model = AutoModelWithLMHead.from_pretrained(model_path)
tokenizer = RobertaTokenizerFast.from_pretrained(model_path, max_len=512)
#
# english_sentences_to_translate = [
#     'What is the capital of Poland?',
#     'Who is the richest man in the World?',
#     'Do aliens exist?',
#     "Her music is noted for its stylized, cinematic quality and exploration of themes of sadness, tragic romance, glamor, and melancholia, containing many references to pop culture, particularly 1950s and 1960s Americana.",
#     "Elizabeth Woolridge Grant (born June 21, 1985), known professionally as Lana Del Rey, is an American singer-songwriter and record producer.",
#     "Elizabeth Woolridge Grant, known professionally as Lana Del Rey, is an American singer-songwriter and record producer.",
#     "The following is a partial list of linguistic example sentences illustrating various linguistic phenomena.",
#     "The multi-word phrase containing the word \"end\" and trade and relations is verb and denotes terminating trade relations.",
#     "Wojtek is a human being.",
#     "Aleksander teaches at a university.",
#     "The multi-word phrase containing minimum and balance and the word \"fee\" is count noun and denotes minimum balance charge.",
#     "The solomon islands is a member of the international community.",
#     "Cramer the name is a lexical word.",
#     "Absolute vodka is a type of object.",
#     "The word \"favorable\" is an english word.",
#     "Every cabinet has some front portal as a proper part.",
#     "Pencil eraser is marketed as stationery product.",
#     "The atomic number of osmium is 76.",
#     "A newborn baby is a type of newborn animal.",
#     ""
# ]

english_sentences_to_translate = [
"She doesn’t study German on Monday.",
"Does she live in Paris?",
"He doesn’t teach math.",
"Cats hate water.",
"Every child likes an ice cream.",
"My brother takes out the trash.",
"The course starts next Sunday.",
"She swims every morning.",
"I don’t wash the dishes.",
"We see them every week.",
"I don’t like tea.",
"When does the train usually leave?",
"She always forgets her purse.",
"You don’t have children.",
"I and my sister don’t see each other anymore.",
"They don’t go to school tomorrow.",
"He loves to play basketball.",
"He goes to school.",
"The Earth is spherical.",
"Julie talks very fast.",
"My brother’s dog barks a lot.",
"Does he play tennis?",
"The train leaves every morning at 18 AM.",
"Water freezes at 0°C",
"I love my new pets.",
"We drink coffee every morning.",
"My Dad never works on the weekends.",
"She doesn’t teach chemistry.",
"I do love my new pets.",
"Mary brushes her teeth twice a day.",
"He drives to work.",
"Mary enjoys cooking.",
"She likes bananas.",
"My mother never lies.",
"You don’t listen to me.",
"I run four miles every morning.",
"They speak English at work.",
"The train does not leave at 12 AM.",
"I have no money at the moment.",
"Do they talk a lot?",
"Tomorrow early morning first I go to morning walk.",
"Does she drink coffee?",
"You run to the party.",
"You have some schoolwork to do.",
"She doesn’t use a computer.",
"It snows a lot in winter in Russia.",
"We live in Texas.",
"You go to holiday every summer.",
"Do you like spaghetti?",
"My daughter does the laundry."
]
for english_sentence in english_sentences_to_translate:
    inputs = tokenizer.encode(english_sentence, return_tensors="pt")
    outputs = model.generate(inputs)
    output = tokenizer.decode(outputs[0])
    translated_word = output.split('</s>')[0].replace('<s>', '')
    print(english_sentence)
    print(translated_word)
    # print(output)
    print()
