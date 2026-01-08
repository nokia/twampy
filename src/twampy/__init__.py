#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2013-2026 Nokia

"""twampy - TWAMP/TWAMP-light/STAMP implementation.

Python implementation of Two-Way Active Measurement Protocol (TWAMP/TWAMP-light)
as defined in RFC 5357, Simple Two-Way Active Measurement Protocol (STAMP) as
defined in RFC 8762, and STAMP Optional Extensions as defined in RFC 8972.

Developed for validation of Nokia SR OS and SR Linux TWAMP/STAMP implementations.
"""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("twampy")
except PackageNotFoundError:
    # Package not installed (development mode before pip install -e .)
    __version__ = "0.0.0-dev"

__author__ = "Sven Wisotzky"
__license__ = "BSD-3-Clause"
__copyright__ = "Copyright (c) 2013-2026 Nokia"

__all__ = []
