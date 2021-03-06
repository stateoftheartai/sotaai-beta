# -*- coding: utf-8 -*-
# Author: Tonio Teran
# Copyright: Stateoftheart AI PBC 2021.
'''NLP Architect's wrapper module.

Model information taken from:
- https://intellabs.github.io/nlp-architect/tagging/sequence_tagging.html
Dataset information taken from:
'''

SOURCE_METADATA = {
    'name': 'nlparchitect',
    'original_name': 'NLP Architect',
    'url': 'https://intellabs.github.io/nlp-architect/'
}

MODELS = {
    'part-of-speech tagging': ['NeuralTagger', 'IDCNN', 'CNNLSTM'],
    'named entity recognition': ['NeuralTagger', 'IDCNN', 'CNNLSTM'],
    'intent extraction': [
        'MultiTaskIntentModel', 'Seq2Seq2IntentModel', 'MostCommonWordSense',
        'NERCRF', 'NP2vec'
    ],
    'semantic segmentation': ['NpSemanticSegClassifier',]
}


def load_model(name: str) -> dict:
  return {'name': name, 'source': 'nlparchitect'}
