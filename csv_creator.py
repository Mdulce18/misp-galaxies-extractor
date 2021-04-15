# This file has to take the list of community identifiers and pass them to a csv
from misp_galaxy_parser import community_extractor

extractor = community_extractor()
json = extractor.parse_community_identifiers_json()
extractor.create_list(json)
extractor.get_community_identifiers()
breakpoint()


