from DialogueManagement import DialogueManagement
from Sentence import Sentence

DM1 = DialogueManagement()
sentence = input()
sentence = Sentence(sentence)
DM1.diliverSlots(sentence)
DM1.diliverIntent(sentence)
DM1.chooseDM(sentence.intent)

# print("singer:",DM1.singer)
# print("song:",DM1.song)
# print("intent:",DM1.intent)
DM1.DM()