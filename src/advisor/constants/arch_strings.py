"""
Copyright 2017-2018 Arm Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

SPDX-License-Identifier: Apache-2.0
"""

AARCH64_ARCHS = ['arm', 'aarch64', 'arm64', 'neon', 'sve']

NON_AARCH64_ARCHS = ['alpha', 'altivec', 'amd64', 'avx', 'avx512', 'hppa',
                     'i386', 'i586', 'i686', 'ia64', 'intel', 'intel64', 'ix86', 'loongarch64',
                     'm68k', 'microblaze', 'mips', 'nios2', 'otherarch', 'penryn', 'power',
                     'powerpc', 'powerpc32', 'powerpc64', 'ppc', 'ppc64', 'ppc64le', 'riscv64',
                     'sandybridge', 's390', 'sh', 'sifive_x280', 'sparc', 'sse', 'sse2', 'sse3',
                     'tile', 'x64', 'x86', 'x86_64', 'zarch', 'zen', 'zen2', 'zen3']

COMPILERS = ['clang', 'cray', 'flang', 'gcc', 'gfortran', 'gnuc', 'gnug', 'ibmcpp', 'ibmxl', 'icc', 'ifort',
             'intel', 'intel_compiler', 'llvm', 'pathscale', 'pgi', 'pgic', 'sunpro', 'xlc', 'xlf']
