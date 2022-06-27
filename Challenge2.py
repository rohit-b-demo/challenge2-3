#!/usr/bin/env python2
import json
import requests

imds_server_base_url = "http://169.254.169.254"
instance_api_version = "2021-02-01"
instance_endpoint = imds_server_base_url + "/metadata/instance?api-version=" + instance_api_version

def api_call(endpoint):
    headers = {'Metadata': 'True'}
    json_obj = requests.get(endpoint, headers=headers).json()
    return json_obj

def get_value(val, expected_key):
    for key, val in val.items():
        if key in expected_key:
            print("Value of key " + key + "is : " + val)
            #return (val)
            break
        elif isinstance(val, dict):
            get_value(val, expected_key)
        else:
            continue
            #print ("Not Matched")

def read_output():
    f = open('output.json')
    json_sample = json.load(f)
    return json_sample

def main():
    # Instance provider API call, uncomment below 3 lines to execute the Azure API call
    # instance_json = api_call(instance_endpoint)
    # print("Instance provider data:")
    # print (json.dumps(instance_json, indent=1))

    #Funtion to read the JSON output in case can't run againt Azure API call
    instance_json = read_output()

    # Function of get the specific key value
    get_value(instance_json, "vmId")

if __name__ == "__main__":
    main()