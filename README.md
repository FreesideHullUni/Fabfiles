# Freeside-Fabfiles

> The official _Fabfile_ for Freeside.

A _FabFile_ is a configuration file for [fabric](http://www.fabfile.org/) way of automatically installing software on many machines at once. If you'd like some software installed on the Freeside machines, then it's the _Fabfile_ in this repository that you'll want to edit! See the instructions below for more details.

## Usage
Using the fabric _FabFile_ in this repository is easy. Here's how:

Run a task:
```bash
fab -R {desktops,servers} taskname 
```

Example:
```bash
fab -R desktops install_neovim
```

## Contributing
Want some software installing on the Freeside computers? You've come to the right place! Here's a simnple guide on how to request software to be installed:

1. Make sure you're logged into your GitHub account.
2. Take a look at [fabfile/__init__.py](https://github.com/FreesideHull/Freeside-Fabfiles/blob/master/fabfile/__init__.py). 
3. Press the edit button in the top-right.
4. Figure out how to install the software you want on a standard _Fedora_ machine.
5. Add a new function to the _Fabfile_ in the same vein that the existing ones that installs the software you want. We prefer it if the software is available through `dnf`, _Fedora_'s official package manager. That way it stays up-to-date automatically!
6. Click _Propose File Change_ at the bottom of the page and follow it through to submit a _Pull Request_ for your changes.
7. Once your pull request is accepted, then your software will automatically get installed on the Freeside computers through a git hook.
8. You're done!
