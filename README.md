# Texed

Texed is a lightweight, fast, and simple text editor written in Python. Designed with simplicity and efficiency in mind, Texed leverages the cross-platform `prompt_toolkit` library to ensure a smooth and consistent experience across different operating systems.

## Features
- **Lightweight**: Minimal resource usage for optimal performance.
- **Cross-Platform**: Runs seamlessly on Linux, macOS, and Windows.
- **Fast and Responsive**: Built using the highly efficient `prompt_toolkit` library.
- **Simple and Intuitive**: Focused on essential editing features without unnecessary complexity.

## Installation
Texed requires Python 3.8 or higher. To get started:

### First method

1. Clone this repository:
   ```bash
   git clone https://github.com/jean0t/texed.git
   cd texed
   ```

2. Install the required dependency:
   ```bash
   pip install prompt_toolkit
   pip install pygments
   ```

3. Run Texed:
   ```bash
   python texed.py
   ```

### Second method

1. Clone this repository
    ```bash
    git clone https://github.com/jean0t/texed.git
    cd texed
    ```

2. Go for the distribution (dist/):
    ```bash
    cd dist/ 
    ```

3. Install with pipx:
    ```bash
    pipx install texed*.whl
    ```

_obs:_ Do not forget to install the dependency


## Usage
Once Texed is running, you can use the following basic commands:
- Start typing to edit text.
- Save your file with `ctrl+s`.
- Exit the editor with `ctrl+q`.


## License
Texed is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html). Feel free to use, modify, and distribute the software under the terms of this license.

## Contributing
Contributions are welcome! If you have ideas, suggestions, or improvements, feel free to fork the repository and submit a pull request.

## Acknowledgments
Texed is powered by the [prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit), a robust library for building interactive command-line applications.

---

Start editing smarter with Texed today!


