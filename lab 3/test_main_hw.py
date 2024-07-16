# -*- coding: utf-8 -*-

import pytest
import main
import pickle
import math
import numpy as np

from typing import Union, List, Tuple

expected = pickle.load(open('expected','rb'))

results_absolut_error = expected['absolut_error']
results_relative_error = expected['relative_error']



@pytest.mark.parametrize("v,v_aprox,result", results_absolut_error)
def test_absolut_error(v: Union[int, float, List, np.ndarray], v_aprox: Union[int, float, List, np.ndarray], result):
    if np.any(np.isnan(result)):
        assert np.isnan(main.absolut_error(v, v_aprox)), 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.absolut_error(v, v_aprox))
    else:
        assert main.absolut_error(v, v_aprox) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.absolut_error(v, v_aprox))


@pytest.mark.parametrize("v,v_aprox,result", results_relative_error)
def test_relative_error(v: Union[int, float, List, np.ndarray], v_aprox: Union[int, float, List, np.ndarray], result):
    if np.any(np.isnan(result)):
        assert np.isnan(main.relative_error(v, v_aprox)), 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.relative_error(v, v_aprox))
    else:
        assert main.relative_error(v, v_aprox) == pytest.approx(result), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.relative_error(v, v_aprox))
