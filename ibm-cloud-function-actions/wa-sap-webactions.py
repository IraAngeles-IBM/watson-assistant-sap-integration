import requests
import urllib3
urllib3.disable_warnings()

def main(arg):
    url = f'https://{arg["hostname"]}:{arg["port"]}/sap/opu/odata/sap/API_MATERIAL_STOCK_SRV/A_MaterialStock(%27{arg["material"]}%27)/to_MatlStkInAcctMod?$top=50&$inlinecount=allpages'

    try:
        
        headers = {
            'Authorization' : f'Basic {arg["basic_auth"]}',
            'Accept' : 'application/json',
            'Content-Type' : 'application/json',
            'DataServiceVersion' : '2.0',
        }
         
        response = requests.get(url, headers=headers, verify=False)
        
        print(response)
        
        if response.status_code == 200:
            data = response.json()
            print(data["d"]["results"][0])
            return data["d"]["results"][0]
        else:
            print(f"Request failed with status code: {response.status_code}")
            
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error retrieving certificate: {str(e)}"
        }       
