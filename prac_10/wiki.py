import wikipedia


def main():
    """Search for a page on Wikipedia and print its details until the user enters a blank input."""
    search_phrase = input("Enter page title:")
    while len(search_phrase.strip()) != 0:
        try:
            page = wikipedia.page(search_phrase, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print("(BeautifulSoup warning)")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f'Page id "{search_phrase}" does not match any pages. Try another id!')
        search_phrase = input("\nEnter page title:")
    print("Thank you.")


main()
