from abc import ABC, abstractmethod
from pathlib import Path


class BaseTemplate(ABC):

    @abstractmethod
    def render(self, src_dir: Path, dst_dir: Path) -> None:
        pass
