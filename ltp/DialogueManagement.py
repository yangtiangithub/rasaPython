def DialogueManagement(object):
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

        self.intent = None

        #选择不同的意图内对话管理函数
        self.DM_switch = {
            "search_by_singer_song":DM_search_by_singer_song(),
            "search_by_song":DM_search_by_song(),
            "search_by_singer":DM_search_by_singer(),
            "search_by_label":DM_search_by_label(),
            "search_by_instrument":DM_search_by_instrument(),
            "search_by_language":DM_search_by_language(),
            "search_by_language_song":DM_search_by_language_song(),
            "search_by_video_videoScene":DM_search_by_video_videoScene(),
            "search_by_scene":DM_search_by_scene(),
            "search_by_mood":DM_search_by_mood()
        }

    #意图内对话管理
    #search_by_singer_song 意图内对话管理
    def DM_search_by_singer_song(self):
        pass

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