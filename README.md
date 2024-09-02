# File Folder Organizer

## Overview

The **File Folder Organizer** project automates file management using the `watchdog` library for monitoring file system events and the `schedule` library for periodic tasks. This script organizes `.cpp` and `.mp4` files by moving them to specific directories and handles folder management tasks on a scheduled basis.

This project was created to address the problem of manually organizing and managing files in specific directories, which can be tedious and error-prone. By automating the process, it ensures that files are consistently organized and frees up time for more productive tasks. Also created to handle making directories for my CS class!

## Features

- **File Monitoring**: Watches the `Downloads` and `Videos` folders for new `.cpp` and `.mp4` files.
- **File Movement**: Automatically moves `.cpp` files to `Desktop/CPP Files` and `.mp4` files to `Videos/mp4`.
- **Scheduled Folder Management**: Periodically creates and manages folders according to the defined schedule.
- **Event Logging**: Logs file movements and deletions for tracking purposes.
