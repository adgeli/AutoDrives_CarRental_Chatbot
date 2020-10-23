# Imports
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta
# --- from botocore.vendored import requests --- This import request allows you to run.....

# --- Helpers that build all of the responses ---

def get_slots(intent_request):
    """
    Fetch all the slots and their values from the current intent.
    """
    return intent_request["currentIntent"]["slots"]

def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slots,
            'slotToElicit': slot_to_elicit,
            'message': message
        }
    }

def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }

    return response


def delegate(session_attributes, slots):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Delegate',
            'slots': slots
        }
    }

# --- Helper Functions ---

# Takes in a string and truns it into an integer
def safe_int(n):
    """
    Safely convert non-numeric (n) value to int.
    """
    if n is not None:
        return int(n)
    return n

# Takes in a string and truns it into a float 
def parse_float(n):
    """
    Securely converts a non-numeric value to float.
    """
    try:
        return float(n)
    except ValueError:
        return float("nan")

# Before we communicate back to Lex we have to communicate if the response if valid, if there is no
# Msg content, which slot has invalid data
def build_validation_result(is_valid, violated_slot, message_content):
    """
    Defines an internal validation message structured as a python dictionary.
    """
    if message_content is None:
        return {"isValid": is_valid, "violatedSlot": violated_slot}

    return {
        "isValid": is_valid,
        "violatedSlot": violated_slot,
        "message": {"contentType": "PlainText", "content": message_content},
    }

# validate_data(): This function validates the data provided by the user across the 
# intent's dialogue on Amazon Lex according to the business logic.
def validate_data(begin, driver_age, car_type, intent_request):
    """
    Validates the data provided by the user.
    """

    # Validate booking process 
    if begin and not is_valid_process(begin):
        return build_validation_result(
            False,
            'Begin',
            'Sorry to hear that. We hope you will like to book with us soon.',
        )

    # Validate that the user is over 21 years old
    if driver_age is not None:
        birth_date = datetime.strptime(driver_age, "%Y-%m-%d")
        age = relativedelta(datetime.now(), birth_date).years # caclulates the current date to their inputed bday
        if age < 21:
            return build_validation_result(
                False,
                "DriverAge", 
                "Your driver must be at least 21 to rent a car. "  
                "Can you provide the age of a different driver? "
                "Or make sure the driver's birth date is inputed as YYYY-MM-DD",
            )
    
    # Validate the car type
    if car_type and not is_valid_car_type(car_type):
        return build_validation_result(
            False,
            'CarType',
            'I did not recognize that model.  What type of car would you like to rent?  '
            'Popular cars are economy, midsize, or luxury. '
            'Other options include crossover, convertible, standard, 2 door, and truck.',
            )
    

    # A True results is returned if age or amount are valid
    return build_validation_result(True, None, None)

# car_type slot function
def is_valid_car_type(car_type): 
    car_types = ['standard', 'full size', 'convertible', 'midsize', 'crossover', 'truck', '2 door', 'luxury', 'coupe', 'economy', 'minivan']
    return car_type.lower() in car_types

# begin booking process slot function 
def is_valid_process(begin):
    begin_confirmation = ['yes', 'y', 'Yes']
    return begin.lower() in begin_confirmation

### Intents Handlers ###
def book_car(intent_request):
    """
    Performs dialog management and fulfillment for converting from dollars to bitcoin.
    """

    # Gets slots' values
    first_name = get_slots(intent_request)["FirstName"]
    begin = get_slots(intent_request)["Begin"]
    driver_age = get_slots(intent_request)["DriverAge"]
    car_type = get_slots(intent_request)["CarType"]
    duration = get_slots(intent_request)["Duration"]
    rental_time = get_slots(intent_request)["RentalTime"]
    pick_up_city = get_slots(intent_request)["PickUpCity"]
    pick_up_date = get_slots(intent_request)["PickUpDate"]
    pick_up_time = get_slots(intent_request)["PickUpTime"]
    drop_off_city = get_slots(intent_request)["DropOffCity"]
    occupancy = get_slots(intent_request)["Occupancy"]
    car_accessories = get_slots(intent_request)["CarAccessories"]
    final_confirmation = get_slots(intent_request)["FinalConfirmation"]

    # Gets the invocation source, for Lex dialogs "DialogCodeHook" is expected.
    source = intent_request["invocationSource"]

    if source == "DialogCodeHook":
        # This code performs basic validation on the supplied input slots.

        # Gets all the slots
        slots = get_slots(intent_request)

        # Validates user's input using the validate_data function
        validation_result = validate_data(begin, driver_age, car_type, intent_request)

        # If the data provided by the user is not valid,
        # the elicitSlot dialog action is used to re-prompt for the first violation detected.
        if not validation_result["isValid"]:
            slots[validation_result["violatedSlot"]] = None  # Cleans invalid slot

            # Returns an elicitSlot dialog to request new data for the invalid slot
            return elicit_slot(
                intent_request["sessionAttributes"],
                intent_request["currentIntent"]["name"],
                slots,
                validation_result["violatedSlot"],
                validation_result["message"],
            )

        # Fetch current session attributes
        output_session_attributes = intent_request["sessionAttributes"]

        # Once all slots are valid, a delegate dialog is returned to Lex to choose the next course of action.
        return delegate(output_session_attributes, get_slots(intent_request))

         # Fetch current session attributes
        output_session_attributes = intent_request["sessionAttributes"]

        # Once all slots are valid, a delegate dialog is returned to Lex to choose the next course of action.
        return delegate(output_session_attributes, get_slots(intent_request))

    # Return a message with conversion's result.
    return close(
        intent_request["sessionAttributes"],
        "Fulfilled",
        {
            "contentType": "PlainText",
            "content": """Okay {}, I have you booked for {} {} on {} at {}. 
            You will be picked up from {} in a {} equipped with a(n) {}.
            Thank you for booking with AutoDrives.ca it was a pleasure assisting you today! 
            No further booking action is required, you will receive a virtual ID shortly. 
            To review payment statements and booking fees please visit your account. 
            24 hours prior to your travel time, Evie will contact you for exact address details.
            """.format(
                first_name, rental_time, duration, pick_up_date, pick_up_time, pick_up_city, car_type, car_accessories
            ),
        },
    )

### Intents Dispatcher ###
# The purpose of the dispatch() function is to validate that the current intent is valid, 
# and to dispatch the intent to the corresponding intent handler.
def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    # Get the name of the current intent
    intent_name = intent_request["currentIntent"]["name"]

    # Dispatch to bot's intent handlers
    if intent_name == "BookCar":
        return book_car(intent_request)

    raise Exception("Intent with name " + intent_name + " not supported")


### Main Handler ###
# Every time a user sends a message to Amazon Lex, using text or voice, 
# an event will be sent to AWS Lambda; the lambda_handler() function catches every event 
# and returns a response to Lex via the dispatch() function.
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """

    return dispatch(event)





