import urllib.request,json
from .models import Quotes



# Getting the Quotes base url
base_url = None

def configure_request(app):
    global base_url

    base_url = app.config['QUOTES_URL']
    

def get_quotes():
    '''
    Function that gets the json response to our url request
    '''
    quotes_object=None

    with urllib.request.urlopen(base_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        

        if get_quotes_response:
            authors= get_quotes_response.get('author')
            quotes=get_quotes_response.get('quote')
        
            quotes_object=Quotes(authors,quotes)

    return quotes_object

