# A Comparison of Writing Styles in Detective-like Novels

## About the project

Everyone knows who Sherlock Holmes is, you'll hardly find someone unfamiliar with this name. But a not very known name is Anna Katherine Green, once called "the mother of detective novel" (Wikipedia). Still according to Wikipedia, she was one of the first writers of detective fiction in the United States. Both were chosen for this analysis due to having their books written in similar times (Anna was born only 13 years before Arthur). That being said, this analysis is focused on comparing their writing styles using grammatical structures in novels about detective work.

The writing style will be compared using two grammatical structures and verifying their frequency throughout the book, this way it will be possible to identify preferences for structures. This project will analyse the frequency of **Noun Phrases** and **Verb Phrases** in the five books and, with some luck, we'll discover something interesting. Is there a preference for one structure over another?

Also, the amount of details in the books will be analysed to see which author provides more complete descriptions of scenarios, characters, situations, etc. This can be done by analysing the amount of adjectives present in the book. Adjectives can modify the meaning of many words. Therefore, their presence in the book is directly related with the detailing of the novel.

Tools and libraries
In order to enable those structures to take place in Python, some tools and techniques were used to not only manipulate the data but also search through it. Those are:

* Regular Expressions (regex)
* NLTK - Natural Language Toolkit
* POS tagging (part-of-speech tagging)
* Tokenization
* Chunking
* Syntax Parsing Analysis


**Note:** Preprocessing/Normalization is a common part of most NLP-related work. However, in this case, some of the techniques like Lemmatization (bringing words to their root word) or Stopwords removal (removing grammatical words such as prepositions) would make the search of patterns through grammatical structures impossible. Therefore, the only preprocessing stage included in this project is tokenization (breaking paragraphs and sentences into smaller units).

The complete table with the labels for the **pos_tag()** function is available in this link:

***POS tags:*** https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

The *Noun Phrase* and *Verb Phrase* structures can be checked on Cambridge's Grammar Dictionary, in the following link:

***Cambridge Grammar Dictionary:***  https://dictionary.cambridge.org/grammar/british-grammar/

## About the books

They are ALL available on the Gutenberg Project's website, as public domains. They can all be found through the following link:

***Project Gutenberg:*** https://www.gutenberg.org/