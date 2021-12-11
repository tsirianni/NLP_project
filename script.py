from nltk.tokenize import PunktSentenceTokenizer, word_tokenize
from nltk import pos_tag, RegexpParser
from collections import Counter


# Import books
sh_adventures = open("The Adventures of Sherlock Holmes.txt",encoding='utf-8').read().lower()

sh_memoirs = open("The Memoirs of Sherlock Holmes.txt",encoding='utf-8').read().lower()

sh_return = open("The Return of Sherlock Holmes.txt",encoding='utf-8').read().lower()

anna_leavenworth = open("THE LEAVENWORTH CASE.txt",encoding='utf-8').read().lower()

anna_nd_affair = open("THAT AFFAIR NEXT DOOR.txt",encoding='utf-8').read().lower()


# Tokenization
def book_tokenizer(book): # Tokenizes by both sentence and words
    sentence_tokenizer = PunktSentenceTokenizer(book)
    tokenized_sentence = sentence_tokenizer.tokenize(book)
    
    tokenized_words = list()
    
    for sentence in tokenized_sentence:
        tokenized_words.append(word_tokenize(sentence))
    
    return tokenized_words

tokenized_sh_adventures = book_tokenizer(sh_adventures)
tokenized_sh_memoirs = book_tokenizer(sh_memoirs)
tokenized_sh_return = book_tokenizer(sh_return)
tokenized_anna_leavenworth = book_tokenizer(anna_leavenworth)
tokenized_anna_nd_affair= book_tokenizer(anna_nd_affair)


# Part-of-speech tag
def book_tagging(book):
    
    tagged_book = []
    
    for word in (book):
        tagged_book.append(pos_tag(word))
    
    return tagged_book


# Tagged books
tagged_sh_adventures = book_tagging(tokenized_sh_adventures)
tagged_sh_memoirs = book_tagging(tokenized_sh_memoirs)
tagged_sh_return = book_tagging(tokenized_sh_return)
tagged_anna_leavenworth = book_tagging(tokenized_anna_leavenworth)
tagged_anna_nd_affair = book_tagging(tokenized_anna_nd_affair)


# Defining the grammatical structures
np_chunk = "NP: {<DT><JJ>*<NN.>?<NN.>}" # Noun Phrase
np_parser = RegexpParser(np_chunk)

vp_chunk = "VP: {<MD><V..?>*<V..?>}" # Verb Prhase
vp_parser = RegexpParser(vp_chunk)


# Defining counters
def np_chunk_counter(chunked_sentences):
    
    chunks = list()

    for chunked_sentence in chunked_sentences:
        for subtree in chunked_sentence.subtrees(filter=lambda t: t.label() == 'NP'):
            chunks.append(tuple(subtree))

    chunk_counter = Counter()

    for chunk in chunks:
        chunk_counter[chunk] += 1

    return chunk_counter

def vp_chunk_counter(chunked_sentences):

    chunks = list()

    for chunked_sentence in chunked_sentences:
        for subtree in chunked_sentence.subtrees(filter=lambda t: t.label() == 'VP'):
            chunks.append(tuple(subtree))

    chunk_counter = Counter()

    for chunk in chunks:
        chunk_counter[chunk] += 1

    return chunk_counter

# Book Analysis - Adventures of Sherlock Holmes
np_chunks_sh_adventures = []
vp_chunks_sh_adventures = []

for word in tagged_sh_adventures:
    np_chunks_sh_adventures.append(np_parser.parse(word))
    vp_chunks_sh_adventures.append(vp_parser.parse(word))


np_chunk_counter(np_chunks_sh_adventures)
len(np_chunk_counter(np_chunks_sh_adventures))

vp_chunk_counter(vp_chunks_sh_adventures)
len(vp_chunk_counter(vp_chunks_sh_adventures))

# Common chunks
def np_common_chunks(chunked_sentences):
    
    chunks = list()

    for chunked_sentence in chunked_sentences:
        for subtree in chunked_sentence.subtrees(filter=lambda t: t.label() == 'NP'):
            chunks.append(tuple(subtree))

    chunk_counter = Counter()

    for chunk in chunks:
        chunk_counter[chunk] += 1

    return chunk_counter.most_common(15)


def vp_common_chunks(chunked_sentences):

    chunks = list()

    for chunked_sentence in chunked_sentences:
        for subtree in chunked_sentence.subtrees(filter=lambda t: t.label() == 'VP'):
            chunks.append(tuple(subtree))

    chunk_counter = Counter()

    for chunk in chunks:
        chunk_counter[chunk] += 1

    return chunk_counter.most_common(15)

np_common_chunks(np_chunks_sh_adventures)
vp_common_chunks(vp_chunks_sh_adventures)

# The Memoirs of Sherlock Holmes

np_chunks_sh_memoirs = []
vp_chunks_sh_memoirs = []

for word in tagged_sh_memoirs:
    np_chunks_sh_memoirs.append(np_parser.parse(word))
    vp_chunks_sh_memoirs.append(vp_parser.parse(word))

np_chunk_counter(np_chunks_sh_memoirs)
len(np_chunk_counter(np_chunks_sh_memoirs))
vp_chunk_counter(vp_chunks_sh_memoirs)
len(vp_chunk_counter(vp_chunks_sh_memoirs))

np_common_chunks(np_chunks_sh_memoirs)
vp_common_chunks(vp_chunks_sh_memoirs)

# The Return of Sherlock Holmes

np_chunks_sh_return = []
vp_chunks_sh_return = []

for word in tagged_sh_return:
    np_chunks_sh_return.append(np_parser.parse(word))
    vp_chunks_sh_return.append(vp_parser.parse(word))

np_chunk_counter(np_chunks_sh_return)
len(np_chunk_counter(np_chunks_sh_return))
vp_chunk_counter(vp_chunks_sh_return)
len(vp_chunk_counter(vp_chunks_sh_return))

np_common_chunks(np_chunks_sh_return)
vp_common_chunks(vp_chunks_sh_return)

# The Leavenworth Case

np_chunks_leavenworth = []
vp_chunks_leavenworth = []

for word in tagged_anna_leavenworth:
    np_chunks_leavenworth.append(np_parser.parse(word))
    vp_chunks_leavenworth.append(vp_parser.parse(word))

np_chunk_counter(np_chunks_leavenworth)
len(np_chunk_counter(np_chunks_leavenworth))
vp_chunk_counter(vp_chunks_leavenworth)
len(vp_chunk_counter(vp_chunks_leavenworth))

np_common_chunks(np_chunks_leavenworth)
vp_common_chunks(vp_chunks_leavenworth)

# That Affair Next Door

np_chunks_nd_affair = []
vp_chunks_nd_affair = []

for word in tagged_anna_nd_affair:
    np_chunks_nd_affair.append(np_parser.parse(word))
    vp_chunks_nd_affair.append(vp_parser.parse(word))

np_chunk_counter(np_chunks_nd_affair)
len(np_chunk_counter(np_chunks_nd_affair))
vp_chunk_counter(vp_chunks_nd_affair)
len(vp_chunk_counter(vp_chunks_nd_affair))

np_common_chunks(np_chunks_nd_affair)
vp_common_chunks(vp_chunks_nd_affair)


# Complexity Analysis

adj = "ADJ: {<JJ.?>*}"
adj_parser = RegexpParser(adj)

sh_adventures_complexity = []

for adjective in tagged_sh_adventures:
    sh_adventures_complexity.append(adj_parser.parse(adjective))

def adjective_counter(chunked_sentences):
    
    chunks = list()

    for chunked_sentence in chunked_sentences:
        for subtree in chunked_sentence.subtrees(filter=lambda t: t.label() == 'ADJ'):
            chunks.append(tuple(subtree))

    chunk_counter = Counter()

    for chunk in chunks:
        chunk_counter[chunk] += 1

    return chunk_counter

adjective_counter(sh_adventures_complexity)
len(adjective_counter(sh_adventures_complexity))


# Memoir
sh_memoirs_complexity = []

for adjective in tagged_sh_memoirs:
    sh_memoirs_complexity.append(adj_parser.parse(adjective))

adjective_counter(sh_memoirs_complexity)
len(adjective_counter(sh_memoirs_complexity))

# Return
sh_return_complexity = []

for adjective in tagged_sh_return:
    sh_return_complexity.append(adj_parser.parse(adjective))

adjective_counter(sh_return_complexity)
len(adjective_counter(sh_return_complexity))

# Leavenworth
leavenworth_complexity = []

for adjective in tagged_anna_leavenworth:
    leavenworth_complexity.append(adj_parser.parse(adjective))

adjective_counter(leavenworth_complexity)
len(adjective_counter(leavenworth_complexity))

# That Affair
nd_affair_complexity = []

for adjective in tagged_anna_nd_affair:
    nd_affair_complexity.append(adj_parser.parse(adjective))

adjective_counter(nd_affair_complexity)
len(adjective_counter(nd_affair_complexity))