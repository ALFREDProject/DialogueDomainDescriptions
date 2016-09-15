#!/usr/bin/env python

import subprocess
import sys

subprocess.call("tdm_session_and_backend_manager.py --open-recognizer-support %s" % (" ".join(sys.argv[1:])), shell=True)
