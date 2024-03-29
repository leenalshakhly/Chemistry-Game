# Chemistry-Game

* A video of your program running (1min or less, no voiceover):
https://drive.google.com/file/d/1hTBxegxFouS22y1U1XFTdgvasPocdg6x/view?usp=sharing
# Functionality Summarisation:
This program is divided into two levels. The user of this program is given three to four substance options before having to select one. Following the user's selection of an element, a dialogue would appear with a narrative explaining what would happen; you would either live or die. You will survive if you make the right choice of substance. Additionally, it has a feature that prompts the user to restart the level if they want to try again after dying. The system will congratulate you for finishing two levels and for producing a new, profound substance  which you will name, when you pass both of them. 

# Why does it exist / Who is it for?
Making this helped me gain experience with and proficiency in the Python programming language. Given that I currently lack a lot of Python expertise, it is only supposed to be a beginning of what I might produce in the future. This could be something entertaining for my friends to try out. It's also for those who enjoy playing text-based games and chemistry! 

# Learned to do something new:
My friend Saif taught me how to use "time.sleep()." Due to the unexpected consequences that will take place if you choose the incorrect substance, it greatly assisted in making the game more suspenseful. I frequently used "time.sleep()"; if you check here...

<img width="564" alt="Screen Shot 2023-01-20 at 6 40 19 PM" src="https://user-images.githubusercontent.com/112869836/213741727-e4e4809e-9dc1-42d2-b9b1-ae03d8a2c127.png">

I used it because, as I indicated previously, it would result in unexpected occurrences if you choose the wrong substance, which would heighten user expectation and make the game more suspenseful. As you can see from the sample up top, I tried to make the user more anticipatory and created a welcoming greeting for them to begin the second level.

# Data Abstration:
<img width="746" alt="Screen Shot 2023-01-20 at 6 49 35 PM" src="https://user-images.githubusercontent.com/112869836/213743339-7cf3f052-4f5b-446d-a93c-e1b013b430a4.png">

This is an example of data abstrction because the values are stored for all the different substances of the different levels. The values are retrieved in the conditional statements, that, depending on which type of substance used, it would print out scenario of the evensts that will occur. The values for the various substaces of the various levels would have nowhere to be stored if I had not incorporated this data abstraction into this portion of the program. Since there wouldn't be any interactions and the coding would simply not function as intended, the game would be useless.
 
# Procedural Abstraction (functions)
Sequencing, Selection, and Iteration

<img width="856" alt="Screen Shot 2023-01-20 at 6 56 26 PM" src="https://user-images.githubusercontent.com/112869836/213744808-53dd4d69-ce28-412b-be9f-e09a90cb4a92.png">
   
The sequencing that takes place in this specific function ("stagetwo") is how the computer reads the code from top to bottom. The way I did my code is I put stage 2 at the top and stage 1 at the bottom. The reason why I did that is because functions need to be defined first before they call so if I were to define the functions I'd have to put all the code for them above it to define the first because the computer reads the code from top to bottom. So that's why I put stage 2 at the top and stage 1 at the bottom.
 
Then we see iteration, through the use of a While Loop, that will keep on running these conditional statements of the code unless the user chooses the wrong subsatnce and would have the choice if they want to replay or retry level or just leave the game.

By making it simple for me to call the functions that held the game's whole core code, this procedural abstraction helped me manage complexity in my code. After the user completed the first level, It could  give the user the option to quit playing or replay it. By offering me a place to store my code and a way to call it whenever I need to, it also aids in complexity management because it offers the code a place to stay until it is needed and called rather than requiring me to copy and paste enormous portions of code.
    
