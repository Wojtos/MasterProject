import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
import json



def print_training_plots(
        transfer_learning_filename,
        learning_from_scratch_filename,
):
    transfer_learning_log = read_json_training_log(transfer_learning_filename)
    learning_from_scratch_log = read_json_training_log(learning_from_scratch_filename)
    render_plots(*transfer_learning_log, *learning_from_scratch_log)


def read_json_training_log(filename):
    json_data = read_json_file(filename)
    logs = json_data['log_history']
    logs = [log for log in logs if 'learning_rate' in log]
    epoch = [log['epoch'] for log in logs]
    learning_rate = [log['learning_rate'] for log in logs]
    return epoch, learning_rate


def read_json_file(filename):
    file = open(filename, 'r')
    return json.loads(file.read())


def render_plots(
    transfer_learning_epochs,
    transfer_learning_learning_rates,
    learning_from_scratch_epochs,
    learning_from_scratch_learning_rates,
):
    fig = plt.figure()
    ax = plt.axes()

    ax.plot(transfer_learning_epochs, transfer_learning_learning_rates, color='blue', label='Transfer learning')
    ax.plot(learning_from_scratch_epochs, learning_from_scratch_learning_rates, color='red', label='Learning from scratch')
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
               ncol=2, mode="expand", borderaxespad=0.)
    plt.show()

print_training_plots(
    '../models/en_cycl_2021_opus_mt_en_de_transfer_learning_10/trainer_state.json',
    '../models/en_cycl_2021_opus_mt_en_de_from_scratch_10/trainer_state.json',
)