import numpy as np
import pandas as pd

# airlines
airlines_df = pd.read_csv(
    "data/airlines.dat",
    sep="\t",
    engine="python",
    encoding="ISO-8859-1",
)

airlines_df.rename({"# airline-id": "airline_id"}, axis=1, inplace=True)

# routes
routes_df = pd.read_csv(
    "data/routes.dat",
    sep="\t",
    engine="python",
    encoding="ISO-8859-1",
)

routes_df.rename({"# airline": "airline_id"}, axis=1, inplace=True)
routes_df.drop([0], axis=0, inplace=True)
routes_df.at[1, "airline"] = "C7"

# concat airlines and routes dfs
flight_routes = pd.merge(airlines_df, routes_df, on="airline_id")
print(flight_routes)
