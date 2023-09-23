import mido

# List available MIDI input ports
input_ports = mido.get_input_names()
print("Input Ports:", input_ports)

# List available MIDI output ports
output_ports = mido.get_output_names()
print("Output Ports:", output_ports)

