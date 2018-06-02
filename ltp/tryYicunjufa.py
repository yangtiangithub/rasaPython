import Sentence

def testYicunjufa(sentence):
    sentence = Sentence.Sentence(sentence)
    print(sentence.words)
    print('\t'.join('%s, %s' % (arc.head, arc.relation) for arc in sentence.arcs))

if __name__ == "__main__":
    testYicunjufa("我想搜周杰伦的歌")
    testYicunjufa("搜周杰伦的歌")
    testYicunjufa("我想搜周杰伦唱的歌")
    testYicunjufa("我想找周杰伦唱的等你下课")
    testYicunjufa("张杰唱的歌他不懂")
    testYicunjufa("周杰伦的等你下课")
    testYicunjufa("帮我搜张杰唱的歌他不懂")
