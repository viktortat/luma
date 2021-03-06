# coding=utf-8
"""Author: Michal Wrona
Copyright (C) 2016 ACK CYFRONET AGH
This software is released under the MIT license cited in 'LICENSE.txt'

Example Swift credentials generator.
"""

import ConfigParser
import os

from luma.credentials import SwiftCredentials

config = ConfigParser.RawConfigParser()
config.read(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), 'generators.cfg'))

USER_NAME = config.get('swift', 'user_name')
PASSWORD = config.get('swift', 'password')


def create_user_credentials(storage_type, storage_id, space_name, client_ip,
                            user_details):
    """Creates user credentials for Swift storage based on provided user data.
    """
    return SwiftCredentials(USER_NAME, PASSWORD)
