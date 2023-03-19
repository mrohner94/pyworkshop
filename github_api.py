import requests

def create_query(languages, min_stars=50000):
    query = f"stars:>{min_stars} "

    for language in languages:
        query += f"language:{language} "

    return query


def repos_with_most_stars(languages, sort="stars", order="desc"):
    gh_api_url = "https://api.github.com/search/repositories"
    
    query = create_query(languages)
    params = {"q": query, "sort": sort, "order": order}

    response = requests.get(gh_api_url, params)

    if response.status_code != 200:
        raise RuntimeError(f"An error occured.  Status code was: {response.status_code}")
    
    response_json = response.json()["items"]
    return response_json

if __name__ == "__main__":
    languages = ["Python", "Javascript", "Go"]
    results = repos_with_most_stars(languages)
    # print(len(results))

    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"-> {name} is a {language} repo with {stars} stars")

