from transformers import GPT2LMHeadModel, GPT2Tokenizer
import streamlit as st
import torch
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class BertAlternativeEncoder:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            stop_words='english', 
            max_features=5000,
            ngram_range=(1, 2),
            sublinear_tf=True
        )
        self.is_fitted = False
    
    def encode(self, sentences):
        if isinstance(sentences, str):
            sentences = [sentences]
        
        if not self.is_fitted:
            # Fit on all sentences to ensure consistent feature space
            all_sentences = sentences
            self.vectorizer.fit(all_sentences)
            self.is_fitted = True
        
        vectors = self.vectorizer.transform(sentences)
        return vectors.toarray()

@st.cache_resource()
def load_question_model():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained(
        "gpt2", pad_token_id=tokenizer.eos_token_id)
    model_BERT = BertAlternativeEncoder()

    return model, model_BERT, tokenizer
