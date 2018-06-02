from Sentence import Sentence

'''
sentence = Sentence('我要听周杰伦的歌')
print(sentence.words)
print(sentence.postags)
print(sentence.personNames)
print('\t'.join ('%s,%s' % (arc.head,arc.relation)for arc in sentence.arcs))
print(type(sentence.arcs))
print(dir(sentence.arcs))
print('\t'.join ('%s, %s' % (type(arc.head), (type(arc.relation)))for arc in sentence.arcs))
'''

def testSentence(sentence):
    sentence = Sentence(sentence)
    print(sentence.words)
    # print(sentence.singer)
    # print("intent:\t",sentence.intent)
    # print("scene:\t",sentence.scene)
    # print("mood:\t",sentence.mood)
    # print("song:\t",sentence.song)
    # print(sentence.label)
    # print("instrument:","\t",sentence.instrument)
    # print("video:",sentence.video)
    # print("video_scene:",sentence.video_scene)
    print('\t'.join('%s, %s' % (arc.head, arc.relation) for arc in sentence.arcs))
    # for arc in sentence.arcs:
    #     print(arc.head, '\t', arc.relation)
# #%[search_by_singer]
# testSentence("周杰伦")
# testSentence("搜周杰伦")
# testSentence("周杰伦的歌")
# testSentence("搜周杰伦的歌")
# testSentence("帮我搜周杰伦的歌")
# testSentence("我要听周杰伦的歌")
# #%[search_by_song]
# testSentence("晴天")
# testSentence("搜晴天")
# testSentence("搜歌晴天")
# testSentence("我想听晴天")
# #%[search_by_singer_song]
# testSentence("周杰伦的晴天")
# testSentence("我想听周杰伦的晴天")
# testSentence("我想听周杰伦的晴天")
# #%[search_by_label]
# testSentence("伤感类型的歌")
# testSentence("我想听伤感类型的歌")
# #%[search_by_instrument]
# testSentence("钢琴音乐")
# testSentence("我想听钢琴音乐")
# testSentence("钢琴演奏的音乐")
# #%[search_by_language]
# testSentence("粤语歌")
# testSentence("粤语的歌")
# testSentence("我想听粤语的晴天我在哪里")
# #%[search_by_language_song]
# testSentence("粤语的他不懂")
# #%[search_video_videoScene]
# testSentence("火影忍者的主题曲")
# testSentence("夏目友人帐的片尾曲")
# testSentence("琅琊榜的背景音乐")
# #%[search_by_scene]
# testSentence("在学习时听的歌")
# testSentence("在学习时候听的歌")
# testSentence("工作时听的歌")
# testSentence("工作的时候听的歌")
# #%search_by_mood
testSentence("我有点难过")




