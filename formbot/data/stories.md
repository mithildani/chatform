## greet 1
* greet
    - utter_greet
    - action_restart

## greet 2
* greet
    - utter_greet
    - action_restart

## thank 1
* thankyou
    - utter_noworries
    - action_restart

## thank 2
* thankyou
    - utter_noworries
    - action_restart

## only good form 1
* request_jobposting
    - jobposting_form
    - form{"name": "jobposting_form"}
    - form{"name": null}
    - utter_slots_values
    - action_reset_all_slots
    - action_restart

## only good form 2
* request_jobposting
    - jobposting_form
    - form{"name": "jobposting_form"}
    - form{"name": null}
    - utter_slots_values
    - action_reset_all_slots
    - action_restart

## good form + chitchat 1
* request_jobposting
    - jobposting_form
    - form{"name": "jobposting_form"}
* chitchat
    - utter_chitchat
    - jobposting_form
    - form{"name": null}
    - utter_slots_values
    - action_reset_all_slots
    - action_restart

## good form + chitchat 1
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
* chitchat
    - utter_chitchat
    - jobposting_form
    - form{"name": null}
    - utter_slots_values
    - action_reset_all_slots
    - action_restart

## stop but complete form 1
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
    - action_restart

## stop but complete form 2
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
    - action_restart

## stop and really stop path 1
* request_jobposting
    - jobposting_form
    - form{"name": "jobposting_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - action_restart

## stop and really stop path 2
* request_jobposting
    - jobposting_form
    - form{"name": "jobposting_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - action_restart

## happy path
* request_jobposting
    - jobposting_form
    - form{"name": "jobposting_form"}
    - form{"name": null}
    - utter_slots_values
    - action_reset_all_slots
    - action_restart

## unhappy path
* request_jobposting
    - jobposting_form
    - form{"name": "jobposting_form"}
* chitchat
    - utter_chitchat
    - jobposting_form
    - form{"name": null}
    - utter_slots_values
    - action_reset_all_slots
    - action_restart

## very unhappy path
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
    - action_restart

## stop but continue path
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
    - action_restart

## stop and really stop path
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
    - action_restart

## stop but continue and chitchat path
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
    - action_restart

## chitchat stop but continue and chitchat path
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
    - action_restart

## chitchat, stop and really stop path
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