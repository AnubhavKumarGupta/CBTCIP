import sounddevice as sd
import numpy as np
import wavio

# Define recording parameters
duration = 5  # seconds
sample_rate = 44100  # Hz

print("Recording...")
# Record audio
recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype=np.int16)
sd.wait()  # Wait until recording is finished
print("Recording finished")

# Save the recording as a .wav file
wavio.write("my_recording.wav", recording, sample_rate, sampwidth=2)
print("Recording saved as my_recording.wav")
