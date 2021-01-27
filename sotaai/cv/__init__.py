# -*- coding: utf-8 -*-
# Author: Tonio Teran <tonio@stateoftheart.ai>
# Author: Hugo Ochoa <hugo@stateoftheart.ai>
# Copyright: Stateoftheart AI PBC 2021.
"""Main CV module to abstract away library specific API and standardize."""
from sotaai.cv import utils
from sotaai.cv import abstractions
import importlib


def load_model(name: str) -> abstractions.CvModel:
  """Fetch a model from a specific source, and return standardized object.

  Args:
    name (str):
      Name of the model.

  Returns (abstractions.CvModel):
    The standardized model.
  """
  model_source_map = utils.map_name_sources("models")
  source = model_source_map[name][0]

  wrapper = importlib.import_module("sotaai.cv." + source + "_wrapper")
  raw_object = wrapper.load_model(name)

  return abstractions.CvModel(raw_object, name)


def load_dataset(name: str) -> abstractions.CvDataset:
  """Fetch a dataset from a specific source, and return standardized object.

  Args:
    name (str):
      Name of the dataset.

  Returns (abstractions.CvDataset):
    The standardized dataset.

  # TODO(tonioteran) Add input sanitizer checks to make sure we're loading only
  # available models.
  """
  # TODO(hugo) Switch for new function to get the dataset source.
  ds_source_map = utils.map_name_sources("datasets")
  source = ds_source_map[name][0]

  wrapper = importlib.import_module("sotaai.cv." + source + "_wrapper")
  raw_object = wrapper.load_dataset(name)

  return abstractions.CvDataset(raw_object, name)
