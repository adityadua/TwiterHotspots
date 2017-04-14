import json
import dateparser
import datetime

def peak(pro_list): #function to be executed when sudden rise in tweets occur
	l = []
	X=0
	Y=0
	for i in range(len(pro_list)):
		x=(pro_list[i][1][0][0][0]+pro_list[i][1][0][1][0]+pro_list[i][1][0][2][0]+pro_list[i][1][0][3][0])/4.0
		y=(pro_list[i][1][0][0][1]+pro_list[i][1][0][1][1]+pro_list[i][1][0][2][1]+pro_list[i][1][0][3][1])/4.0
		if [x,y] not in l:
			l.append([x,y])
			X=X+x
			Y=Y+y
	X=X/50.0
	Y=Y/50.0
	return [X,Y]
		
j=1
pro_list=[]
hourly_thresh = [datetime.time(0, 7, 2)]*24		#dynamic threshold for hourly average of tweets per second
hour=0
days=1
threshold_val = 0.1;							#statistically calculated value which adjusts the sensitivity of product
with open('python.json', 'r') as f:
	d=datetime.datetime.now()
	hour = d.hour
	t2=dateparser.parse(((json.loads(f.readline()))['created_at'])[11:19])
	tweetcount=0
	for  i in f:
		d=datetime.datetime.now()
		tweetcount=tweetcount+1
		if d.minute==0:
			new_thresh=datetime.time(0,(tweetcount*72)/60,(tweetcount*72)%60)	#new threshold value added through weighted averaging
			hourly_thresh[hour]=(hourly_thresh[hour]*days+new_thresh)/(days+1)
			hour = (hour + 1)%24
			if hour==0:
				days=days+1
		tweet = json.loads(i)
		ele = [dateparser.parse((tweet['created_at'])[11:19]),((tweet['place'])['bounding_box'])['coordinates']]
		pro_list.append(ele)
		if j==50:			#keeping an adjustable interval of 50 tweets to check peaks for reducing computation
			tx = ele[0]-t2
			T = int((hourly_thresh[hour].minute*60+hourly_thresh[hour].second)*(1-threshold_val))
			T = datetime.time(0,T/60,T%60);
			if (datetime.datetime.min + tx).time()<T:
				print peak(pro_list)
			prolist = []
			t2=ele[0]
			j=0
		j=j+1
		