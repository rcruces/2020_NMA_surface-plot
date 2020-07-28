"""
This function was copied from github.com/ansteeg, the original code can be found here:
     https://github.com/ansteeg/NeuroMatchProject
"""

import os

import pandas as pd

class HCPRegions:
    """
    Translates short region names into more information.
    Attributes:
        table_path(str): path to the hcp_parcels.csv file
        table(pd.DataFrame): the loaded table as a pandas dataframe
    From the paper (doi:10.1038/nature18933):
    "Table 1 lists the 180 areas of the cortical parcellation with index number, short name,
    description, whether or not the area is new or not, the sections the area is described in,
    synonyms or ‘quasi-synonyms’ for the area, and key studies used for the area’s
    identification. A “Yes” in the ‘New?’ column signifies an area that was not previously
    described in the neuroanatomical literature as far as we are aware. For some areas, “Yes*”
    signifies subdivisions of a previously described area, homologues, or similarity to a
    previously described area but not the same. “No” means that the area was previously
    described in a very similar form to what we found here. The bold section number is the
    primary section in which the area is described. Bold studies are those that had surfacemapped
    data available for us to make direct comparisons on the same atlas mesh."
    """

    table_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'atlas', 'hcp_parcels.csv')
    table = None

    def __init__(self):
        """ Inits the HCPRegions class and loads the table from file. """
        # Load table
        self.table = pd.read_csv(self.table_path, delimiter=',', encoding='utf-8')

    def get_entry(self, region_name_or_index: 'str/int'):
        """
        Retrieves the table entry for the given region.
        Args:
        region_name_or_index (str or int): the short region name, or its index
        Returns:
        (pandas entry): A pandas row containing information about this region
            columns: ParcelIndex,AreaName,AreaDescription,New,Sections,OtherNames,KeyStudies
        """

        if isinstance(region_name_or_index, str):
            regions = self.table.loc[self.table['AreaName'] == region_name_or_index]
        elif isinstance(region_name_or_index, int):
            # ParcelIndex starts at 1
            regions = self.table.loc[self.table['ParcelIndex'] == region_name_or_index + 1]
        else:
            raise ValueError(f'Region name or index must be str or int; received {type(region_name_or_index)}.')
        if regions.empty:
            raise ValueError(f'No region with name or index {region_name_or_index} found.')
        return regions.iloc[0]

    def wtf_is(self, region_name_or_index: 'str/int', verbose=False):
        """
        Prints information about the given region to the console.
        Args:
        region_name_or_index (str or int): the short region name, or its index
        verbose (bool, default=False): Returns more information if set to true
        """

        region = self.get_entry(region_name_or_index)
        if not verbose:
            print(f'Region {region["AreaName"]} ({region["ParcelIndex"]})\n' \
                f'Area description: {region["AreaDescription"]}\n' \
                f'Other names: {region["OtherNames"]}')
        else:
            print(f'Region {region["AreaName"]}\n' \
                f'ParcelIndex: {region["ParcelIndex"]}\n' \
                f'Area description: {region["AreaDescription"]}\n' \
                f'Other names: {region["OtherNames"]}\n' \
                f'New?: {region["New"]}\n' \
                f'Sections: {region["Sections"]}\n' \
                f'Key studies: {region["KeyStudies"]}')
