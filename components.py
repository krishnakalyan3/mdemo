import logging
import os
import warnings
import torch
import gradio as gr
import torchvision.transforms as T
from lightning.components.serve import ServeGradio
from lightning.storage import Path
from torch import nn

warnings.simplefilter("ignore")
logger = logging.getLogger(__name__)

class ImageServeGradio(ServeGradio):

    inputs = gr.inputs.Image(type="pil", image_mode="RGB", shape=(300, 300))
    outputs = gr.outputs.Label(num_top_classes=4)

    def __init__(self, cloud_compute, *args, **kwargs):
        super().__init__(*args, cloud_compute=cloud_compute, **kwargs)
        self.examples = None
        self.best_model_path = None
        self._transform = None
        self._labels = {idx: str(idx) for idx in range(10)}

    def run(self, best_model_path):
        self.examples = [os.path.join(str("./example_images"), f) for f in os.listdir("./example_images")]
        self.best_model_path = best_model_path
        self._transform = T.Compose([T.Resize((28, 28)), T.ToTensor()])
        super().run()

    def predict(self, img):
        img = self._transform(img)[0]
        img = img.unsqueeze(0).unsqueeze(0)
        prediction = torch.exp(self.model(img))
        return {self._labels[i]: prediction[0][i].item() for i in range(10)}

    def build_model(self):
        model = torch.load(self.best_model_path)
        for p in model.parameters():
            p.requires_grad = False
        model.eval()
        return model
