import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
import json



def print_training_plots(
        plot_name,
        transfer_learning_filename,
        learning_from_scratch_filename,
):
    transfer_learning_log = read_json_training_log(transfer_learning_filename)
    learning_from_scratch_log = read_json_training_log(learning_from_scratch_filename)
    print(transfer_learning_log)
    print(learning_from_scratch_log)
    render_plots(plot_name, *transfer_learning_log, *learning_from_scratch_log)


def read_json_training_log(filename):
    json_data = read_json_file(filename)
    logs = json_data['log_history']
    logs = [log for log in logs if 'learning_rate' in log]
    epoch = [log['epoch'] for log in logs]
    loss = [log['loss'] for log in logs]
    return epoch, loss


def read_json_file(filename):
    file = open(filename, 'r')
    return json.loads(file.read())


def render_plots(
    plot_name,
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
    plt.title(f'{plot_name}')
    plt.savefig(f'output/{plot_name}.png')
    plt.show()


plots_to_draw = {
    'opus_mt_en_de': [
        '../models_2021_06_26/opus_mt_en_de_transfer_learning_10/trainer_state.json',
        '../models_2021_06_26/opus_mt_en_de_train_from_scratch_10/trainer_state.json',
    ],
    't5_small': [
        '../models_2021_06_26/t5_small_transfer_learning_10/trainer_state.json',
        '../models_2021_06_26/t5_small_train_from_scratch_10/trainer_state.json',
    ],
    't5_base': [
        '../models_2021_06_26/t5_base_transfer_learning_3/trainer_state.json',
        '../models_2021_06_26/t5_base_train_from_scratch_3/trainer_state.json',
    ],
    'opus_mt_de_en': [
        '../models_2021_06_26/opus_mt_de_en_transfer_learning_3/trainer_state.json',
        '../models_2021_06_26/opus_mt_de_en_train_from_scratch_3/trainer_state.json',
    ]
}


for name in plots_to_draw:
    paths = plots_to_draw[name]
    print_training_plots(
        name,
        paths[0],
        paths[1]
    )
