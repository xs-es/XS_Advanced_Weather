# send_notifications.py
from twilio.rest import Client

def send_weather_alerts(data):
    """Send severe weather alerts using Twilio."""
    try:
        account_sid = 'your_account_sid_here'
        auth_token = 'your_auth_token_here'
        client = Client(account_sid, auth_token)

        for alert in data.get("alerts", []):
            message = client.messages.create(
                body=f"Weather Alert: {alert['description']}",
                from_='+1234567890',  # Twilio phone number
                to='+0987654321'  # Your verified phone number
            )
            print(f"Alert sent: {message.sid}")

    except Exception as e:
        print(f"Error sending notifications: {e}")

if __name__ == "__main__":
    # Example usage
    sample_alerts = {
        "alerts": [
            {"description": "Severe Thunderstorm Warning in your area."}
        ]
    }
    send_weather_alerts(sample_alerts)
