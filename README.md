# IMAP Mon

Tool for monitoring IMAP mailboxes and retransmitting received emails via alternative channels

## Quick start

1. Create a file `docker-compose.override.yml` or update `docker-compose.yml` with environment variables defined below.
2. Start the app with:
    ```shell
    docker-compose up
    ```

## Settings

Some options can be set via an environment variable (real or [dotenv](https://github.com/theskumar/python-dotenv)) or a command line flag.

| Environment variable name | Command line flag | Required | Description |
| --- | --- | --- | --- |
| `IMAP_HOSTNAME` | `--hostname`/`-h` | ☑️ | IMAP server hostname |
| `IMAP_USERNAME` | `--username`/`-u` | ☑️ | IMAP username |
| `IMAP_PASSWORD` | `--password`/`-p` | ☑️ | IMAP password/key/token |
| `CHANNELS` | `--channel`/`-c` | ☑️ | Channel to retransmit messages |
| `TELEGRAM_BOT_TOKEN` | `--telegram-bot-token` | ☑️/✖️ | Telegram Bot Token |
| `TELEGRAM_CHAT_ID` | `--telegram-chat-id` | ☑️/✖️ | Telegram Chat ID (channel ID, group ID or @username) |
| `LOG_LEVEL` | `--log-level`/`-l` | ✖️ | Log level for console messages |

## Examples

0. Get help:
    ```bash
    imapmon --help
    ```
1. Passing parameters via a command-line:
    ```bash
    imapmon --hostname imap.example.com -u user@example.com -p qwerty123 -c telegram --telegram-bot-token "1234567890:EtneWwZtnEibpH6WZVsnZimbPXZLRurw" --telegram-chat-id "12345678"
    ```
2. Passing parameters via environment variables:
    ```bash
    export IMAP_HOSTNAME=imap.example.com
    export IMAP_USERNAME=user@example.com
    export IMAP_PASSWORD=qwerty123
    CHANNELS=telegram TELEGRAM_BOT_TOKEN=xxx TELEGRAM_CHAT_ID=123 imapmon
    ```
