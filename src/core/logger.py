import logging
import sys
from typing import ClassVar

from src.core.config import config


class Logger:
    FMT: ClassVar[str] = "%(asctime)s | %(levelname) | %(name)-5s | %(message)s"
    DATEFMT: ClassVar[str] = "%Y-%m-%d %H:%M:%S"

    @classmethod
    def setup(cls, name: str = __name__) -> logging.Logger:
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        if logger.hasHandlers():
            logger.handlers.clear()

        formatter = cls._get_formatter()

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        return logger

    @classmethod
    def _get_formatter(cls) -> logging.Formatter:
        if not config.ENABLE_LOGGER:
            return logging.Formatter("%(message)s")

        return logging.Formatter(fmt=cls.FMT, datefmt=cls.DATEFMT)
