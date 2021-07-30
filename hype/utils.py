#                   Copyright (c) 2021, Serum Studio

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from typing import Optional
from typing import Any
from typing import Callable
import inspect


def convert_param_to_option(param: str = None) -> str:
    if len(param) > 1:
        fmt_str = "--{}".format(param)

    else:
        fmt_str = "-{}".format(param)

    return fmt_str

def convert_option_to_string(option: str=None) -> str:
    return option.split('--')[1]


class ParamOption:
    def __init__(
        self,
        name: str = None,
        required: bool = None,
        default: Any = None,
        type: type = None,
    ):

        self.name = name
        self.required = required
        self.default = default
        self.type = type

    @property
    def to_dict(self):
        return {
            "name": self.name,
            "required": self.required,
            "default": self.default,
            "type": self.type,
        }


class CommandDict:
    def __init__(
        self,
        name: str,
        usage: str = None,
        help: str = None,
        aliases: tuple = None,
        opt: list = [],
        func: Callable[..., Any] = None,
    ):

        self.name = name
        self.usage = usage
        self.help = help
        self.aliases = aliases
        self.opt = opt
        self.func = func

    @property
    def to_dict(self):
        return {
            "name": self.name,
            "usage": self.usage,
            "help": self.help,
            "aliases": self.aliases,
            "options": self.opt,
            "func": self.func,
        }