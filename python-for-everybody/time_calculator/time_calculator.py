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
        end_dict["12hours"] = "PM"
        end_dict["hours"] -= 12
    else:
        end_dict["12hours"] = "AM"
    if end_dict["hours"] == 0: end_dict["hours"] += 12

    if day:
        index = (days.index(day) + end_dict.get("days", 0)) % 6
        end_dict["day"] = days[index]


    print(end_dict)

    new_time = False



    return new_time

add_time("3:00 PM", "3:10")
add_time("11:30 AM", "2:32", "Monday")
add_time("11:43 AM", "0:20")
add_time("10:10 PM", "3:30")
add_time("11:43 PM", "24:20", "tueSday")
add_time("6:30 PM", "205:12")
