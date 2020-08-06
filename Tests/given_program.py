import requests

class GivenProgram:

    def public_data(self, api_url, data_payload):
        response = requests.get(api_url, data_payload)

        #print response.content
        if response.status_code == 200 :
            return "It works!!!"
        else:
            return "Error with status code",response.status_code
