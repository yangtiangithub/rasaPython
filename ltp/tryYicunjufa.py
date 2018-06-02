import Sentence

def testYicunjufa(sentence):
    sentence = Sentence.Sentence(sentence)
    print(sentence.words)
    print('\t'.join('%s, %s' % (arc.head, arc.relation) for arc in sentence.arcs))

if __name__ == "__main__":
    testYicunjufa("我想搜周杰伦的歌")