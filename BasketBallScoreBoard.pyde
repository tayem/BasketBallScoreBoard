import displayObject as dO;
seconds = 0;
minutes = 10;
homeScore = 100;
awayScore = 0;
timeStatus = True;
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
    timeBox = dO.displayObject(displayWidth/6, displayHeight/2.8, 180,100, 2);
    timeBox.Draw(str(homeScore), 80);
    return None;
    
def keyPressed():
    global homeScore;
    global awayScore;
    global timeStatus;
    if key == "h":
        homeScore += 1;
    elif (key == " "):
        print("efsefsef");
        if timeStatus == True:
            timeStatus = False;
        else:
            timeStatus = True;