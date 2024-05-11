# Suricata Redis to MongoDB bridge

This script allows uploading of Suricata Redis que to MongoDB. This allows for building web interfaces and more advances quering.

## Requirements

- Redis server
- MongoDB

## Quick start

Configure Suricata dump

```
  - eve-log:
      enabled: yes
      filetype: redis
      redis:
        server: 127.0.0.1
        port: 6379
        mode: list
        key: suricata
```

### Tip

When `/etc/suricata/suricata.yaml` is configured use Redis it's important to estimate how much data your sever can handle before cleaning up the que. If for some reason the que list is not cleaned it will continue growing and crash your server. Solution I've found is to add a **crontab** task that trims Redis que every to 10000 latest items.

`0 * * * * redis-cli LTRIM 10000 0 9999`