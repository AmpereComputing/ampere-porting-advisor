"""
SPDX-License-Identifier: Apache-2.0
Copyright (c) 2024, Ampere Computing LLC
"""

from .issue import Issue
from ..localization import _
from ..report_item import ReportItem


class ArchSpecificBuildOptionIssue(Issue):
    def __init__(self, filename, lineno, opt_name):
        description = _("architecture-specific build option is not available on aarch64: -m%s") % \
            opt_name
        super().__init__(description=description, filename=filename,
                         lineno=lineno)
        
class NeoverseSpecificBuildOptionIssue(Issue):
    def __init__(self, filename, lineno, opt_name, opt_value):
        description = (_("neoverse-specific build option may not appropriate for AmpereOne: "
                         "-m%s=%s, see https://amperecomputing.com/tutorials/gcc-guide-ampere-processors for more details.") \
                         % (opt_name, opt_value))
        super().__init__(description=description, filename=filename,
                         lineno=lineno, item_type=ReportItem.NEUTRAL)
        
class AmpereoneSpecificBuildOptionIssue(Issue):
    def __init__(self, filename, lineno):
        description = (_("Missing build option for AmpereOne, see "
                         "https://amperecomputing.com/tutorials/gcc-guide-ampere-processors for more details."))
        super().__init__(description=description, filename=filename,
                         lineno=lineno, item_type=ReportItem.NEUTRAL)
