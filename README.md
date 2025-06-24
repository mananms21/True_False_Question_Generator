# True_False_App
We want to generate true false questions from the given text. We have used 2 approaches till now to generate false sentences-

1. We have done extractive summarisation using bert-extractive-summarizer and then identified keywords from the summarized text using PKE. Then we have generated distractors for the generated keywords sense2vec and then replaced those distractors in the sentences containing those keywords.

2. We have used the Berkley Constituency parser to split a sentence at ending verb phrase or noun phrase. Eg : If the input sentence is "Divergent plate boundaries also occur in the continental crust" we split it at the ending noun phrase to get "Divergent plate boundaries also occur in". Now we give the partial sentence "Divergent plate boundaries also occur in" to OpenAI GPT-2 to generate sentences with different endings. Now, among the generated sentences, we have filtered the ones that are similar using Sentence BERT, since we want to keep only dissimilar ones as False sentences.
