import requests
import logging

def send_to_webhook(webhook_url, message):
    payload = {"text": message}
    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            logging.info(f"Notification sent: {message}")
        else:
            logging.error(f"Failed to send notification: {response.status_code}")
    except requests.RequestException as e:
        logging.error(f"Error sending notification: {e}")