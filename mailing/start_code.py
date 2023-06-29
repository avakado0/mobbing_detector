import pandas as pd
import mailbox

# Path to the mailbox file
mailbox_file = 'path/to/your/mailbox.mbox'

# Create an empty DataFrame to store email data
emails_df = pd.DataFrame(columns=['From', 'To', 'Subject', 'Date', 'Body'])

# Iterate over each email in the mailbox file
for message in mailbox.mbox(mailbox_file):
    email_data = {
        'From': message['From'],
        'To': message['To'],
        'Subject': message['Subject'],
        'Date': message['Date'],
        'Body': message.get_body()  # Fetch the email body
    }
    emails_df = emails_df.append(email_data, ignore_index=True)

# Save the DataFrame to a CSV file
emails_df.to_csv('emails.csv', index=False)

