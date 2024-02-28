import mailchimp_marketing as MailchimpMarketing
import traceback


# Set your Mailchimp API key and server
api_key = "f94d942c3630d61648cf22306b2a8734-us21"
data_center = "us21"

# Initialize the Mailchimp client
client = MailchimpMarketing.Client()
client.set_config({
    "api_key": api_key,
    "server": data_center
})

# Create a campaign
campaign_data = {
    "type": "regular",
    "recipients": {
        "list_id": "a37d5995b6"
    },
    "settings": {
        "subject_line": "Score Sheet",
        "title": "Marks Scored in Each Subject",
        "from_name": "Shiva",
        "reply_to": "Lavanyabk16@gmail.com"
    },
    "content": {
        "html": "<p>Your HTML content here</p>",
        "plain_text": "100 Maths"  # Plain text version of the email
    }
}

try:
    # Create the campaign
    response = client.campaigns.create(campaign_data)
    print(response)

    # Retrieve the campaign ID from the response
    campaign_id = response['id']
    print("Campaign ID:", campaign_id)

    # Send the campaign
    response_send = client.campaigns.send(campaign_id=campaign_id)
    print("Campaign created and sent successfully!")
except Exception as e:
    print("An error occurred:", e)
    traceback.print_exc()