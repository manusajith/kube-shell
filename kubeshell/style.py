# Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from __future__ import print_function, absolute_import, unicode_literals
from pygments.token import Token
from pygments.util import ClassNotFound
from pygments.styles import get_style_by_name
from prompt_toolkit.styles import style_from_pygments_cls, merge_styles, Style
from pygments.styles.default import DefaultStyle


class StyleFactory(object):
    """Provide styles for the autocomplete menu and the toolbar.

    :type style: :class:`pygments.style.StyleMeta`
    :param style: Contains pygments style info.
    """

    def __init__(self, style_name):
        self.style = self.style_factory(style_name)

    def style_factory(self, style_name):
        """Retrieve the specified pygments style.

        If the specified style is not found, the vim style is returned.

        :type style_name: str
        :param style_name: The pygments style name.

        :rtype: :class:`pygments.style.StyleMeta`
        :return: Pygments style info.
        """

        return merge_styles([style_from_pygments_cls(DefaultStyle),
                            Style.from_dict({
            'path': 'ansicyan underline',
            'prompt': 'fg:ansiblue bold',
            'state': 'fg:ansigreen bold',
            'danger': 'fg:ansired bold',
            })])
