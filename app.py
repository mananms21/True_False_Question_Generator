from functions import *
import streamlit as st
st.title('True_False_sentence_generator')
text = st.text_area("Text Block")
cand_sents = get_candidate_sents(text)
filter_quotes_and_questions = preprocess(cand_sents)
# for each_sentence in filter_quotes_and_questions:
#     print(each_sentence)
#     print("\n")


sent_completion_dict = get_sentence_completions(filter_quotes_and_questions)

# print(sent_completion_dict)

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
    st.markdown("  **False Sentences (GPT-2 Generated)**")
    i = 0
    for ind, false_sent in enumerate(false_sentences):
        print_string_choices = "**%s** %s" % (choice_list[ind], false_sent)
        st.markdown(print_string_choices)
        i = i+1
        if (i == 3):
            break
    index = index+1

    print("\n\n")
