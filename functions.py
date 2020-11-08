import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/List_of_tallest_buildings"
soup = BeautifulSoup(requests.get(URL).text, 'lxml')


def table_structured(table_tag):
    rows = table_tag("tr")
    cols = rows[0](["td", "th"])
    table = [[None] * len(cols) for _ in range(len(rows))]
    for row_i, row in enumerate(rows):
        for col_i, col in enumerate(row(["td", "th"])):
            insert(table, row_i, col_i, col)
    return table


def insert(table, row, col, element):
    if row >= len(table) or col >= len(table[row]):
        return
    if table[row][col] is None:
        value = element.get_text()
        table[row][col] = value
        if element.has_attr("colspan"):
            span = int(element["colspan"])
            for i in range(1, span):
                table[row][col + i] = value
        if element.has_attr("rowspan"):
            span = int(element["rowspan"])
            for i in range(1, span):
                table[row + i][col] = value
    else:
        insert(table, row, col + 1, element)


def get_number_column(index):
    return [float(x[index].replace(',', '.')) for x in
            table_structured(soup.find('table', class_='wikitable sortable'))[2::1]]


def get_string_column(index):
    return [x[index] for x in table_structured(soup.find('table', class_='wikitable sortable'))[2::1]]


def get_oldest_building():
    return get_string_column(1)[get_number_column(8).index(min(get_number_column(8)))].strip()


def get_most_common(index):
    most_common = None
    qty_most_common = 0
    countries = get_string_column(index)
    for item in countries:
        qty = countries.count(item)
        if qty > qty_most_common:
            qty_most_common = qty
            most_common = item
    return most_common.strip()


def is_column_sorted(index, reverse):
    return get_number_column(index) == sorted(get_number_column(index), reverse=reverse)
