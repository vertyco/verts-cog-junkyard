# Vert's Cog Junkyard

![Artwork](https://i.imgur.com/8QGMhkj.png)
Various cogs live here, they have either been succeeded by their newer rewrite, don't work anymore, or are just no
longer being maintained.

### Cogs found here may or may not still work!

I am not providing support for these cogs anymore.

![Python 3.8](https://img.shields.io/badge/python-v3.8-orange?style=for-the-badge)
![Discord.py](https://img.shields.io/badge/discord-py-blue?style=for-the-badge)
![black](https://img.shields.io/badge/style-black-000000?style=for-the-badge&?link=https://github.com/psf/black)
![license](https://img.shields.io/github/license/Vertyco/verts-cog-junkyard?style=for-the-badge)

![Lines of code](https://img.shields.io/tokei/lines/github/Vertyco/verts-cog-junkyard?color=yellow&label=Lines&style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/Vertyco/verts-cog-junkyard?color=blueviolet&style=for-the-badge)

## Cogs

| Cog                                              | Type | Working | Combatible With | Description                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------|------|---------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HaloStats                                        | Cog  | ❌       | Red v3.4        | <details><summary>Get your halo infinite stats!</summary> Pull stats via webscraping.</details>                                                                                                                                                                                                                                                                                                               |
| DayZTools                                        | Cog  | ❓       | Red v3.4        | <details><summary>Manage your Nitrado DayZ servers.</summary> Status logs, player counts, management commands ect...</details>                                                                                                                                                                                                                                                                                |
| EcoTools                                         | ✓    | ✅       | Red v3.4-3.5    | <details><summary>Tool for sending RCON commands to your ECO game server.</summary> Add your servers and send RCON commands through discord.</details>                                                                                                                                                                                                                                                        |
| [MCTools](mctools/README.md)                     | ✓    | ✅       | Red v3.4-3.5    | <details><summary>Super simple status cog for Minecraft Bedrock servers.</summary> Displays a status embed showing server version and player count. Only for BEDROCK dedicated servers since there is already one that supports Java.</details>                                                                                                                                                               |
| modals                                           | Cog  | ✅       | Red v3.5        | <details><summary>Just a test cog for modals</summary> Literally that's it</details>                                                                                                                                                                                                                                                                                                                          |
| [SCTools](sctools/README.md)                     | ✓    | ✅       | Red v3.4-3.5    | <details><summary>View detailed Star Citizen ship info.</summary> Right now there is only one command (scships) that displays detailed info for ships in SC, you can use "[p]scships shipname" to search for a specific ship.</details>                                                                                                                                                                       |
| Support                                          | ✓    | ✅       | Red v3.4        | <details><summary>(Red 3.4 Only) Your basic support ticket system, but with buttons.</summary> Configure a ticket category and support message for the button to be added to, includes ticket log feature and optional transcripts.</details>                                                                                                                                                                 |
| [YouTubeDownloader](youtubedownloader/README.md) | ✓    | ✅       | Red v3.4-3.5    | <details><summary>Download YouTube videos as audio files.</summary> Allows you to download entire playlists, all videos from a channel, or individual videos as audio files. You can either download them locally or have them sent directly to discord. WARNING: Downloading YouTube videos via 3rd party methods is against their ToS and I am not responsible if you get your bots ip suspended.</details> |

## Modules/Misc

| Module                 | Dpy Version | Description                               |
|------------------------|-------------|-------------------------------------------|
| dislash-menu-example   | 1.7.3       | Button menu for dpy1                      |
| dpy2-menu-example      | 2.0.0       | Button menu for dpy2                      |
| get-user-reply-example | Any         | Async context manager for getting replies |

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/vertyco)

# Installation

Run the following commands with your Red instance, replacing `[p]` with your prefix:

If you haven't loaded the Downloader cog already, go ahead and do that first with: `[p]load downloader`. Then,

```ini
[p]repo add verts-cog-junkyard https://github.com/vertyco/verts-cog-junkyard
                                                                   [p]cog install verts-cog-junkyard <list of cogs>
[p]load <list of cogs>
```

# Contributing

I do not maintain these cogs, but I will be happy to review and approve pull requests.

