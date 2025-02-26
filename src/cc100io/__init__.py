# -*- coding: utf-8 -*-

from importlib.metadata import version

from .io import digitalWrite, analogWrite, digitalRead, digitalReadWait, analogRead, delay, tempRead

__version__ = version("cc100io")
