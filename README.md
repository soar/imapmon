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

| Environment variable name | Command line flag | Description |
| --- | --- | --- |
