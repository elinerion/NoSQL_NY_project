import pandas as pd

#Firehouse
firehouse = pd.read_csv("FDNY_Firehouse_Listing.csv")
firehouse.set_value(62, 'FacilityName', "Engine 46/ Ladder 27")
firehouse.index.name = 'id'
firehouse.reset_index(inplace=True)
firehouse = firehouse[firehouse.FacilityName != 'FacilityName']


#Borough
d = {'Borough' : firehouse.Borough.unique()}
borough = pd.DataFrame(d)
borough.index.name = 'id'
borough.reset_index(inplace=True)
borough.to_csv('borough.csv', sep=',', index=False)

#Maths_Test
mathsTest = pd.read_csv("Math_Test_Results_2006-2012_-_Borough_-_Gender.csv")
mathsTest = mathsTest [["Borough","Grade","Year","Demographic", "Number Tested","Mean Scale Score"]]
mathsTest.index.name = 'id'
mathsTest.reset_index(inplace=True)

#Restaurant
restaurant = pd.read_csv("DOHMH_New_York_City_Restaurant_Inspection_Results.csv")
restaurant = restaurant [["DBA","BORO","BUILDING","STREET","CUISINE DESCRIPTION","INSPECTION DATE","SCORE","GRADE"]]
restaurant.index.name = 'id'
restaurant.reset_index(inplace=True)

#Population
population = pd.read_csv("New_York_City_Population_By_Neighborhood_Tabulation_Areas.csv")
population.index.name = 'id'
population.reset_index(inplace=True)


#Firehouse indices table relation 
firehouse.loc[firehouse.Borough == 'Manhattan', 'Borough'] = 0
firehouse.loc[firehouse.Borough == 'Bronx', 'Borough'] = 1
firehouse.loc[firehouse.Borough == 'Brooklyn', 'Borough'] = 2
firehouse.loc[firehouse.Borough == 'Queens', 'Borough'] = 3
firehouse.loc[firehouse.Borough == 'Staten Island', 'Borough'] = 4
dfIn = {'boroughId' : firehouse.Borough, 'firehouseId' : firehouse.id}
firehouseIsIn = pd.DataFrame(dfIn)
firehouseIsIn.to_csv('firehouse_is_in.csv', sep=',', index=False)
firehouse.drop('Borough', axis=1, inplace=True) 
firehouse.to_csv('firehouse.csv', sep=',', index=False)

#Maths_Test indices table relation 
mathsTest.loc[mathsTest.Borough == 'MANHATTAN', 'Borough'] = 0
mathsTest.loc[mathsTest.Borough == 'BRONX', 'Borough'] = 1
mathsTest.loc[mathsTest.Borough == 'BROOKLYN', 'Borough'] = 2
mathsTest.loc[mathsTest.Borough == 'QUEENS', 'Borough'] = 3
mathsTest.loc[mathsTest.Borough == 'STATEN ISLAND', 'Borough'] = 4
dMIn = {'boroughId' : mathsTest.Borough, 'mathsTestId' : mathsTest.id}
mathsTestIsIn = pd.DataFrame(dMIn)
mathsTestIsIn.to_csv('mathsTest_is_in.csv', sep=',', index=False)
mathsTest.drop('Borough', axis=1, inplace=True) 
mathsTest.to_csv('mathsResult.csv', sep=',', index=False)

#Restaurant indices table relation 
#restaurant.loc[restaurant.BORO == 'MANHATTAN', 'BORO'] = 0
#restaurant.loc[restaurant.BORO == 'BRONX', 'BORO'] = 1
#restaurant.loc[restaurant.BORO == 'BROOKLYN', 'BORO'] = 2
#restaurant.loc[restaurant.BORO == 'QUEENS', 'BORO'] = 3
#restaurant.loc[restaurant.BORO == 'STATEN ISLAND', 'BORO'] = 4
#restaurant = restaurant[restaurant.BORO != 'MISSING']
#drIn = {'boroughId' : restaurant.BORO, 'restaurantId' : restaurant.id}
#restaurantIsIn = pd.DataFrame(drIn)
#restaurantIsIn.to_csv('restaurant_is_in.csv', sep=',', index=False)
#restaurant.drop('BORO', axis=1, inplace=True) 
restaurant.to_csv('restaurant.csv', sep=',', index=False)

#Population indices table relation 
population.loc[population.Borough == 'Manhattan', 'Borough'] = 0
population.loc[population.Borough == 'Bronx', 'Borough'] = 1
population.loc[population.Borough == 'Brooklyn', 'Borough'] = 2
population.loc[population.Borough == 'Queens', 'Borough'] = 3
population.loc[population.Borough == 'Staten Island', 'Borough'] = 4
dpIn = {'boroughId' : population.Borough, 'populationId' : population.id}
populationIsIn = pd.DataFrame(dpIn)
populationIsIn.to_csv('population_is_in.csv', sep=',', index=False)
population.drop('Borough', axis=1, inplace=True) 
population.to_csv('population.csv', sep=',', index=False)
