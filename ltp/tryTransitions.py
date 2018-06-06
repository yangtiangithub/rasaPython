from transitions import Machine
from Sentence import Sentence

class DialogueManagement(object):

    #states
    states = ['init_state','singer','singer_song','song',"singer_language","language","label","scene","instrument"]

    def __init__(self):

        self.machine = Machine(model=self,states=DialogueManagement.states,initial="init_state",send_event=True)
        self.machine.add_transition("add_singer","init_state","singer",after="in_singer")
        self.machine.add_transition("singer_add_song","singer","singer_song",after='in_singer_song')
        self.machine.add_transition("finish_call","*","init_state",after="in_init")
        self.machine.add_transition("add_singer_song","init_state","singer_song",after="in_singer_song")
        self.machine.add_transition("add_song","init_state","song",after="in_song")
        self.machine.add_transition("song_add_singer","song","singer_song",after="in_singer_song")
        self.machine.add_transition("singer_add_language","singer","singer_language",after="in_singer_language")
        self.machine.add_transition("add_language","init_state","language",after="in_language")
        self.machine.add_transition("language_add_singer","language","singer_language",after="in_singer_language")
        self.machine.add_transition("add_label","init_state","label",after="in_label")
        self.machine.add_transition("add_scene","init_state","scene",after="in_scene")
        self.machine.add_transition("add_instrument","init_state","instrument",after="in_instrument")

    def in_singer(self,event):
        singer = event.kwargs.get("singer")
        print('state:',self.state)
        print('singer:',singer)
        print("：请问你想听%s的哪首歌，还是哪种语言的歌，还是随机播放？"%(singer))
        u1 = input()
        sentence0 = Sentence(u1)
        if u1.find("随便") != -1 or u1.find("随便") != -1 or u1.find("随机播放")!= -1:
            print("：好的，那我给你随机播放%s的歌" % (singer))
            self.finish_call()
        elif sentence0.intent == "search_by_language":
            self.singer_add_language(singer = singer, language = sentence0.language)
        else:
            song = u1
            self.singer_add_song(singer = singer,song = song)

    def in_singer_song(self,event):
        print('state:', self.state)
        singer = event.kwargs.get('singer')
        song = event.kwargs.get('song')
        print('singer:',singer,'\t','song:','\t',song)
        print("：好的，我帮你搜%s的歌曲%s" % (singer,song))
        self.finish_call()

    def start(self):
        print('state:',self.state)
        u0 = input()
        sentence = Sentence(u0)
        # print(sentence.intent)
        if sentence.intent == "search_by_singer":
            self.add_singer(singer = sentence.singer)
        if sentence.intent == "search_by_singer_song":
            self.add_singer_song(singer = sentence.singer, song = sentence.song)
        if u0.find("搜歌") != -1:
            song = u0[u0.find("搜歌") + 2 : (len(u0))]
            self.add_song(song = song)
        if sentence.intent == "search_by_language":
            language = sentence.language
            self.add_language(language=language)
        if sentence.intent == "search_by_label":
            label = sentence.label
            self.add_label(label = label)
        if sentence.intent == "search_by_scene":
            scene = sentence.scene
            self.add_scene(scene = scene)
        if sentence.intent == "search_by_instrument":
            instrument = sentence.instrument
            self.add_instrument(instrument = instrument)

    def in_init(self,event):
        self.start()
    def in_song(self,event):
        song = event.kwargs.get("song")
        print("state:",self.state)
        print("song:",song)
        print("：好的，我帮你搜歌曲%s" % (song))
        u0 = input()
        u0 = Sentence(u0)
        if u0.singer != None:
            self.song_add_singer(singer = u0.singer,song = song)
        else:
            self.finish_call()
    def in_singer_language(self,event):
        singer = event.kwargs.get("singer")
        language = event.kwargs.get("language")
        print("state:",self.state)
        print("singer:",singer,"\tlanguage:",language)
        print(":好的，我帮你搜%s的%s歌"%(singer,language))
        self.finish_call()
    def in_language(self,event):
        language = event.kwargs.get("language")
        print("state:",self.state)
        print("language:",language)
        print("：好的，我帮你搜%s的歌曲"%(language))
        u0 = input()
        sentence0 = Sentence(u0)
        if sentence0.singer != None:
            singer = sentence0.singer
            self.language_add_singer(singer = singer, language = language)
        else:
            self.finish_call()
    def in_label(self,event):
        label = event.kwargs.get("label")
        print("state:",self.state)
        print("label:",label)
        print("：好的，我帮你搜%s类型的歌曲"%(label))
        self.finish_call()
    def in_scene(self,event):
        scene = event.kwargs.get("scene")
        print("state:",self.state)
        print("scene:",scene)
        print("：好的，我帮你搜适合%s听的歌曲" % (scene))
        self.finish_call()
    def in_instrument(self,event):
        instrument = event.kwargs.get("instrument")
        print("state:",self.state)
        print("instrument:",instrument)
        print("：好的，我帮你搜%s演奏的音乐" % (instrument))
        self.finish_call()

if __name__ == "__main__":
    DM = DialogueManagement()
    DM.start()