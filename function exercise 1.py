def movie_ticket_price(age, day_of_week, other_parameters):
  BASE_PRICE = 13 
  CHILD_DISCOUNT = 0.5 
  SENIOR_DISCOUNT = 0.75 
  WEEKEND_SURCHARGE = 1.35 
  TUESDAY_DISCOUNT = 0.25 
  if age <= 12:
    total_price = BASE_PRICE * CHILD_DISCOUNT
    if day_of_week == "Weekend":
      total_price += WEEKEND_SURCHARGE * CHILD_DISCOUNT
    elif day_of_week == "Tuesday":
      total_price += TUESDAY_DISCOUNT * CHILD_DISCOUNT
    else:
      total_price += TUESDAY_DISCOUNT * SENIOR_DISCOUNT
    return round(total_price, 2)
  elif age <= 65:
    total_price = BASE_PRICE * SENIOR_DISCOUNT
    if day_of_week == "Weekend":
      total_price += WEEKEND_SURCHARGE * SENIOR_DISCOUNT
    elif day_of_week == "Tuesday":
      total_price += TUESDAY_DISCOUNT * SENIOR_DISCOUNT
    else:
      total_price += TUESDAY_DISCOUNT * CHILD_DISCOUNT
    return round(total_price, 2) 
  else:
    return "Invalid age" 
print(movie_ticket_price(10, "Friday", ["3D", "2D"])) 
print(movie_ticket_price(20, "Monday", ["3D", "2D"])) 
print(movie_ticket_price(18, "Wednesday", ["3D"])) 
print(movie_ticket_price(15, "Saturday", ["3D"])) 