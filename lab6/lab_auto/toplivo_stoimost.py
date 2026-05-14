def calculate_fuel(car, distance_km, load_kg, fuel_price_per_liter):
    load_factor = 1 + (load_kg / car.max_load) * 0.5
    consumption = car.fuel_per_km_empty * load_factor * distance_km
    cost = consumption * fuel_price_per_liter
    return consumption, cost