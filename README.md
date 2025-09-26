# Cron Parser

A simple Python script to parse and display cron expressions in a human-readable format.

---

## Features

- Supports standard cron fields: **minute, hour, day, month, weekday**
- Handles:
  - Wildcards (`*`)
  - Ranges (`1-5`)
  - Steps (`*/2`)
  - Lists (`1,3,5`)
- Displays expanded values for each field along with the command.

---


## Installation

1. Clone the repository:

```bash
git clone <repository_url>
cd cron-parser
