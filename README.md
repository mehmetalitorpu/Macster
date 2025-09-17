# MACster - MAC Address Changer Tool

![MACster Banner](https://img.shields.io/badge/MACster-MAC%20Changer-green?style=for-the-badge&logo=terminal)

MACster is a user-friendly Python script developed for changing MAC addresses on Linux systems. It performs secure and effective MAC address changing operations using existing system tools.

## Features

- **Easy to Use**: User-friendly menu interface
- **Automatic MAC Changing**: Automatic MAC changes at specified intervals
- **Safe Restoration**: Secure return to original MAC address
- **Dynamic Monitoring**: Real-time MAC address tracking
- **System Service**: Automatic startup on system boot
- **Logging**: Detailed logging of all operations
- **Multi-Interface Support**: Wired and wireless interfaces

## Installation

### Requirements

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install macchanger ifconfig iwconfig ethtool

# CentOS/RHEL/Fedora
sudo yum install macchanger net-tools wireless-tools ethtool
# or
sudo dnf install macchanger net-tools wireless-tools ethtool

# Arch Linux
sudo pacman -S macchanger net-tools wireless_tools ethtool
```

### Script Installation

```bash
# Clone the repository
git clone https://github.com/username/Macster.git
cd Macster

# Make it executable
chmod +x Macster.py

# Run with root privileges
sudo python3 Macster.py
```

## Usage

### Basic Usage

```bash
sudo python3 Macster.py
```

### Menu Options

1. **Start MAC Changing** - Starts MAC changing process for a specific interface
2. **Stop MAC Changing** - Stops all MAC changing processes and returns to original MACs
3. **Set Auto Startup** - Configures automatic startup on system boot
4. **Remove Auto Startup** - Removes automatic startup configuration
5. **Restore Original MAC** - Returns selected interface to original MAC address
6. **View MAC Addresses** - Dynamically monitors MAC addresses of all interfaces
7. **Exit** - Exits the program

### Command Line Usage

```bash
# Run in daemon mode
sudo python3 Macster.py --daemon [interface] [count] [interval]

# Example: Change wlan0 interface 10 times per hour
sudo python3 Macster.py --daemon wlan0 10 360
```

## Technical Details

### System Tools Used

- **`ifconfig`** - For changing MAC addresses
- **`macchanger`** - For restoring original MAC
- **`iwconfig`** - For detecting wireless interfaces
- **`ethtool`** - For getting original MAC address

### Security Features

- Root privilege check
- Interface existence validation
- Error handling and logging
- Safe restoration mechanism

## File Structure

```
macster/
├── macster.py          # Main script file
├── README.md           # This file
└── requirements.txt    # Python requirements
```

## Important Notes

- **Root Privileges Required**: Script requires root privileges to modify network interfaces
- **System Compatibility**: Tested on Linux systems
- **Backup**: Don't forget to save original MAC addresses
- **Legal Warning**: Use this tool only for legal purposes

## Troubleshooting

### Common Issues

1. **"This script requires root privileges!" error**
   ```bash
   sudo python3 Macster.py
   ```

2. **macchanger not found error**
   ```bash
   sudo apt install macchanger  # Ubuntu/Debian
   sudo yum install macchanger  # CentOS/RHEL
   ```

3. **Interface not found error**
   ```bash
   ifconfig -a  # List available interfaces
   ```

### Log Files

```bash
# Check log files
ls -la /tmp/mac_changer_*.log
tail -f /tmp/mac_changer_wlan0.log
```

## Contributing

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Star This Project

If you like this project, don't forget to give it a star!


## Acknowledgments

- Linux community
- Open source projects
- Testing users

---

**Legal Warning**: This tool is developed only for educational and legal testing purposes. The user accepts all responsibilities arising from the use of this tool.
