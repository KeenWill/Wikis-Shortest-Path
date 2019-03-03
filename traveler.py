import wikipedia
from filter import clean
import spacy
from concurrent.futures import ThreadPoolExecutor

def wiki_search(query):
	results_list =  wikipedia.search(query, results=3)

	#ensure 3 elements
	while len(results_list) > 0 and len(results_list) < 3:
		results_list.append("")
		
	return results_list

def is_valid(page):
	try:
		wikipedia.page(page)
	except:
		return False
	return True


def search(curr, target):
	path = []
	target_words = clean(target)
	
	while curr != target:
		print("next page is: ", curr)
		path.append(curr)
		#gets all links from the current page
		all_links = wikipedia.page(curr).links

		curr = find_best_page(all_links, target_words, target, path)

	path.append(curr)

	f = open("results.txt", "w")
	f.write(str(path))
	f.close


def find_best_page(pages, target_words, target, path):
	max_score = 0
	best_page = None
	#find the best page
	for page in pages:
		#avoid cycles
		if page in path:
			continue
		#direct link
		if page == target:
			return page
		
		curr_score = score(page, target_words, target)
		if curr_score == 500:
			return page

		if curr_score > max_score:
			max_score = curr_score
			best_page = page

	return best_page

def score(page_name, target_words, target):
	#list of filtered tokens from page summary
	curr_words = clean(page_name)
	score = 0
	bonus = False
	proper_noun_points = 0
	for curr_token in curr_words:
		#page's summary contains the target
		if str(curr_token) == target:
			bonus = True

		for target_token in target_words:
			#always add the similarity points
			score += curr_token.similarity(target_token)
			#add bonus 50 if there is a shared proper noun
			if curr_token.pos_ == "PROPN" and\
			str(curr_token) == str(target_token):
				proper_noun_points += 2

	#adjust the weight by page length
	if len(curr_words) != 0:
		score = score / len(curr_words)

	#add the proper noun bonus
	score += proper_noun_points

	#if the target page's name appears in the summary, increase points by 5
	if bonus:
		score += 20
	
	print(page_name, score)

	return score



def execute(pages):
	search(pages[0], pages[1])
	

#ASDAS
def main(page1, page2):
	pages = (page1, page2)

	#execute(pages)
	executor = ThreadPoolExecutor(max_workers = 10)
	task1 = executor.submit(execute(pages))

