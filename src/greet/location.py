"""Send greetings."""

import arrow


def greet():
    """Greet a location."""
    tz = "America/New_York"
    now = arrow.now(tz)
    friendly_time = now.format("h:mm a")
    location = tz.split("/")[-1].replace("_", " ")
    return f"Hello, {location}! The time is {friendly_time}."
