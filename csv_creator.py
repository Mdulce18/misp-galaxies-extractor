# This file has to take the list of community identifiers and pass them to a csv
from actor import Actor


extractor = Actor(6)
raw_list = extractor.parse_community_identifiers_json()
# raw_list = ['comment_panda','commentpanda' , 'apt_1', 'apt1', 'advanced_persistent_threat_1','group_3', 'group3','fin6']
extractor.format_data(raw_list)
na=extractor.get_community_identifiers()


# APT28 = Actor()
breakpoint()
