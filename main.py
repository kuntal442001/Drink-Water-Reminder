import time
from plyer import notification

def drink_water_reminder(interval_seconds):
    while True:
        notification.notify(
            title="Hydration Reminder",
            message="Time to drink a glass of water!",
            timeout=10
        )
        time.sleep(interval_seconds)
        break

# Set your preferred interval in seconds (e.g., every 10 seconds)
drink_water_reminder(5)

