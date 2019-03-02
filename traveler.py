import wikipedia
from filter import clean
import spacy

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
	path = []
	target_words = clean(target)

	while curr != target:
		path.append(curr)
		#gets all links from the current page
		all_links = wikipedia.page(curr).links

		#filters down the links to the best 20
		#links_and_scores = most_relevant(all_links, target_words)
		#best_links = [str(x[0]) for x in links_and_scores]
		#finds the best page from the top 20
		curr = find_best_page(all_links, target_words, target)

	path.append(curr)

	return path

def find_best_page(pages, target_words, target):
	max_score = 0
	best_page = None
	#find the best page
	for page in pages:
		#direct link
		if page == target:
			return page
		
		curr_score = score(page, target_words)
		if curr_score > max_score:
			max_score = curr_score
			best_page = page

	return page

def score(page_name, target_words):
	#list of filtered tokens from page summary
	curr_words = clean(page_name)

	score = 0
	for curr_token in curr_words:
		for target_token in target_words:
			score += curr_token.similarity(target_token)

	#adjust the weight by page length
	if len(curr_words) != 0:
		score = score / len(curr_words)
	return score


def main():
	pages = user_prompt()

	print(search(pages[0], pages[1]))

main()
wikipedia.donate()