from typing import List
from datetime import date

from natasha import (
    Doc,
    MorphVocab,
    Segmenter,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    DatesExtractor,
)
from natasha.extractors import Match
from natasha_utils.helpers import find_dates_as_word, parse_natasha_date_to_datetime