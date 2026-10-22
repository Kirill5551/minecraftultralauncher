# Minecraft Ultra Launcher

A console launcher for Minecraft servers. It downloads server and proxy cores from the
PaperMC API, sets up the EULA, starts the server with a chosen amount of RAM, and shows
the latest log.

Everything runs from the terminal — no GUI required.

## Features

- Installs server cores: **Paper**, **Folia**, and proxy cores: **Velocity**, **Waterfall**, **Travertine**
- Downloads the latest build for the version you pick
- Creates `eula.txt` automatically (after you accept the EULA)
- Starts the server with `-Xms1G -Xmx<ram>G` and the `nogui` flag
- Counts plugins in the `plugins/` folder
- Prints `logs/latest.log` with line numbers
- Removes the core file

## Requirements

- Python 3
- Java (JDK 17 or newer, depending on the core version)
- Windows (the script uses `cls` and `pause`)

Install the dependencies:

```bash
pip install requests questionary cloudscraper
```

## Usage

1. Put the launcher in an empty folder and run it:

```bash
python start.py
```

2. On the first run the launcher asks which core to install. Pick a core and a version —
   the latest build is downloaded into the script's folder.
3. Accept the EULA when prompted, so `eula.txt` is created.
4. Choose an action from the menu:
   - **Start** — start the server, allocating the amount of RAM you enter
   - **Plugins** — show how many `.jar` plugins are detected
   - **Log** — print `logs/latest.log`
   - **Delete core** — remove the downloaded core file

## Notes

- The server runs in the same folder as the launcher.
- Stopping the server with `Ctrl+C` or the `stop` command in the console ends the session
  normally and prints `The server was stopped or crashed.`

## Roadmap

- **v2** — launch several selected servers in one terminal at the same time
