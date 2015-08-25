#!/usr/bin/env python3
"""
Estimates time of DMC frames using GPS & fire data, when they exist.
work in progress

We use UT1 Unix epoch time instead of datetime, since we are working with HDF5 and also need to do fast comparisons

Outputs:
--------
    UT1_unix:   double-precision float (64-bit) estimate of frame exposure START

Michael Hirsch
"""
from __future__ import division #always important, and critically important for this function!
from six import string_types
from datetime import datetime
from dateutil.parser import parse
from warnings import warn
#
tepoch = datetime(1970,1,1,0,0,0)

def fallback(tstart,fps,rawind):
    """ if you don't have GPS & fire data, you use this function for a software-only
    estimate of time. This estimate may be off by more than a minute, so think of it
    as a relative indication only. You can try verifying your absolute time with satellite
    passes in the FOV using a plate-scaled calibration and ephemeris data.
    Contact Michael Hirsch, he does have Github code for this.
    """

    if isinstance(tstart,string_types):
        tstart = parse(tstart)
    elif isinstance(tstart,(list,tuple)):
        tstart = tstart[0]
        warn('using first value {} as tstart.'.format(tstart))
        return fallback(tstart,fps,rawind)
    elif isinstance(tstart,datetime):
        pass
    else:
        warn('I do not know how to handle your tstart of type {}'.format(type(tstart)))
        return None

    #total_seconds is required for Python 2 compatibility
    # this variable is in units of seconds since Jan 1, 1970, midnight
    return (tstart-tepoch).total_seconds() + (rawind-1)/fps


def firetime(tstart,Tfire):
    """ Highly accurate sub-millisecond absolute timing based on GPSDO 1PPS and camera fire feedback.
    Right now we have some piecemeal methods to do this, and it's time to make it industrial strength
    code.

    """
    raise NotImplementedError("Yes this is a high priority, would you like to volunteer?")