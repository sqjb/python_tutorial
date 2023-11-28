import abc
import dataclasses
from abc import ABC


class Model(metaclass=abc.ABCMeta):
    """AI model base class"""

    def __init__(self, model_type, model_name, version):
        self.model_type = model_type
        self.model_name = model_name
        self.__version = version

    def __str__(self):
        return f"{self.model_type}-{self.model_name}-{self.__version}"

    def update_version(self, ver):
        self.__version = ver

    @abc.abstractmethod
    def run(self):
        pass


class YoloModel(Model):
    """Yolo model"""

    def __init__(self, model_type, model_name, version, config):
        super().__init__(model_type, model_name, version)
        self.__config = config

    def run(self):
        print(f"{self.__doc__} {self} running")


@dataclasses.dataclass
class Vector:
    x: int
    y: int
    name: str


v1 = Vector(1, 2, "abc")
v2 = Vector(3, 3, "def")
print(v1.x, v1.y, v1.name)
print(v2.x, v2.y, v2.name)

yolo = YoloModel("yolov5", "yolov5s", "v6.0", "")
yolo.run()

