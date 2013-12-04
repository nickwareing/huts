import sys
import csv
from decimal import Decimal

from browser.models import Hut

filename = 'doc-huts.csv'


class Column:
    NAME = 1
    CAT = 3
    LAT = 4
    LONG = 5


def get_hut_category(x):
    return {
        'Standard Hut': 'standard',
        'Serviced Hut': 'serviced',
        'Great Walk Hut': 'great',
        'Basic Hut/bivvy': 'bivvy',
        'Serviced Alpine Hut': 'alpine',
        'Serviced-Alpine Hut': 'alpine',
    }[x]


def to_title(name):
    words = name.split(' ')
    words = [word.title() for word in words]
    return ' '.join(words)


def create_objects():
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        huts = []
        try:
            for row in reader:
                if reader.line_num == 1:
                    pass
                else:
                    hut = Hut()
                    hut.name = to_title(row[Column.NAME])
                    hut.category = get_hut_category(row[Column.CAT])
                    hut.lat = Decimal(row[Column.LAT])
                    hut.long = Decimal(row[Column.LONG])
                    huts.append(hut)
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
        print "%d Hut objects created" % len(huts)
    return huts


def save_objects(huts):
    Hut.objects.bulk_create(huts)
    print "%d Hut objects saved" % len(huts)
