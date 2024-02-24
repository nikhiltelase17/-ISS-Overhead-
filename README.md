# ISS Tracker with Nighttime Email Notification

## Overview

This Python project is a simple yet fascinating International Space Station (ISS) tracker that notifies you via email when the ISS is passing overhead during nighttime. It leverages open APIs to get real-time ISS position data and sunrise/sunset times for your location.

## Features

- **ISS Overhead Check:** Utilizes the Open Notify API to determine if the ISS is currently overhead based on its latitude and longitude.
  
- **Nighttime Check:** Uses the Sunrise-Sunset API to verify if it's nighttime at your location. The script compares the current time with sunrise and sunset times.

- **Email Notification:** If the ISS is overhead and it's nighttime, the script sends an email alert. It uses the smtplib library to connect to Gmail's SMTP server.

## APIs Used

- [Open Notify API](http://api.open-notify.org/iss-now.json)
- [Sunrise-Sunset API](https://api.sunrisesunset.io/json)

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/nikhiltelase17/-ISS-Overhead-.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Gmail account:
    - Replace `"your_email@gmail.com"` and `"your_email_password"` in the script with your actual email credentials.

4. Run the script:

    ```bash
    python iss_tracker.py
    ```

5. Enjoy the notifications whenever the ISS is passing overhead during nighttime!

## Contributing

Contributions are welcome! If you have any ideas or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [Open Notify](http://open-notify.org/) and [Sunrise-Sunset API](https://sunrise-sunset.org/api) for providing the APIs used in this project.

---

Feel free to add more sections or details depending on your project's specifics. Include any additional setup instructions, troubleshooting tips, or usage examples that might help users understand and use your project effectively.
