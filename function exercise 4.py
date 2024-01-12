# Import the pandas library for data analysis
import pandas as pd
def travel_cost(destination, style, duration):
  data = pd.read_csv("travel_cost_data.csv")
  data = data[data["destination"] == destination]
  if len(data) == 0:
    return "Invalid destination"
  if style == "budget":
    total_cost = (data["budget_transport"] + data["budget_accommodation"] + data["budget_activities"]) * duration
  elif style == "luxury":
    total_cost = (data["luxury_transport"] + data["luxury_accommodation"] + data["luxury_activities"]) * duration
  else:
    return "Invalid travel style"
  return round(total_cost.item(), 2)
print(travel_cost("Paris", "budget", 5)) 
print(travel_cost("New York", "luxury", 3)) 
print(travel_cost("Tokyo", "budget", 7)) 
print(travel_cost("London", "luxury", 4)) 
print(travel_cost("Berlin", "mid-range", 6)) 
print(travel_cost("Sydney", "budget", 5)) 
