# TensorFlow Datasets

Wrapper: [`torch_wrapper.py`](../../../sotaai/cv/torch_wrapper.py)

General Notes:

- Wraps models and datasets of the
  [Torchvision](https://pytorch.org/docs/stable/torchvision/index.html) library.
- Provides standardized functions to load datasets and models: `load_dataset`,
  `load_model`.

## Datasets

Function: `load_dataset`

Return Type: `TorchDatasetDict` (see below)

## Models

Function: `load_model`

Return Type: TODO(huguito)

## Return Types

### `TorchDatasetDict`

A python
[`dict`](https://docs.python.org/3/tutorial/datastructures.html#dictionaries).
For the most part, Each dictionary key corresponds to an object of the same
type\-\-\-`torch.utils.data.dataloader.DataLoader`\-\-\-with a bunch of exceptions:

- `torchvision.datasets.celeba.CelebA`
- `torchvision.datasets.mnist.EMNIST`
- `torchvision.datasets.omniglot.Omniglot`
- `torchvision.datasets.semeion.SEMEION`
- `torchvision.datasets.svhn.SVHN`
- `torchvision.datasets.stl10.STL10`
- `torchvision.datasets.voc.VOCDetection`
- `torchvision.datasets.voc.VOCSegmentation`
- `torchvision.datasets.sbd.SBDataset`
- `torchvision.datasets.phototour.PhotoTour`

Each of the datasets we retrieve is encapsulated by a dictionary, where the
different elements inside the dictionary correspond to a data split. The
possible types of data splits available are:

- `train`:
- `extra_training_set`:
- `val`:
- `evaluation`:
- `test`:
- `data`:
- `unlabeled`:
- `background`:

For a single dataset, all splits are of the same object type; e.g., `CIFAR10`
will be returned as a dictionary with two entries (`train` and `test`), with the
objects corresponding to both keywords being of type
`torch.utils.data.dataloader.DataLoader`.