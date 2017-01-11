# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
test_server_group
----------------------------------

Functional tests for `shade` server_group resource.
"""

from shade.tests.functional import base


class TestServerGroup(base.BaseFunctionalTestCase):

    def test_server_group(self):
        server_group_name = self.getUniqueString()
        self.addCleanup(self.cleanup, server_group_name)
        server_group = self.demo_cloud.create_server_group(
            server_group_name, ['affinity'])

        server_group_ids = [v['id']
                            for v in self.demo_cloud.list_server_groups()]
        self.assertIn(server_group['id'], server_group_ids)

        self.demo_cloud.delete_server_group(server_group_name)

    def cleanup(self, server_group_name):
        server_group = self.demo_cloud.get_server_group(server_group_name)
        if server_group:
            self.demo_cloud.delete_server_group(server_group['id'])
