import sys
from colorama import Fore, Back


def yellow_background(s: str) -> str:  # pragma: no cover
    """Yellow color string if tty
    
    Args:
        s (str): String to color
    
    Returns:
        str: Colored string
    """
    if sys.stdout.isatty():
        return Back.YELLOW + Fore.BLACK + s + Fore.RESET + Back.RESET
    else:
        return s


def red(s: str) -> str:    # pragma: no cover
    """Red color string if tty
    
    Args:
        s (str): String to color
    
    Returns:
        str: Colored string

    Examples:
        >>> from chepy.modules.internal.colors import red
        >>> print(RED("some string"))
    """
    return Fore.RED + s + Fore.RESET if sys.stdout.isatty() else s


def blue(s: str) -> str:    # pragma: no cover
    """Blue color string if tty
    
    Args:
        s (str): String to color
    
    Returns:
        str: Colored string

    Examples:
        >>> from chepy.modules.internal.colors import blue
        >>> print(BLUE("some string"))
    """
    return Fore.BLUE + s + Fore.RESET if sys.stdout.isatty() else s


def cyan(s: str) -> str:    # pragma: no cover
    """Cyan color string if tty
    
    Args:
        s (str): String to color
    
    Returns:
        str: Colored string

    Examples:
        >>> from chepy.modules.internal.colors import cyan
        >>> print(CYAN("some string"))
    """
    return Fore.CYAN + s + Fore.RESET if sys.stdout.isatty() else s


def green(s: str) -> str:    # pragma: no cover
    """Green color string if tty
    
    Args:
        s (str): String to color
    
    Returns:
        str: Colored string

    Examples:
        >>> from chepy.modules.internal.colors import green
        >>> print(GREEN("some string"))
    """
    return Fore.GREEN + s + Fore.RESET if sys.stdout.isatty() else s


def yellow(s: str) -> str:    # pragma: no cover
    """Yellow color string if tty
    
    Args:
        s (str): String to color
    
    Returns:
        str: Colored string

    Examples:
        >>> from chepy.modules.internal.colors import yellow
        >>> print(YELLOW("some string"))
    """
    return Fore.YELLOW + s + Fore.RESET if sys.stdout.isatty() else s


def magenta(s: str) -> str:    # pragma: no cover
    """Magenta color string if tty
    
    Args:
        s (str): String to color
    
    Returns:
        str: Colored string

    Examples:
        >>> from chepy.modules.internal.colors import magenta
        >>> print(MAGENTA("some string"))
    """
    return Fore.MAGENTA + s + Fore.RESET if sys.stdout.isatty() else s
