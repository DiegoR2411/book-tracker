from enum import Enum


class ReadingStatus(str, Enum):
    WANT_TO_READ = "Want to Read"
    READING = "Reading"
    RE_READING = "Re-reading"
    ON_HOLD = "On Hold"
    READ = "Read"
    DROPPED = "Dropped"