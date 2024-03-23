# Project-Echidna

<!-- display gif -->
![echidna](
https://i.imgur.com/JtUSkaT.gif)

Project echidna is a 2.5D video game prototype built from scratch with pygame. 

The prototype showcases a randomly generated world build using the [wave function collapse](https://youtu.be/2SuvO4Gi7uY) algorithm. The game features a character that can move around the world, jump, and collide with the environment. The character has a set of animations that are triggered based on the character's state. It also showcases how a seemingly 3D isometric game can be rendered purely using 2D sprites and layering.

 The game is still in development and will be updated with more features in the future.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Requirements
- [Python 3.8](https://www.python.org/downloads/release/python-380/)
- [pipenv](https://pypi.org/project/pipenv/)

### Installation

```py
pipenv install
```

### Usage

```py
pipenv run python src/main.py
```

### Roadmap
- [x] tilesets
- [x] character sprites
- [x] physics
- [x] charachter animations 
- [x] character movement
- [x] character collision
- [x] game state logic
- [x] world generation (wave function collapse)
- [x] events
- [ ] UI (menu, text popups, inventory)
- [ ] sound design

## Built with

- [pygame](https://pygame.readthedocs.io/en/latest/) - Pygame is a set of Python modules designed for creating video game engines.

