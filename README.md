## Info

Primary purpose (at this point): to efficiently access and output player data relevant to the NEXOMANIA placements team, such that it can be easily transferred to our Google Sheets database.

## To Do

- Figure out how to store Player info in JSON
- Add team info to Player

- Goals for what Player can contain:

    - Battletag
        - player_overview
            - last_updated
            - team
                - most_recent
                - NGSs14
                    - team name
                    - division
                - RTNs3
                - NEXOs6
                - ...
            - role_info
                - Tank
                    - Current
                        - [Primary / Secondary / Flex / Unlikely]
                    - Past
                        - [Primary / Secondary / Flex / Unlikely]
                - Healer
                    - ^
                - Bruiser
                    - ^
                - Assassin
                    - ^
            - Notes
            - NGS
                - Games played
                - Games won
                - Games lost
                - WR
            # long-term: add RTN and Nexo games
            - SL
                - MMR
                - Games played
                - Games won
                - Games lost
                - WR
            - QM
                - ^
            # could add other modes but probably not worth it
        - Abathur
            - hero_overview
                - Main/Preferred/Flex/Unlikely/Unknown
            - NGS
                - Games played
                - Games won
                - Games lost
                - WR
            - SL
                - MMR
                - Games played
                - Games won
                - Games lost
                - WR
            - QM
                - ^
            - UR
                - ^

## Credits

[SirCaptainMitch](https://github.com/SirCaptainMitch) is responsible for:

```
- \app\ext\Helper.py
- \app\classes\Player.py
- other programs still in progress
- setting up the venv framework
- troubleshooting and moral support
```

Troubleshooting and moral support credit also go to [Mesos] and [eYeYellow]