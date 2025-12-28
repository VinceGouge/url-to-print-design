"""Main file for URL to print design project."""

import json

from trafilatura import extract, fetch_url

from src.model.article import Article

def main():
    """Program entrypoint."""
    # url = "https://www.prnewswire.com/news-releases/alkami-launches-sdk-wizard-merlin-furthering-the-companys-techfin-initiative-302120954.html"
    url = "https://finsiders.com.br/norte-americana-oak-esta-no-brasil-selecionando-fintechs-para-investir/"
    content = fetch_url(url)
    json_str_data = extract(filecontent=content, url=url, output_format="json", with_metadata=True)
    if not json_str_data:
        print("Extraction is empty")
        return

    data = json.loads(json_str_data)
    article = Article.model_validate(data)
    print(f"Title: {article.title}")
    print(f"Author: {article.author}")

if __name__ == "__main__":
    main()
