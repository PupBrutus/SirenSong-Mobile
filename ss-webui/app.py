from flask import Flask, render_template, request
from jinja2 import TemplateNotFound
from pythonosc.udp_client import SimpleUDPClient

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    server = '127.0.0.1'
    port = '1234'
    data_retrieve_port = '5678'
    binural_output_gain_value = 0
    binural_frequency_value = 0
    transposition_value = 0
    mix_value = 0
    spread_value = 0
    window_value = 2
    tone_frequency_value = 20
    tone_volume_value = 0
    pink_noise_volume_value = 0
    lookahead_value = 0
    compressor_volume_value = 0
    compressor_comp_value = 0
    compressor_softclip_value = 0
    compressor_attack_value = 0
    compressor_sustain_value = 0
    sound_volume_value = 0
    sound_volume_value2 = 0
    if request.method == 'POST':
        action = request.form.get('action')
        instance_param = request.form.get('instanceParam')
        if action == 'connect':
            try:
                client = SimpleUDPClient(server, int(port))
                if 'binuralOutputGainSlider' in request.form:
                    binural_output_gain_value = request.form.get('binuralOutputGainSlider')
                    client.send_message(instance_param, float(binural_output_gain_value))
                if 'binuralFrequencySlider' in request.form:
                    binural_frequency_value = request.form.get('binuralFrequencySlider')
                    client.send_message(instance_param, float(binural_frequency_value))
                if 'transpositionSlider' in request.form:
                    transposition_value = request.form.get('transpositionSlider')
                    client.send_message(instance_param, float(transposition_value))
                if 'mixSlider' in request.form:
                    mix_value = request.form.get('mixSlider')
                    client.send_message(instance_param, float(mix_value))
                if 'spreadSlider' in request.form:
                    spread_value = request.form.get('spreadSlider')
                    client.send_message(instance_param, float(spread_value))
                if 'windowSlider' in request.form:
                    window_value = request.form.get('windowSlider')
                    client.send_message(instance_param, float(window_value))
                if 'toneFrequencySlider' in request.form:
                    tone_frequency_value = request.form.get('toneFrequencySlider')
                    client.send_message(instance_param, float(tone_frequency_value))
                if 'toneVolumeSlider' in request.form:
                    tone_volume_value = request.form.get('toneVolumeSlider')
                    client.send_message(instance_param, float(tone_volume_value))
                if 'pinkNoiseVolumeSlider' in request.form:
                    pink_noise_volume_value = request.form.get('pinkNoiseVolumeSlider')
                    client.send_message(instance_param, float(pink_noise_volume_value))
                if 'playButton' in request.form:
                    client.send_message(instance_param, 1)
                if 'stopButton' in request.form:
                    client.send_message(instance_param, 1)
                if 'loopButton' in request.form:
                    loop_value = request.form.get('loopButton')
                    client.send_message(instance_param, int(loop_value))
                if 'fileDropdown' in request.form:
                    file_value = request.form.get('fileDropdown')
                    client.send_message(instance_param, file_value)
                if 'soundVolumeSlider' in request.form:
                    sound_volume_value = request.form.get('soundVolumeSlider')
                    client.send_message(instance_param, float(sound_volume_value))
                if 'soundVolumeSlider2' in request.form:
                    sound_volume_value2 = request.form.get('soundVolumeSlider2')
                    client.send_message(instance_param, float(sound_volume_value2))
                if 'playButton2' in request.form:
                    client.send_message(instance_param, 1)
                if 'stopButton2' in request.form:
                    client.send_message(instance_param, 1)
                if 'loopButton2' in request.form:
                    loop_value2 = request.form.get('loopButton2')
                    client.send_message(instance_param, int(loop_value2))
                if 'fileDropdown2' in request.form:
                    file_value2 = request.form.get('fileDropdown2')
                    client.send_message(instance_param, file_value2)
                return '', 204  # No Content response for AJAX request
            except Exception as e:
                return f"Failed to connect to server: {e}", 500
        if 'lookaheadDropdown' in request.form:
            lookahead_value = request.form.get('lookaheadDropdown')
            client.send_message(instance_param, float(lookahead_value))
        if 'compressorVolumeSlider' in request.form:
            compressor_volume_value = request.form.get('compressorVolumeSlider')
            client.send_message(instance_param, float(compressor_volume_value))
        if 'compressorCompSlider' in request.form:
            compressor_comp_value = request.form.get('compressorCompSlider')
            client.send_message(instance_param, float(compressor_comp_value))
        if 'compressorSoftclipSlider' in request.form:
            compressor_softclip_value = request.form.get('compressorSoftclipSlider')
            client.send_message(instance_param, float(compressor_softclip_value))
        if 'compressorAttackSlider' in request.form:
            compressor_attack_value = request.form.get('compressorAttackSlider')
            client.send_message(instance_param, float(compressor_attack_value))
        if 'compressorSustainSlider' in request.form:
            compressor_sustain_value = request.form.get('compressorSustainSlider')
            client.send_message(instance_param, float(compressor_sustain_value))
        if 'loadButton' in request.form:
            load_value = request.form.get('loadButton')
            client.send_message(instance_param, ["s", f'"{load_value}"'])
    try:
        return render_template('index.html', 
                               server=server, 
                               port=port, 
                               data_retrieve_port=data_retrieve_port,
                               binural_output_gain_value=binural_output_gain_value, 
                               binural_frequency_value=binural_frequency_value, 
                               transposition_value=transposition_value, 
                               mix_value=mix_value, 
                               spread_value=spread_value, 
                               window_value=window_value, 
                               tone_frequency_value=tone_frequency_value, 
                               tone_volume_value=tone_volume_value, 
                               pink_noise_volume_value=pink_noise_volume_value,
                               lookahead_value=lookahead_value,
                               compressor_volume_value=compressor_volume_value,
                               compressor_comp_value=compressor_comp_value,
                               compressor_softclip_value=compressor_softclip_value,
                               compressor_attack_value=compressor_attack_value,
                               compressor_sustain_value=compressor_sustain_value,
                               sound_volume_value=sound_volume_value,
                               sound_volume_value2=sound_volume_value2)
    except TemplateNotFound:
        return "Template not found", 404

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)  # Listen on all network interfaces