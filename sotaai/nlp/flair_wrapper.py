# -*- coding: utf-8 -*-
# Author: Tonio Teran
# Copyright: Stateoftheart AI PBC 2021.
'''Flair's wrapper module.

Model information taken from:
Dataset information taken from:
'''

SOURCE_METADATA = {
    'name': 'flair',
    'original_name': 'flair',
    'url': 'https://github.com/flairNLP/flair'
}

DATASETS = {
    'text classification': [
        'AMAZON_REVIEWS', 'COMMUNICATIVE_FUNCTIONS', 'IMDB', 'NEWSGROUPS',
        'SENTEVAL_CR', 'SENTEVAL_MPQA', 'SENTEVAL_MR', 'SENTEVAL_SST_BINARY',
        'SENTEVAL_SST_GRANULAR', 'SENTEVAL_SUBJ', 'SENTIMENT_140', 'TREC_50',
        'TREC_6'
    ],
    'named entity recognition': [
        'BIOFID', 'CONLL_03', 'CONLL_03_DUTCH', 'CONLL_03_GERMAN',
        'CONLL_03_SPANISH', 'DANE', 'LER_GERMAN', 'NER_BASQUE', 'NER_FINNISH',
        'NER_SWEDISH', 'WIKINER_DUTCH', 'WIKINER_ENGLISH', 'WIKINER_FRENCH',
        'WIKINER_GERMAN', 'WIKINER_ITALIAN', 'WIKINER_POLISH',
        'WIKINER_PORTUGUESE', 'WIKINER_RUSSIAN', 'WIKINER_SPANISH', 'WNUT_17'
    ],
    'chunking': ['CONLL_2000'],
    'similarity learning': ['FeideggerCorpus'],
    'unknown': ['GERMEVAL_14'],
    'keyword extraction': ['INSPEC', 'SEMEVAL2010', 'SEMEVAL2017'],
    'universal dependency treebanks': [
        'UD_ARABIC', 'UD_BASQUE', 'UD_BULGARIAN', 'UD_CATALAN', 'UD_CHINESE',
        'UD_CROATIAN', 'UD_CZECH', 'UD_DANISH', 'UD_DUTCH', 'UD_ENGLISH',
        'UD_FINNISH', 'UD_FRENCH', 'UD_GERMAN', 'UD_GERMAN_HDT', 'UD_HEBREW',
        'UD_HINDI', 'UD_INDONESIAN', 'UD_ITALIAN', 'UD_JAPANESE', 'UD_KOREAN',
        'UD_NORWEGIAN', 'UD_PERSIAN', 'UD_POLISH', 'UD_PORTUGUESE',
        'UD_ROMANIAN', 'UD_RUSSIAN', 'UD_SERBIAN', 'UD_SLOVAK', 'UD_SLOVENIAN',
        'UD_SPANISH', 'UD_SWEDISH', 'UD_TURKISH'
    ],
    'text regression': [
        'WASSA_ANGER', 'WASSA_FEAR', 'WASSA_JOY', 'WASSA_SADNESS'
    ],
    'biological named entity recognition': [
        'AnatEM	', 'Arizona Disease	', 'BioCreative II GM	',
        'BioCreative V CDR ', 'BioInfer	', 'BioNLP 2013 Cancer Genetics (ST)',
        'BioNLP 2013 Pathway Curation (ST)', 'BioSemantics*	', 'CellFinder	',
        'CEMP	', 'CHEBI	', 'CHEMDNER', 'CLL', 'DECA	', 'FSU	', 'GPRO	',
        'CRAFT (v2.0)', 'CRAFT (v4.0.1)', 'GELLUS	 ', 'IEPA	', 'JNLPBA	 ',
        'LINNEAUS', 'LocText	,', 'miRNA	', 'NCBI Disease	', 'Osiris v1.2	',
        'Plant-Disease-Relations', 'S800	', 'SCAI Chemicals	', 'SCAI Disease	',
        'Variome'
    ]
}

MODELS = {
    'named entity recognition': [
        'ner', 'ner-fast', 'ner-ontonotes', 'ner-ontonotes-fast', 'ner-multi',
        'multi-ner', 'ner-multi-fast', 'multi-ner-fast', 'ner-multi-fast-learn',
        'multi-ner-fast-learn', 'upos', 'pos', 'upos-fast', 'pos-fast',
        'pos-multi', 'multi-pos', 'pos-multi-fast', 'multi-pos-fast', 'frame',
        'frame-fast', 'chunk', 'chunk-fast', 'da-pos', 'da-ner', 'de-pos',
        'de-pos-tweets', 'de-ner', 'de-ner-germeval', 'fr-ner', 'nl-ner',
        'nl-ner-rnn', 'ml-pos', 'ml-upos', 'keyphrase', 'negation-speculation',
        'de-historic-indirect', 'de-historic-direct', 'de-historic-reported',
        'de-historic-free-indirect'
    ],
    'part-of-speech tagging': [
        'ner', 'ner-fast', 'ner-ontonotes', 'ner-ontonotes-fast', 'ner-multi',
        'multi-ner', 'ner-multi-fast', 'multi-ner-fast', 'ner-multi-fast-learn',
        'multi-ner-fast-learn', 'upos', 'pos', 'upos-fast', 'pos-fast',
        'pos-multi', 'multi-pos', 'pos-multi-fast', 'multi-pos-fast', 'frame',
        'frame-fast', 'chunk', 'chunk-fast', 'da-pos', 'da-ner', 'de-pos',
        'de-pos-tweets', 'de-ner', 'de-ner-germeval', 'fr-ner', 'nl-ner',
        'nl-ner-rnn', 'ml-pos', 'ml-upos', 'keyphrase', 'negation-speculation',
        'de-historic-indirect', 'de-historic-direct', 'de-historic-reported',
        'de-historic-free-indirect'
    ],
    'text classification': [
        'de-offensive-language', 'sentiment', 'en-sentiment', 'sentiment-fast',
        'communicative-functions'
    ]
}


def load_model(name: str) -> dict:
  return {'name': name, 'source': 'flair'}


def load_dataset(name: str) -> dict:
  return {'name': name, 'source': 'flair'}
