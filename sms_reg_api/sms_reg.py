import time
import requests
from sms_reg_api.exceptions import *


class Sms:
    def __init__(self, api_key):
        self._api_key = api_key
        self._check_auth()

    def _send(self, method, param=None):
        response = requests.get(f'http://api.sms-reg.com/{method}.php?{param}&apikey={self._api_key}').json()
        if response['response'] == 'ERROR':
            raise MethodError(response.get('error_msg', None))
        else:
            return response

    def _check_auth(self):
        if requests.get(f'http://api.sms-reg.com/getBalance.php?&'
                        f'apikey={self._api_key}').json()['response'] == 'ERROR':
            raise BadToken('Wrong api key')

    def balance(self):
        return self._send('getBalance')['balance']

    def set_rate(self, rate):
        return self._send('setRate', param=f'{float(rate)}')

    def get_list(self, extended=None):
        return requests.get(f'http://api.sms-reg.com/getList.php?extended={extended}&'
                            f'apikey={self._api_key}').json()['services']

    def get_num(self, service, country=None):
        if country:
            return self._send('getNum', param=f'country={country}&service={service}')['tzid']
        else:
            return self._send('getNum', param=f'service={service}')['tzid']

    def get_num_repeat(self, tzid):
        return self._send('getNumRepeat', param=f'tzid={tzid}')

    def set_ready(self, tzid):
        return self._send('set_ready', param=f'tzid={tzid}')

    def _get_state(self, tzid):
        return self._send('getState', param=f'tzid={tzid}')

    def get_operations(self, opstate=None, count=None, output=None):
        return self._send('getOperations', param=f'opstate={opstate}&'
                                                 f'count={count}&'
                                                 f'output={output}')

    def wait_number(self, tzid):
        while self._get_state(tzid).get('response', None) == 'TZ_INPOOL':
            time.sleep(3)

        response = self._get_state(tzid)

        if response.get('response', None) == 'TZ_NUM_PREPARE':
            return response['number']
        else:
            return False

    def wait_answer(self, tzid):
        while self._get_state(tzid).get('response', None) == 'TZ_NUM_WAIT':
            time.sleep(3)

        response = self._get_state(tzid)

        if response.get('response', None) == 'TZ_NUM_ANSWER':
            return response['msg']
        else:
            return False

    def set_ok(self, tzid):
        return self._send('setOperationOk', param=f'tzid={tzid}')

    def set_used(self, tzid):
        return self._send('setOperationUsed', param=f'tzid={tzid}')
