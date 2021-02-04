import requests

def get_request(url, header, header_value):
    """
    Makes a HTTP GET request with specified header and value
    """
    return requests.get(url, headers={header:header_value})

if __name__ == "__main__":
    url = 'https://www.google.com'
    header = 'Pragma'
    header_value = 'no-cache'

    r = get_request(url, header, header_value)
    print(r.status_code)