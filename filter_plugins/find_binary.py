from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
  filter: find_binary
  author: Alex Wicks <alex@awicks.io>
  short_description: Return path to binary
  description:
    - Find binary passed as parameter to filter
    - stdout_lines from pacman -Ql should be provided as input, and name of file to find as argument
"""
from ansible import errors


class FilterModule(object):

    def filters(self):
        return {
          "find_binary": self.find_binary,
        }

    def find_binary(self, pacman_stdout, binary_name):

        if not isinstance(pacman_stdout, list):
            raise errors.AnsibleFilterError("Expected list. Use stdout_lines")

        for line in pacman_stdout:
            # Extract file path
            filename = line.split()[1]

            # Split by '/' into path components
            # Then check if our parameter is in the list
            if binary_name in filename.split("/"):
                return filename

        # Catch-all
        # Return None if nothing found
        return None
