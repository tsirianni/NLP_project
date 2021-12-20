## Português

## Comparativo de Estilos de Escrita em Romances Investigativos

### Sobre o projeto

Todos sabem quem Sherlock Holmes é, deficilmente encontrará alguém que não esteja familiarizado(a) com esse nome. Mas um nome pouco conhecido é Anna Katharine Green, uma vez chamda de "a mãe dos romances investigativos" (wikipedia). Ainda de acordo com Wikipedia, ela foi uma das primeiras escritoras de ficção investigativa nos Estados Unidos. Ambos foram escolhidos para este projeto (Anna e Arthur Conan Doyle) por terem seus trabalhos escritos praticamente na mesma época (Anna é apenas 13 anos mais velha do que Arthur). Sendo assim, a análise foca em seus estilos de escrita utilizando estruturas gramaticais em romances investigativos.

Duas estruturas gramaticais são utilizadas para analisar seus estilos com base na frequência em que estas são utilizadas. Este projeto analisa a frequência em que **Noun Phrases** e **Verb Phrases** aparecem nos cinco livros e, com um pouco de sorte, descobriremos algo interessante. Há uma preferência por uma estrutura sobre a outra?

Além disso, a quantidade de detalhes nos livros será analisada para verificar qual autor fornece descrições mais específicas sobre os cenários, personagens, situações, etc. Isso pode ser alcançado analisando a quantidade de adjetivos presente nos livros. Adjetivos podem modificar o significado de muitas palavras. Portanto, sua presença nos livros está diretamente relacionada a complexidade dos mesmos.

Ferramentas e módulos
Visando possiblitar o uso destas estruturas no Python, algumas ferramentas e técnicas foram utilizadas para manipular os textos e filtrar as estruturas. São elas:

* Regular Expressions (regex)
* NLTK - Natural Language Toolkit
* POS tagging (part-of-speech tagging)
* Tokenization
* Chunking
* Syntax Parsing Analysis

**Observação:** Normalização é um processo comum na maioria dos projetos que envolvem NLP. Contudo, neste caso, algumas técnicas como *lemmatization* - trazer as palavras para sua palavra de origem - ou a remoção de palavras gramaticais (stopwords) impossibilitariam o filtro com base nas estruturas gramaticais. Sendo assim, a única técnica de normalização utilizada neste projeto é *tokenization* (quebrar os textos em sentenças e palavras).

Uma lista completa das tags para a função **pos_tag()** pode ser encontrada neste link:<br>
***POS tags:*** https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

As estruturas utilizadas para filtrar **Noun Phrases** e **Verb Phrases** podem ser verificadas no dicionário de gramática de Cambridge:
***Cambridge Grammar Dictionary:***  https://dictionary.cambridge.org/grammar/british-grammar/

### Sobre os livros

Todos estão disponíveis online em domínio público e fazem parte do projeto Gutenberg. Eles podem ser encontrados neste link:<br>
***Project Gutenberg:*** https://www.gutenberg.org/
<br>
<br>

## English

## A Comparison of Writing Styles in Detective-like Novels

### About the project

Everyone knows who Sherlock Holmes is, you'll hardly find someone unfamiliar with this name. But a not very known name is Anna Katherine Green, once called "the mother of detective novel" (Wikipedia). Still according to Wikipedia, she was one of the first writers of detective fiction in the United States. Both were chosen for this analysis (Anna and Arthur Conan Doyle) due to having their books written in similar times (Anna was born only 13 years before Arthur). That being said, this analysis is focused on comparing their writing styles using grammatical structures in detective novels.

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

### About the books

They are ALL available on the Gutenberg Project's website, as public domains. They can all be found through the following link:

***Project Gutenberg:*** https://www.gutenberg.org/
