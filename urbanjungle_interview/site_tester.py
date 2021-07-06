import requests

url = "https://myurbanbungle.com"

def check_website(url):
    # Head request
    try:
        r = requests.head(url)
        print(r)
    except Exception as e:
        print(e)
        return


    # Initial get request
    try:
        page_html_response = requests.get(url)
        print(page_html_response.text)
    except Exception as e:
        print(e)
        return


    # Check title is correct
    def check_title(url):
        resp = requests.get(url)
        page_html = resp.text
        page_lines = page_html.split("\n")
        extracted_title = page_lines[4]
        expected_title = "  <title>Urban Jungle Insurance - Designed for Urban Life</title>"
        if extracted_title == expected_title:
            print("Title line matches.")
        else:
            raise ValueError(
                'Title line does not match. (Found: "{}")'.format(extracted_title)
            )
        return True


    try:
        check_title(url)
    except ValueError as e:
        print(e)
        return
# print(x)
