import pandas as pd

from .plot import plot


def _from_keras_log_format(data, outputpath):
    data_val = pd.DataFrame(data[['epoch']])

    data_val['acc'] = data['val_acc']
    data_val['loss'] = data['val_loss']
    data_val['data'] = 'validation'

    data_training = pd.DataFrame(data[['acc', 'loss', 'epoch']])
    data_training['data'] = 'training'

    result = pd.concat([data_training, data_val], sort=False)
    plot(result)


def from_keras_log(csv_path, output_path):
    # automatically get seperator
    data = pd.read_csv(csv_path, sep=None, engine='python')
    _from_keras_log_format(data, output_path)


def from_keras_history(history, output_path):
    pass
