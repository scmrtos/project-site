function Link(el)
    local target = el.target
    
    -- skip external links, abs paths, links w/o .md extension, etc
    if target:match('^https?://') or
       target:match('^/') or
       target:match('^%w+://') or
       not target:match('%.md#') then
        return el
    end
    
    -- search only relative links <filename>.md#<anchor> (filename w/o path preceding)
    local anchor = target:match('^[^/#]+%.md#([^#]+)$')
    
    if anchor then
        el.target = '#' .. anchor
    end
    
    --print(el.target)
    return el
end
