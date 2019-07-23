import requests


def get_url():
    return requests.get('https://api.github.com')


def prt(x):
    return x


def prt2(x):
    return x


def prt3(x):
    return x


if __name__ == '__main__':
    data = get_url()
    print(data.headers)
