![NBA Tip-Off Home Page](/NBAtipoffhomepage.png)

# NBA Tip-Off: A Basketball Stats Database Website

Welcome to the NBA Tip-Off, a Basketball Stats Database Website repository! This website provides a comprehensive collection of NBA player statistics, allowing users to explore player and team data, compare player and team data, and more. This README file will guide you through the setup and usage of the website.

## Features

-Player stats: View individual player statistics, including points percentage, rebound percentage, assist percentage, and more.

-Team stats: Explore team performance data, such confrence rank, points rank, and rebound rank.

-Game results: Access the results of past NBA games, including scores, leading scorers, and game summaries.

-Search functionality: Search for specific players by name, position, or jersey number. Search for teams by season year, name, or team confrence in the search bar.

## Need to update and add more to readme.md for github
VS Code offers [a feature](https://code.visualstudio.com/docs/remote/containers) that lets you use a Docker container as your full-time development environment.

Install the [Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack), and then when you open a project that has a `.devcontainer` folder/file, VS Code will prompt you to re-open the project inside a container. This can take several minutes to set up on the initial run, but should be quicker afterwards

This will make it so that all necessary system and project dependencies are installed all at once. Neat!

### Codebase Summary

This repo consists of a Postgres database, a pgAdmin web server, and a Python Flask web server application skeleton.

### Seeding the database

If you wish to initialize the database upon creation, you can add `.sql` files in a `/.devcontainer/pg_init` folder. See the [postgres docker readme](https://github.com/docker-library/docs/blob/master/postgres/README.md#initialization-scripts) for details.

### Running the Flask Application

Inside the integrated terminal in VS Code, type

```
flask --debug run
```
