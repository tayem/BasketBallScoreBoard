import displayObject as dO;
seconds = 0;
minutes = 10;
homeScore = 0;
awayScore = 0;
timeStatus = True;
scoreStatus = 0;
def setup():
    fullScreen();
    colorMode(RGB,255,255,255);
    smooth();
    return None;
def draw():
    global seconds;
    global minutes;
    global timeString;
    global homeScore;
    global awayScore;
    if timeStatus:
        if frameCount % 60 == 0: 
            if seconds % 60 == 0:
                minutes-=1;
                seconds = 60;
            seconds-=1;
    timeString = str(minutes) + ":" + '%02d' % seconds;
    rectMode(CENTER);
    timeBox = dO.displayObject(displayWidth/2, displayHeight/10, 300,120, 1);
    timeBox.Draw(timeString, 90);
    homeBox = dO.displayObject(displayWidth/6, displayHeight/2.8, 180,100, 2);
    homeBox.Draw(str(homeScore), 80);
    awayBox = dO.displayObject(displayWidth/1.2, displayHeight/2.8, 180,100, 2);
    awayBox.Draw(str(awayScore), 80);
    return None;
    
def keyPressed():
    global homeScore;
    global awayScore;
    global timeStatus;
    global scoreStatus;
    if key == "h":
        if scoreStatus == 0:
            scoreStatus = 1;
        else: scoreStatus = 0;
    elif key == "1":
        if scoreStatus == 0:
            homeScore += 1;
        else:
            awayScore += 1;
    elif key == "2":
        if scoreStatus == 0:
            homeScore += 2;
        else:
            awayScore += 2;
    elif key == "3":
        if scoreStatus == 0:
            homeScore += 3;
        else:
            awayScore += 3;
    elif key == "n":
        if scoreStatus == 0:
            homeScore -= 1;
        else: awayScore -=1;
    elif (key == " "):
        if timeStatus == True:
            timeStatus = False;
        else:
            timeStatus = True;