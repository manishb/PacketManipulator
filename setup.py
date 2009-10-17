#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2008 Adriano Monteiro Marques
#
# Author: Abhiram Kasina <abhiram.casina@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

import os.path
from umit.pm.gui.plugins.containers import setup

setup(
    name='MSC',
    version='0.1',
    author=['Abhiram Kasina', 'Luís A. Bastião Silva'],
    license=['GPL'],
    copyright=['2009 Adriano Monteiro Marques'],
    url='http://trac.umitproject.org/wiki/AbhiramKasina',
    scripts=['sources/main.py', 'sources/chart.py', 'sources/preferences.py',
             'sources/prefmanager.py' , 'sources/filter.py' ],
    start_file="main", 
    data_files=[('data', ['dist/logo.png'])],
    provide=['=MSC-0.1'],
    description='Message Sequence Flowchart',
    output='msc.ump'
)
