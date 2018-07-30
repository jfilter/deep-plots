import os

import deep_plots


def test_from_keras_log():
    fname = os.path.join(os.path.dirname(__file__), 'log.csv')
    deep_plots.from_keras_log(fname, '.')


def test_from_keras_log_args():
    fname = os.path.join(os.path.dirname(__file__), 'log.csv')
    deep_plots.from_keras_log(fname, '.', width=4, height=4)
