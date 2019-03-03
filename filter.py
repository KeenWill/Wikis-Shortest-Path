import wikipedia
import spacy

print("Loading English language...")
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
		    filtered_text.append(token)
	return filtered_text

def contains(tkn, tkn_list):
	for t in tkn_list:
		if str(t) == str(tkn):
			return True

	return False
