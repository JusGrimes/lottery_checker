from typing import List, Dict, Tuple

import requests
import sqlite3
import logging

DB_file = "Lotto_numbers.db"


class LottoNumber:

    def __init__(self, raw_number: str):
        self.first_numbers, self.powernum = self._parse_number(raw_number)

    # noinspection PyMethodMayBeStatic
    def _parse_number(self, raw_number: str):
        splitlist = raw_number.split(':')
        first_five = splitlist[0].split()
        power_num = splitlist[1].strip()

        return first_five, power_num

    def check_winners(self):
        """Check to see if any of the number combinations have won. Need to pass in DB connection"""
        pass

    def _check_powerball(self):
        pass

    def _check_mega(self):
        pass


def setup_db():

    mega_csv_url = "https://data.ny.gov/api/views/5xaw-6ayf/rows.csv?accessType=DOWNLOAD"
    powerball_csv_url = "https://data.ny.gov/api/views/5xaw-6ayf/rows.csv?accessType=DOWNLOAD"

    mega_csv = requests.get(mega_csv_url).content
    powerball_csv = requests.get(powerball_csv_url).content

    conn = sqlite3.connect(DB_file)
    # TODO Finish SQL statement for creating database
    conn.execute("""
                    CREATE TABLE mega_numbers (
                    draw_date INTEGER
                    winning_number TEXT""")

#
# def parse_number(rawstr: str)-> List[str]:
#     return rawstr.split(':')
#
# y lo
# def check_winning_dates(json_response: List[Dict]):
#     if json_response:
#         print('Winning Dates: ')
#         for elem in json_response:
#             print(elem['draw_date'][0:9]) #print only the date portion of timestamp
#     else:
#         print('No Winners!')
#
#
# def check_winner(lotto_num):
#     mega_url = 'https://data.ny.gov/resource/h6w8-42p9.json'
#     pb_url = 'https://data.ny.gov/resource/8vkr-v8vh.json'
#     lotto_num = lotto_num.split(':')
#     first_five_nums = lotto_num[0].replace(' ','%20')
#     last_num = lotto_num[1]
#
#     response = requests.get(''.join([mega_url,'?winning_numbers=',first_five_nums,'&mega_ball=',last_num]))
#     mega_json = response.json()
#     response = requests.get(''.join([pb_url,'?winning_numbers=',first_five_nums,'%20',last_num]))
#     pb_json = response.json()
#
#     print('Checking MegaMillions...')
#     check_winning_dates(mega_json)
#     print('Checking Powerball...')
#     check_winning_dates(pb_json)


def lotto_num_prompt() -> LottoNumber:
    number = input('Enter your lotto number as NN NN NN NN NN:NN')
    return LottoNumber(number)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    lotto_num = lotto_num_prompt()
