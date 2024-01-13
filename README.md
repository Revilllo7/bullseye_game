Python game project
date started: 21/12/2023


idea:
Archery game that utilises the competitiveness of the sport and works as a way to see who can get more points in a set amount of time




TODO:
- [✅] Make a MENU
- [✅ ] Add settings? (only hosts scoreboard)
- [✅] Add quit button
- [ ] Create the game:
- - [ ] Scoring system
- - [ ] Arrow physics
- - [ ] Stamina/Hold bar (since holding a strung bow is tiresome)
- - [ ] Timer
- - [ ] Graphics:
    - [✅] character 
    - [ ] ground
    - [ ] animations
    - [ ] background
- - [ ] X and Y axis shot (shot predictor exists, however it's baaad...)
- - [ ] hit animations?









Captain log:
1. created a repo, made a run.py file, got the pygame lib
2. created a menu that changes displays between: "start game", "settings", "quit"
3. created buttons file that is responsible for: initialising buttons, updating buttons, detecting inputs, changing color on hover for visual clarity.
4. added custom font.
5. added images, however, they require fixing, due to resolution issues. Need to make my own.
6. fixed centring issues, fixed resolution issues, made my own background and button borders.
7. Added player character
8. Added player movement
9. Added gravity and jumping
10. Added shot indicator on Q
11. START takes you to the game
12. SETTINGS -> SCOREBOARD takes you to the scoreboard
13. Scoreboard looks for scores.txt file and prints them out correctly sorting as it goes
14. Added background image for the menu. play and settings sections have their special backgrouns, alongside scoreboards.
15. Added player collision with walls
16. 
