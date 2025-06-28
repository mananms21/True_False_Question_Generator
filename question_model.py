from transformers import GPT2LMHeadModel, GPT2Tokenizer
from sentence_transformers import SentenceTransformer
import streamlit as st
import torch

@st.cache_resource
def load_question_model():
    try:
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        tokenizer.pad_token = tokenizer.eos_token
        
        model = GPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)
        model.eval()
        
        if torch.cuda.is_available():
            model = model.cuda()
        
        model_BERT = SentenceTransformer('all-MiniLM-L6-v2')
        
        return model, model_BERT, tokenizer
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None, None, None
