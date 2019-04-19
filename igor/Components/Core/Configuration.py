# Copyright 2019 SocIsomer
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import json


class Config:

    CONFIGURATION_JSON = None
    CONFIGURATION_JSON_PATH = None
    CURRENT_PROJECT = None
    CURRENT_PROJECT_PATH = None
    FONT = None
    RECENT_PROJECTS = []

    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(__file__))
        pass

    def load_configuration(self):
        Config.CONFIGURATION_JSON_PATH = os.path.join(self.path, 'default.json')

        with open(Config.CONFIGURATION_JSON_PATH, 'r') as config_file:
            Config.CONFIGURATION_JSON = json.loads(config_file.read())

        Config.CURRENT_PROJECT = Config.CONFIGURATION_JSON['project_name']
        Config.CURRENT_PROJECT_PATH = Config.CONFIGURATION_JSON['project_path']

    def import_project(self):
        pass

    def save_configuration(self):
        pass