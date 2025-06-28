from transformers import GPT2LMHeadModel, GPT2Tokenizer, AutoTokenizer, AutoModel
import streamlit as st
import torch
import numpy as np

class SimpleBertEncoder:
    def __init__(self):
        # Use DistilBERT instead - smaller and doesn't use sentencepiece
        self.tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')
        self.model = AutoModel.from_pretrained('distilbert-base-uncased')
        self.model.eval()
    
    def encode(self, sentences):
        if isinstance(sentences, str):
            sentences = [sentences]
        
        embeddings = []
        for sentence in sentences:
            inputs = self.tokenizer(sentence, return_tensors='pt', 
                                  truncation=True, padding=True, max_length=512)
            
            with torch.no_grad():
                outputs = self.model(**inputs)
                # Use [CLS] token embedding (first token)
                sentence_embedding = outputs.last_hidden_state[:, 0, :].squeeze()
                embeddings.append(sentence_embedding.numpy())
        
        return np.array(embeddings)

@st.cache_resource()
def load_question_model():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained(
        "gpt2", pad_token_id=tokenizer.eos_token_id)
    model_BERT = SimpleBertEncoder()

    return model, model_BERT, tokenizer
