from dependency_injector import containers, providers
# from headswapper.utils.image_info_extractor import ImageInfoExtractor
# import head_segmentation.segmentation_pipeline as seg_pipeline
import logging
from langchain_community.llms import Ollama
logger = logging.getLogger("_")


# def load_skin_model(skin_model_path):
#     state_dict = torch.load(skin_model_path, map_location=torch.device("cpu"))
#     model = BiSeNetV2(["skin"])
#     model.load_state_dict(state_dict)
#     model.eval()
#     return model

class Configs(containers.DeclarativeContainer):
    config = providers.Configuration()

class Services(containers.DeclarativeContainer):

    config = providers.Configuration()

    from chat import Chat
    # Chat(users, allowed_models, chat_history=None, configs=None)
    from chat import  ChatUser

    cu = ChatUser("user", ["gpt-4o", "gpt-4o-mini", "o1-preview", "o1-mini"], "all", False)
    allowed_models = ["gpt-4o", "gpt-4o-mini", "o1-preview", "o1-mini"]
    # self.chat_history = ChatHistory()

    new_chat = providers.Singleton(
        Chat,
        users=[cu],
        allowed_models=allowed_models,
        # logger=logger,
        configs=None
    )

    #users = [user1], allowed_models = allowed_models, logger = logger

    # providers.Callable(









