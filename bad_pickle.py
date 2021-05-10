# contains bunch of buggy examples
# taken from
# https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03
"""
I have no idea what this does, but i hope its secure
"""

import base64
import subprocess
import _pickle as cPickle


# Input injection
def transcode_file(filename):
    """Transcodes file to output_file.mpg"""
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    subprocess.call(command, shell=False)  # a bad idea!


# Assert statements
def assert_admin(user):
    """Checks if user is admin, and executes secure code"""
    if not user.is_admin:
        print('user does not have access')
        return
    # secure code...


# Pickles
class RunBinSh:
    """used for running bash"""
    def __reduce__(self):
        return subprocess.Popen, (('/bin/sh',),)


print(base64.b64encode(cPickle.dumps(RunBinSh())))
