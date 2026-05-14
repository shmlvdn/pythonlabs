def calculate_time(distance_km, avg_speed_kmh):
    if avg_speed_kmh <= 0:
        return 0
    hours = distance_km / avg_speed_kmh
    return hours