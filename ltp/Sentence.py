from LtpUtil import LtpUtil

class Sentence(object):
    def __init__(self,sentence):
        self.sentence = sentence
        self.ltpUtil = LtpUtil()
        self.words = list(self.ltpUtil.Segmentor(sentence))
        self.postags = list(self.ltpUtil.Postagger_with_words(self.words))
        self.netags = list(self.ltpUtil.NamedEntityRecognizer_with_wordsAndPostags(self.words, self.postags))
        self.arcs = self.ltpUtil.Parser_with_wordsAndPostags(self.words, self.postags)
        #slots
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
        self.intentList = ["search_by_singer",
                           "search_by_song",
                           "search_by_singer_song",
                           "search_by_label",
                           "search_by_instrument",
                           "search_by_language",
                           "search_by_language_song",
                           "search_video_videoScene",
                           "search_by_scene",
                           "search_by_mood"]
        #init singer
        self.setSinger(self.words, self.postags)
        #init intent
        self.intent = self.judgeIntents()

    #识别句子中人名，并设置为歌手名
    def setSinger(self, words, postags):
        for num in range(len(postags)):
            if postags[num] == 'nh':
                self.singer = words[num]
    #意图识别
    def judgeIntents(self):
        # 含有人名，并且ATT（定中关系）
        # 规则：singer 的 xxx,如果xxx是“歌”，则为search_by_singer，否则为search_by_singer_song
        # 解决意图search_by_singer,search_by_singer_song
        singer_num = None
        if self.singer != None:
            for num in range(len(self.postags)):
                if self.postags[num] == 'nh':
                    singer_num = num
            if self.arcs[singer_num].relation == "ATT":
                self.intent = "search_by_singer_song"
                self.song = self.words[self.arcs[singer_num].head - 1]
                return self.intent
            else:
                self.intent = "search_by_singer"
                return self.intent
        #包含关键词“类型”，则为search_by_label
        #规则xxx类型/一类
        for word in self.words:
            if word == "类型" or word == "一类":
                self.intent = "search_by_label"
                for num in range(len(self.arcs)):
                    if self.arcs[num].relation == "ATT" and self.words[self.arcs[num].head-1] == "类型":
                        self.label = self.words[num]
                return self.intent
        #包含乐器，则为search_by_instrument
        #规则：xxx（乐器）
        instrumentList = ["钢琴",
                          "琵琶",
                          "吉他",
                          "管弦",
                          "缸琴",
                          "葫芦丝",
                          "唢呐",
                          "竖琴",
                          "小提琴",
                          "笛子",
                          "大提琴",
                          "二胡",
                          "风琴",
                          "手风琴",
                          "口琴",
                          "琵琶",
                          "萨克斯"]
        for instrument in instrumentList:
            for word in self.words:
                if instrument == word:
                    self.instrument = instrument
                    self.intent = "search_by_label"
                    return self.intent
        #包含语言，search_by_language
        #规则：xxx(语言)的歌，xxx（语言）歌，xxx（语言）的xxx（歌）
        languageList = [
            "日语",
            "粤语",
            "韩语",
            "华语",
            "德语",
            "印度语",
            "英文",
            "泰国",
            "普通话",
            "葡萄牙语",
            "阿拉伯语",
            "香港话",
            "国语",
            "藏族",
            "蒙语",
            "日语",
            "广东话"]
        for language in languageList:
            for word_num in range(len(self.words)):
                if language == self.words[word_num]:
                    self.language = language
                    # if self.words[word_num+1] == "歌":
                    #     self.intent = "search_by_language"
                    # else:
                    if self.words[word_num+1] != "歌" and self.words[word_num+2] != "歌":
                        self.intent = "search_by_language_song"
                        #合并歌名
                        self.song = ""
                        for word_num1 in range(len(self.words)):
                            if word_num1 > word_num + 1:
                                self.song += self.words[word_num1]
                                return self.intent
                    else:
                        self.intent = "search_by_language"
                        return self.intent

        #包含关键词：背景音乐，主题曲，片尾曲,对应意图search_by_videoScene
        #规则：xxx的背景音乐/主题曲/片尾曲,xxx背景音乐/主题曲/片尾曲
        sceneIndex1 = self.sentence.find("背景音乐")
        sceneIndex2 = self.sentence.find("主题曲")
        sceneIndex3 = self.sentence.find("片尾曲")
        if sceneIndex1 != -1:
            self.intent = "search_by_videoScene"
            self.video_scene = "背景音乐"
            if self.sentence[sceneIndex1-1] == "的":
                self.video = self.sentence[0:sceneIndex1-1]
            else:
                self.video = self.sentence[0:sceneIndex1]
            return self.intent
        if sceneIndex2 != -1:
            self.video_scene = "主题曲"
            self.intent = "search_by_videoScene"
            if self.sentence[sceneIndex2-1] == "的":
                self.video = self.sentence[0 : (sceneIndex2 +1)]
            else:
                self.video = self.sentence[0:sceneIndex2]
            return self.intent
        if sceneIndex3 != -1:
            self.video_scene = "片尾曲"
            self.intent = "search_by_videoScene"
            if self.sentence[sceneIndex3-1] == "的":
                self.video = self.sentence[0:sceneIndex3-1]
            else:
                self.video = self.sentence[0:sceneIndex3]
            return self.intent
        #分词含有关键词“时”、“时候”，考虑是scene查找，主要是ATT(定中关系)，定语就是scene,解决意图search_by_scene
        #规则：xxx(的)时/时候
        scene_num = None
        scene_time_num = None
        for word_num in range(len(self.words)):
            if self.words[word_num] == "时" or self.words[word_num] == "时候":
                scene_time_num = word_num
                for arc_num in range(len(self.arcs)):
                    if self.arcs[arc_num].relation == "ATT" and self.arcs[arc_num].head - 1 == scene_time_num:
                        self.scene = self.words[arc_num]
                        self.intent = "search_by_scene"
                        return self.intent
        #前面几个意图识别都错过，考虑剩下一个按照心情匹配，匹配心情的关键词，解决意图search_by_mood
        #规则：xxx（心情）
        mood_num = None
        moodList = ["兴奋",
                    "愉快",
                    "欢乐",
                    "欢悦",
                    "孤单",
                    "喜悦",
                    "开心",
                    "昂奋",
                    "忧伤",
                    "难过",
                    "寂寞",
                    "抑郁",
                    "哀愁",
                    "欣喜",
                    "快乐",
                    "难受",
                    "哀伤",
                    "伤感",
                    "感动",
                    "孤独",
                    "激动",
                    "高兴",
                    "欢愉",
                    "焦虑"]
        for word_num in range(len(self.words)):
            for mood in moodList:
                if self.words[word_num] == mood:
                    self.mood = mood;
                    self.intent = "search_by_mood"
                    return self.intent







