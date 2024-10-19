from pathlib import Path
from core.containers import Configs, Services
import logging

# Configure logging
logger = logging.getLogger("Analyser")
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def setup_dependencies():
    configs = Configs()

    dummy_path = Path("../").resolve()
    assert dummy_path.exists()

    # skin_model_path = Path("assets/cv_data/weights/model_segmentation_realtime_skin_30.pth").resolve()
    # assert skin_model_path.exists()

    configs.config.update({
        'dummy_path': str(dummy_path)
        # 'skin_model_path': str(skin_model_path),
    })

    # configs.config.update({
    #     'landmark_predictor_path': str(landmark_predictor_path),
    #     'skin_model_path': str(skin_model_path),
    # })

    # Print configuration values
    logger.debug("Configuration loaded:")
    logger.debug(f"dummy_path Path: {configs.config.landmark_predictor_path()}")
    # logger.debug(f"Face Detector Path: {configs.config.face_detector()}")
   # logger.debug(f"Skin Model Path: {configs.config.skin_model_path()}")

    # services = Services()
    services = Services(config=configs.config)
    # services.config.override(configs.config)
    services.configs = configs
    return services


# def setup_dependencies2():
#     configs = Configs()
#
#     landmark_predictor_path = Path("assets/cv_data/weights/shape_predictor_68_face_landmarks.dat").resolve()
#     assert landmark_predictor_path.exists()
#
#     skin_model_path = Path("assets/cv_data/weights/model_segmentation_realtime_skin_30.pth").resolve()
#     assert skin_model_path.exists()
#
#     configs.config.update({
#         'landmark_predictor_path': str(landmark_predictor_path),
#         'skin_model_path': str(skin_model_path),
#     })
#
#     # Print configuration values
#     logger.debug("Configuration loaded:")
#     logger.debug(f"Landmark Predictor Path: {configs.config.landmark_predictor_path()}")
#     # logger.debug(f"Face Detector Path: {configs.config.face_detector()}")
#     logger.debug(f"Skin Model Path: {configs.config.skin_model_path()}")
#
#     # services = Services()
#     services = Services2(config=configs.config)
#     # services.config.override(configs.config)
#     services.configs = configs
#     return services


# def initialize_services(services):
#     # Force initialization by accessing the singleton
#
#     configs = services.configs
#     # configs = services.configs.config
#     logger.debug("initialize_services called")
#     logger.debug(f"Landmark Predictor Path: {configs.config.landmark_predictor_path()}")
#     # logger.debug(f"Face Detector Path: {configs.config.face_detector()}")
#     logger.debug(f"Skin Model Path: {configs.config.skin_model_path()}")
#
#     _ = services.mtcnn()
#
#
#     _ = services.headseg_pipeline()
#     _ = services.landmark_predictor()
#
#     _ = services.facexformerpipeline()
#
#     _ = services.skin_model()
#     _ = services.iie()
#
#     logger.info("All models and resources have been loaded and cached")
#



def initialize_services(services):
    # Force initialization by accessing the singleton

    configs = services.configs
    # configs = services.configs.config
    logger.debug("initialize_services called")
    logger.debug(f"dummy_path: {configs.config.dummy_path()}")
    # logger.debug(f"Face Detector Path: {configs.config.face_detector()}")
    #logger.debug(f"Skin Model Path: {configs.config.skin_model_path()}")

    _ = services.new_chat()

  #  _ = services.mtcnn()
  #  _ = services.headseg_pipeline()
  #  _ = services.landmark_predictor()

    # _ = services.facexformerpipeline()
    #
    # _ = services.skin_model()
    # _ = services.iie()

    logger.info("All models and resources have been loaded and cached")



def main():

    # from image_input_handler import UniversalImageInputHandler
    services = setup_dependencies()
    initialize_services(services)

    new_chat = services.new_chat()
    print(new_chat)



    # test_image_path = "assets/cv_data/testimages/img1_cropped.jpg"
    # uuih = UniversalImageInputHandler(test_image_path)
    # img=uuih.img
    #
    # print("Testing mtcnn...")
    # boxes, probs  = mtcnn.detect(img)
    # x_min, y_min, x_max, y_max = boxes[0][0], boxes[0][1], boxes[0][2], boxes[0][3]
    # x_min = int(x_min)
    # y_min = int(y_min)
    # x_max = int(x_max)
    # y_max = int(y_max)
    # w = x_max - x_min
    # h = y_max - y_min
    # faces = [(x_min, y_min, w, h)]
    # print(faces)
    # print(" ")
    #
    # print("Testing landmark_predictor...")
    # import dlib
    # rect = dlib.rectangle(x_min, y_min, x_max, y_max)
    # import cv2
    # from imutils import face_utils
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # shape = landmark_predictor(gray, rect)
    # # shape = landmark_predictor(gray, faces[0])
    # shape = face_utils.shape_to_np(shape)
    # print(shape)
    # print("len(shape):", len(shape))
    #
    # print("Testing headseg_pipeline...")
    # result=headseg_pipeline(img)
    # print(result)
    #
    # print("Testing facexformer...")
    #
    # result =facexformerpipeline.run_model(img)
    # print(result)

    # skin_model = services.skin_model()

if __name__ == '__main__':
     main()


