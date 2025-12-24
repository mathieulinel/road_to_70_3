import requests
import urllib3
import pandas as pd
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)




# print("Requesting Token...\n")
# response = requests.post(auth_url, data=payload)
# access_token = response.json()['access_token']
# refresh_token = response.json()['refresh_token']
# print(access_token)
# print(refresh_token)


access_token = '1858564209ea1bd79d7fbfcebb854bcdcc60fc81'

## Doc script 
# Configure OAuth2 access token for authorization: strava_oauth
swagger_client.configuration.access_token = access_token

# create an instance of the API class
api_instance = swagger_client.ActivitiesApi()
id = 1 # Long | The identifier of the activity.
# includeAllEfforts = True # Boolean | To include all segments efforts. (optional)

try: 
    # Get Activity
    api_response = api_instance.get_activity_by_id(id) #, includeAllEfforts=includeAllEfforts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_activity_by_id: %s\n" % e)
    
## End Doc script 



## Previous script to get access token
# auth_url = "https://www.strava.com/oauth/token"

# You need to update this information from your Strava account before you can run the rest of this code
# See tutorial video here for info on how: https://www.youtube.com/watch?v=sgscChKfGyg&list=PLO6KswO64zVvcRyk0G0MAzh5oKMLb6rTW

# payload = {
#     'client_id': "186926",
#     'client_secret': '79fbb5fb15243ed9259ffd5a8ad62f6d3bc5173e',
#     'code': '2fe91f4e68e3e8e980ba113da512e60af1c06ad2',
#     'grant_type': "authorization_code",
#     # 'refresh_token': 'd2563983165e6d93d156dff07f40a366de8756b2',
#     # 'grant_type': "refresh_token",
#     # 'f': 'json'
# }


#old way to get access token
# res = requests.post(auth_url, data=payload, verify=False)
# access_token = res.json()['access_token']
# print("Access Token = {}\n".format(access_token))


# Now we need to import a list of activities and some top level stats about them.
# This will be 1 row per activity.

# Initialize the dataframe
# col_names = ['id','type', 'name', 'distance', 'moving_time', 'elapsed_time', 'total_elevation_gain', 'start_date',  'start_latlng', 'kilojoules', 'average_heartrate', 'max_heartrate', 'elev_high', 'elev_low', 'average_speed', 'max_speed']
# activities = pd.DataFrame(columns=col_names)

# activites_url = "https://www.strava.com/api/v3/athlete/activities"
# header = {'Authorization': 'Bearer ' + access_token}
# print(header)
# page = 1
# per_page = 50
# print(f"Getting page {page} of activities from Strava")
# # get page of activities from Strava
# param = {'per_page': per_page, 'page': page}
# r = requests.get(activites_url, headers=header, params=param).json()

# print(r)

# while True:
#     print(f"Getting page {page} of activities from Strava")
#     try:
#         # get page of activities from Strava
#         param = {'per_page': per_page, 'page': page}
#         r = requests.get(activites_url, headers=header, params=param).json()

#         # if no results then exit loop
#         if (not r):
#             break
        
#         # otherwise add new data to dataframe
#         for x in range(len(r)):
#             for c in col_names:
#                 try:
#                     activities.loc[x + (page-1)*50, c] = r[x][c]
#                 except KeyError:
#                     print(f"KeyError: {c} not found in activity {x + (page-1)*50}")
#                     activities.loc[x + (page-1)*50, c] = 'null'
#                     break


#         # increment page
#         page += 1
#         print(f"Page {page} of activities imported")

#         print("Activites imported")
#         print(activities)

#         activities.to_csv('activities.csv')
#     except Exception as e:
#         print(f"Error: {e}")
#         break