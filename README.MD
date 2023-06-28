
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
send-discohook-json
</h1>
<h3>◦ Hook into the disco with JSON precision!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
</p>

![GitHub top language](https://img.shields.io/github/languages/top/MatchPort/send-discohook-json?style&color=5D6D7E)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/MatchPort/send-discohook-json?style&color=5D6D7E)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/MatchPort/send-discohook-json?style&color=5D6D7E)
![GitHub license](https://img.shields.io/badge/license-gato-&color=5D6D7E)
</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [🚀 Getting Started](#-getting-started)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The project, titled "send-discohook-json", is a code snippet written in Python that allows users to send JSON payloads to a Discord webhook URL. The payload can include text messages as well as embedded content with titles, descriptions, colors, and fields. The code also includes a verification mechanism to ensure the success of the request. This project provides a simple and efficient solution for integrating JSON-based messages with Discord, enhancing communication capabilities for users.

---

## ⚙️ Features

Feature | Description |
|-----|-----|
| **🏗 Architecture** | The codebase follows a simple architecture with a single Python script (`send-it.py`) that handles sending JSON payloads to a Discord webhook URL. It leverages the HTTP protocol for communication. |
| **✔️ Testing** | For testing you can just run the send-it.py file. |
| **🔌 Integrations** | The codebase is designed to integrate with Discord's webhook feature, allowing for convenient message posting to Discord channels. It exposes a simple API for sending JSON payloads, making it easy to integrate into other systems or tools. |

---





---

## 🧩 Modules

<details closed><summary>Root</summary>

| File       | Summary                                                                                                                                                                                                                                                                                                                                          | Module     |
|:-----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|
| send-it.py | This code snippet sends a JSON payload to a Discord webhook URL. The payload includes a'content' field for the message text and an'embeds' field for richer embedded content including titles, descriptions, colors, and fields. It also checks the response status code and raises an error if it is not 204 (indicating a successful request). | send-it.py |

</details>

---

## 🚀 Getting Started



### 🖥 Installation

1. Clone the send-discohook-json repository:
```sh
git clone https://github.com/MatchPort/Find-Files.git
```

Or download it here: https://github.com/MatchPort/Find-Files/releases/tag/v1.0.1

2. Change to the project directory:
```sh
cd send-discohook-json
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



### 🤖 Using send-discohook-json

```sh
python main.py
```

---




---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the `[ℹ️  GATO]` License. See the [LICENSE](https://raw.githubusercontent.com/MatchPort/Find-Files/main/LICENSE) file for additional info.

---

## 👏 Acknowledgments

> - Orion for giving me the idea of config system!

---
