class Comparable:
    """Wrapper class for items that are not comparable."""

    def __init__(self, data, _priority=1):
        self.data = data
        self._priority = _priority

    def __str__(self):
        """Returns the string rep of the contained datum."""
        return str(self.data)

    def __eq__(self, other):
        """Returns True if the contained priorities are equal
        or False otherwise."""
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self._priority == other._priority

    def __lt__(self, other):
        """Returns True if self’s _priority < other’s _priority,
        or False otherwise."""
        return self._priority < other._priority

    def __le__(self, other):
        """Returns True if self’s _priority <= other’s _priority,
        or False otherwise."""
        return self._priority <= other._priority

    def get_priority(self):
        """Returns the contained _priority."""
        return self._priority
