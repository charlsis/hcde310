# AI log

## HW0: Class 1, build an app with AI

Paste every prompt you sent, in order, with the AI's replies. A share link to the chat is fine too, but paste the prompts here either way. Your thinking about it goes in `day1.md`.

**Share link (optional):**

### Prompt 1

```
Build a single-page interactive web app. It calls the Art Institute of Chicago API (https://api.artic.edu/api/v1/artworks/search) when the user searches or filters, and shows results with images. Keep it under ~150 lines. Audience: Art students who want to learn how artists make creative decisions in famous artworks
-> study an artwork interactively, first interpreting what they see themselves, then discovering the artist’s intentions and the reasoning behind specific artistic choices by hovering over elements

The user can
- Explore a famous artwork by hovering over different areas to discover the meaning and reasoning behind the artist’s creative choices.
- Interpret an artwork themselves before revealing information about its composition, symbolism, and historical context.
- Learn about the artist’s life and experiences to understand why they chose elements in the artwork the way they did. 

My sketch is attached; follow it. Explain how the code works in plain language, section by section.
Attached- Sketch we draw on paper

```

**AI's reply:**

I built ArtWhy.dc.html from your sketch, in about 140 lines. It goes gallery wall → "What's your interpretation?" → hover over the artwork to see the artist's decisions. It's out for review now.
How the code works, section by section
Setup (the <helmet> block). Loads the Broadsheet stylesheet and components, so the page gets the newspaper look: the serif fonts, paper-white background and cyan accent.
Header. The "ArtWhy?" title and a one-line intro.
Gallery (search and filters). A search box and filter buttons (All, Painting, Print, Sculpture, Photograph). When you search or pick a filter, search() asks the Art Institute's search API for up to 16 public-domain works. It keeps only those that have an image and shows them as a grid of framed thumbnails. Clicking one opens it for study.
Study, step 1: your interpretation. The artwork appears large next to the question "What's your interpretation of this artwork?" You type in the box. The Reveal button stays disabled until you've written something, so you have to look and think before learning anything.
Study, step 2: the reveal. reveal() sends Claude the artwork's title, artist, date, medium, the museum's description and what you typed. Claude sends back four things:
a short reply to your reading
4–5 hotspots, each with a position on the image and an explanation of why the artist made that choice
composition, symbolism and historical context
how the artist's life shaped those choices
The hotspots appear as numbered cyan dots on the image. Hovering over one shows its explanation in the side panel. If Claude can't be reached, the page shows the museum's own notes instead.
renderVals(). This is the link between the stored data and what's on screen. It decides which step is visible, builds the image links, marks which filter is selected and picks which hotspot's note to show.
Things to know
The API doesn't mark where things are in a picture, so Claude estimates the hotspot positions and some dots may sit slightly off.
The API has no curated "famous works" list. The gallery opens on a Van Gogh search as a starting point.

### Prompt 2

```
I want it to be a vintage style website and the artwork has a frame and will be able to move two lines and move in a circle.
```

**AI's reply:**

I made the vintage version as a new file, ArtWhy v2.dc.html; your original is unchanged. It's out for review now.
Vintage look: the header has an old newspaper-style heading with thick and thin rules, a "Est. MDCCCLXXIX · Chicago" line and a large all-caps title.
Frames: every artwork sits in a dark wood-style frame with a cream mat, and the thumbnails have a light sepia tint. A small caption under each shows the title and artist. The large artwork on the study page gets the same frame.
Two moving rows: the search results are split into two rows that scroll across the page in opposite directions and loop back around continuously. A row stops when you hover over it so you can click an artwork.
I read "moving in a circle" as rows that loop continuously. If you meant frames going round in a 3D ring, I can change it to that.

### Prompt 3

```
Can you use this style to restyle?
Attached- Example image on pinterest

```

**AI's reply:**

I restyled the gallery after your painting as a new file, ArtWhy v3.dc.html; v2 is unchanged. It's out for review now.
Walls and text: a warm cream wall with dark brown text.
Frames: all artworks, including the large one on the study page, are in gold frames with a cream mat and a soft drop shadow. I removed the sepia tint so the paintings show their true colors.
Room: a gold rail and a green lower wall sit under the two moving rows, with a wooden floor below.
Buttons and highlights: these are now museum green instead of cyan, with a deep red as the second color.
This moves away from the Broadsheet design system's colors, because you asked for this specific look.

### Prompt 4

```
change the background color to maroon red, and the darker texts to lighter colors

```

**AI's reply:**

The background is now maroon red. All text is light cream, with softer cream for secondary lines such as artist names and details. The italic reply to the student's reading on the study page is now light gold so it shows up on the maroon.
The two image-loading errors in the console appear before the artwork links arrive and don't affect the page.

### Prompt 5

```
I think u did some image wrong, we only want the image in this api https://api.artic.edu/api/v1/artworks/search?q=cats&fields=title,artist_display,date_display,image_id

```

**AI's reply:**

The search now asks the API for the same four fields as your link: title, artist, date and image. It's out for review now.
Default search: the gallery opens on "cats" instead of Van Gogh.
Image links: these now use the image address the API returns in each response, instead of one I had typed in myself.
Public-domain filter removed: results are now the plain search results. The downside is that some artworks may come back without a viewable image.
Filter buttons still work: Painting, Print and the others still narrow the results when you pick one.
Because the museum description isn't requested any more, the study page no longer shows the medium. Claude also now works only from the title, artist and date when it explains the artist's choices.