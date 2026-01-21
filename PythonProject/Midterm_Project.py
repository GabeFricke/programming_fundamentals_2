import requests
import pandas
pd= pandas.DataFrame()
url = "https://www.statmuse.com/cfb/player/eli-stowers-64507/game-log?seasonYear=2025"
response= requests.get(url)
print(response.text)
word_of_interest = ",{&quot;value&quot;:[0,"
index= response.text.index(word_of_interest)
print(index)
the_text = response.text
url_important_stuff= response.text[index: index + len(word_of_interest)+3]
print(url_important_stuff)
# my_list= []
rec_list = []
target_list=[]
yards_list=[]


counter = 0
for i in range(120):
    word_of_interest = "value&quot;:[0,"
    index = the_text.find(word_of_interest)
    # print(index)
    #
    # print(close_index)
    # print(the_text[index: index + close_index + 1])
    # the_text = the_text[index + 1]


    # next_number_index = the_text.find(",],")
    # print(the_text[index+1: index + next_number_index+1:])
    # print(next_number_index)

    # print(index)
    close_index = the_text[index:].find("],")
    url_important_stuff = the_text[index + len(word_of_interest): index + close_index  ]
    # print(url_important_stuff)
    # print(index)
    # print(len(word_of_interest))
    # print(close_index)
    the_text = the_text[index + close_index + 1:]
    try:
        print(float(url_important_stuff))
        print(counter)
        counter +=1
    except:
        print("gap")
        counter = 0
    if counter == 2:
        rec_list.append(float(url_important_stuff))
    if counter == 3:
        target_list.append(float(url_important_stuff))
    if counter == 4:
        yards_list.append(float(url_important_stuff))
print("Receptions")
print(rec_list)
print("targets")
print(target_list)
print("yards")
print(yards_list)
print(sum(rec_list)/len(rec_list))
print(sum(target_list)/len(target_list))
print(sum(yards_list)/len(yards_list))

rec_list_2= (sum(rec_list)/len(rec_list))
target_list_2= (sum(target_list)/len(target_list))
yards_list_2= (sum(yards_list)/len(yards_list))
new_rec_list = (rec_list+[rec_list_2])
new_target_list = (target_list+[target_list_2])
new_yards_list = (yards_list+[yards_list_2])
print(new_rec_list)
print(new_target_list)
print(new_yards_list)

dictionary = {"receptions": new_rec_list , "targets": new_target_list, "yards": new_yards_list}
df = pandas.DataFrame(dictionary)
df.to_csv("midterm_project", index = False)



# url_2= "https://www.statmuse.com/cfb/player/justin-joly-67573/game-log?seasonYear=2025"
# response_2 = requests.get(url_2)
# print(response_2.text)

