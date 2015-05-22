#!/usr/bin/env python

# todo.txt task manager cli
# Copyright (C) 2015 Robert van Bregt
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import argparse

__version__   = "0.0.1"
__date__      = "2015-05-22"
__author__    = "Robert van Bregt (robert@robertvanbregt.nl)"
__copyright__ = "Copyright 2015, Robert van Bregt"
__license__   = "GPL"

def todo_arguments():
    parser = argparse.ArgumentParser(description='Manage your TODO.TXT')
    args = parser.parse_args()
    
if __name__ == "__main__":
    args = todo_arguments()
    sys.exit()