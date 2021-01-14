# Among Us regionInfo.dat creator

This is a simple python script to generate the regionInfo file needed for custom servers in Among Us.

## Why?

Compared to most other scripts and programs which all create the same regionInfo file, this program allows you to change the name that shows up in the bottom when in Among Us.

I've also tried to make the code as readable and simple as possible.

## Basic usage:

```sh
python main.py "Server name" 127.0.0.1
```

This will generate a file called regionInfo.dat in your current folder, which could then be placed at:
`C:\Users\username\AppData\LocalLow\Innersloth\Among Us\regionInfo.dat`

This could for example be used to create a custom name for the server when using the [Impostor server](https://github.com/AeonLucid/Impostor) for among us


## Run online:

You can run this online in [this repl.it project](https://repl.it/@Evla03/among-us-region-info-py) without the need to set up a local python instance.

After running the program in the shell, [download the project zip from repl.it](https://docs.repl.it/tutorials/02-managing-files-using-repl-it#exporting-our-weather-data-files) and extract the regionInfo.dat file.
