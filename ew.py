import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

# Initialize Mailchimp client
client = MailchimpMarketing.Client()
client.set_config({
    "api_key": "c0d3f7c35a59aaef9c9c27376b89ef59-us21",
    "server": "us21"
})

# Campaign ID of the campaign you want to send
campaign_id = "f7b2f3ee30fb"

try:
    # Send the campaign
    response_send = client.campaigns.send(campaign_id=campaign_id)
    print("Campaign sent successfully!")
except ApiClientError as error:
    print(f"An API error occurred: {error}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")