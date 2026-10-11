# HW1 notes

## Part 4: Predict, run, explain

**My prediction for `predict.py` (written BEFORE running it):**
I predict that the function will go through each artwork upto the 2nd index (bc 3 range)
and therefore prints:

0 The Bedroom 1989
1 Nighthawks 2042
2 American Gothic 2030
3 #number of titles
10 #number of letters in title 0, The Bedroom


**What it actually printed:**
0 The Bedroom 1989
1 Nighthawks 2042
2 American Gothic 2030
10
11

**Explain:** If I was off, which line surprised me and why? If I was right, why do the last two lines print different numbers?
I was off because I counted just the titles in the prior for loop, when the function is out of that loop and therefore counts the total index in the list (10). On the last one, it counts the characters in "The Bedroom". My mistake was counting just the letters, when the space also counts towards it.


## Part 5: Reflection (about 100 words)

Look back at your Day 1 app: its code if you can still open it, or your screenshots of it running. Is there anything you can now recognize (a loop, an `if`, a list)? Where? If you only have screenshots, what do you think the code had to do to make the app behave that way?
![reflection_screenshot](image.png)
I think the filter buttons (all, painting, print, sculpture, photograph) is an example of a loop with if statements. The code holds those 5 category names in a list and then loops through it. Inside the loop, an if statement asks if the button is the one that the user clicks. If yes, the button becomes highlighted green and if else, it stays plain. When a different filter is clicked, the loop runs again and the highligt moves.
