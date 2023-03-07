import requests


def ask(q,apikey):
    url = "https://evaluate-expression.p.rapidapi.com/"

    querystring = {"expression":q}

    headers = {
        "X-RapidAPI-Key": apikey,
        "X-RapidAPI-Host": "evaluate-expression.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.text:
        return response.text
    else:
        return "Something Did'nt Go Right , You can only ask math questions,timezone/date related questions,unit conversions/currency conversions"
