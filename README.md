# Wiki's Shortest Path: WSP
## Summary
The purpose of this program is to explore the different ways that knowledge is related in the vast graph of connected wikipedia articles. Given two wikipedia pages, the Wiki's Shortest Path program uses a heuristic to find an efficient path of links between the two articles. It does this through a combination of directed-graph traversal algorithms and natural language processing techniques to determine the best page to visit next. The NLP library (spaCy) performs relevancy analysis between the current page and the target page to determine which neighboring pages are most relevant, and thus which neighboring page the algorithm should visit next.

For those who know what the Wikipedia Game is, this program essentially looks to efficiently play that game. For the uninitiated, check out the wikipedia article on the wikipedia game here: https://en.wikipedia.org/wiki/Wikipedia:Wiki_Game

## How to run:
0. Have python3 and pip installed
1. Download the project as a zip folder and extract
2. From terminal, cd into the project folder
3. run pip install wikipedia and pip install spacy (otherwise, pip install -U spacy)
4. run python3 -m spacy download en_core_web_md (for windows replace python3 with python)
5. run python3 graphics.py (same rule applies for windows)

## APIs/Frameworks:
The WSP program is written entirely in Python 3 to make use of the extensive I/O and NLP libraries available in the language. The wikipedia API allows quick access to a wikipedia article's information: including the article length, article summary, links listed on the page, etc. The program relies on this API to traverse the graph of Wikipedia pages by updating the current page it is visiting. Another essential library is the spaCy NLP library. spaCy is extremely powerful in that it provides very effective breakdown of natural language text into Tokens. Token objects can then be compared to each other to figure out the relevancy between two or more texts. Finally, the GUI is built on the Tkinter library to create a native interface.

### External Dependencies:
1. wikipedia
2. spacy

## Algorithm:
![](https://i.imgur.com/DyXIhR3.png)
This figure depicts the graph of Wikipedia articles. Source and target nodes refer to the start and end pages. An edge from node A to B denotes A's page containing a link to B's page. n marks the neighboring pages of the current pointer that starts at the source.

The graph traversal algorithm is a greedy, heuristic algorithm that starts at the source node, and advances to its best neighboring page at each step. The best page to advance to is defined as the page that will bring the program closest to the target page, and is determined through a series of NLP tools. The underlying idea is that, the more relevant the contents of a neighboring page is to the taret page, the closer it is to the target page. 

First, every link that the current page has is collected from the wikipedia API. For every page that a link points to, the summary is retrieved for that page and is cleaned: menial words such as articles, adjectives, prepositions, etc. are removed. 

Once the summaries are cleaned, the remaining tokens from each page are compared with the cleaned tokens of the target page. Each pair of token is compared for relevancy and given a score. The average score of all tokens from a given neighbor page is assigned to the overall score for that page (how relevant that page's content is to the target page). However, certain weighted modifiers are taken into account. If a neighbor page contains the title of the target page, that neighbor page's score is increased by a significant factor (although, it is not immediately obvious that that page is the best page. This is because a page can contain the title of the target page, but not a link to it). Any proper nouns that are shared between a neighbor page and the target page increases the neighbor page's score by a smaller margin. We found that the final weights for the score modifiers lead to a very accurate ranking of each neighboring page, and thus allowed the program to find very short paths between any two pages.

Once the best neighbor is determined by selecting the neighbor with the highest weighted average relevancy score, the algorithm visits it as the greedy recursive step. The recursion continues until the target page is reached (note: the implementation is done iteratively to save stack space, even though the algorithm is recursive in nature). 

## Improvements:
Currently, the average runtime of the program is around 30 minutes for a randomly chosen pair of Wikipedia articles. The bottleneck stems from I/O through the Wikipedia API, as the latency is set by Wikipedia to provide access to an article's information. Beyond asymptotic efficiency on the algorithm, the program attempts to reduce this runtime through various ways such as multi-threading, caching previously visited Wikipedia pages, and only ranking pages through their summaries and not the entire content of the article. Even with these optimizations, the program takes around 30 minutes to find an efficient path between two Wikipedia pages (the paths however, are generally very optimized). 

Looking forward, we are currently considering a precomputation step on the Wikipedia graph as a way of optimization. Wikipedia currently allows the downloading of their entire public database. Thus, the program could theoretically run offline on a preprocessed database of Wikipedia that we host either locally or on a cloud computing service such as AWS or GCP.
