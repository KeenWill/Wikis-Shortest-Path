import wikipedia
from filter import clean
import spacy
from concurrent.futures import ThreadPoolExecutor

#pages = None

#Prompts user for the start and end pages, and returns in a tuple
def user_prompt():
	start_page = None
	while start_page == None:
		#prompt user for start page
		start_page = input("Enter start page\n")
		#give 3 options
		results = wikipedia.search(start_page, results=3)
		print("Select one of the results by pressing 1 - 3")
		user_pick = input(str(results) + "\n")
		print()
		start_page = results[int(user_pick) - 1]

		#check valid page
		try:
			wikipedia.page(start_page)
		except wikipedia.exceptions.DisambiguationError as error:
			print("try again, ambiguous page picked")
			start_page = None
	#print the option they picked
	print("You picked " + start_page + " as your start page")

	#prompt user for start page
	end_page = None
	while end_page == None:
		end_page = input("Enter end page\n")
		#give 3 options
		results = wikipedia.search(end_page, results=3)
		print("Select one of the results by pressing 1 - 3")
		print()
		user_pick = input(str(results) + "\n")
		print()
		end_page = results[int(user_pick) - 1]

		#check valid page
		try:
			wikipedia.page(end_page)
		except wikipedia.exceptions.DisambiguationError as error:
			print("try again, ambiguous page picked")
			end_page = None
	#print the option they picked
	print("You picked " + end_page + " as your end page")

	return (start_page, end_page)


def search(curr, target):
	print("Got here")
	path = []
	print("Search before clean")
	target_words = clean(target)
	print("search after clean")
	while curr != target:
		print("next page is: ", curr)
		path.append(curr)
		#gets all links from the current page
		all_links = wikipedia.page(curr).links

		#filters down the links to the best 20
		#links_and_scores = most_relevant(all_links, target_words)
		#best_links = [str(x[0]) for x in links_and_scores]
		#finds the best page from the top 20
		curr = find_best_page(all_links, target_words, target, path)

	path.append(curr)
	print(path)

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
			print("target in sight")
			bonus = True

		for target_token in target_words:
			#always add the similarity points
			score += curr_token.similarity(target_token)
			#add bonus 50 if there is a shared proper noun
			if curr_token.pos_ == "PROPN" and\
			str(curr_token) == str(target_token):
				print("found common proper noun", str(curr_token))
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
	print("accessed execute")
	print(pages)
	search(pages[0], pages[1])

#ASDAS
def main(page1, page2):
	print("access main")

	pages = (page1, page2)

	print("pages assigned")
	print(pages)
	#execute(pages)
	executor = ThreadPoolExecutor(max_workers = 10)
	task1 = executor.submit(execute(pages))



#if __name__ == '__main__':
	#pages = user_prompt()
	#main()

#wikipedia.donate()