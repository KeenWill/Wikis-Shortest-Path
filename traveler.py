import wikipedia
from filter import clean
import spacy

#Prompts user for the start and end pages, and returns in a tuple
def user_prompt():
	#prompt user for start page
	start_page = input("Enter start page\n")
	#give 3 options
	results = wikipedia.search(start_page, results=3)
	print("Select one of the results by pressing 1 - 3")
	user_pick = input(str(results) + "\n")
	print()
	start_page = results[int(user_pick) - 1]
	#print the option they picked
	print("You picked " + start_page + " as your start page")

	#prompt user for start page
	end_page = input("Enter end page\n")
	#give 3 options
	results = wikipedia.search(end_page, results=3)
	print("Select one of the results by pressing 1 - 3")
	print()
	user_pick = input(str(results) + "\n")
	print()
	end_page = results[int(user_pick) - 1]
	#print the option they picked
	print("You picked " + end_page + " as your end page")

	return (start_page, end_page)


def search(curr, target):
	path = []
	target_words = clean(target)

	while curr != target:
		path.append(curr)
		curr_obj = wikipedia.page(curr)
		curr = find_best_page(curr_obj.links, target_words)

	path.append(curr)

	return path

def find_best_page(pages, target_words):
	max_score = 0
	best_page = None
	#find the best page
	for page in pages:
		curr_score = score(page, target_words)
		if curr_score > max_score:
			max_score = curr_score
			best_page = page

	return best_page

def score(page_name, target_words):
	curr_words = clean(page_name)
	print(page_name)
	return 0


def main():
	pages = user_prompt()
	search(pages[0], pages[1])

main()
wikipedia.donate()