#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright 2018, GeoSolutions Sas.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
#
#########################################################################

from django.conf.urls import include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = [
    url(r"^o/", include("serapide_core.urls", namespace="serapide_core")),
]


urlpatterns += [url(r"^admin/", admin.site.urls)]
