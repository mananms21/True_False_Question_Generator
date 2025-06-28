import streamlit as st
import nltk
import os

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    with st.spinner('Downloading NLTK data...'):
        nltk.download('punkt', quiet=True)

try:
    import benepar
    if not os.path.exists(os.path.expanduser('~/.benepar')):
        with st.spinner('Downloading parsing model...'):
            benepar.download('benepar_en3')
except Exception as e:
    st.error(f"Error setting up benepar: {e}")

from functions import *

st.title('True_False_sentence_generator')
text = st.text_area("Text Block", height=200)

if text and len(text.strip()) > 50:
    with st.spinner('Processing text and generating sentences...'):
        try:
            cand_sents = get_candidate_sents(text)
            if not cand_sents:
                st.warning("No suitable sentences found. Please provide a longer text.")
            else:
                filter_quotes_and_questions = preprocess(cand_sents)
                
                if not filter_quotes_and_questions:
                    st.warning("No sentences remaining after filtering. Please provide different text.")
                else:
                    sent_completion_dict = get_sentence_completions(filter_quotes_and_questions)
                    
                    if not sent_completion_dict:
                        st.warning("Could not generate sentence completions. Please try different text.")
                    else:
                        index = 1
                        choice_list = ["a)", "b)", "c)", "d)", "e)", "f)"]
                        
                        for key_sentence in sent_completion_dict:
                            partial_sentences = sent_completion_dict[key_sentence]
                            false_sentences = []
                            print_string = "**%s) True Sentence (from the story) :**" % (str(index))
                            st.markdown(print_string)
                            st.write("  ", key_sentence)
                            
                            for partial_sent in partial_sentences:
                                false_sents = generate_sentences(partial_sent, key_sentence)
                                false_sentences.extend(false_sents)
                            
                            if false_sentences:
                                st.markdown("  **False Sentences (GPT-2 Generated)**")
                                i = 0
                                for ind, false_sent in enumerate(false_sentences):
                                    if ind >= len(choice_list):
                                        break
                                    print_string_choices = "**%s** %s" % (choice_list[ind], false_sent)
                                    st.markdown(print_string_choices)
                                    i = i+1
                                    if (i == 3):
                                        break
                            index = index+1
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.error("Please check your input text and try again.")
elif text:
    st.info("Please enter at least 50 characters of text.")
