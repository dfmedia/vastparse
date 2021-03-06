def accept_none(parse_func):
    def parse(xml_dict):
        if xml_dict is None:
            return None
        return parse_func(xml_dict)

    return parse


def unicode_to_dict(parse_func):
    def parse(xml_dict):
        try:
            from __builtin__ import basestring
        except ModuleNotFoundError:
            basestring = str
        if isinstance(xml_dict, basestring):
            xml_dict = {"#text": xml_dict}
        return parse_func(xml_dict)

    return parse


def accept_falsy(parse_func):
    def parse(xml_dict):
        if not xml_dict:
            return None
        return parse_func(xml_dict)

    return parse


@accept_none
def parse_duration(duration_str):
    """

    :param duration_str: format of HH:MM:SS 
    :return: duration in seconds int
    """
    h, m, s = list(map(int, duration_str.split(":")))
    return h * 3600 + m * m * 60 + s


def unparse_duration(duration_int):
    """

    :param duration_int: in seconds
    :return: in format HH:MM:SS
    """
    d = duration_int
    h, m, s = d / 3600, (d % 3600) / 60, (d % 3600) % 60
    return "%02d:%02d:%02d" % (h, m, s)

