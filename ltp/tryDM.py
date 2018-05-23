from DialogueManagement import DialogueManagement
from Sentence import Sentence

DM1 = DialogueManagement()
sentence1 = Sentence("我想听周杰伦的晴天")
DM1.diliverSlots(sentence1)
DM1.diliverIntent(sentence1)
DM1.chooseDM(sentence1.intent)

print("singer:",DM1.singer)
print("song:",DM1.song)
print("intent:",DM1.intent)
DM1.DM()