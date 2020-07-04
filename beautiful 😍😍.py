from bs4 import BeautifulSoup
import requests
from datetime import date
import csv
req=requests.get("https://www.nairaland.com/#featured").text
soup=BeautifulSoup(req, 'lxml' )
tr=soup.find("td",class_="featured w")
todays_date=date.today()
current_month=todays_date.strftime("%b")
current_day=todays_date.strftime("%d")
csv_file=open("/storage/emulated/0/my_website_scrape.csv","w")
csv_writer=csv.writer(csv_file)
csv_writer.writerow(["username","post_header","section","day_posted","month_posted","time_posted"])
for a_tag in tr.find_all("a"):
	
	link=a_tag.get("href")
	
	individual_post_requests=requests.get(link).text
	post_soup=BeautifulSoup(individual_post_requests,"lxml")
	time_date_span_list=post_soup.find("span",class_="s").text.split(" On ")
	time=time_date_span_list[0]
	#posts that were created today do not show month and day so i have to assign it to todays date if it was created today
	try:
		month_day_list=time_date_span_list[1].split(" ")
	except IndexError:
		month_day_list=[current_month,current_day]
	month=month_day_list[0]
	day=month_day_list[1]
	header_with_section_as_list=post_soup.find("h2").text.split(" - ")
	header=header_with_section_as_list[0]
	section=header_with_section_as_list[1]

	user=post_soup.find("a",class_="user").text
	print(user)
	print(header)
	print(section)
	print(day)
	print(month)
	print(time)
	csv_writer.writerow([user,header,section,day,month,time])

csv_file.close()