import wikipedia
import spacy
from operator import itemgetter

top_number = 20
nlp = spacy.load('en_core_web_md')

def clean(page_text):
	doc = nlp(wikipedia.page(page_text).content)
	filtered_text = []
	for token in doc:
		if token.pos_ == "NUM" or token.pos_ == "PROPN" or token.pos_ == "NOUN":
		    #if len(filtered_text) != 0 and filtered_text[-1].pos_ == "NUM":
		    	#filtered_text[-1] = filtered_text[-1] + token
		    #else:
		    filtered_text.append(token)
	return filtered_text

def to_tokens_list(string_list):
	concated_list = " ".join(string_list)
	print(concated_list)
	
	print(concated_list)

	doc = nlp(concated_list)
	return doc

def top_list(tuple_list):
	top_scores = []
	for i in range(top_number):
		max_tuple = max(tuple_list, key = lambda x: x[1])
		print(max_tuple)
		top_scores.append(max_tuple)
		tuple_list.remove(max_tuple)
	return top_scores

def most_relevant(list_links, list_words):
	list_links = to_tokens_list(list_links)
	list_words = to_tokens_list(list_words)
	linked_scores = []
	for link in list_links:
		sim = 0
		for word in list_words:
			sim += link.similarity(word)
		linked_scores.append((link,sim))
	return top_list(linked_scores)

