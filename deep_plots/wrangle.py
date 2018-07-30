import pandas as pd

from .plot import plot


def _from_keras_log_format(data, **kwargs):
    """Plot accuracy and loss from a panda's dataframe.

    Args:
        data: Panda dataframe in the format of the Keras CSV log.
        output_dir_path: The path to the directory where the resultings plots
            should end up.
    """
    data_val = pd.DataFrame(data[['epoch']])

    data_val['acc'] = data['val_acc']
    data_val['loss'] = data['val_loss']
    data_val['data'] = 'validation'

    data_training = pd.DataFrame(data[['acc', 'loss', 'epoch']])
    data_training['data'] = 'training'

    result = pd.concat([data_training, data_val], sort=False)
    plot(result, **kwargs)


def from_keras_log(csv_path, output_dir_path, **kwargs):
    """Plot accuracy and loss from a Keras CSV log.

    Args:
        csv_path: The path to the CSV log with the actual data.
        output_dir_path: The path to the directory where the resultings plots
            should end up.
    """
    # automatically get seperator by using Python's CSV parser
    data = pd.read_csv(csv_path, sep=None, engine='python')
    _from_keras_log_format(data, output_dir_path=output_dir_path, **kwargs)
