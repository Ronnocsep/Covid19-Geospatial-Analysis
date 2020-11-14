import pandas as pd
import numpy as np
import geopandas as gpd


def make_df_across_all_cantons_and_dates(start_date, end_date, canton_list):
    
    #Make a master df with every date and every canton AGAIN
    #Use full range of covid data for dates
    dates = pd.date_range(start_date, end_date, freq='d')
    cantons = canton_list

    list_of_dates = []
    list_of_cantons = []

    for canton in cantons:
        for date in dates:
            list_of_cantons.append(canton)
            list_of_dates.append(date.date())

    covid_df_per_day = pd.DataFrame({"Date": list_of_dates, "Canton": list_of_cantons})
    covid_df_per_day["Cases on that day"] = np.nan * len(covid_df_per_day)

    return covid_df_per_day



'''
TEST

start = pd.to_datetime("10/11/20", dayfirst=True).date()
end = pd.to_datetime("14/11/20", dayfirst=True).date()

print(start)
print(end)

canton_df = gpd.read_file("/Users/connorhughes/Documents/GitHub/Covid19-Geospatial-Analysis/CHE_adm/CHE_adm1.shp")
canton_df.drop(["ID_0","ISO","NAME_0","ID_1","TYPE_1","ENGTYPE_1","NL_NAME_1","VARNAME_1"], axis=1, inplace=True)

canton_list = canton_df["NAME_1"].tolist()
#print(canton_list)

make_df_with_all_cantons_and_dates(start, end, canton_list)
'''


