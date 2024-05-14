"""
SPDX-License-Identifier: Apache-2.0
Copyright (c) 2024, Ampere Computing LLC
"""

import io
import unittest
from src.advisor.reports.report import Report
from src.advisor.scanners.meson_scanner import MesonScanner


class TestMesonScanner(unittest.TestCase):
    def test_accepts_file(self):
        meson_scanner = MesonScanner()
        self.assertFalse(meson_scanner.accepts_file('test'))
        self.assertTrue(meson_scanner.accepts_file('meson.build'))

    def test_scan_file_object(self):
        meson_scanner = MesonScanner()
        report = Report('/root')
        io_object = io.StringIO('xxx')
        meson_scanner.scan_file_object(
            'meson.build', io_object, report)
        self.assertEqual(len(report.issues), 0)


    def test_arch_specific_libs_re(self):
        match = MesonScanner.ARCH_SPECIFIC_LIBS_RE_PROG.search("cc.find_library('foo')")
        self.assertIsNone(match)
        match = MesonScanner.ARCH_SPECIFIC_LIBS_RE_PROG.search("cc.find_library('otherarch')")
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), "otherarch")

    def test_arch_specific_libs(self):
        meson_scanner = MesonScanner()
        report = Report('/root')
        io_object = io.StringIO("cc.find_library('otherarch')")
        meson_scanner.scan_file_object(
            'meson.build', io_object, report)
        self.assertEqual(len(report.issues), 1)

    def test_neoverse_specific_opts_line_re(self):
        match = MesonScanner.NEOVERSE_SPECIFIC_OPTS_RE_PROG.search("'compiler_options':  ['-mcpu=ampere1a'],")
        self.assertIsNone(match)
        match = MesonScanner.NEOVERSE_SPECIFIC_OPTS_RE_PROG.search("'compiler_options':  ['-mcpu=neoverse-n2'],")
        self.assertIsNotNone(match)

    def test_ampereone_specific_opts_line_re(self):
        match = MesonScanner.AMPEREONE_SPECIFIC_OPTS_RE_PROG.search("'compiler_options':  ['-mcpu=neoverse-n2'],")
        self.assertIsNone(match)
        match = MesonScanner.AMPEREONE_SPECIFIC_OPTS_RE_PROG.search("'compiler_options':  ['-mcpu=ampere1a'],")
        self.assertIsNotNone(match)

    def test_neoverse_specific_opts_line(self):
        meson_scanner = MesonScanner()

        report = Report('/root')
        io_object = io.StringIO("'compiler_options':  ['-mcpu=neoverse-n2'],")
        meson_scanner.scan_file_object(
            'meson.build', io_object, report)
        # Should report 2 issues, one for neoverse flag indication, another for ampereone flag missing.
        self.assertEqual(len(report.issues), 2)

        report = Report('/root')
        io_object = io.StringIO("'compiler_options':  ['-mcpu=ampere1a'],\n'compiler_options':  ['-mtune=ampere1a'],\n'compiler_options':  ['-mcpu=neoverse-v2'],\n'compiler_options':  ['-mtune=neoverse-v2'],\n")
        meson_scanner.scan_file_object(
            'meson.build', io_object, report)
        self.assertEqual(len(report.issues), 2)


