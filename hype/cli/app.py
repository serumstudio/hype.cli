
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

import optparse
import inspect
from typing import Callable
from typing import Any
from typing import Optional
from typing import get_type_hints
from .utils import CommandDict


class HypeCLI:
    """
    
    """

    #: This variable is used for storing all commands.
    #: Return dictionary.
    __commands: dict = {}

    def __init__(self, *, name: Optional[str] = None,
                help: Optional[str] = None):

        #: The name of the app, cli to be used in.
        #: Default value = None.
        self.name = name

        #: Your custom help command for the app.
        #: Default value = None
        self.help = help


    
    @property
    def commands(self):
        """ List of all commands """
        return [item[0] for item in self.__commands.items()]


    def command(self, name: Optional[str] = None, description: Optional[str] = None, 
            default: Optional[Any] = None, hidden: Optional[bool] = False, 
            deprecated: Optional[bool] = False, _func: Callable[..., Any] = None):

        """
        A command decorator for creating commands.

        Example:

            >>> app = HyperCLI()
            >>> ...
            >>> @app.commands(name='greet')
            >>> def greet(name: str):
            >>>     print(f"Hello {name}!")


        Parameters:
            name (str):
                The name of the command. If none, return the function name

            description (str):
                The description for the command.
            
            default (str):
                Default value for the command.

            hidden (bool):
                Set if the command is hidden.

            deprecated (bool):
                Set if the command is deprecated.
        
        """

        _name = name or _func.__name__
        _desc = description
        _default = default
        _hidden = hidden
        _deprecated = deprecated

        
        def deco(_func):
            
            
            sign = inspect.signature(_func)
            type_hints = get_type_hints(_func)
            params = []
            
            for param in sign.parameters.values():
                
                if param.name in type_hints:
                    annotation = type_hints[param.name]
                    _params = (param.name, annotation)

                else:
                    _params = (param.name, None)

                params.append(_params)


            command_dict = CommandDict(name = _name, params = params, desc = _desc,
                    default = _default, hidden = _hidden, deprecated = _deprecated, func = _func)

            self.__commands.update(command_dict.dict())

            return _func
                
        return deco(_func) if _func else deco


    def run(self):
        """
        Run the application as well as load all the commands.
        
        Example Application:

            >>> app = HyperCLI()
            >>> ...
            >>> @app.commands(name='greet')
            >>> def greet(name: str):
            >>>     print(f"Hello {name}!")
            >>> ...
            >>> if __name__ == "__main__":
            >>>     app.run() 
        
        """

        