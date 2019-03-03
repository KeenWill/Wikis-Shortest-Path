import wikipedia
import spacy
from operator import itemgetter

top_number = 20
nlp = spacy.load('en_core_web_md')

def clean(page_text):
	try:
		doc = nlp(wikipedia.summary(page_text))
	except:
		return []
	filtered_text = []
	for token in doc:
		if not contains(token, filtered_text) and\
		(token.pos_ == "NUM" or token.pos_ == "PROPN" or token.pos_ == "NOUN"):
		    #if len(filtered_text) != 0 and filtered_text[-1].pos_ == "NUM":
		    	#filtered_text[-1] = filtered_text[-1] + token
		    #else:
		    filtered_text.append(token)
	return filtered_text

def contains(tkn, tkn_list):
	for t in tkn_list:
		if str(t) == str(tkn):
			return True

	return False

# def to_tokens_list(string_list):
# 	return [Token.__init__(s) for s in string_list]

# 	# concated_list = ""
# 	# for s in string_list:
# 	# 	concated_list += (s + ' ')

# 	# doc = nlp(concated_list)
# 	# return doc

# def top_list(tuple_list):
# 	top_scores = []
# 	for i in range(top_number):
# 		max_tuple = max(tuple_list, key = lambda x: x[1])
# 		top_scores.append(max_tuple)
# 		tuple_list.remove(max_tuple)
# 	return top_scores

# def most_relevant(list_links, list_words):
# 	list_links = to_tokens_list(list_links)
# 	#list_words = to_tokens_list(list_words)
# 	linked_scores = []
# 	for link in list_links:
# 		sim = 0
# 		for word in list_words:
# 			sim += link.similarity(word)
# 		linked_scores.append((link,sim))
# 	print("These are all links")
# 	print(list_links)
# 	print("These are target words")
# 	print(list_words)
# 	return top_list(linked_scores)
