
# External Tools - Sublime Text

Run any external tool with an keyboard shortcut and/or via the command palette.

## Quickstart

- Install via [PackageControl](http://wbond.net/sublime_packages/package_control): `External Tools`
- Open *Preferences --> Key bindings*
- Add ```{ "keys": ["alt+1"], "command": "external_tools_run", "args": {"cmd": ["explorer.exe", "/select,", "$file"]}}```
- Save & close
- Press `ALT+1` 

## Installation

### Package Control

If you have [PackageControl](http://wbond.net/sublime_packages/package_control) installed, you can use it to install the package.

Just type `CTRL+SHIFT+P` (or if you're on a mac: `CMD+SHIFT+P`) to bring up the command pallete and pick *Package Control: Install Package* from the dropdown, search and select `External Tools` there and you're all set.

### Manual installation

- Enter directory through *Preferences --> Browse Packages...* in the Sublime Text menu.
- Run the following command from your command line

    ```
    git clone https://github.com/FelixBoers/sublime-external-tools.git ./ExternalTools
    ```

## Usage

### Custom key bindings

You can add custom keybinding by go to *Settings -> Key Bindings* and bind your keystrokes to the `external_tools_run` command. 

- Open Windows Explorer with the current file selected:
	```json
	{ "keys": ["alt+1"], "command": "external_tools_run", "args": {"cmd": ["explorer.exe", "/select,", "$file"]}}
	```
- Open Git bash in the current project root or if no project is opened in the root of the first opened folder
	```json
	{ "keys": ["alt+2"], "command": "external_tools_run", "args": {"cmd": ["C:/Program Files/Git/bin/bash.exe"], "working_dir": "${project_path:$folder}" }}
	```

### Custom entries in the command palette

In the same way you can define your own entries in the command palette (*CTRL + SHIFT + P*). Go to *Preferences --> Package Settings --> External Tools --> Command Palette* and add:

```json
{
	"caption": "Cmd here",
	"command": "external_tools_run",
	"args": {
		"cmd": [ "cmd.exe", "/K"],
		"working_dir": "${project_path:$folder}"
	}
}
```

### Shared configurations

If you want to open the app via key binding or via the command palette you can define the app in the plugin settings *Preferences --> Package Settings --> External Tools --> Settings*.

This is how a configuration could look like:

```json
{
  "apps": [
    {
      "id": "explorer",
      "name": "Explorer",
      "cmd": [
        "explorer.exe",
        "/select,",
        "$file"
      ]
    },
    {
    	"id": "cmd",
    	"cmd": ["cmd.exe", "/K"],
    	"working_dir": "$folder"
    }
  ]
}
```

The key binding configuration should then look like:
```json
{ "keys": ["alt+3"], "command": "external_tools_run", "args": {"id": "explorer" }}
```

And the command palette configuration like this:
```json
{ "caption": "Cmd here", "command": "external_tools_run", "args": { "id": "cmd" } }
```

All apps defined in the plugin settings are listed if you run *External Tool* via the command palette.

### Variables

Along to all your system environment variables the following variables are getting expanded too:

|      Variable      |                          Description                           |
|--------------------|----------------------------------------------------------------|
| $file              | The full path to the current file, e.g., C:\Files\Chapter1.txt |
| $file_path         | The directory of the current file, e.g., C:\Files              |
| $file_extension    | The name portion of the current file, e.g., txt                |
| $file_base_name    | The name only portion of the current file, e.g., Document      |
| $packages          | The full path to the Packages folder                           |
| $folder            | The path to the first folder opened in the current project     |
| $project           | The full path to the current project file                      |
| $project_path      | The directory of the current project file                      |
| $project_name      | The name portion of the current project file                   |
| $project_extension | The extension portion of the current project file              |
| $project_base_name | The name-only portion of the current project file              |

Placeholder variables are supported too:

```
${project_name:Default} 	# Use 'Default' as project name if no project is open
${project_path:$folder}		# If no project opened use first folder
```

The name of the placeholder is case sensitive!