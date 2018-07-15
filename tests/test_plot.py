import os

import deep_plots


def test_from_keras_log():
    fname = os.path.join(os.path.dirname(__file__), 'log.csv')
    deep_plots.from_keras_log(fname, '.')
