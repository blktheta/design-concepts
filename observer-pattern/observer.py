from api.slack_listener import setup_slack_event_handlers
from api.log_listener import setup_log_event_handlers
from api.email_listener import setup_email_event_handlers

from api.user import register_new_user, password_forgotten
from api.plan import upgrade_plan

# initialize the event structure
setup_slack_event_handlers()
setup_log_event_handlers()
setup_email_event_handlers()


# register a new user
register_new_user("Arjan", "BestPasswordEva", "hi@arjanegges.com")

# send a password reset message
password_forgotten("hi@arjanegges.com")

# upgrade the plan
upgrade_plan("hi@arjanegges.com")
