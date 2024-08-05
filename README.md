# Cytron-Order-Id-Printer
Scan Qr code order id and print numbering label via USB in Raspberry Pi.

{ TO AUTO-RUN BY CREATE THE SHELL SCRIPT }

step 1: Open a terminal on your Raspberry Pi

step 2: nano ~/open_serial_monitor.sh

step 3: #1/bin/bash 
Ixterminal -e "python3 /home/pi/tester/space-test-py" 
// please use replace ur file name at {space-test-py}

-press 'ctrl+x' and Y and enter



step 4: chmod + X ~/open_serial_monitor. Sh

step 5: mkdir -p ~/.config/autostart

step 6: nano ~/.config/autostort/open_serial_monitor. desktop



step7 : [Desktop Entry]

        Type = Application

        Exec=/home/pi/open_serial_monitor. sh

        Name = Open Serial Monitor

        Comment = Opens the serial monitor at startup

        X-GNOME-Auto start-enabled = true

step 8: Save (crtl+x), (y) and Enter)

step 9: Sudo reboot
