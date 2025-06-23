import datetime





def verify(data):
    try:
        data = str(data)
        year_months_days = data.split("-")
        print(year_months_days)
        date = datetime.datetime(int(year_months_days[0]), int(year_months_days[1].replace("0", "")), int(year_months_days[2]))
        return True
    except Exception as e:
        print(e)
        return False



