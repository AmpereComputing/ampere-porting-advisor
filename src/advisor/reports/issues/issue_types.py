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

import importlib
import os
import pkgutil
from .issue import Issue

pkg_dir = os.path.dirname(__file__)
for (module_loader, name, ispkg) in pkgutil.iter_modules([pkg_dir]):
    if name.endswith('_issue'):
        importlib.import_module('.' + name, __package__)

def _transitive_closure(cls):
    subclasses = cls.__subclasses__()
    return subclasses + [descendant for subcls in subclasses for descendant in _transitive_closure(subcls)]

ISSUE_TYPES = {cls.display_name(): cls for cls in _transitive_closure(Issue)}

