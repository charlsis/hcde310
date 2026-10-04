# Day 1 "before" snapshot

Write your own, even if you worked in a pair. Keep it: we come back to it at mid-quarter (Week 6) and at the end (Week 11). Your prompts go in `ai_log.md`, not here.

**Name:** Charlene Siswanto
**Partner (if any):** Riley Fang

## Before we prompted

### 1. Who is it for, and what do they want to do?

It's for Art students who want to learn how artists make creative decisions in famous artworks.

**"The user can..." sentences:**
1.Explore a famous artwork by hovering over different elements to learn their meaning and reasoning behind the artist's choices
2.Interpret an artwork themselves before revealing information about its composition, symbolism, and historical context.

### 2. Our sketch

Put the photo in this `hw0` folder, then change the filename below to match:

![sketch](sketch.jpg)

### 3. Our prediction

We expected the AI would accurately use my sketch as the basis of layouts, and the hover-based flow of the paintings.

## What we got

### 4. What the AI made

Put the screenshot in this `hw0` folder, then change the filename below to match:

![screenshot1](screenshot1.png)
![screenshot2](screenshot2.png)
![screenshot3](screenshot3.png)

### 5. Sketch vs. app

- **Matches our sketch:**
There are frames positioned side-by-side
The name ArtWhy is accurate to what we wrote
- **Different from our sketch:**
Layout concept
It created its own buttons for different types of artworks
- **The AI decided** (something we never said):
It chose a white background color initially
The paintings are random, not based on API data

### 6. What did I keep, change, or reject, and why?
I changed the background color into a maroon color as I think it gives color to the museum. I edited text colors to contrast with the background. I kept the button options as it gives more options for the users to find their desired artwork.


### 7. Explain back
Pick one part of the code. In your own words, what does it do?
<helmet>
  <link rel="stylesheet" href="_ds/broadsheet-9f7df910-3a02-41d0-9056-c87372662e8b/styles.css">
  <script src="_ds/broadsheet-9f7df910-3a02-41d0-9056-c87372662e8b/_ds_bundle.js"></script>
  <style>:root{--color-bg:oklch(0.32 0.11 22);--color-text:oklch(0.95 0.03 85);--color-accent:oklch(0.42 0.08 145);--color-accent-600:oklch(0.36 0.08 145);--color-accent-700:oklch(0.85 0.1 88);--color-accent-900:oklch(0.25 0.05 145);--color-accent-100:oklch(0.9 0.04 145);--color-accent-2:oklch(0.5 0.14 30);--color-neutral-700:oklch(0.85 0.04 70)} body{margin:0;background:var(--color-bg)} a{color:var(--color-accent-700)} a:hover{color:var(--color-accent-900)} @keyframes loopL{from{transform:translateX(0)}to{transform:translateX(-50%)}} @keyframes loopR{from{transform:translateX(-50%)}to{transform:translateX(0)}}</style>
</helmet>
My Explanation:
This chunk of code edits the style and script of the <head> of a webpage.
    - The upper link tag connects it to a Stylesheet theme called "broadsheet"
    - The script tag loads the JavaScript bundle
    - The style tag customizes the color variables with the oklch() CSS color format that are written with 3 values: lightness, saturation, hue (value from 0-1)
The two @keyframes define looping horizontal animation. The loopL slides the content to the left



## Looking ahead

### 8. What does it do? Does it work? What broke?
The AI generated web was able to retrieve data from the API and arranged them into clickable framed paintings. Users can interact with elements of each painting to expand and view explanations about the artwork. Nothing major broke, but the final layout was different from the "museum" style I sketched.

### 9. How much do I understand about how it works? (0–100%)

**My number:** 40%

**Why that number:** I can match lines of code to the elements they create on the website, but I struggle to explain how each part works on its own.



### 10. What would I need to know to tell whether it's *well designed or well built*?
A well designed web should function to solve the intended problem, easily understood and used by users. To tell if it is well built, I'll need to understand how the code works and if its effectively written.


### 11. What do I hope to be able to do by week 10?
I hope to understand more on how the AI builds websites by being able to identify the code lines and its purpose, and to utilize them better.

