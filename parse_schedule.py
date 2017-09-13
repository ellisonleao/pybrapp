
import bs4
import glob
import re
import urllib
import json

dates = {
    'day1.html': '2017-10-06',
    'day2.html': '2017-10-07',
    'day3.html': '2017-10-08',
}

TRACKS = {
    "Minas Foyer": "M. Foyer",
    "Sala Chrystal": "Chrystal",
    "Sala Aventurine e Alexandrite": "Aventurine",
    "Sala Amethyst": "Amethyst",
}


def parse_track_names(lecture):
    tracks = []
    for hour in lecture.find_all('p', attrs={'class': 'hour'}):
        p_tag = hour.find_next('p')
        t_names = []
        while True:
            track = p_tag.findChildren()
            if track:
                names = [t.getText() for t in track]
                t_names.extend([name for name in names if name not in ('Keynote', 'Lightning Talk')])
            p_tag = p_tag.find_next('p')
            if p_tag is None:
                break

            if p_tag.attrs.get('class', ['no_class'])[0] == 'hour':
                break
        tracks.append(t_names)

    return list(set(','.join([','.join(track) for track in tracks if track]).split(',')))


def parse_slots(lecture, tracks):
    '''Slot format:
        {
          "talk_id": "00",
          "title": "Registration",
          "start_time": "08:00",
          "end_time": "09:00",
          "track": "all"
        },
    '''

    slots = []
    for talk_id, hour in enumerate(lecture.find_all('p', attrs={'class': 'hour'})):
        start_tag = hour
        while True:
            start_time = hour.time.getText()
            title_tag = start_tag.find_next('p', attrs={'class': 'talk'})
            title = title_tag.getText()
            track_tag = start_tag.find_next('span', attrs={'class': 'track'})
            if track_tag:
                track_name = track_tag.getText()
                track_abrev = TRACKS[track_name]
                track = str(tracks.index(track_abrev)+1)
            else:
                track = 'all'

            speaker_tag = title_tag.find_next('p', attrs={'class': 'speaker'})

            # Lunch time
            if speaker_tag is None:
                hour_tag = title_tag.find_next('p', attrs={'class': 'hour'})
                slots.append(
                    {"talk_id": "{:02d}".format(talk_id),
                     "title": title,
                     "start_time": start_time,
                     "end_time": hour_tag.time.getText(),
                     "track": "all"}
                )
                break

            hour_tag = speaker_tag.find_next('p', attrs={'class': 'hour'})
            if hour_tag:
                end_time = hour_tag.time.getText()
            else:
                end_time = '18:00'

            slots.append(
                {"talk_id": "{:02d}".format(talk_id),
                    "title": title,
                    "start_time": start_time,
                    "end_time": end_time,
                    "track": track}
            )

            # Propably the last slot of the day.
            if hour_tag is None:
                break
            # End of slots in the same hour.
            elif speaker_tag.find_next('p').attrs.get('class', ['no_class'])[0] == 'hour':
                break
            else:
                start_tag = speaker_tag

    return slots

# with open('schedule.html') as schedule:
#     soup = bs4.BeautifulSoup(schedule.read())
# soup.find_all('li')

days = []
output = {"0.0.1": [{}]}
for day in dates.keys():
    f_day = urllib.urlopen(
        'https://raw.githubusercontent.com/pythonbrasil/pythonbrasil13-site/'
        'master/theme/templates/includes/days/{}'.format(day)
    )
    soup = bs4.BeautifulSoup(f_day.read())
    days.append(soup)
    lecture = soup.find('div', attrs={'class': 'lecture'})
    # All the days have the same room names, don't need to parse all them.
    # if output.get('tracks') is None:
    #    output["0.0.1"].append({'tracks': parse_track_names(lecture)})
    # Track names are fixed, they will not change.
    tracks_abrev = sorted(TRACKS.values())
    output["0.0.1"][0]['tracks'] = tracks_abrev
    output["0.0.1"][0][dates[day]] = parse_slots(lecture, tracks_abrev)

with open('pybr/data/schedule_new.json', 'w') as f_schedule:
    json.dump(output, f_schedule, indent=4)
