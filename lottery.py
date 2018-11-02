from typing import List, Dict

import requests

import argparse
import logging


def parse_number(rawstr: str)-> List[str]:
    return rawstr.split(':')


def check_winning_dates(json_response: List[Dict]):
    if json_response:
        print('Winning Dates: ')
        for elem in json_response:
            print(elem['draw_date'][0:9]) #print only the date portion of timestamp
    else:
        print('No Winners!')


def check_winner(lotto_num):
    mega_url = 'https://data.ny.gov/resource/h6w8-42p9.json'
    pb_url = 'https://data.ny.gov/resource/8vkr-v8vh.json'
    lotto_num = lotto_num.split(':')
    first_five_nums = lotto_num[0].replace(' ','%20')
    last_num = lotto_num[1]

    response = requests.get(''.join([mega_url,'?winning_numbers=',first_five_nums,'&mega_ball=',last_num]))
    mega_json = response.json()
    response = requests.get(''.join([pb_url,'?winning_numbers=',first_five_nums,'%20',last_num]))
    pb_json = response.json()

    print('Checking MegaMillions...')
    check_winning_dates(mega_json)
    print('Checking Powerball...')
    check_winning_dates(pb_json)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('lotto_num', help='Check to see if the number has won Powerball or MegaMillions'
                        '\nFormat=nn nn nn nn:nn')
    args = parser.parse_args()
    check_winner(args.lotto_num)
