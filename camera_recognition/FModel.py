from keras.models import model_from_json
import numpy as np

class FModel(object):
    TARGET_LIST = ["1","2","3","4","5","6"]

    def __init__(self, model_json_file,model_weights_file):
        with open(model_json_file,"r") as json_file:
            loaded_model_json = json_file.read()
            self.loaded_model = model_from_json(loaded_model_json)

        self.loaded_model.load_weights(model_weights_file)
        self.loaded_model._make_predict_function()

    def predict_e(self,img):
        self.preds = self.loaded_model.predict(img)
        return FModel.TARGET_LIST[np.argmax(self.preds)]




