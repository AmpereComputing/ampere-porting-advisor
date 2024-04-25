"""
SPDX-License-Identifier: Apache-2.0
Copyright (c) 2024, Ampere Computing LLC
"""

import os
import re
from ..constants.arch_strings import AARCH64_ARCHS, NON_AARCH64_ARCHS
from ..constants.arch_specific_libs import ARCH_SPECIFIC_LIBS
from ..constants.arch_specific_options import X86_SPECIFIC_OPTS
from ..constants.arch_specific_options import NEOVERSE_SPECIFIC_OPTS
from ..constants.arch_specific_options import AMPEREONE_SPECIFIC_OPTS
from ..parsers.continuation_parser import ContinuationParser
from ..reports.issues.arch_specific_library_issue import ArchSpecificLibraryIssue
from ..reports.issues.arch_specific_build_option_issue import ArchSpecificBuildOptionIssue
from ..reports.issues.arch_specific_build_option_issue import NeoverseSpecificBuildOptionIssue
from ..reports.issues.arch_specific_build_option_issue import AmpereoneSpecificBuildOptionIssue
from ..reports.issues.define_other_arch_issue import DefineOtherArchIssue
from .scanner import Scanner


class MesonScanner(Scanner):
    """Scanner that scans Meson builds"""

    MESON_NAMES = ['meson.build']

    X86_SPECIFIC_OPTS_RE_PROG = re.compile(r'-m(%s)' %
                                            '|'.join([(r'%s\b' % x) for x in X86_SPECIFIC_OPTS]))
    ARCH_SPECIFIC_LIBS_RE_PROG = re.compile(r'(?:find_package|find_library)\((%s)' %
                                            '|'.join([(r'%s\b' % x) for x in ARCH_SPECIFIC_LIBS]))
    NEOVERSE_SPECIFIC_OPTS_RE_PROG = re.compile(r'-m(cpu|tune)=(%s)' %
                                            '|'.join([(r'%s\b' % x) for x in NEOVERSE_SPECIFIC_OPTS]))
    AMPEREONE_SPECIFIC_OPTS_RE_PROG = re.compile(r'-m(cpu|tune)=(%s)' %
                                            '|'.join([(r'%s\b' % x) for x in AMPEREONE_SPECIFIC_OPTS]))

    def accepts_file(self, filename):
        basename = os.path.basename(filename)
        return basename in MesonScanner.MESON_NAMES

    def scan_file_object(self, filename, file, report):
        continuation_parser = ContinuationParser()
        seen_neoverse_build_flag = False
        seen_ampere1_build_flag = False

        for lineno, line in enumerate(file, 1):
            line = continuation_parser.parse_line(line)

            if not line:
                continue

            match = MesonScanner.ARCH_SPECIFIC_LIBS_RE_PROG.search(line)
            if match:
                lib_name = match.group(1)
                report.add_issue(ArchSpecificLibraryIssue(
                    filename, lineno + 1, lib_name))
            match = MesonScanner.X86_SPECIFIC_OPTS_RE_PROG.search(line)
            if match:
                opt_name = match.group(1)
                report.add_issue(ArchSpecificBuildOptionIssue(
                    filename, lineno + 1, opt_name))
            match = MesonScanner.NEOVERSE_SPECIFIC_OPTS_RE_PROG.search(line)
            if match:
                seen_neoverse_build_flag = True
                opt_name = match.group(1)
                opt_value = match.group(2)
                report.add_issue(NeoverseSpecificBuildOptionIssue(
                    filename, lineno + 1, opt_name, opt_value))
            match = MesonScanner.AMPEREONE_SPECIFIC_OPTS_RE_PROG.search(line)
            if match:
                seen_ampere1_build_flag = True
        if seen_neoverse_build_flag and not seen_ampere1_build_flag:
            report.add_issue(AmpereoneSpecificBuildOptionIssue(filename, lineno + 1))
