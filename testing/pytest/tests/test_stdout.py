import sys
import pytest
import random


def greeting(name):
    print('Hi, {}'.format(name))


def test_greeting(capsys):
    greeting('rick')
    out, err = capsys.readouterr()
    assert out == 'Hi, rick\n'
    assert err == ''

    greeting('ab')
    greeting('cd')
    out, err = capsys.readouterr()
    assert out == 'Hi, ab\nHi, cd\n'
    assert err == ''


def log_err(problem):
    print('Error: {}!'.format(problem), file=sys.stderr)


def test_yikes(capsys):
    log_err('sites down.')
    out, err = capsys.readouterr()
    assert out == ''
    assert 'sites down' in err


@pytest.mark.skip
def test_capsys_disabled(capsys):
    with capsys.disabled():
        print('\nalways print this')
        print('normal print, usually captured')


@pytest.mark.parametrize('i', range(4))
def test_for_fun(i, capsys):
    if random.randint(1, 10) == 2:
        pass
        # with capsys.disabled():
        #    sys.stdout.write('F')
