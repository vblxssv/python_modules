from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


class InputStage:
    pass


class TransformStage:
    pass


class OutputStage:
    pass


class ProcessingPipeline(ABC):
    def __init__(self):
        self.stages: List = []

    def add_stage(self, stage: Union[InputStage, TransformStage, OutputStage]):
        self.stages.append(stage)


class NexusManager:
    def __init__(self):
        self.pipelines: List[ProcessingPipeline] = []




