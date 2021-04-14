import pyaudio
py_audio = pyaudio.PyAudio()
audio_stream = py_audio.open(
    rate=pv.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=pv.frame_length)