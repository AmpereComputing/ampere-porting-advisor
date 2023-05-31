"""
SPDX-License-Identifier: Apache-2.0
Copyright (c) 2021, Ampere Computing LLC
"""

from .issue import Issue
from ..localization import _


class ArchSpecificBuildOptionIssue(Issue):
    def __init__(self, filename, lineno, opt_name):
        description = _("architecture-specific build option is not available on aarch64: -m%s") % \
            opt_name
        super().__init__(description=description, filename=filename,
                         lineno=lineno)
