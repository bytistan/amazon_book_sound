# Amazon Book Sound

This application was written to pull data from amazon to use for educational purposes.

## How to Use

1. First, clone the project to your computer:

    ```bash
    git clone https://github.com/findik-faresi/amazon_book_sound
    ```

2. Go to the project directory:

    ```bash
    cd amazon_book_sound
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Add links you want the download sound:

    ```bash
    nano resources/links.txt
    ```
    
5. Run the following command to start:

    ```bash
    python main.py
    ```
    
## Features

- Audio auto save in the audio folder.
- Auto save to json file.

## Example Json

```json
    [
      {
          "title": " Atomic Habits",
          "author": "James Clear",
          "audio": "./audio/_atomic_habits.mp3"
      },
      {
          "title": " Iron Flame",
          "author": "Rebecca Yarros",
          "audio": "./audio/_iron_flame.mp3"
      }
    ]
```
