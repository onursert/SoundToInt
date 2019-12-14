import pyaudio
import struct

p = pyaudio.PyAudio()

# List of audio devices
input_device_ids = []
# output_device_ids = []
for i in range(p.get_device_count()):
    device = p.get_device_info_by_index(i)
    if device.get('maxInputChannels') > 0:
        print("Input Device ", i, " - ", device.get('name'))
        input_device_ids.append(i)
    # if device.get('maxOutputChannels') > 0:
        # print("Output Device ", i, " - ", device.get('name'))
        # output_device_ids.append(i)

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 48000

INPUT_DEVICE_INDEX = input("Select input device index you want to use: ")
while not INPUT_DEVICE_INDEX.isdigit() or int(INPUT_DEVICE_INDEX) not in input_device_ids:
    INPUT_DEVICE_INDEX = input("Select correct input device index you want to use: ")
INPUT_DEVICE_INDEX = int(INPUT_DEVICE_INDEX)

# OUTPUT_DEVICE_INDEX = input("Select output device index you want to use: ")
# while not OUTPUT_DEVICE_INDEX.isdigit() or int(OUTPUT_DEVICE_INDEX) not in output_device_ids:
    # OUTPUT_DEVICE_INDEX = input("Select correct output device index you want to use: ")
# OUTPUT_DEVICE_INDEX = int(OUTPUT_DEVICE_INDEX)

stream = p.open(frames_per_buffer=CHUNK,
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                input_device_index=INPUT_DEVICE_INDEX)
                # output_device_index=OUTPUT_DEVICE_INDEX

while True:
    # Read Data
    data = stream.read(CHUNK)

    # Unpack Data to Int
    count = len(data) / 2
    format = "%dh" % (count)
    data_int = struct.unpack(format, data)

    # Print
    print(data_int)

    # Pack Data to Byte
    data_bytes = struct.pack("%dh" % (len(data_int)), *list(data_int))

    # Play
    # stream.write(data_bytes)
