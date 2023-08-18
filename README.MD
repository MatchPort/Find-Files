### 🖥 Installation

1. Clone the Find-Files repository:
```sh
git clone https://github.com/MatchPort/Find-Files.git
```

Or download it here: https://github.com/MatchPort/Find-Files/releases/tag/v1.0.1

2. Change to the project directory:
```sh
cd find-files
```

3. Setup config:

Open the config.cfg file in notepad or vscode and change the following:

For file extension you would like to find change .env To what you want
```sh
FileExtension = .env
```
To change the drive you wanna scan change D:\\ To your drive your scanning.
```sh
Path = D:\\
```
Example:


```sh
Path = F:\\
```

### 📂 Scanning one folder

You can scan one folder by add the name of the folder after the //'s 

Example:

```sh
Path = D:\\others\
```


### 🤖 Using Find-Files

```sh
python main.py
```
