# HA-Bridge device DB updater

This Python script is designed to update the `uniqueid` values in the `device.db` file used by the HA-Bridge project. 
The script replaces each device's `uniqueid` with a new, sequentially numbered value, ensuring consistency across your devices.

## Features

- **Automatic `uniqueid` Update:** Replaces `uniqueid` values in the `device.db` file with a consistent format: `00:11:22:33:44:55:66:XX-00`, where `XX` is a counter incremented from `01` to `99`.
- **Counter Reset:** The counter resets to `01` after reaching `99`, maintaining a continuous sequence.
- **JSON Parsing and Writing:** Efficiently reads, modifies, and writes JSON data, preserving the structure of your `device.db` file.

## Prerequisites

- Python 3.x installed on your machine.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/ha-bridge-device-db-updater.git
    cd ha-bridge-device-db-updater
    ```

2. **Place Your `device.db` File:**
   
   Ensure your `device.db` file is located in the project directory.

3. **Install Dependencies (if any):**

    ```bash
    pip install -r requirements.txt
    ```

    *Note: This script currently has no external dependencies. The `requirements.txt` is included for potential future use.*

## Usage

1. **Backup Your Original File:**

   Before running the script, make sure to back up your original `device.db` file.

2. **Run the Script:**

    ```bash
    python update_uniqueid.py
    ```

3. **Check the Updated File:**

   The script modifies the `device.db` file in place. The `uniqueid` values will be updated as specified.

## Example

Suppose your `device.db` contains devices with arbitrary `uniqueid` values. After running the script, each device will have a `uniqueid` formatted like `00:11:22:33:44:55:66:01-00`, `00:11:22:33:44:55:66:02-00`, up to `00:11:22:33:44:55:66:99-00`.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [HA-Bridge](https://github.com/bwssytems/ha-bridge) - The HA-Bridge project that inspired this tool.
