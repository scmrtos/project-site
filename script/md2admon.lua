function Pandoc(doc)
    local new_blocks = {}
    local i = 1
    
    while i <= #doc.blocks do
        local block = doc.blocks[i]

        if block.tag == "Para" and pandoc.utils.stringify(block):match("!!!%s+") then
            local para_text = pandoc.utils.stringify(block)
            local typ = para_text:match("!!!%s+(%w+)")
            local title = para_text:match('"([^"]+)"') or "Note"

            local colors = {
              warning = "orange",
              note    = "cyan",
              tip     = "green",
              info    = "blue",
              error   = "red"
            }

            local color = colors[typ] or "blue"

            local tcb_open = string.format([[
                \begin{tcolorbox}[colback=%s!5!white, 
                                  breakable,
                                  enhanced,
                                  colframe=%s!75!black,
                                  title={%s},
                                  fonttitle=\bfseries,
                                  boxsep=5pt,
                                  left=5pt,
                                  right=5pt,
                                  top=5pt,
                                  bottom=5pt,
                                  before upper=\setlength{\parskip}{0.7em}]
            ]], color, color, title)

            table.insert(new_blocks, pandoc.RawBlock("latex", tcb_open))
            
            i = i + 1  -- next block
            while i <= #doc.blocks do
                local lb = doc.blocks[i]
                if lb.tag == "CodeBlock" and #lb.classes == 0 then
                    if lb.text and #lb.text > 0 then
                        -- reparse code block text as markdown
                        local temp_doc = pandoc.read(lb.text, "markdown")
                        for _, block in ipairs(temp_doc.blocks) do
                          table.insert(new_blocks, block)  -- Готовое форматирование!
                        end
                    end
                    i = i + 1
                else
                    break -- admonition end
                end
            end

            table.insert(new_blocks, pandoc.RawBlock("latex", "\\end{tcolorbox}"))
            
        else
            table.insert(new_blocks, block)
            i = i + 1
        end
    end
    
    doc.blocks = new_blocks
    return doc
end
