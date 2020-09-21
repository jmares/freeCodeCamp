def add_time(start, duration, day = None):

    start = start.strip()
    duration = duration.strip()
    if day: day = day.strip().lower().capitalize()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    start_dict = dict()
    start_dict["hours"] = int(start.split()[0].split(":")[0])
    start_dict["minutes"] = int(start.split()[0].split(":")[1])
    start_dict["12hour"] = start.split()[1] # AM or PM

    duration_minutes = int(duration.split(":")[0]) * 60 + int(duration.split(":")[1])
    total_minutes = duration_minutes + start_dict["hours"] * 60 + start_dict["minutes"]
    if start_dict["12hour"] == "PM":
        # add 12 hours or 720 minutes
        total_minutes +=  720

    end_dict = dict()
    end_dict["hours"] = total_minutes // 60
    end_dict["minutes"] = total_minutes % 60
    if end_dict["hours"] > 24:
        end_dict["days"] = end_dict["hours"] // 24
        end_dict["hours"] = end_dict["hours"] % 24
    if end_dict["hours"] >= 12:
        end_dict["12hour"] = "PM"
        end_dict["hours"] -= 12
    else:
        end_dict["12hour"] = "AM"
    if end_dict["hours"] == 0: end_dict["hours"] += 12

    if day:
        index = (days.index(day) + end_dict.get("days", 0)) % 7
        end_dict["day"] = days[index]

    new_time = str(end_dict["hours"]) + ":"
    if end_dict["minutes"] < 10: new_time += "0"
    new_time += str(end_dict["minutes"]) + " " + end_dict["12hour"]
    if day: new_time += ", " + end_dict["day"]
    if end_dict.get("days", 0) == 1: new_time += " (next day)"
    if end_dict.get("days", 0) > 1: new_time += " (" + str(end_dict["days"]) + " days later)"
    
    return new_time
