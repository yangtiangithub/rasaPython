from transitions import Machine
from Sentence import Sentence

class DiologueManagement(object):

    #states
    states = ['init_state','singer','singer_song']

    def __init__(self):

        self.machine = Machine(model=self,states=DiologueManagement.states,initial="init_state",send_event=True)
        self.machine.add_transition("add_singer","init_state","singer",after="in_singer")
        self.machine.add_transition("singer_add_song","singer","singer_song",after='in_singer_song')

    def in_singer(self,event):
        singer = event.kwargs.get("singer")
        print("请问你想听%s的哪首歌，还是随机播放？"%(singer))
        u1 = input()
        if u1 == "随便吧" or u1 == "随意吧" or u1 == "随机播放":
            print("：好的，那我给你随机播放%s的歌" % (singer))
        # elif:
        #     sentence0 =
        else:
            song = u1
            self.machine.singer_add_song(singer = singer,song = song)

    def in_singer_song(self,event):
        singer = event.kwargs.get('singer')
        song = event.kwargs.get('song')
        print("帮你搜%s的%s" % (singer,song))

    def start(self):
        u0 = input()
        sentence = Sentence(u0)
        if sentence.intent == "search_by_singer":
            self.add_singer(singer = sentence.singer)


if __name__ == "__main__":
    DM = DiologueManagement()
    DM.start()