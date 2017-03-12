# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 10:31:37 2017

@author: Sujit
"""

'''
POS TAG LIST

1.	CC	Coordinating conjunction
2.	CD	Cardinal number
3.	DT	Determiner
4.	EX	Existential there
5.	FW	Foreign word
6.	IN	Preposition or subordinating conjunction
7.	JJ	Adjective
8.	JJR	Adjective, comparative
9.	JJS	Adjective, superlative
10.	LS	List item marker
11.	MD	Modal
12.	NN	Noun, singular or mass
13.	NNS	Noun, plural
14.	NNP	Proper noun, singular
15.	NNPS	Proper noun, plural
16.	PDT	Predeterminer
17.	POS	Possessive ending
18.	PRP	Personal pronoun
19.	PRP$	Possessive pronoun
20.	RB	Adverb
21.	RBR	Adverb, comparative
22.	RBS	Adverb, superlative
23.	RP	Particle
24.	SYM	Symbol
25.	TO	to
26.	UH	Interjection
27.	VB	Verb, base form
28.	VBD	Verb, past tense
29.	VBG	Verb, gerund or present participle
30.	VBN	Verb, past participle
31.	VBP	Verb, non-3rd person singular present
32.	VBZ	Verb, 3rd person singular present
33.	WDT	Wh-determiner
34.	WP	Wh-pronoun
35.	WP$	Possessive wh-pronoun
36.	WRB	Wh-adverb
'''



'''
Identifiers:

\d = any number
\D = anything but a number
\s = space
\S = anything but a space
\w = any letter
\W = anything but a letter
. = any character, except for a new line
\b = space around whole words
\. = period. must use backslash, because . normally means any character.


Modifiers:

{1,3} = for digits, u expect 1-3 counts of digits, or "places"
+ = match 1 or more
? = match 0 or 1 repetitions.
* = match 0 or MORE repetitions
$ = matches at the end of string
^ = matches start of a string
| = matches either/or. Example x|y = will match either x or y
[] = range, or "variance"
{x} = expect to see this amount of the preceding code.
{x,y} = expect to see this x-y amounts of the precedng code
'''


import nltk


NOUN = []
nouns = []
stored = []
Entities = []
Entity = []

f = open('TEST1.txt', 'r')
train_text = f.read()

sentences = nltk.sent_tokenize(train_text)

   

for sent in sentences:
    words = nltk.word_tokenize(sent)
    tags = nltk.pos_tag(words)
    chunks = nltk.ne_chunk(tags, binary = True)
    for i in range(len(chunks)):
        if "NE" in str(chunks[i]):
            Entities.append(chunks[i][0][0])
    for word,tag in tags:
        if(tag == 'NN' or tag == 'NNS' or tag == 'NNP' or tag == 'NNS'):
            nouns.append(word)
for i in Entities:
    if i not in stored:
        Entity.append(i)
        stored.append(i)
stored = []
for i in nouns:
    if i not in stored:
        NOUN.append(i)
        stored.append(i)
print(""""""""""PRINTING ALL NOUNS""""""""""""""") 
print(NOUN)
print("\n")
print(""""""""""PRINTING NAMED ENTITY RECOGNITION""""""""""""""""") 
print(Entity)

