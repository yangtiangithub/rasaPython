# -*- coding: utf-8 -*-
import pyltp

class LtpUtil(object):

    def __init__(self, seg_model_path = './ltp_data_v3.4.0/cws.model', seg_lexicon_path = './lexicon/lexicon_test',
                 pos_model_path = './ltp_data_v3.4.0/pos.model', rec_model_path = './ltp_data_v3.4.0/ner.model',
                 par_model_path = './ltp_data_v3.4.0/parser.model'):
        self.seg_lexicon_path = seg_lexicon_path
        self.segmentor = pyltp.Segmentor()
        self.seg_model_path = seg_model_path
        self.segmentor.load(self.seg_model_path)

        self.postagger = pyltp.Postagger()
        self.pos_model_path = pos_model_path
        self.postagger.load(self.pos_model_path)

        self.recognizer = pyltp.NamedEntityRecognizer()
        self.rec_model_path = rec_model_path
        self.recognizer.load(rec_model_path)

        self.parser = pyltp.Parser()
        self.par_model_path = par_model_path
        self.parser.load(self.par_model_path)

    # segment
    def Segmentor(self, sentence):
        words = self.segmentor.segment(sentence)
        return words

    # postagger
    def Postagger(self,sentence):
        words = self.Segmentor(sentence)
        postags = self.postagger.postag(words)
        return postags
    def Postagger_with_words(self,words):    #省略words过程
        postags = self.postagger.postag(words)
        return postags

    # named entity recognizer
    def NamedEntityRecognizer(self,sentence = None):
        words = self.Segmentor(sentence)
        postags = self.Postagger(sentence)
        netags = self.recognizer.recognize(words, postags)
        return netags
    def NamedEntityRecognizer_with_wordsAndPostags(self,words,postags):    #省略words和postags过程
        netags = self.recognizer.recognize(words, postags)
        return netags

    # parser
    def Parser(self,sentence = None):
        words = self.Segmentor(sentence)
        postags = self.Postagger(sentence)
        arcs = self.parser.parse(words, postags)
        return arcs
    def Parser_with_wordsAndPostags(self,words,postags):    #省略words和postags过程
        arcs = self.parser.parse(words, postags)
        return arcs

    def __del__(self):
        if self.segmentor != None:
            self.segmentor.release()

        if self.postagger != None:
            self.postagger.release()

        if self.recognizer != None:
            self.recognizer.release()

        if self.parser != None:
            self.parser.release()