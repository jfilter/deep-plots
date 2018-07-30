import os

import matplotlib
import pandas as pd

if os.environ.get('DISPLAY', '') == '':
    # this has to be done before doing anything with mathplotlib
    print('deep_plots: No display found. Using non-interactive Agg backend.')
    matplotlib.use('agg')

from plotnine import *  # nopep8


def get_epoch_max_val_acc(data):
    """Gets the epoch with the highest validation accuracy.
        Args:
            data: Panda dataframe in *the* format.
        Returns:
            Row with the maximum validatin accuracy.
    """
    df_val = data[data['data'] == 'validation']
    return df_val[df_val['acc'] == df_val['acc'].max()]


def plot_accuracy(data, output_dir_path='.', output_filename='accuracy.png',
                  width=10, height=8):
    """Plot accuracy.
        Args:
            data: Panda dataframe in *the* format.
    """
    output_path = os.path.join(output_dir_path, output_filename)

    max_val_data = get_epoch_max_val_acc(data)
    max_val_label = round(max_val_data['acc'].values[0], 4)

    # max_val_epoch = max_val_data['epoch'].values[0]
    max_epoch_data = data[data['epoch'] == data['epoch'].max()]

    plot = ggplot(data, aes('epoch', 'acc', color='factor(data)')) + \
        geom_line(size=1, show_legend=False) + \
        geom_vline(aes(xintercept='epoch', color='data'),
                   data=max_val_data, alpha=0.5, show_legend=False) + \
        geom_label(aes('epoch', 'acc'), data=max_val_data,
                   label=max_val_label, nudge_y=-0.02, va='top', label_size=0,
                   show_legend=False) + \
        geom_text(aes('epoch', 'acc', label='data'), data=max_epoch_data,
                  nudge_x=2, ha='center', show_legend=False) + \
        geom_point(aes('epoch', 'acc'), data=max_val_data,
                   show_legend=False) + \
        labs(y='Accuracy', x='Epochs') + \
        theme_bw(base_family='Arial', base_size=15) + \
        scale_color_manual(['#ef8a62', '#67a9cf', "#f7f7f7"])

    plot.save(output_path, width=width, height=height)


def get_epoch_min_val_loss(data):
    """Gets the epoch with the lowest validation loss.
        Args:
            data: Panda dataframe in *the* format.
        Returns:
            Row with the minimum validation loss.
    """
    df_val = data[data['data'] == 'validation']
    return df_val[df_val['loss'] == df_val['loss'].min()]


def plot_loss(data, output_dir_path='.', output_filename='loss.png',
              width=10, height=8):
    """Plot loss.
        Args:
            data: Panda dataframe in *the* format.
    """
    output_path = os.path.join(output_dir_path, output_filename)

    max_val_data = get_epoch_min_val_loss(data)
    max_val_label = round(max_val_data['loss'].values[0], 4)

    # max_val_epoch = max_val_data['epoch'].values[0]
    max_epoch_data = data[data['epoch'] == data['epoch'].max()]

    plot = ggplot(data, aes('epoch', 'loss', color='factor(data)')) + \
        geom_line(size=1, show_legend=False) + \
        geom_vline(aes(xintercept='epoch', color='data'), data=max_val_data,
                   alpha=0.5, show_legend=False) + \
        geom_label(aes('epoch', 'loss'), data=max_val_data,
                   label=max_val_label, nudge_y=0.02, va='bottom',
                   label_size=0, show_legend=False) + \
        geom_text(aes('epoch', 'loss', label='data'), data=max_epoch_data,
                  nudge_x=2, ha='center', show_legend=False) + \
        geom_point(aes('epoch', 'loss'), data=max_val_data,
                   show_legend=False) + \
        labs(y='Loss', x='Epochs') + \
        theme_bw(base_family='Arial', base_size=15) + \
        scale_color_manual(['#ef8a62', '#67a9cf', "#f7f7f7"])

    plot.save(output_path, width=width, height=height)


def plot(data, output_dir_path='.', width=10, height=8):
    """Create two plots: 1) loss 2) accuracy.
        Args:
            data: Panda dataframe in *the* format.
    """
    if not isinstance(data, pd.DataFrame):
        data = pd.DataFrame(data)
    plot_accuracy(data, output_dir_path=output_dir_path,
                  width=width, height=height)
    plot_loss(data, output_dir_path, width=width, height=height)
