# train_nlu.py £ºtrain NLU model

from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config

#训练模型
def train():
    # 实例数据
    training_data = load_data('data/chatito_output_chn.json')
    # pipeline配置
    trainer = Trainer(RasaNLUConfig("sample_configs/config_jieba_mitie_sklearn.json"))
    trainer.train(training_data)
    model_directory = trainer.persist('./models')  #返回nlu模型的储存位置；如果config文件中没有project_name，模型默认存储在/models/default


#
# from rasa_nlu.training_data import load_data
# from rasa_nlu import config
# from rasa_nlu.components import ComponentBuilder
# from rasa_nlu.model import Trainer
# def train():
#     builder = ComponentBuilder(use_cache=True)      # will cache components between pipelines (where possible)
#
#     training_data = load_data('data/nlu.json')
#     trainer = Trainer(config.load("sample_configs/config_jieba_mitie_sklearn.json"), builder)
#     trainer.train(training_data)
#     model_directory = trainer.persist('./models')  # Returns the directory the model is stored in

#识别意图
def predict(model_directory):
    from rasa_nlu.model import Metadata, Interpreter
    # 用模型初始化interpreter
    interpreter = Interpreter.load(model_directory, RasaNLUConfig("sample_configs/config_jieba_mitie_sklearn.json"))
    # 使用加载的interpreter处理文本
    print("晴天", interpreter.parse("搜歌晴天"))
    print("小情歌", interpreter.parse("小情歌"))

    print("周杰伦", interpreter.parse("搜周杰伦的歌"))
    print("周杰伦", interpreter.parse("我想听周杰伦唱的歌"))
    print("张杰", interpreter.parse("张杰"))
    print("睡觉", interpreter.parse("搜适合睡觉的歌"))
    print("学习", interpreter.parse("搜适合学习的歌"))
    print("纯音乐", interpreter.parse("搜纯音乐类型的歌"))
    print("红歌", interpreter.parse("搜红歌"))



if __name__=='__main__':
    # train()
    predict('models/default/model_20180511-134447')


