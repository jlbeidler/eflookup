"""eflookup.lookup: defines constants used throughout eflookup package, along
with a basic EF look-up class

TODO: Make these immutable
"""

__author__      = "Joel Dubowy"
__copyright__   = "Copyright 2015, AirFire, PNW, USFS"

class Phase:
    FLAMING = 'flaming'
    SMOLDERING = 'smoldering'
    RESIDUAL = 'residual'

class FuelCategory:
    WOODY = 'woody'
    DUFF = 'duff'

class BasicEFLookup(dict):
    """Look-up object for arbitrary, phase specific emission factors
    """

    def get(self, **keys):
        """Looks up and returns emission factors

        Lookup Keys:
         - phase -- emissions factor set identifier ('flaming', 'smoldering',
            'residual')
         - species -- chemical species; phase (and fuel_category if phase is
            'residual') must also be defined

        Notes:
         - ignores any other keys
         - returns None if any of the arguments are invalid.

        Examples:
        >>> lu = BasicLookUp({'flaming':{'CO':34}, 'smoldering': {'CO':3}, 'residual': {'CO':34.9}})
        >>> lu.get()
        >>> lu.get(phase='flaming')
        >>> lu.get(phase='flaming', species='CO')
        >>> lu.get()
        >>> lu.get(phase='flaming')
        >>> lu.get(phase='flaming', species='CO')
        """
        phase = keys.get('phase')
        species = keys.get('species')

        if not phase and species:
            raise LookupError("Specify phase when also specifying species")

        try:
            if phase:
                if species:
                    return self[phase][species]
                return self[phase]
            return self

        except KeyError:
            return None

    def species(self, phase):
        return set(self[phase].keys())
