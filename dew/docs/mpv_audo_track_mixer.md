# mpv_audio_track_mixer.lua

## Description

A Lua script for MPV-based players that automatically mixes all available audio tracks into one output stream when a
media file is loaded.

It was made and tested for **SMPlayer**, but it should also work with other players that use MPV and support custom
Lua scripts.

## Usage

In **SMPlayer**, set the MPV options field at:

`Options->Preferences->Audio->Advanced->mpv->Options`

to:

`--script="/path/to/mpv_audio_track_mixer.lua"`

> [!NOTE]
> If you are using flatpak SMPlayer, make sure that it has permission to access the script file.

> [!TIP]
> For flatpaks I recommend adding read-only permission using Flatseal with: `/path/to/file:ro`

## Requirements

- MPV with Lua scripting support
- Optionally: SMPlayer

## Features

- Detects all audio tracks in the loaded file
- Automatically builds an audio mixing filter
- Mixes multiple audio tracks together using MPV's filter graph
- Leaves playback unchanged when only one or no audio track is present

## Behaviour

- Runs when a file is loaded
- If more than one audio track exists, the script enables audio mixing
