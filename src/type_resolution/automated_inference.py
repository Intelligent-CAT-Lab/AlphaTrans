import json
import os
import re
import argparse


def main(args):
    
    universal_type_map = {}
    with open(f'data/type_resolution/universal_type_map.json', 'r') as f:
        universal_type_map = json.load(f)

    def has_pattern_0(s): # "List<String>"
        return bool(re.match(r"^[^<>]*<[^<>]*>[^<>]*$", s))
    
    def has_pattern_1(s): # TypeA.TypeB
        total_dots = s.count('.')
        if total_dots == 1 and '<' not in s and '>' not in s:
            return True
        return False

    def has_pattern_2(s): # "Map<String, String>"
        return bool(re.match(r".*<.*,.*>", s)) and s.count(',') == 1 and '.' not in s

    def has_pattern_3(s): # "Map<String, String, String>"
        return bool(re.match(r".*<.*,.*,.*>", s)) and s.count(',') == 2 and '.' not in s

    for type_ in universal_type_map.copy():
        if not universal_type_map[type_] == "":
            continue

        if type_.endswith("<>"):
            if type_[:-2] in universal_type_map:
                universal_type_map[type_] = universal_type_map[type_[:-2]]
        
        if type_ in ['M', 'B', 'I', 'H', 'WO', 'W', 'G', 'O', 'N', 'TG']:
            universal_type_map[type_] = "Any"
            continue

        if has_pattern_3(type_):

            outer_type = type_[:type_.find('<')].strip()
            generic_types = type_[type_.find('<')+1:type_.rfind('>')].split(',')

            assert len(generic_types) == 3

            inner_type_1 = generic_types[0].strip()
            inner_type_2 = generic_types[1].strip()
            inner_type_3 = generic_types[2].strip()

            inferred_type = "UNKNOWN"

            if outer_type in universal_type_map and inner_type_1 in universal_type_map and inner_type_2 in universal_type_map and inner_type_3 in universal_type_map:
                if universal_type_map[outer_type] == "" or universal_type_map[inner_type_1] == "" or universal_type_map[inner_type_2] == "" or universal_type_map[inner_type_3] == "":
                    continue
                inferred_type = f"{universal_type_map[outer_type]}[{universal_type_map[inner_type_1]}, {universal_type_map[inner_type_2]}, {universal_type_map[inner_type_3]}]"
            
            if inferred_type == "UNKNOWN":
                continue

            universal_type_map[type_] = inferred_type

            continue

        elif has_pattern_2(type_):

            outer_type = type_[:type_.find('<')].strip()
            inner_type_1 = type_[type_.find('<')+1:type_.find(',')]
            inner_type_2 = type_[type_.find(',')+1:type_.rfind('>', type_.find(',')+1)]

            assert outer_type != "" and inner_type_1 != "" and inner_type_2 != ""

            inferred_type = "UNKNOWN"

            if outer_type in universal_type_map and inner_type_1 in universal_type_map and inner_type_2 in universal_type_map:
                if universal_type_map[outer_type] == "" or universal_type_map[inner_type_1] == "" or universal_type_map[inner_type_2] == "":
                    continue
                inferred_type = f"{universal_type_map[outer_type]}[{universal_type_map[inner_type_1]}, {universal_type_map[inner_type_2]}]"
        
            if inferred_type == "UNKNOWN":
                continue

            universal_type_map[type_] = inferred_type
            continue

        elif has_pattern_0(type_):
            outer_type = type_.split('<')[0].strip()
            inner_type = type_.split('<')[1].split('>')[0].strip()

            inferred_type = "UNKNOWN"

            if outer_type in universal_type_map and inner_type in universal_type_map:
                if universal_type_map[outer_type] == "" or universal_type_map[inner_type] == "":
                    continue
                inferred_type = f"{universal_type_map[outer_type]}[{universal_type_map[inner_type]}]"
            
            if inferred_type == "UNKNOWN":
                continue

            universal_type_map[type_] = inferred_type
            continue

        elif has_pattern_1(type_):
            outer_type = type_.split('.')[0].strip()
            inner_type = type_.split('.')[1].strip()

            if outer_type in universal_type_map and inner_type in universal_type_map:
                if universal_type_map[outer_type] == "" or universal_type_map[inner_type] == "":
                    continue
                del universal_type_map[type_]
            
            continue
    
    total_resolved = 0
    for k, v in universal_type_map.items():
        if v != '':
            total_resolved += 1

    print(f'Total resolved: {total_resolved}')
    print(f'Total unresolved: {len(universal_type_map) - total_resolved}')
    print(round((total_resolved / len(universal_type_map)) * 100, 2))

    with open(f'data/type_resolution/universal_type_map.json', 'w') as f:
        json.dump(universal_type_map, f, indent=4)


if __name__ == '__main__':
    parser_ = argparse.ArgumentParser(description='Translate java types to python types')
    args = parser_.parse_args()
    main(args)
