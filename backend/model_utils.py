import base64, io, json, os
import numpy as np
from PIL import Image
from keras.models import load_model

MODEL_INPUT_SHAPE = (224, 224)


def get_model(
        model_path: str
        ):
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    model = load_model(model_path)
    return model

def get_clf_model():
    model_path = 'models/InceptionResNetV2.h5'
    model = get_model(model_path)
    return model

def clf_breed(
        model,
        image_bytes: bytes,
        top_n: int=3
        ) -> dict:
    """
    This function takes in a model and an image-64-bit data and returns the top N breeds with probability percentages.
    """
    image = preprocess_image(image_bytes)
    prediction = model.predict(image)[0]

    with open("models/breeds_dict.json") as f:
        breed_dict = json.load(f)

    top_n_pred_score = np.argsort(prediction)[-top_n:][::-1]
    top_n_pred_breed = {
                breed_dict[str(i)]: float(prediction[i])
                for i in top_n_pred_score
            }
    return top_n_pred_breed

def preprocess_image(image_bytes: bytes) -> np.ndarray:
    """
    Preprocess the image to be used for prediction.
    """
    # Resize the image to the model input shape
    image = Image.open(io.BytesIO(base64.decodebytes(image_bytes)))
    image = image.resize(MODEL_INPUT_SHAPE).convert('RGB')
    image = np.array([np.array(image)]) / 255
    return image
