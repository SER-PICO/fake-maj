# Fake Windows Update

This program simulates a Windows update process using Python's tkinter library.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/SER-PICO/fake-maj.git
    ```

2. Navigate to the project directory:

    ```bash
    cd fake-maj
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install tk
    pip install Pillow
    ```

## Description

This program displays a fake Windows update screen that mimics the appearance of a BIOS update. It includes an image, progress bar, and status messages to simulate the update process. The program runs in full-screen mode and prevents the window from closing using Alt + F4.

- The `update_messages` list contains simulated update messages.
- The `update_status_message()` function updates the status message based on the progress.
- The `update_progress()` function updates the progress bar and the %.
- The main window is created using tkinter, with a customized appearance resembling a Windows update.
- An image is loaded and displayed on the screen.
- The progress bar updates at random intervals to simulate progress.
- The window stays on top and cannot be closed using Alt + F4.
- The progress bar stays on the screen for approximately 1 minute.

## Usage

Simply run the Python script `fake_maj.py` to start the fake update process.

```bash
python fake_maj.py
