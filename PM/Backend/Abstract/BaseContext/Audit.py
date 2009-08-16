#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2008 Adriano Monteiro Marques
#
# Author: Francesco Piccinno <stack.box@gmail.com>
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

from Timed import TimedContext
from PM.Backend.Abstract.Context import register_audit_context

class BaseAuditContext(TimedContext):
    "A context representing an audit"

    has_stop = True
    has_pause = False
    has_restart = False
    file_types = []

    def __init__(self, dev1, dev2=None, bpf_filter=None, capmethod=0):
        """
        @param dev1 the first interface to sniff on
        @param dev2 the second interface to sniff on (used in bridged sniffing)
                    or None
        @param bpf_filter pcap filter to apply to the inputs interfaces
        @param capmethod use 0 for standard capture, 1 for tcpdump and 2 for
                         dumpcap helper
        @return a BaseAuditContext
        """

        TimedContext.__init__(self)

        self._iface1 = dev1
        self._iface2 = dev2

        # These are sockets used to send packets
        self._l2_socket = None
        self._l3_socket = None
        self._lb_socket = None

        # Listen sockets
        self._listen_dev1 = None
        self._listen_dev2 = None

        self.capmethod = capmethod
        self.status = self.SAVED

    def _stop(self):
        pass

    def get_l2socket(self): return self._l2_socket
    def get_l3socket(self): return self._l3_socket
    def get_lbsocket(self): return self._lb_socket

    def get_ip1(self): pass
    def get_mac1(self): pass
    def get_ip2(self): pass
    def get_mac2(self): pass
    def get_mtu(self): pass
    def get_mtu1(self): pass
    def get_mtu2(self): pass
    def get_iface1(self): return self._iface1
    def get_iface2(self): return self._iface2
    def get_netmask1(self): pass
    def get_netmask2(self): pass

    l2_socket = property(get_l2socket)
    l3_socket = property(get_l3socket)
    lb_socket = property(get_lbsocket)

    ip1 = property(get_ip1)
    ip2 = property(get_ip2)

    mac1 = property(get_mac1)
    mac2 = property(get_mac2)

    mtu = property(get_mtu)
    mtu1 = property(get_mtu1)
    mtu2 = property(get_mtu2)

    iface1 = property(get_iface1)
    iface2 = property(get_iface2)

    netmask1 = property(get_netmask1)
    netmask2 = property(get_netmask2)

AuditContext = register_audit_context(BaseAuditContext)