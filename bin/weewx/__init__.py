#
#    Copyright (c) 2009, 2010, 2011 Tom Keffer <tkeffer@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#
#    $Revision$
#    $Author$
#    $Date$
#
"""Package weewx. A set of modules for supporting a weather station on a sqlite database.

"""
import time

__version__="2.0.0a3"

# Holds the program launch time in unix epoch seconds:
# Useful for calculating 'uptime.'
launchtime_ts = time.time()

# Set to true for extra debug information:
debug = False

# Exit return codes
CMD_ERROR    = 2
CONFIG_ERROR = 3
IO_ERROR     = 4

# Constants used to indicate a unit system:
METRIC = 0x10
US     = 0x01

#===============================================================================
#           Define possible exceptions that could get thrown.
#===============================================================================

class WeeWxIOError(IOError):
    """Base class of exceptions thrown when encountering an I/O error with the console."""

class WakeupError(WeeWxIOError):
    """Exception thrown when unable to wake up the console"""
    
class CRCError(WeeWxIOError):
    """Exception thrown when unable to pass a CRC check."""

class RetriesExceeded(WeeWxIOError):
    """Exception thrown when max retries exceeded."""

class UnknownArchiveType(StandardError):
    """Exception thrown after reading an unrecognized archive type."""

class UnsupportedFeature(StandardError):
    """Exception thrown when attempting to access a feature that is not supported (yet)."""
    
class ViolatedPrecondition(StandardError):
    """Exception thrown when a function is called with violated preconditions."""
    
#===============================================================================
#                       Possible event types.
#===============================================================================

class STARTUP(object):
    """Event issued when the engine first starts up. Services have not been loaded."""
class PRE_LOOP(object):
    """Event issued just before the main packet loop is started. Services have been loaded."""
class NEW_LOOP_PACKET(object):
    """Event issued when a new LOOP packet is available. The event contains attribute 'packet',
    which is the new LOOP packet."""
class CHECK_LOOP(object):
    """Event issued in the main loop, right after a new LOOP packet has been processed. Generally,
    it is used to throw an exception, breaking the main loop, so the console can be used
    for other things."""
class NEW_ARCHIVE_RECORD(object):
    """Event issued when a new archive record is available. The event contains attribute 'record',
    which is the new archive record."""
class POST_LOOP(object):
    """Event issued right after the main loop has been broken. Services hook into this to
    access the console for things other than generating LOOP packet."""

#===============================================================================
#                       Class Event
#===============================================================================
class Event(object):
    """Represents an event."""
    def __init__(self, event_type, **argv):
        self.event_type = event_type

        for key in argv:
            setattr(self, key, argv[key])

    def __str__(self):
        """Return a string with a reasonable representation of the event."""
        et = "Event type: %s | " % self.event_type
        s = "; ".join("%s: %s" %(k, self.__dict__[k]) for k in self.__dict__ if k!="event_type")
        return et + s


