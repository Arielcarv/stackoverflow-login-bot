# stackoverflow-login
English version | [中文](README_CN.md)

This project is for a consecutive visit on https://stackoverflow.com/. If you visit https://stackoverflow.com/ for 30 consecutive days, you can earn `Enthusiast` badge. And 100 days, `Fanatic` badge.

## Disclaimer

**This project is a fork from [CoXier/stackoverflow-login
](https://github.com/CoXier/stackoverflow-loginEdit). With updates and some personal changes.**

1. Updated dependencies.
2. Uploaded a new dockerfile for execution.
3. Added a docker-compose.yml file.
3. Added an alert of executed login through telegram bot (needs a registered telegram bot token).

## Usage

**By Docker (recommended):**

You can build the Docker Image yourself, or use my Image [arielcarv/stackoverflow-login-bot](https://hub.docker.com/r/arielcarv/stackoverflow-login-bot).

Run `docker run -e EMAIL="your-email" -e PASS="your-password" BOT_API_TOKEN="your-telegram-bot-token" -e USER_ID="your-telegram-user-id" -d arielcarv/stackoverflow-login-bot`.

Or, use Docker Compose. Create [docker-compose.yml](docker-compose.yml) (file in the repo) and run:

``` bash
docker-compose up -d
```

**By Python:**

First, install the dependencies in `requirements.txt`. Then, set up Environment Variables:

* `EMAIL` your StackOverflow Account Email
* `PASS` your StackOverflow Account Password
* `APPPATH` point to this application's path, e.g, `export APPPATH=/root/apps/stackoverflow-login`

You can choose to set a scheduled task by crontab:

```bash
crontab -e
# Put below command to new tab
0 0 * * * project_path/stackoverflow-login-bot/dev_script/robot.sh
```
