from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import AllSlotsReset
from store_db import DataUpdate

class JobpostingForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "jobposting_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["profile", "experience", "gender"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "profile": self.from_entity(entity="profile", not_intent="chitchat"),
            "experience": [
                self.from_entity(
                    entity="experience", intent=["inform"]
                ),
                self.from_text(intent="inform"),
            ],
            "gender": [
                self.from_entity(
                    entity="gender", intent=["inform", "request_restaurant"]
                ),
            ],
            # "outdoor_seating": [
            #     self.from_entity(entity="seating"),
            #     self.from_intent(intent="affirm", value=True),
            #     self.from_intent(intent="deny", value=False),
            # ],
            # "preferences": [
            #     self.from_intent(intent="deny", value="no additional preferences"),
            #     self.from_text(not_intent="affirm"),
            # ],
            # "feedback": [self.from_entity(entity="feedback"), self.from_text()],
        }

    # USED FOR DOCS: do not rename without updating in docs
    @staticmethod
    def profile_db() -> List[Text]:
        """Database of supported profiles"""

        return [
            "driver",
            "accountant",
            "maid"
        ]

    @staticmethod
    def experience_db() -> List[Text]:
        """Database of supported experiences"""

        return [
            "0 - 6 months",
            "1 - 2 years",
            "more than 2 years"
        ]

    @staticmethod
    def gender_db() -> List[Text]:
        """Database of supported gender"""

        return [
            "male",
            "female",
            "both"
        ]

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""

        try:
            int(string)
            return True
        except ValueError:
            return False

    # USED FOR DOCS: do not rename without updating in docs
    def validate_profile(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate cuisine value."""

        if value.lower() in self.profile_db():
            # validation succeeded, set the value of the "profile" slot to value
            return {"profile": value}
        else:
            dispatcher.utter_message(template="utter_wrong_profile")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"profile": None}

    def validate_experience(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate cuisine value."""

        if value.lower() in self.experience_db():
            # validation succeeded, set the value of the "experience" slot to value
            return {"experience": value}
        else:
            dispatcher.utter_message(template="utter_wrong_experience")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"experience": None}

    def validate_gender(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate cuisine value."""

        if value.lower() in self.gender_db():
            # validation succeeded, set the value of the "gender" slot to value
            return {"gender": value}
        else:
            dispatcher.utter_message(template="utter_wrong_gender")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"gender": None}

    # def validate_num_people(
    #     self,
    #     value: Text,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict[Text, Any],
    # ) -> Dict[Text, Any]:
    #     """Validate num_people value."""
    #
    #     if self.is_int(value) and int(value) > 0:
    #         return {"num_people": value}
    #     else:
    #         dispatcher.utter_message(template="utter_wrong_num_people")
    #         # validation failed, set slot to None
    #         return {"num_people": None}
    #
    # def validate_outdoor_seating(
    #     self,
    #     value: Text,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict[Text, Any],
    # ) -> Dict[Text, Any]:
    #     """Validate outdoor_seating value."""
    #
    #     if isinstance(value, str):
    #         if "out" in value:
    #             # convert "out..." to True
    #             return {"outdoor_seating": True}
    #         elif "in" in value:
    #             # convert "in..." to False
    #             return {"outdoor_seating": False}
    #         else:
    #             dispatcher.utter_message(template="utter_wrong_outdoor_seating")
    #             # validation failed, set slot to None
    #             return {"outdoor_seating": None}
    #
    #     else:
    #         # affirm/deny was picked up as T/F
    #         return {"outdoor_seating": value}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_submit")
        print(tracker.get_slot("profile"))
        print(tracker.get_slot("experience"))
        print(tracker.get_slot("gender"))
        # print(tracker.get_slot("company_name"))
        DataUpdate(tracker.get_slot("profile"),tracker.get_slot("experience"),tracker.get_slot("gender"),"Workindia")
        return []


class ActionResetAllSlots(Action):

    def name(self):
        return "action_reset_all_slots"

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]