import wikipedia
import spacy

def filter(page_text):
	filtered_text = []
	for token in page_text:
		if token.pos_ == "NUM" or token.pos_ == "PROPN" or token.pos_ == "NOUN":
		    #if len(filtered_text) != 0 and filtered_text[-1].pos_ == "NUM":
		    	#filtered_text[-1] = filtered_text[-1] + token
		    #else:
		    filtered_text.append(token)
	return filtered_text

class filter:
	page_name = ""
	nlp = spacy.load('en_core_web_md')
	doc = None
	def __init__(self, page_name):
		self.page_name = page_name

	def get_filtered_text(self):
		doc = nlp(wikipedia.page(page_name))
		return filter(doc)


#nlp = spacy.load('en_core_web_md')
#doc = nlp(wikipedia.summary("GitHub"))

#print(wikipedia.summary("GitHub"))
#print("================")
#print(filter(doc))

#docx = nlp((wikipedia.page("Piano")).content)

#for token in docx:
#	print(token.text, token.pos_, token.dep_)



