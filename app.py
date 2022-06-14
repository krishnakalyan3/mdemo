import os.path as ops
import lightning as L
from components import ImageServeGradio


class TrainDeploy(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.serve_work = ImageServeGradio(cloud_compute=L.CloudCompute("cpu-small"))

    def run(self):
        self.serve_work.run("demo_weights")

    def configure_layout(self):
        tab_grado= {"name": "Interactive demo", "content": self.serve_work}
        return [tab_grado]

app = L.LightningApp(TrainDeploy())
