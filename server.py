# -*- coding: utf-8 -*-
import logging
from SocketServer import TCPServer
from collections import defaultdict

from umodbus import conf
from umodbus.server.tcp import RequestHandler, get_server
from umodbus.utils import log_to_stream

config = {
    'log_level': logging.DEBUG,
    'signed_values': True,
    'ip-address': '192.168.1.122',
    'port': 1502,
    'data-file': '/home/pi/data.txt',
    'value-separator': ";",
    'address-range': list(range(0, 10))
}

log_to_stream(level=config['log_level'])

conf.SIGNED_VALUES = config['signed_values']

TCPServer.allow_reuse_address = True
app = get_server(TCPServer, (config['ip-address'], config['port']), RequestHandler)

@app.route(slave_ids=[1], function_codes=[3, 4], addresses=config['address-range'])
def read_data_store(slave_id, function_code, address):
    """" Return value of address. """
    data = _read_file()
    return int(data[address])

@app.route(slave_ids=[1], function_codes=[6, 16], addresses=config['address-range'])
def write_data_store(slave_id, function_code, address, value):
    """" Set value for address. """
    data = _read_file()    
    data[address] = value
    _write_file(data)

def _read_file():
    with open(config['data-file'], "r") as data_file:
        return data_file.read().split(config['value-separator'])   
     
def _write_file(data):
    with open(config['data-file'], "w") as data_file:
        data_file.write(config['value-separator'].join(map(str, data)))

if __name__ == '__main__':
    app.serve_forever()