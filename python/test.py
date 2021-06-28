import datetime


def func1():
    """
    """

    today = datetime.datetime.now()
    print(today.strftime("%Y/%m/%d %H:%M:%S"))


if __name__ == '__main__':

    func1()
