import wikipedia
import spacy

def clean(page_text):
	nlp = spacy.load('en_core_web_md')
	doc = nlp(wikipedia.page(page_text).content)
	filtered_text = []
	for token in doc:
		if token.pos_ == "NUM" or token.pos_ == "PROPN" or token.pos_ == "NOUN":
		    #if len(filtered_text) != 0 and filtered_text[-1].pos_ == "NUM":
		    	#filtered_text[-1] = filtered_text[-1] + token
		    #else:
		    filtered_text.append(token)
	return filtered_text


#class filter:
#	page_name = ""
#	nlp = spacy.load('en_core_web_md')
#	doc = None
#	def __init__(self, page_name):
#		self.page_name = page_name
#
#	def get_filtered_text(self):
#		
#		return filter(doc)


#nlp = spacy.load('en_core_web_md')
#doc = nlp(wikipedia.summary("GitHub"))

#print(wikipedia.summary("GitHub"))
#print("================")
#print(filter(doc))

#docx = nlp((wikipedia.page("Piano")).content)

#for token in docx:
#	print(token.text, token.pos_, token.dep_)



