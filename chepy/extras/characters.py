from string import ascii_lowercase, ascii_uppercase, digits


def base64_char_sets() -> dict:
    """Get various combinations of base64 character sets
    
    Returns:
        dict: Dict of various char sets
    """
    return {
        "standard": ascii_uppercase + ascii_lowercase + digits + "+/=",
        "url_safe": ascii_uppercase + ascii_lowercase + digits + "-_",
        "filename_safe": ascii_uppercase + ascii_lowercase + digits + "+\\-=",
        "itoa64": "./" + digits + ascii_uppercase + ascii_lowercase + "=",
        "xml": ascii_uppercase + ascii_lowercase + digits + "_.",
        "y64": ascii_uppercase + ascii_lowercase + digits + "._-",
        "z64": digits + ascii_lowercase + ascii_uppercase + "+/=",
        "radix64": digits + ascii_uppercase + ascii_lowercase + "+/=",
        "uuencoding": " -_",
        "xxencoding": "+\\-" + digits + ascii_uppercase + ascii_lowercase,
        "unix_crypt": f"./{digits}{ascii_uppercase}{ascii_lowercase}",
    }
