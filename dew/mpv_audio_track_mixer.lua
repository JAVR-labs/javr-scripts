local function mix_audio()
    local tracks = mp.get_property_native("track-list") or {}
    local inputs = {}

    for _, track in ipairs(tracks) do
        if track.type == "audio" and track.id then
            table.insert(inputs, string.format("[aid%d]", track.id))
        end
    end

    if #inputs > 1 then
        local graph = table.concat(inputs, "") ..
            string.format("amix=inputs=%d[ao]", #inputs)
        mp.set_property("lavfi-complex", graph)
    else
        mp.set_property("lavfi-complex", "")
    end
end

mp.register_event("file-loaded", mix_audio)
