from django.shortcuts import render
from django.shortcuts import render
import requests
import pandas as pd

def run_stats(request):
    try:
        url = "https://www.statmuse.com/cfb/player/eli-stowers-64507/game-log?seasonYear=2025"
        response = requests.get(url)
        the_text = response.text

        word_of_interest = "value&quot;:[0,"
        rec_list, target_list, yards_list = [], [], []
        counter = 0

        for i in range(120):
            index = the_text.find(word_of_interest)
            if index == -1:
                break
            close_index = the_text[index:].find("],")
            url_important_stuff = the_text[index + len(word_of_interest): index + close_index]
            the_text = the_text[index + close_index + 1:]

            try:
                val = float(url_important_stuff)
                counter += 1
            except:
                counter = 0
                continue

            if counter == 2:
                rec_list.append(val)
            if counter == 3:
                target_list.append(val)
            if counter == 4:
                yards_list.append(val)

        if len(rec_list) == 0:
            return render(request, "statsapp/stats.html", {"error": "Could not extract stats from the page."})

        rec_avg = sum(rec_list)/len(rec_list)
        target_avg = sum(target_list)/len(target_list)
        yards_avg = sum(yards_list)/len(yards_list)

        new_rec_list = rec_list + [rec_avg]
        new_target_list = target_list + [target_avg]
        new_yards_list = yards_list + [yards_avg]

        dictionary = {"receptions": new_rec_list, "targets": new_target_list, "yards": new_yards_list}
        df = pd.DataFrame(dictionary)
        df.to_csv("midterm_project.csv", index=False)

        return render(request, "statsapp/stats.html", {
            "receptions": new_rec_list,
            "targets": new_target_list,
            "yards": new_yards_list,
            "rec_avg": rec_avg,
            "target_avg": target_avg,
            "yards_avg": yards_avg,
            "csv_created": True
        })

    except Exception as e:
        return render(request, "statsapp/stats.html", {"error": str(e)})

# Create your views here.
