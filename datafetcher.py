import requests
from bs4 import BeautifulSoup


def fetch(n, type_data, user, time_interval, scrobble_option):

    # n is an indicator for datagui.py, it will be used to divide the data into two parts.
    # type_data is one of [albums, tracks, artists].
    # user is the username.
    # time_interval is, as the name suggests, determines the time interval.
    # scrobble_option is the indicator that carries the information about the option "include scrobbles".

    _dict_ = {"last week": "7", "last month": "30", "last 3 months": "90", "last 6 months": "180", "last year": "365",
              "all time": "all"}

    time_interval = _dict_[time_interval]

    if time_interval[0] == "a":
        time = "date_preset=ALL"

    else:
        time = "date_preset=LAST_{}_DAYS".format(time_interval)

    link = "https://www.last.fm/user/{}/library/{}?{}".format(user, type_data, time)
    output = ""

    last = requests.get(link)
    stat = BeautifulSoup(last.content, "lxml")

    data = stat.find_all("td", attrs={"class", "chartlist-name"})
    scrobbles = stat.find_all("span", attrs={"class", "chartlist-count-bar-value"})
    length = len(scrobbles) + (len(scrobbles) % 2 == 1)
    scrobbles_data = []

    if scrobble_option:
        for scrobble in scrobbles:
            if len(scrobbles_data) < 9:
                scrobbles_data.append(str(scrobble.get_text()).replace("\n", "")[52:])

            else:
                scrobbles_data.append(str(scrobble.get_text()).replace("\n", "")[51:])

    else:
        scrobbles_data = ["" for i in range(50)]

    rank = 1

    if len(data) == 0:
        if n == 1:
            return "!!!"

        else:
            return f"{user} didn't scrobble during the selected date range, or isn't a valid username."

    for i in data:
        _data_ = i.find_all("a")

        for b in _data_:
            title = b.get("title")
            if n == 1 and rank <= length / 2:
                output = output + str(rank) + " - " + title + scrobble_option * "\n" + scrobbles_data[rank - 1] + "\n"
            elif n == 2 and length >= rank > length / 2:
                output = output + str(rank) + " - " + title + scrobble_option * "\n" + scrobbles_data[rank - 1] + "\n"
            rank += 1

    return output
