from flask import Flask, request, redirect, render_template
import json
# from flask_ngrok import run_with_ngrok
# import main
import detect_language
import speech
import speech_to_text
import voice_output

app = Flask(__name__)
# run_with_ngrok(app)
# app.config["SECRET_KEY"] = str(urandom(24));

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/translate', methods = ['POST',"GET"])
def translate():
  form_data=request.get_json(force = True)
  ta_src_lang = form_data['ta_src_lang']
  src_lang = form_data['src_lang']
  if src_lang=="detect":
    candidate_langs = detect_language.detect_lang(ta_src_lang)
    # source_lang = candidate_langs[0]["language"]
    src_lang = candidate_langs
  dest_lang = form_data['dest_lang']
  trans_text=ta_src_lang
  # trans_text = main.translate(src_lang,dest_lang, ta_src_lang)
  response=json.dumps({"src_lang": src_lang,"dest_lang": dest_lang,"ta_src_lang": ta_src_lang,"ta_dest_lang":trans_text})
  return response


@app.route('/text_to_speech', methods = ['POST'])
def text_to_speech():
  form_data = request.get_json(force = True)
  dest_lang = form_data['dest_lang']
  ta_dest_lang = form_data['ta_dest_lang']
  path = speech.play_text(ta_dest_lang,dest_lang)
  response=json.dumps({"dest_lang": dest_lang,"ta_dest_lang":ta_dest_lang,"path":path})
  return response

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		f.save(('uploads/file1.txt'))
		with open("uploads/file1.txt", "r") as f:
			content = f.readlines()
		return render_template('display_file.html', txt = content)

@app.route('/speechToText', methods = ['GET','POST'])
def speechToText():
  form_data=request.get_json(force = True)
  print(form_data)
  src_lang = form_data['src_lang']
  if src_lang=="detect":
    response=json.dumps({"error": "Choose a specific language to enable voice input"})
    return response
  print(src_lang)
  text_recognized = speech_to_text.speech_to_text(src_lang)
  # trans_text = main.translate(src_lang,dest_lang, ta_src_lang)
  response=json.dumps({"text_recognized": text_recognized})
  return response

@app.route('/manual_speech_src', methods = ['GET','POST'])
def manual_speech_src():
  form_data=request.get_json(force = True)
  # print(form_data)
  src_lang = form_data['src_lang']
  if src_lang=="detect":
    response=json.dumps({"error": "Choose a specific language to enable voice input"})
    return response
  dest_lang = form_data['dest_lang']
  text_recognized = speech_to_text.speech_to_text(src_lang)
  # trans_text = main.translate(src_lang,dest_lang, ta_src_lang)
  path = speech.play_text(text_recognized,dest_lang)
  response=json.dumps({"text_recognized": text_recognized})
  return response

@app.route('/manual_speech_trg', methods = ['GET','POST'])
def manual_speech_trg():
  form_data=request.get_json(force = True)
  # print(form_data)
  src_lang = form_data['src_lang']
  if src_lang=="detect":
    response=json.dumps({"error": "Choose a specific language to enable voice input"})
    return response
  dest_lang = form_data['dest_lang']
  text_recognized = speech_to_text.speech_to_text(dest_lang)
  # trans_text = main.translate(src_lang,dest_lang, ta_src_lang)
  path = speech.play_text(text_recognized,src_lang)
  response=json.dumps({"text_recognized": text_recognized})
  return response

if __name__ == '__main__':
	app.run(debug=True)
