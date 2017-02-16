from admin_division import AdminDivision
from county import County
from community import Community
from ui import UI

class Statistic():

    @staticmethod
    def total():
        result = []
        divisions = {
                     'wojewódźtwo': 0,
                     'powiat': 0,
                     'gmina wiejska': 0,
                     'gmina miejska': 0,
                     'gmina miejsko-wiejska': 0,
                     'obszar wiejski': 0,
                     'miasto': 0,
                     'miasto na prawach powiatu': 0,
                     'delegatura': 0
                     }
        for item in AdminDivision.objects:
            divisions[item.typ] += 1
            if item.typ == 'miasto na prawach powiatu':
                divisions['powiat'] += 1
        for key, value in divisions.items():
            if key == 'powiat':
                key = 'powiaty'
            result.append([value, key])

        return sorted(result, key=lambda x: x[1], reverse=True)

    @staticmethod
    def three_longest_city():
        all_cities = []
        for powiat in County.objects:
            if powiat.typ == 'miasto na prawach powiatu':
                all_cities.append(powiat.name)

        for gmina in Community.objects:
            if gmina.typ == 'miasto':
                all_cities.append(gmina.name)

        return sorted(all_cities, key= lambda x: len(x), reverse=True)[:3]

    @staticmethod
    def largest_number_of_commun():
        counties = {}
        for community in Community.objects:
            if community.pow_id not in counties.keys():
                counties[community.pow_id] = 0
            counties[community.pow_id] += 1

        largest_county_id =  max(counties, key=lambda k: counties[k])
        for county in County.objects:
            if county.id == largest_county_id:
                return 'Powiat {}'.format(county.name)

    @staticmethod
    def more_than_one_category():
        locations_dict = {}
        result = []
        for location in AdminDivision.objects:
            if location.name not in locations_dict.keys():
                locations_dict[location.name] = 0
            locations_dict[location.name] += 1

        for key, value in locations_dict.items():
            if value > 1:
                result.append(key)

        return '\n'.join(sorted(result))

    @staticmethod
    def advanced_search(search):
        result = []
        for item in AdminDivision.objects:
            if search.lower() in item.name.lower():
                result.append([item.name, item.typ])

        return sorted(result)

