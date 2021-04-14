# from ibm_watson import SpeechToTextV1
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# import speech_recognition as sr
# import json

# authenticator = IAMAuthenticator('Y64EeqmgBmC53atVuS6I-GVagSkx8yG04QyKqOEt-fGn')
# speech_to_text = SpeechToTextV1(
#     authenticator=authenticator
# )
# # speech_to_text.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/71fdca9c-9384-46e6-934a-f391e4aeb395/v1/recognize')
# speech_to_text.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com')

# import speech_recognition as SRG 
# from os import path
# import json

# r = SRG.Recognizer()
# print("this speech to text")
# with SRG.Microphone() as s: 
#     audio = r.record(s, duration=4)
# HOUNDIFY_CLIENT_ID = "Ovd0W-cjF2V_dMQHvQ58pw=="
# HOUNDIFY_CLIENT_KEY= "6HEyuH2opwqpkLnSoSc-XiMWK2RiAuNxawHkhtgHWMn-tvKBm_g81itzQtRffLGDQUpCjUtc4zZtrjZOh-kHbQ=="

# try:
#     text_output = r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY)
#     print(text_output)
#     # return text_output
# except r.UnknownValueError:
#     response=json.dumps({"error": "Sorry I didn't get that."})
#     print(response)
# except r.RequestError as e:
#     print("Could not request results from Houndify service; {0}".format(e))