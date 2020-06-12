## happy path
* greet
    - utter_greet
* request_jobposting
    - jobposting_form
    - form{"name": "jobposting_form"}
    - form{"name": null}
    - utter_slots_values
    - action_reset_all_slots
* thankyou
    - utter_noworries
    - action_restart

## unhappy path
* greet
    - utter_greet
* request_jobposting
    - jobposting_form
    - form{"name": "jobposting_form"}
* chitchat
    - utter_chitchat
    - jobposting_form
    - form{"name": null}
    - utter_slots_values
    - action_reset_all_slots
* thankyou
    - utter_noworries
    - action_restart

## very unhappy path
* greet
    - utter_greet
* request_jobposting
    - jobposting_form
    - form{"name": "jobposting_form"}
* chitchat
    - utter_chitchat
    - jobposting_form
* chitchat
    - utter_chitchat
    - jobposting_form
* chitchat
    - utter_chitchat
    - jobposting_form
    - form{"name": null}
    - utter_slots_values
    - action_reset_all_slots
* thankyou
    - utter_noworries
    - action_restart

## stop but continue path
* greet
    - utter_greet
* request_jobposting
    - jobposting_form
    - form{"name": "jobposting_form"}
* stop
    - utter_ask_continue
* affirm
    - jobposting_form
    - form{"name": null}
    - utter_slots_values
    - action_reset_all_slots
* thankyou
    - utter_noworries
    - action_restart

## stop and really stop path
* greet
    - utter_greet
* request_jobposting
    - jobposting_form
    - form{"name": "jobposting_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - action_restart

## chitchat stop but continue path
* request_jobposting
    - jobposting_form
    - form{"name": "jobposting_form"}
* chitchat
    - utter_chitchat
    - jobposting_form
* stop
    - utter_ask_continue
* affirm
    - jobposting_form
    - form{"name": null}
    - utter_slots_values
    - action_reset_all_slots
* thankyou
    - utter_noworries
    - action_restart

## stop but continue and chitchat path
* greet
    - utter_greet
* request_jobposting
    - jobposting_form
    - form{"name": "jobposting_form"}
* stop
    - utter_ask_continue
* affirm
    - jobposting_form
* chitchat
    - utter_chitchat
    - jobposting_form
    - form{"name": null}
    - utter_slots_values
    - action_reset_all_slots
* thankyou
    - utter_noworries
    - action_restart

## chitchat stop but continue and chitchat path
* greet
    - utter_greet
* request_jobposting
    - jobposting_form
    - form{"name": "jobposting_form"}
* chitchat
    - utter_chitchat
    - jobposting_form
* stop
    - utter_ask_continue
* affirm
    - jobposting_form
* chitchat
    - utter_chitchat
    - jobposting_form
    - form{"name": null}
    - utter_slots_values
    - action_reset_all_slots
* thankyou
    - utter_noworries
    - action_restart

## chitchat, stop and really stop path
* greet
    - utter_greet
* request_jobposting
    - jobposting_form
    - form{"name": "jobposting_form"}
* chitchat
    - utter_chitchat
    - jobposting_form
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - action_restart

## bot challenge
* bot_challenge
  - utter_iamabot
    - action_restart