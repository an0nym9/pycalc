import sys
import inspect
from functools import wraps

class Result:
    def __init__(self, result: any, safe: bool, /) -> None:
        """Initialize a Result object."""
        self.result = result
        self.safe = safe

    def __str__(self) -> str:
        """Return the result as a string."""
        return str(self.result)

    def __repr__(self) -> str:
        """Return the result as a string wrap in an Ok or Err."""
        return (
            f"Ok({self.result})"
            if self.safe else
            f"Err({self.result})"
        )

    def __bool__(self) -> bool:
        """Returns True or False if safe"""
        return self.result if self.safe else False

    def unwrap(self, msg: str = "Error Occured", /) -> any:
        """Exit the program if not safe else return result."""
        if not self.safe:
            print(msg)
            sys.exit(1)
        return self.result

    def unwrap_or(self, default: any = None, /) -> any:
        """Return a default value if not safe else return result."""
        if not self.safe:
            return default
        return self.result

    def ok(self) -> any:
        """Return the result if safe else return None."""
        return self.result if self.safe else None

    def err(self) -> any:
        """Return the result if not safe else return None."""
        return self.result if not self.safe else None

    def is_ok(self) -> bool:
        """Return True if safe else return False."""
        return self.safe

    def is_err(self) -> bool:
        """Return True if not safe else return False."""
        return not self.safe

def handle_exception(func: callable, /,) -> callable:
    """Safely handle errors to prevent code from crashing."""
    @wraps(func)
    def wrapper(*args, **kwargs,) -> Result:
        try:
            return Result(func(*args, **kwargs,), True,)
        except Exception as err:
            return Result(err, False,)
    return wrapper

def enhance_params(func: callable, /,) -> callable:
    """Enhance function parameter types."""
    original = getattr(func, "__wrapper__", func) # get the original function
    def wrapper(*args, **kwargs,) -> any:
        annotations = func.__annotations__
        sig = inspect.signature(func)
        bound = inspect.signature(wrapper).bind_partial(*args, **kwargs)
        pos = {key: i for i, key in enumerate(annotations.keys()) if key != "return"}
        for name, param, in sig.parameters.items():
            if param.default is not inspect.Parameter.empty:
                continue
            if str(param.kind) == "POSITIONAL_ONLY":
                if ((a := param.annotation) != (b := type(pargs := bound.arguments["args"][pos[name]])) and
                    str(param.annotation).split('[')[0] != b.__name__ and not any(type(arg) == str for arg in pargs)):
                    raise TypeError(f"Parameter '{name}' is expected to be of type {a.__name__}, got {b.__name__}.")
        return original(*args, **kwargs)
    return wrapper
