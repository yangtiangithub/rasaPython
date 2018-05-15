# script/train_dm.py

from rasa_core.agent import Agent
from rasa_core.policies.memoization import MemoizationPolicy

# ÑµÁ·policyÄ£ÐÍ
def train_mom_dm():
    agent = Agent("../mom/domain.yml",
                  policies=[MemoizationPolicy()])

    agent.train(
            training_data_file,
            max_history=3,
            epochs=100,
            batch_size=50,
            augmentation_factor=50,
            validation_split=0.2
    )

    agent.persist(model_path)