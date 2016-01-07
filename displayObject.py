class displayObject():
    def __init__(self, sX, sY, sWidth, sHeight,Type):
        self.X = sX;
        self.Y = sY;
        self.Width = sWidth;
        self.Height = sHeight;
        self.Type = Type;
    def Draw(self, Text="no text", textsize = 50, textX = 3.5, textY = 1.5):
        if self.Type == 0:
            fill(0,0,0);
            rect(self.X, self.Y, self.Width, self.Height);
        if self.Type == 1:
            fill(0,0,0);
            rectMode(CENTER);
            rect(self.X, self.Y, self.Width, self.Height);
            fill(255,5,5);
            rectMode(CENTER);
            textAlign(CENTER, CENTER);
            textSize(textsize);
            text(Text, self.X, self.Y);
        if self.Type == 2:
            fill(0,0,0);
            rect(self.X, self.Y, self.Width, self.Height);
            fill(255,5,5);
            textAlign(CENTER, CENTER);
            textSize(textsize);
            text(Text, self.X, self.Y);