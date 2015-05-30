# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:

# Copyright 2014-2015 Florian Bruhin (The Compiler) <mail@qutebrowser.org>
#
# This file is part of qutebrowser.
#
# qutebrowser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# qutebrowser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with qutebrowser.  If not, see <http://www.gnu.org/licenses/>.

"""Tests for the Enum class."""

from qutebrowser.utils import usertypes

import pytest

# FIXME: Add some more tests, e.g. for is_int


@pytest.fixture
def enum():
    return usertypes.enum('Enum', ['one', 'two'])


def test_values(enum):
    """Test if enum members resolve to the right values."""
    assert enum.one.value == 1
    assert enum.two.value == 2


def test_name(enum):
    """Test .name mapping."""
    assert enum.one.name == 'one'
    assert enum.two.name == 'two'


def test_unknown(enum):
    """Test invalid values which should raise an AttributeError."""
    with pytest.raises(AttributeError):
        _ = enum.three


def test_start():
    """Test the start= argument."""
    e = usertypes.enum('Enum', ['three', 'four'], start=3)
    assert e.three.value == 3
    assert e.four.value == 4
