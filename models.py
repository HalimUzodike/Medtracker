"""Model for Medication Tracker."""
"""NOT IN USE CURRENTLY"""


class Medication():
    """Medication model."""

    def __init__(self, name, notes, frequency):
        self._name = name
        self._notes = notes
        self._frequency = frequency

    def get_name(self):
        '''returns name for a medication object'''
        return self._name

    def get_notes(self):
        """returns notes for a medication object"""
        return self._notes

    def get_frequency(self):
        """returns frequency for a medication object"""
        return self._frequency

