from typing import List, Dict, Tuple

import requests
import sqlite3
import logging

class LottoNumber:

    def __init__(self, raw_number: str):
        self.first_numbers, self.powernum = self._parse_number(raw_number)

    def _parse_number(self, raw_number: str):
        splitlist = raw_number.split(':')
        first_five = splitlist[0].split()
        power_num = splitlist[1].strip()

        return first_five, power_num

    def check_winners(self):
        '''Check to see if any of the number combinations have won. Need to pass in DB connection'''
        pass





#
# def parse_number(rawstr: str)-> List[str]:
#     return rawstr.split(':')
#
#
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


def lotto_num_prompt():
    number = input('Enter your lotto number as NN NN NN NN NN:NN')



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)


    lotto_num = lotto_num_prompt()
