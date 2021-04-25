Yuan-Sheng Program (Private)

# Yuan-Sheng Program
this show the function, class and it's attributes and methods, parameters
* * *
## ***Function***
### main.py:
#### ***`def run_game()`***:**run full game**

### Game.py:

#### ***`def check_event(screen, gameSetting, xlim, ylim)`***:**check events from keyboard and mouse**

#### ***`def check_key_down(event)`***:**check key down event , and change then into string**

#### ***`def print_text(screen, gameSetting, textString, size = 'Normal', place = (0, 0)`***:**print text on the surface of the screen**

#### ***`def set_button(screen, gameSetting, place, size, color, textString)`***:**create a button on the screen**

### Start.py:

#### ***`def start_game(screen, gameSetting, person)`***:**get ready for the game biginning**

#### ***`def get_name(screen, gameSetting, person)`***:get the character's name
***

## ***Class***

### Setting.py:
#### ***`class Settings()`***:**give the parameters of whole game**
##### attributes:
`self.screenHeight` : Give the height of the screen
`self.screenWidth` : Give the width of the screen
`self.bgcolor` : Give the background color of the screen
`self.caption` : Give the caption of the game
`self.myFont`:Give the normal size of the font
`self.mySmallFont`:Gice the small size of the font

### person.py:
#### ***`class Person(self)`***:the main character's modal
##### attributes:
`self.name`:Person's name
`self.blood`:Person's blood
`self.attack`:Person's attack
`self.defence`:Person's defence
`self.exp`:Person's exp
`self.maxexp`:Person's maxexp
`self.gold`:Person's gold
##### methods:
***`def set_name(selfname)`***:Get the Person's name

***
## ***Parameters***
***