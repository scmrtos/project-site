function Str(el)
    local replacements = {
        ["✔"] = [[\goodcheck]],
        ["✘"] = [[\goodcross]],
    }
    if replacements[el.text] then
        return pandoc.RawInline('tex', replacements[el.text])
    end
    return el
end
