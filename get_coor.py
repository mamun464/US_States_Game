import pandas as pd

import camelcase

camel = camelcase.CamelCase()




class Get_coor:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.visitedCity=[]
        AllData = pd.read_csv("50_states.csv")
        self.all_city_list=AllData.state.to_list()


    def have_available(self,userChoise):
        userChoise_modify = camel.hump(userChoise.strip())
        AllData = pd.read_csv("50_states.csv")
        cityList=AllData.state.to_list()

        if userChoise_modify in self.visitedCity:
            return False
        else:
            if userChoise_modify in cityList:
                return True
            else:
                return False

    def get_location(self, userChoise):
        """Pass the city name and get Coordinate"""
        userChoise_modify = camel.hump(userChoise.strip())
        AllData = pd.read_csv("50_states.csv")
        singleData = AllData[AllData.state == userChoise_modify]
        self.x = int(singleData.x)
        self.y = int(singleData.y)
        self.visitedCity.append(userChoise_modify)
        self.unvisited_city(userChoise_modify)

        return (self.x, self.y)
    def unvisited_city(self,userChoise_modify):
        self.all_city_list.remove(userChoise_modify)







