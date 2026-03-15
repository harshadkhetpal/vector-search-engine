# Author: Harshad Khetpal
from sentence_transformers import SentenceTransformer
import numpy as np

_model = None

def get_embedder(model_name: str = "BAAI/bge-m3"):
    global _model
    if _model is None:
        _model = SentenceTransformer(model_name)
    return _model
