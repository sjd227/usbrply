"""
Aggregates parser engines together
"""

from . import lin_pcap
from . import win_pcap
from . import pcap_util

import json
import sys


def pcap2json(fn, argsj={}):
    """
    argsj: argument dict
    """

    # TODO: add Windows engine back in

    parser = argsj.get("parser", "auto")
    if parser == "auto":
        parser = pcap_util.guess_parser(fn)
        # print("Guess parser: %s" % parser)

    cls = {
        "lin-pcap": lin_pcap.Gen,
        "win-pcap": win_pcap.Gen,
    }[parser]
    gen = cls(fn, argsj)

    # k,v generator
    return gen.run()
