import wikipedia

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

def main():
	pages = user_prompt()
	curr = wikiepdia.page(pages[0])
	target = wikiepdia.page(pages[1])

	search(curr, target)

def search(curr, target):
	path = []

	while not base_case(curr, target):



def base_case(curr, target):

