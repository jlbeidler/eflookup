"""eflookup.crops2ef.lookup:

Adapted from FEPS lookup script
Emissions factors from McCarty 2011
Methods from Pouliot 2017
"""

__author__      = "James Beidler"

__all__ = [
    'Crops2Ef',
]

# Crop codes listed below are from the CDL
# See https://www.nass.usda.gov/Research_and_Science/Cropland/metadata/metadata_Cultivated-Layer-2022.htm for reference to crop name
# EFs in lbs/ton
CROPSEF = {
'1': {'CO2': 3031.37, 'CH4': 4.253396665, 'CO': 106.1001507, 'NOX': 4.601521501, 'SO2': 2.380990744, 'PM2.5': 9.940884755, 'PM10': 21.360925, 'VOC': 18.47246, 'NH3': 19.32, 'hap_50000': 1.025634, 'hap_75070': 1.521677, 'hap_110543': 0.172563, 'hap_71432': 0.227658, 'hap_123386': 0.218663, 'hap_106990': 0.161739, 'hap_108883': 0.170455, 'hap_100425': 0.025581, 'hap_100414': 0.026645, 'hap_540841': 0.006738, 'hap_98828': 0.002136, 'hap_106423': 0.066206, 'PEC': 1.083556438, 'POC': 3.859051462}, 
'2': {'CO2': 3341.458258, 'CH4': 4.075935999, 'CO': 110.2846823, 'NOX': 4.749334055, 'SO2': 0.880120992, 'PM2.5': 8.068089333, 'PM10': 14.09666667, 'VOC': 18.68672, 'NH3': 33.73, 'hap_50000': 1.355905, 'hap_75070': 1.10033, 'hap_110543': 0.313249, 'hap_71432': 0.220424, 'hap_123386': 0.179053, 'hap_106990': 0.127599, 'hap_108883': 0.094804, 'hap_100425': 0.018471, 'hap_100414': 0.01489, 'hap_540841': 0.002262, 'hap_98828': 0.000942, 'hap_106423': 0.040523, 'PEC': 0.879421737, 'POC': 3.132032279}, 
'3': {'CO2': 3031.37, 'CH4': 6.304830611, 'CO': 127.7043834, 'NOX': 6.325035567, 'SO2': 3.131320992, 'PM2.5': 12.37676951, 'PM10': 17.73, 'VOC': 18.47246, 'NH3': 44.94, 'hap_50000': 1.025634, 'hap_75070': 1.521677, 'hap_110543': 0.172563, 'hap_71432': 0.227658, 'hap_123386': 0.218663, 'hap_106990': 0.161739, 'hap_108883': 0.170455, 'hap_100425': 0.025581, 'hap_100414': 0.026645, 'hap_540841': 0.006738, 'hap_98828': 0.002136, 'hap_106423': 0.066206, 'PEC': 1.349067877, 'POC': 4.804661924}, 
'4': {'CO2': 3031.37, 'CH4': 7.206225045, 'CO': 146.124354, 'NOX': 6.889022868, 'SO2': 3.131320992, 'PM2.5': 12.37676951, 'PM10': 17.73, 'VOC': 18.47246, 'NH3': 48.92, 'hap_50000': 1.025634, 'hap_75070': 1.521677, 'hap_110543': 0.172563, 'hap_71432': 0.227658, 'hap_123386': 0.218663, 'hap_106990': 0.161739, 'hap_108883': 0.170455, 'hap_100425': 0.025581, 'hap_100414': 0.026645, 'hap_540841': 0.006738, 'hap_98828': 0.002136, 'hap_106423': 0.066206, 'PEC': 1.349067877, 'POC': 4.804661924}, 
'6': {'CO2': 3031.37, 'CH4': 5.632874736, 'CO': 127.7919467, 'NOX': 5.596176066, 'SO2': 2.344437922, 'PM2.5': 12.31421121, 'PM10': 16.99917976, 'VOC': 18.47246, 'NH3': 16.24, 'hap_50000': 1.025634, 'hap_75070': 1.521677, 'hap_110543': 0.172563, 'hap_71432': 0.227658, 'hap_123386': 0.218663, 'hap_106990': 0.161739, 'hap_108883': 0.170455, 'hap_100425': 0.025581, 'hap_100414': 0.026645, 'hap_540841': 0.006738, 'hap_98828': 0.002136, 'hap_106423': 0.066206, 'PEC': 1.342249022, 'POC': 4.780376792}, 
'7': {'CO2': 3031.37, 'CH4': 3.781497278, 'CO': 105.2686528, 'NOX': 6.232028454, 'SO2': 2.765990744, 'PM2.5': 4.72, 'PM10': 6.61, 'VOC': 18.25821, 'NH3': 26.17, 'hap_50000': 0.695364, 'hap_75070': 1.943024, 'hap_110543': 0.031876, 'hap_71432': 0.234892, 'hap_123386': 0.258272, 'hap_106990': 0.195879, 'hap_108883': 0.246106, 'hap_100425': 0.032692, 'hap_100414': 0.038401, 'hap_540841': 0.011214, 'hap_98828': 0.00333, 'hap_106423': 0.09189, 'PEC': 0.51448, 'POC': 1.832304}, 
'8': {'CO2': 3031.37, 'CH4': 4.58, 'CO': 116.9534832, 'NOX': 6.061767151, 'SO2': 3.321320992, 'PM2.5': 2.38, 'PM10': 9.83, 'VOC': 14.7, 'NH3': 43.03, 'hap_50000': 0.8, 'hap_75070': 0.238933, 'hap_110543': 0.1, 'hap_71432': 0.58, 'hap_123386': 0.044267, 'hap_106990': 0.0, 'hap_108883': 0.6, 'hap_100425': 0.001867, 'hap_100414': 0.92, 'hap_540841': 0.16, 'hap_98828': 0.0, 'hap_106423': 0.00656, 'PEC': 0.947701918, 'POC': 3.375209949}, 
'9': {'CO2': 3031.37, 'CH4': 5.632874736, 'CO': 127.7919467, 'NOX': 5.596176066, 'SO2': 2.344437922, 'PM2.5': 12.31421121, 'PM10': 16.99917976, 'VOC': 18.47246, 'NH3': 39.76, 'hap_50000': 1.025634, 'hap_75070': 1.521677, 'hap_110543': 0.172563, 'hap_71432': 0.227658, 'hap_123386': 0.218663, 'hap_106990': 0.161739, 'hap_108883': 0.170455, 'hap_100425': 0.025581, 'hap_100414': 0.026645, 'hap_540841': 0.006738, 'hap_98828': 0.002136, 'hap_106423': 0.066206, 'PEC': 1.342249022, 'POC': 4.780376792}, 
'12': {'CO2': 3102.437387, 'CH4': 11.43408752, 'CO': 182.1079203, 'NOX': 4.314522868, 'SO2': 0.8, 'PM2.5': 23.22862976, 'PM10': 31.63666667, 'VOC': 18.47246, 'NH3': 12.52, 'hap_50000': 1.025634, 'hap_75070': 1.521677, 'hap_110543': 0.172563, 'hap_71432': 0.227658, 'hap_123386': 0.218663, 'hap_106990': 0.161739, 'hap_108883': 0.170455, 'hap_100425': 0.025581, 'hap_100414': 0.026645, 'hap_540841': 0.006738, 'hap_98828': 0.002136, 'hap_106423': 0.066206, 'PEC': 2.531920644, 'POC': 9.017354073}, 
'13': {'CO2': 3186.414129, 'CH4': 4.164666332, 'CO': 108.1924165, 'NOX': 4.675427778, 'SO2': 1.630555868, 'PM2.5': 9.004487044, 'PM10': 17.72879583, 'VOC': 18.57959, 'NH3': 26.53, 'hap_50000': 1.19077, 'hap_75070': 1.311003, 'hap_110543': 0.242906, 'hap_71432': 0.224041, 'hap_123386': 0.198858, 'hap_106990': 0.144669, 'hap_108883': 0.13263, 'hap_100425': 0.022026, 'hap_100414': 0.020768, 'hap_540841': 0.0045, 'hap_98828': 0.001539, 'hap_106423': 0.053364, 'PEC': 0.981489088, 'POC': 3.49554187}, 
'14': {'CO2': 3186.414129, 'CH4': 5.641080522, 'CO': 128.2045182, 'NOX': 5.819178461, 'SO2': 2.005720992, 'PM2.5': 10.22242942, 'PM10': 15.91333333, 'VOC': 18.57959, 'NH3': 41.33, 'hap_50000': 1.19077, 'hap_75070': 1.311003, 'hap_110543': 0.242906, 'hap_71432': 0.224041, 'hap_123386': 0.198858, 'hap_106990': 0.144669, 'hap_108883': 0.13263, 'hap_100425': 0.022026, 'hap_100414': 0.020768, 'hap_540841': 0.0045, 'hap_98828': 0.001539, 'hap_106423': 0.053364, 'PEC': 1.114244807, 'POC': 3.968347101}, 
'15': {'CO2': 3031.37, 'CH4': 6.755527828, 'CO': 136.9143687, 'NOX': 6.607029217, 'SO2': 3.131320992, 'PM2.5': 12.37676951, 'PM10': 17.73, 'VOC': 18.47246, 'NH3': 46.94, 'hap_50000': 1.025634, 'hap_75070': 1.521677, 'hap_110543': 0.172563, 'hap_71432': 0.227658, 'hap_123386': 0.218663, 'hap_106990': 0.161739, 'hap_108883': 0.170455, 'hap_100425': 0.025581, 'hap_100414': 0.026645, 'hap_540841': 0.006738, 'hap_98828': 0.002136, 'hap_106423': 0.066206, 'PEC': 1.349067877, 'POC': 4.804661924}, 
'16': {'CO2': 3031.37, 'CH4': 5.279113638, 'CO': 116.9022671, 'NOX': 5.463278534, 'SO2': 2.756155868, 'PM2.5': 11.15882713, 'PM10': 19.5454625, 'VOC': 18.47246, 'NH3': 22.94, 'hap_50000': 1.025634, 'hap_75070': 1.521677, 'hap_110543': 0.172563, 'hap_71432': 0.227658, 'hap_123386': 0.218663, 'hap_106990': 0.161739, 'hap_108883': 0.170455, 'hap_100425': 0.025581, 'hap_100414': 0.026645, 'hap_540841': 0.006738, 'hap_98828': 0.002136, 'hap_106423': 0.066206, 'PEC': 1.216312157, 'POC': 4.331856692}, 
'17': {'CO2': 3186.414129, 'CH4': 5.190383305, 'CO': 118.9945329, 'NOX': 5.537184811, 'SO2': 2.005720992, 'PM2.5': 10.22242942, 'PM10': 15.91333333, 'VOC': 18.57959, 'NH3': 39.33, 'hap_50000': 1.19077, 'hap_75070': 1.311003, 'hap_110543': 0.242906, 'hap_71432': 0.224041, 'hap_123386': 0.198858, 'hap_106990': 0.144669, 'hap_108883': 0.13263, 'hap_100425': 0.022026, 'hap_100414': 0.020768, 'hap_540841': 0.0045, 'hap_98828': 0.001539, 'hap_106423': 0.053364, 'PEC': 1.114244807, 'POC': 3.968347101}, 
'25': {'CO2': 3224.4, 'CH4': 5.0, 'CO': 128.48, 'NOX': 7.06, 'SO2': 2.52, 'PM2.5': 25.36, 'PM10': 26.38, 'VOC': 43.25, 'NH3': 1.82, 'hap_50000': 0.0, 'hap_75070': 0.0, 'hap_110543': 0.0, 'hap_71432': 0.0, 'hap_123386': 0.0, 'hap_106990': 0.0, 'hap_108883': 0.0, 'hap_100425': 0.0, 'hap_100414': 0.0, 'hap_540841': 0.0, 'hap_98828': 0.0, 'hap_106423': 0.0, 'PEC': 0.0, 'POC': 0.0}, 
'26': {'CO2': 3224.4, 'CH4': 5.0, 'CO': 128.48, 'NOX': 7.06, 'SO2': 2.52, 'PM2.5': 25.36, 'PM10': 26.38, 'VOC': 43.25, 'NH3': 1.82, 'hap_50000': 0.0, 'hap_75070': 0.0, 'hap_110543': 0.0, 'hap_71432': 0.0, 'hap_123386': 0.0, 'hap_106990': 0.0, 'hap_108883': 0.0, 'hap_100425': 0.0, 'hap_100414': 0.0, 'hap_540841': 0.0, 'hap_98828': 0.0, 'hap_106423': 0.0, 'PEC': 0.0, 'POC': 0.0}
}

class Crops2Ef:
    """Class for looking up emission factors for Crop fuelbed types
    """

    def __init__(self, crop_fuelbed_id):
        """Constructor - reads FCCS-based emissions factors into dictionary
        for quick access.

        Args:
         - crop_fuelbed_id - Integer ID of modified CDL crop type (9000+CDL ID)
        """
        self.crop_fuelbed_id = str(int(crop_fuelbed_id)-9000)

    def get(self, **kwargs):
        """Looks up and returns cover type specific emission factors

        Kwargs:
         - species -- chemical species; phase, fuel_category, and
            if fuel_sub_category must also be defined

        Notes:
         - returns None if any of the arguments are invalid.

        Examples:
        >>> lu = Crops2Ef(9002)
        >>> lu.get(species='CO2')
        """
        if any([not kwargs.get(e) for e in ('species',)]):
            raise LookupError("Specify species")

        species = kwargs.get('species')

        # Lookup the crop bed, select the "other crops" type if it isn't found 
        try:
            crop_ef = CROPSEF[self.crop_fuelbed_id]
        except KeyError:
            print('CDL ID not found. Defaulting to other crops EF.')
            crop_ef = CROPSEF['12']

        # Return in short tons/ton
        try:
            return crop_ef[species] / 2000.
        except KeyError:
            return None



