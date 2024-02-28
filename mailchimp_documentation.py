from mailchimp_marketing import Client
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

#first api call
mailchimp = Client()
mailchimp.set_config({
  "api_key": "f94d942c3630d61648cf22306b2a8734-us21",
  "server": "us21"
})
api_key="f94d942c3630d61648cf22306b2a8734-us21"
data_server="us21"
# response = mailchimp.ping.get()
# print(response)

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

#get list_id
# try:
#   client = MailchimpMarketing.Client()
#   client.set_config({
#     "api_key": api_key,
#     "server": data_server
#   })

#   response = client.lists.get_all_lists()
#   print(response)
# except ApiClientError as error:
#   print("Error: {}".format(error.text))
print('//////////////////////////////////////////////')

# getting information about auidence
try:
  client = MailchimpMarketing.Client()
  client.set_config({
    "api_key": api_key,
    "server": data_server
  })

  response = client.lists.get_list_members_info("a37d5995b6")
  print(response)
except ApiClientError as error:
  print("Error: {}".format(error.text))

#adding email
# try:
#   client = MailchimpMarketing.Client()
#   client.set_config({
#     "api_key": api_key,
#     "server": data_server
#   })

#   response = client.lists.add_list_member("a37d5995b6", {"email_address": "lavanyabk16@gmail.com", "status": "subscribed"})
#   print(response)
# except ApiClientError as error:
#   print("Error: {}".format(error.text))
  
  import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

try:
  client = MailchimpMarketing.Client()
  client.set_config({
    "api_key": api_key,
    "server": data_server
  })

  response = client.reports.get_campaign_report("8edd5bd2769c")
  print(response)
except ApiClientError as error:
  print("Error: {}".format(error.text))