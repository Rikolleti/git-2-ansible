#!/usr/bin/python

# GNU General Public License v3.0+
from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_test

short_description: Create a text file at path with provided content (no updates if exists)
version_added: "1.0.0"
description:
  - Creates a text file on the remote host at the given path with the specified content.
  - If the file already exists, the module does nothing.
options:
  path:
    description: Path to the file on the remote host.
    required: true
    type: path
  content:
    description: Text content to write into the file (UTF-8).
    required: true
    type: str
author:
  - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
- name: Create a file with content (no update if exists)
  my_namespace.my_collection.my_test:
    path: /tmp/hello.txt
    content: "Hello from Ansible!\n"
'''

RETURN = r'''
changed:
  description: Whether the file was created.
  type: bool
  returned: always
path:
  description: Path to the file on the remote host.
  type: str
  returned: always
message:
  description: Result message.
  type: str
  returned: always
'''

import os
from pathlib import Path
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path', required=True),
            content=dict(type='str', required=True),
        ),
    )

    path = Path(module.params['path'])
    content = module.params['content']

    result = {
        'changed': False,
        'path': str(path),
        'message': ''
    }

    if str(path).strip() == '' or str(path).endswith(os.sep):
        module.fail_json(msg="Invalid file path.", **result)

    try:
        if path.exists():
            result['message'] = "File already exists. No action taken."
        else:
            with path.open('x', encoding='utf-8') as f:
                f.write(content)
            result['changed'] = True
            result['message'] = "File created."
        module.exit_json(**result)

    except Exception as e:
        module.fail_json(msg=f"Error: {e}", **result)


def main():
    run_module()


if __name__ == '__main__':
    main()
