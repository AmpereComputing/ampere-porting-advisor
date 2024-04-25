"""
SPDX-License-Identifier: Apache-2.0
Copyright (c) 2024, Ampere Computing LLC
"""

X86_SPECIFIC_OPTS = ['mmx', 'sse', 'sse2', 'sse3', 'ssse3', 'sse4', 'sse4a', 'sse4.1', 'sse4.2', 'avx', 'avx2', 'avx512f', 'avx512pf', 'avx512er', 'avx512cd', 'avx512vl', 'avx512bw', 'avx512dq', 'avx512ifma', 'avx512vbmi', 'sha', 'aes', 'pclmul', 'clflushopt', 'clwb', 'fsgsbase', 'ptwrite', 'rdrnd', 'f16c', 'fma', 'pconfig', 'wbnoinvd', 'fma4', 'prfchw', 'rdpid', 'prefetchwt1', 'rdseed', 'sgx', 'xop', 'lwp', '3dnow', '3dnowa', 'popcnt', 'abm', 'adx', 'bmi', 'bmi2', 'lzcnt', 'fxsr', 'xsave', 'xsaveopt', 'xsavec', 'xsaves', 'rtm', 'hle', 'tbm', 'mwaitx', 'clzero', 'pku', 'avx512vbmi2', 'avx512bf16', 'avx512fp16', 'gfni', 'vaes', 'waitpkg', 'vpclmulqdq', 'avx512bitalg', 'movdiri', 'movdir64b', 'enqcmd', 'uintr', 'tsxldtrk', 'avx512vpopcntdq', 'avx512vp2intersect', 'avx5124fmaps', 'avx512vnni', 'avxvnni', 'avx5124vnniw', 'cldemote', 'serialize', 'amx-tile', 'amx-int8', 'amx-bf16', 'hreset', 'kl', 'widekl', 'avxifma', 'avxvnniint8', 'avxneconvert', 'cmpccxadd', 'amx-fp16', 'prefetchi', 'raoint', 'amx-complex']
"""Options that are not available on aarch64."""

NEOVERSE_SPECIFIC_OPTS = ['neoverse-n1', 'neoverse-n2', 'neoverse-v1', 'neoverse-v2']
"""Options for Arm Neoverse are not appropriate for AmpereOne family."""

AMPEREONE_SPECIFIC_OPTS = ['ampere1', 'ampere1a', 'ampere1b']
"""Options for AmpereOne family."""

ARCH_SPECIFIC_IN_BUILD_FILES = ['meson.build', 'CMakeLists.txt', 'Makefile.in', 'Makefile.am', 'Makefile.arm64', 'Makefile.aarch64']
"""Build files in aarch64 port dir can't be filter out as they might missing support for ampere1."""
