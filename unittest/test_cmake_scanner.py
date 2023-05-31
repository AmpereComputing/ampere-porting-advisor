"""
SPDX-License-Identifier: Apache-2.0
Copyright (c) 2021, Ampere Computing LLC
"""

import io
import unittest
from src.advisor.reports.report import Report
from src.advisor.scanners.cmake_scanner import CMakeScanner


class TestCMakeScanner(unittest.TestCase):
    def test_accepts_file(self):
        cmake_scanner = CMakeScanner()
        self.assertFalse(cmake_scanner.accepts_file('test'))
        self.assertTrue(cmake_scanner.accepts_file('CMakeLists.txt'))

    def test_scan_file_object(self):
        cmake_scanner = CMakeScanner()
        report = Report('/root')
        io_object = io.StringIO('xxx')
        cmake_scanner.scan_file_object(
            'CMakeLists.txt', io_object, report)
        self.assertEqual(len(report.issues), 0)


    def test_arch_specific_libs_re(self):
        match = CMakeScanner.ARCH_SPECIFIC_LIBS_RE_PROG.search('find_library(foo CONFIG REQUIRED)')
        self.assertIsNone(match)
        match = CMakeScanner.ARCH_SPECIFIC_LIBS_RE_PROG.search('find_library(otherarch CONFIG REQUIRED)')
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), "otherarch")

    def test_arch_specific_libs(self):
        cmake_scanner = CMakeScanner()
        report = Report('/root')
        io_object = io.StringIO('find_library(otherarch CONFIG REQUIRED)')
        cmake_scanner.scan_file_object(
            'CMakeLists.txt', io_object, report)
        self.assertEqual(len(report.issues), 1)

    def test_other_arch_cpu_line_re(self):
        match = CMakeScanner.OTHER_ARCH_CPU_LINE_RE_PROG.search('if(${CMAKE_SYSTEM_PROCESSOR} STREQUAL "aarch64"')
        self.assertIsNone(match)
        match = CMakeScanner.OTHER_ARCH_CPU_LINE_RE_PROG.search('if(${CMAKE_SYSTEM_PROCESSOR} STREQUAL "otherarch"')
        self.assertIsNotNone(match)

    def test_aarch64_cpu_line_re(self):
        match = CMakeScanner.AARCH64_CPU_LINE_RE_PROG.search('if(${CMAKE_SYSTEM_PROCESSOR} STREQUAL "otherarch"')
        self.assertIsNone(match)
        match = CMakeScanner.AARCH64_CPU_LINE_RE_PROG.search('if(${CMAKE_SYSTEM_PROCESSOR} STREQUAL "aarch64"')
        self.assertIsNotNone(match)

    def test_other_arch_cpu_line(self):
        cmake_scanner = CMakeScanner()

        report = Report('/root')
        io_object = io.StringIO('if(${CMAKE_SYSTEM_PROCESSOR} STREQUAL "otherarch"')
        cmake_scanner.scan_file_object(
            'CMakeLists.txt', io_object, report)
        self.assertEqual(len(report.issues), 1)

        report = Report('/root')
        io_object = io.StringIO('if(${CMAKE_SYSTEM_PROCESSOR} STREQUAL "arm"\nTARGET_ARCH=aarch64\nif(${CMAKE_SYSTEM_PROCESSOR} STREQUAL "otherarch"\nTARGET_ARCH=otherarch\n!ENDIF')
        cmake_scanner.scan_file_object(
            'CMakeLists.txt', io_object, report)
        self.assertEqual(len(report.issues), 0)

    def test_continuation(self):
        cmake_scanner = CMakeScanner()
        report = Report('/root')
        # Should be treated as a single line and only one issue reported.
        io_object = io.StringIO('find_library(otherarch CONFIG REQUIRED)\\\nfind_package(otherarch CONFIG REQUIRED)')
        cmake_scanner.scan_file_object(
            'CMakeLists.txt', io_object, report)
        self.assertEqual(len(report.issues), 1)
