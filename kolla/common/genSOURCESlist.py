#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-08-28 16:47
# @Author  : czwei

import urllib

openstack_item = [
    'openstack-base',
    'aodh-base',
    'barbican-base',
    'bifrost-base'
    'blazar-base',
    'ceilometer-base',
    'cinder-base',
    'congress-base',
    'cloudkitty-base',
    'designate-base',
    'dragonflow-base',
    'ec2-api',
    'freezer-api',
    'freezer-base',
    'glance-base',
    'gnocchi-base',
    'heat-base',
    'horizon',
    'ironic-base',
    'ironic-inspector',
    'karbor-base',
    'keystone-base',
    'kuryr-base',
    'kuryr-libnetwork',
    'magnum-base',
    'manila-base',
    'mistral-base',
    'monasca-api',
    'monasca-log-api',
    'monasca-notification',
    'monasca-persister',
    'monasca-statsd',
    'murano-base',
    'neutron-base',
    'neutron-bgp-dragent',
    'neutron-lbaas-agent',
    'neutron-vpnaas-agent',
    'nova-base',
    'novajoin-base',
    'octavia-base',
    'opendaylight',
    'panko-base',
    'rally',
    'sahara-base',
    'searchlight-base',
    'senlin-base',
    'solum-base',
    'swift-base',
    'tacker-base',
    'tempest',
    'trove-base',
    'vitrage-base',
    'vmtp',
    'watcher-base',
    'zaqar',
    'zun-base'
]

SOURCES = {}

for item in openstack_item:
    if 'base' in item:
        SOURCES[item] = {'type': 'git', 'location': 'https://github.com/openstack/' + item.split('-')[0], 'reference':
            'stable/ocata' }
    elif 'agent' in item:
        SOURCES[item] = {'type': 'git', 'location': 'https://github.com/openstack/' + item.split('-')[0] +
                                                    item.split('-')[1], 'reference': 'stable/ocata' }
    else:
        SOURCES[item] = {'type': 'git', 'location': 'https://github.com/openstack/' + item, 'reference': 'stable/ocata'
                         }
    url = SOURCES[item]['location']
    state = urllib.urlopen(url).code
    print (url,state)

