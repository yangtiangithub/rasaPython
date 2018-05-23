class DialogueManagement(object):
    def __init__(self):
        # slots
        self.singer = None
        self.song = None
        self.label = None
        self.video = None
        self.video_scene = None
        self.scene = None
        self.mood = None
        self.instrument = None
        self.language = None
        #intent
        self.intent = None
        #选择的意图内DM
        self.DM = None
        #选择不同的意图内对话管理函数
        self.DM_switch = {
            "search_by_singer_song":self.DM_search_by_singer_song,
            "search_by_song":self.DM_search_by_song,
            "search_by_singer":self.DM_search_by_singer,
            "search_by_label":self.DM_search_by_label,
            "search_by_instrument":self.DM_search_by_instrument,
            "search_by_language":self.DM_search_by_language,
            "search_by_language_song":self.DM_search_by_language_song,
            "search_by_video_videoScene":self.DM_search_by_video_videoScene,
            "search_by_scene":self.DM_search_by_scene,
            "search_by_mood":self.DM_search_by_mood
        }
    #传递句子槽值给DM
    def diliverSlots(self,sentence):
        if sentence.singer != None:
            self.singer = sentence.singer
        if sentence.song != None:
            self.song = sentence.song
        if sentence.label != None:
            self.label = sentence.label
        if sentence.video != None:
            self.video = sentence.video
        if sentence.video_scene != None:
            self.video_scene = sentence.video_scene
        if sentence.scene != None:
            self.scene = sentence.scene
        if sentence.mood != None:
            self.mood = sentence.mood
        if sentence.instrument != None:
            self.instrument = sentence.instrument
        if sentence.language != None:
            self.language = sentence.language
    #传递句子意图给DM
    def diliverIntent(self,sentence):
        if sentence.intent != None:
            self.intent = sentence.intent
    #意图内对话管理
    def chooseDM(self,intent):
        if self.intent == None:
            print("还没获取句子意图")
        else:
            self.DM = self.DM_switch[intent]

    #search_by_singer_song 意图内对话管理
    def DM_search_by_singer_song(self):
        print("111")

    def DM_search_by_song(self):
        pass

    def DM_search_by_singer(self):
        pass
    def DM_search_by_label(self):
        pass
    def DM_search_by_instrument(self):
        pass
    def DM_search_by_language(self):
        pass
    def DM_search_by_language_song(self):
        pass
    def DM_search_by_video_videoScene(self):
        pass
    def DM_search_by_scene(self):
        pass
    def DM_search_by_mood(self):
        pass